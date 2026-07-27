#!/usr/bin/env python3
"""Per-connector capability inference.

Replaces archetype-inherited emits/consumes with profiles derived from three ordered
evidence sources, each of which records why it fired:

    1. description rules  -- ordered regex over the connector's directory `role` text
    2. vendor rules       -- hand-authored knowledge of what the company actually sells
    3. archetype prior    -- fills only what 1 and 2 left empty, and is tagged as a prior

Stdlib only, deterministic, matching the style of the skill's existing scripts/atlas.py.

Usage:
    python3 infer.py --out ../data/registry_inferred.json [--vendor-arm a|b] [--report]
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
SKILL = "/root/.claude/skills/connector-atlas/scripts"

# ---------------------------------------------------------------------------
# Key vocabulary
# ---------------------------------------------------------------------------
# Typed keys: finer than the original 18 so that ubiquitous keys stop manufacturing
# edges. `text` is deliberately NOT a key -- free text is Claude-as-adapter, modelled
# as an INFERRED bridge with its own cost (see composition.md), never a join edge.

KEYS = {
    "email", "phone", "domain", "company", "person", "handle",
    "url:permalink", "url:artifact", "url:auth",
    "timestamp",
    "file:blob", "file:ref", "image", "media", "code",
    "rows:tabular", "rows:timeseries",
    "money:txn", "money:amount",
    "geo:point", "geo:region",
    "ticker", "project", "vendor_id",
}

WEAK = {"person", "vendor_id", "handle"}  # match only via crosswalk or same vendor

SIDE_EFFECT_ORDER = ["read", "create", "mutate", "irreversible"]


def worst(a, b):
    """Worst-case side effect of two."""
    return a if SIDE_EFFECT_ORDER.index(a) >= SIDE_EFFECT_ORDER.index(b) else b


# ---------------------------------------------------------------------------
# 1. Description rules
# ---------------------------------------------------------------------------
# Each rule: (id, compiled regex, {"emits": [...], "consumes": [...],
#             "verbs": [...], "side_effects": str|None})
# Rules are additive -- every rule that matches contributes, and every contribution
# records the matched span as evidence. Order does not gate; it only orders evidence.

def _r(pattern):
    return re.compile(pattern, re.I)


DESC_RULES = [
    # --- verbs / direction -------------------------------------------------
    # Analysing, collecting, tracking and reporting all entail reading. Leaving these out
    # gave connectors like SurveyMonkey ("collect responses, analyze results") a verb set
    # of {create} alone, which collapsed direction-fit on every edge leaving them.
    ("verb_read",     _r(r"\b(read|view|browse|explore|access|fetch|retrieve|look\s?up|pull|collect|analy[sz]e|summari[sz]e|track|monitor|report|insight|understand)\b"),
     {"verbs": ["read"]}),
    ("verb_search",   _r(r"\b(search|query|find|discover|lookup|ask)\b"),
     {"verbs": ["search"]}),
    # "upload" is a write. Omitting it made Google Drive ("Search, read, and upload files")
    # look incapable of accepting anything.
    ("verb_create",   _r(r"\b(create|add|draft|generate|build|make|turn .{0,20}into|design|upload|import|save|store|sync)\b"),
     {"verbs": ["create"], "side_effects": "create"}),
    ("verb_update",   _r(r"\b(update|edit|modify|manage|organi[sz]e|complete|reschedul)\b"),
     {"verbs": ["update"], "side_effects": "mutate"}),
    ("verb_delete",   _r(r"\b(delete|remove|archive|trash)\b"),
     {"verbs": ["delete"], "side_effects": "irreversible"}),
    ("verb_export",   _r(r"\b(export|download|render|publish)\b"),
     {"verbs": ["export"]}),
    ("verb_execute",  _r(r"\b(execute|run|automate|control|launch|trigger|orchestrat|deploy)\b"),
     {"verbs": ["execute"], "side_effects": "irreversible"}),

    # --- identity keys -----------------------------------------------------
    ("k_email",       _r(r"\b(e-?mail|inbox|mailbox|newsletter|thread|reply|replies)\b"),
     {"emits": ["email"], "consumes": ["email"]}),
    ("k_phone",       _r(r"\b(phone|sms|call|dial|whatsapp|telephon)\b"),
     {"emits": ["phone"], "consumes": ["phone"]}),
    ("k_company",     _r(r"\b(compan(y|ies)|firm|organi[sz]ation|business|account|vendor|supplier|employer|brand)\b"),
     {"emits": ["company"], "consumes": ["company"]}),
    ("k_domain",      _r(r"\b(domain|website|web ?site|url|link|seo|traffic)\b"),
     {"emits": ["domain"], "consumes": ["domain"]}),
    ("k_person",      _r(r"\b(people|person|contact|candidate|lead|prospect|customer|员工|employee|talent)\b"),
     {"emits": ["person"], "consumes": ["person"]}),
    ("k_handle",      _r(r"\b(social|twitter|x\.com|instagram|tiktok|linkedin|reddit|discord|slack|mastodon|handle|follower)\b"),
     {"emits": ["handle"], "consumes": ["handle"]}),

    # --- web ---------------------------------------------------------------
    ("k_permalink",   _r(r"\b(link|url|permalink|page|article|listing|post|source|citation|hyperlink)\b"),
     {"emits": ["url:permalink"]}),
    ("k_artifact",    _r(r"\b(share|shareable|publish|site|landing page|deck|presentation|prototype|mini-?game|interactive)\b"),
     {"emits": ["url:artifact"]}),

    # --- time --------------------------------------------------------------
    ("k_time",        _r(r"\b(schedul|calendar|date|deadline|due|time|hour|meeting|event|appointment|booking|reminder|history|trend|real.?time|log)\b"),
     {"emits": ["timestamp"], "consumes": ["timestamp"]}),

    # --- content -----------------------------------------------------------
    ("k_file",        _r(r"\b(file|document|doc|pdf|attachment|upload|folder|drive|storage|contract|invoice|receipt|scan)\b"),
     {"emits": ["file:blob", "file:ref"], "consumes": ["file:blob"]}),
    ("k_docref",      _r(r"\b(note|wiki|knowledge base|second brain|memo|matter|case|filing|paper|publication|research)\b"),
     {"emits": ["file:ref"], "consumes": ["file:ref"]}),
    ("k_image",       _r(r"\b(image|photo|picture|screenshot|diagram|chart|graphic|logo|thumbnail|qr|visual|satellite imagery)\b"),
     {"emits": ["image"], "consumes": ["image"]}),
    ("k_media",       _r(r"\b(video|audio|voice|music|podcast|recording|transcript|speech|animation|stream|sound)\b"),
     {"emits": ["media"], "consumes": ["media"]}),
    ("k_code",        _r(r"\b(code|sql|api|repo|repositor|git|script|query language|snippet|function|sdk|terminal|shell|devops|ci/?cd)\b"),
     {"emits": ["code"], "consumes": ["code"]}),

    # --- structured data ---------------------------------------------------
    # NOTE: bare "data" is deliberately excluded. It appears in ~40% of all role texts
    # ("your data", "data platform") and matching it pushed rows:tabular over the 35%
    # prevalence gate, reintroducing exactly the saturation this vocabulary exists to kill.
    ("k_rows",        _r(r"\b(dataset|table|row|record|spreadsheet|database|warehouse|report|inventory|catalog|structured data|crm)\b"),
     {"emits": ["rows:tabular"], "consumes": ["rows:tabular"]}),
    ("k_timeseries",  _r(r"\b(metric|analytic|insight|dashboard|kpi|statistic|telemetry|monitor|measure|performance|trend|surveillance)\b"),
     {"emits": ["rows:timeseries"]}),

    # --- money -------------------------------------------------------------
    ("k_money_txn",   _r(r"\b(payment|transaction|invoic|billing|payout|charge|refund|subscription|revenue|spend|expense|purchase|checkout)\b"),
     {"emits": ["money:txn", "money:amount"], "consumes": ["money:amount"], "side_effects": "irreversible"}),
    ("k_money_amt",   _r(r"\b(price|pricing|cost|budget|salary|valuation|deal|fund|financ|money|amount|discount|coupon|promo)\b"),
     {"emits": ["money:amount"], "consumes": ["money:amount"]}),

    # --- geo ---------------------------------------------------------------
    ("k_geo_point",   _r(r"\b(location|address|venue|store|restaurant|hotel|nearby|route|map|city|destination|pickup)\b"),
     {"emits": ["geo:point"], "consumes": ["geo:point"]}),
    ("k_geo_region",  _r(r"\b(countr(y|ies)|region|state|market|global|worldwide|nationwide|geograph|territor|weather|climate)\b"),
     {"emits": ["geo:region"], "consumes": ["geo:region"]}),

    # --- markets -----------------------------------------------------------
    ("k_ticker",      _r(r"\b(stock|ticker|equit|securit|portfolio|trading|invest|market data|fundamental|earnings|etf|crypto|token)\b"),
     {"emits": ["ticker"], "consumes": ["ticker"]}),

    # --- project -----------------------------------------------------------
    ("k_project",     _r(r"\b(project|task|roadmap|sprint|backlog|board|workflow|pipeline|initiative|planning|to-?do)\b"),
     {"emits": ["project"], "consumes": ["project"]}),

    # --- vendor-internal ---------------------------------------------------
    ("k_vendorid",    _r(r"\b(your|my)\b.{0,24}\b(account|workspace|instance|tenant|portal|environment|assets?)\b"),
     {"emits": ["vendor_id"], "consumes": ["vendor_id"]}),

    # --- risk modifiers ----------------------------------------------------
    ("se_send",       _r(r"\b(send|post|publish|book|order|pay|purchase|reserve|rent|sign|submit|deploy)\b"),
     {"side_effects": "irreversible"}),
    ("se_readonly",   _r(r"\b(read.?only|deterministic retrieval|explore public|guidance)\b"),
     {"side_effects": "read"}),
]


# ---------------------------------------------------------------------------
# Inference
# ---------------------------------------------------------------------------

def apply_desc_rules(role, fired_counter):
    """Return (contribution, evidence list) from description regex rules."""
    emits, consumes, verbs = set(), set(), set()
    se = None
    evidence = []
    for rid, rx, contrib in DESC_RULES:
        m = rx.search(role)
        if not m:
            continue
        fired_counter[rid] += 1
        emits.update(contrib.get("emits", []))
        consumes.update(contrib.get("consumes", []))
        verbs.update(contrib.get("verbs", []))
        if contrib.get("side_effects"):
            se = contrib["side_effects"] if se is None else worst(se, contrib["side_effects"])
        evidence.append({"rule": rid, "span": m.group(0)})
    return {"emits": emits, "consumes": consumes, "verbs": verbs, "side_effects": se}, evidence


def infer_one(conn, vendor_rules, priors, fired_counter):
    role = conn["role"]
    prof = {
        "id": conn["id"],
        "name": conn["name"],
        "role": role,
        "archetype": conn["archetype"],
    }

    provenance = defaultdict(list)
    evidence = []

    # --- source 1: description rules ---
    desc, desc_ev = apply_desc_rules(role, fired_counter)
    emits, consumes, verbs = set(desc["emits"]), set(desc["consumes"]), set(desc["verbs"])
    se = desc["side_effects"]
    evidence.extend(desc_ev)
    for k in emits:
        provenance["emits:" + k].append("description")
    for k in consumes:
        provenance["consumes:" + k].append("description")

    # --- source 2: vendor rules ---
    vr = vendor_rules.get(conn["id"])
    if vr:
        for k in vr.get("emits", []):
            if k not in emits:
                provenance["emits:" + k].append("vendor")
            emits.add(k)
        for k in vr.get("consumes", []):
            if k not in consumes:
                provenance["consumes:" + k].append("vendor")
            consumes.add(k)
        verbs.update(vr.get("verbs", []))
        if vr.get("side_effects"):
            se = vr["side_effects"] if se is None else worst(se, vr["side_effects"])
        if vr.get("not_emits"):
            for k in vr["not_emits"]:
                emits.discard(k)
        evidence.append({"rule": "vendor:" + conn["id"], "span": vr.get("why", "vendor knowledge")})

    # --- source 3: archetype prior (fills only what is still empty) ---
    prior = priors.get(conn["archetype"], {})
    used_prior = False
    if not emits:
        for k in prior.get("emits", []):
            emits.add(k)
            provenance["emits:" + k].append("archetype_prior")
        used_prior = True
    if not consumes:
        for k in prior.get("consumes", []):
            consumes.add(k)
            provenance["consumes:" + k].append("archetype_prior")
        used_prior = True
    if not verbs:
        verbs.update(prior.get("verbs", []))
        used_prior = True
    if se is None:
        se = prior.get("side_effects", "read")
        used_prior = True

    # --- confidence tier ---
    if vr:
        tier = vr.get("confidence", "DOCUMENTED")
    elif desc_ev and not used_prior:
        tier = "DIRECTORY"
    elif desc_ev:
        tier = "DIRECTORY"
    else:
        tier = "ASSUMED"

    prof["emits"] = sorted(k for k in emits if k in KEYS)
    prof["consumes"] = sorted(k for k in consumes if k in KEYS)
    prof["verbs"] = sorted(verbs)
    prof["side_effects"] = se
    prof["confidence"] = tier
    prof["provenance"] = {k: v for k, v in sorted(provenance.items())}
    prof["evidence"] = evidence
    prof["used_archetype_prior"] = used_prior
    return prof


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "registry_inferred.json"))
    ap.add_argument("--registry", default=os.path.join(SKILL, "registry_full.json"))
    ap.add_argument("--vendor-arm", choices=["a", "b"], default="a",
                    help="a = vendor rules EXCLUDE held-out connectors (unbiased generalization "
                         "measurement, the headline arm). b = include them (upper bound).")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    reg = load_json(args.registry)
    priors = load_json(os.path.join(DATA, "archetype_priors.json"))["priors"]
    vendor = load_json(os.path.join(DATA, "vendor_rules.json"))["rules"]
    heldout_ids = {l["id"] for l in load_json(os.path.join(DATA, "heldout_labels.json"))["labels"]}

    if args.vendor_arm == "a":
        vendor = {k: v for k, v in vendor.items() if k not in heldout_ids}

    fired = Counter()
    profiles = [infer_one(c, vendor, priors, fired) for c in reg["connectors"]]

    out = {
        "_schema": {
            "generated_by": "engine/infer.py",
            "source_registry": args.registry,
            "vendor_arm": args.vendor_arm,
            "vendor_rules_applied": len(vendor),
            "key_vocabulary": sorted(KEYS),
            "weak_keys": sorted(WEAK),
            "note": "emits/consumes are typed keys derived from description + vendor knowledge; "
                    "archetype is a prior that fills gaps only, and every field carries provenance.",
        },
        "connectors": profiles,
        "rules_fired": dict(fired.most_common()),
        "dead_rules": sorted(rid for rid, _, _ in DESC_RULES if fired[rid] == 0),
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)

    if args.report:
        n = len(profiles)
        base = {c["id"]: c for c in reg["connectors"]}
        differs = sum(1 for p in profiles
                      if sorted(p["emits"]) != sorted(base[p["id"]]["emits"]))
        prior_only = sum(1 for p in profiles if p["used_archetype_prior"])
        print(f"connectors inferred      : {n}")
        print(f"vendor rules applied     : {len(vendor)} (arm {args.vendor_arm})")
        print(f"differ from archetype    : {differs} ({differs*100//n}%)  [gate: >=60%]")
        print(f"needed prior for a field : {prior_only} ({prior_only*100//n}%)")
        print(f"dead rules               : {out['dead_rules'] or 'none'}")
        ke = Counter()
        for p in profiles:
            ke.update(p["emits"])
        print("\nkey prevalence (emit side), gate: no key > 35%")
        for k, v in ke.most_common():
            flag = "  <-- OVER GATE" if v > n * 0.35 else ""
            print(f"  {k:16s} {v:4d}  {v*100//n:3d}%{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
