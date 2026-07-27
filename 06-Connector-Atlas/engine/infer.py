#!/usr/bin/env python3
"""Function + capability layer for the Connector Atlas.

For every connector in the Claude directory this states, as knowledge:

    1. what it does            -- a plain-language function statement + source + confidence
    2. the jobs it can do      -- functional capability tags (data/capabilities.json)
    3. how it acts, per verb   -- read / create / mutate / irreversible, per verb

Three ordered evidence sources decide verbs and side effects, each recording why it
fired: (1) description rules over the directory `role`, (2) hand-authored vendor
knowledge, (3) archetype prior (fills only what 1 and 2 left empty). Capability tags come
from the archetype map, refined by keyword rules, and overridden by researched knowledge
for the terse minority whose blurb was too thin to stand alone.

This is the "function knowledge" layer that the use-case engines build on. The v1 join-key
composition (emits/consumes typed keys, prevalence gates, held-out precision) is gone --
capabilities, not keys, are how we ask whether a combo makes a use case.

Stdlib only, deterministic.

Usage:
    python3 infer.py [--out ../data/registry_inferred.json] [--report]
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

# Every verb maps to the intrinsic risk of that verb class. The nuance that "sending"
# an email or "posting" to Slack is irreversible even though it is a create/update is
# carried at the capability level (capabilities.json: irreversible_output) and applied
# by the use-case engine only when the connector is actually used as an output.
VERB_SE = {
    "read": "read", "search": "read", "export": "read",
    "create": "create", "update": "mutate",
    "delete": "irreversible", "execute": "irreversible",
}
READ_VERBS = {v for v, se in VERB_SE.items() if se == "read"}
SIDE_EFFECT_ORDER = ["read", "create", "mutate", "irreversible"]


def worst(a, b):
    return a if SIDE_EFFECT_ORDER.index(a) >= SIDE_EFFECT_ORDER.index(b) else b


# ---------------------------------------------------------------------------
# Description rules -- verbs and side effects only (the join-key rules are gone).
# Additive: every rule that matches contributes and records the matched span.
# ---------------------------------------------------------------------------

def _r(pattern):
    return re.compile(pattern, re.I)


DESC_RULES = [
    ("verb_read",   _r(r"\b(read|view|browse|explore|access|fetch|retrieve|look\s?up|pull|collect|analy[sz]e|summari[sz]e|track|monitor|report|insight|understand)\b"),
     {"verbs": ["read"]}),
    ("verb_search", _r(r"\b(search|query|find|discover|lookup|ask)\b"),
     {"verbs": ["search"]}),
    ("verb_create", _r(r"\b(create|add|draft|generate|build|make|turn .{0,20}into|design|upload|import|save|store|sync)\b"),
     {"verbs": ["create"], "side_effects": "create"}),
    ("verb_update", _r(r"\b(update|edit|modify|manage|organi[sz]e|complete|reschedul)\b"),
     {"verbs": ["update"], "side_effects": "mutate"}),
    ("verb_delete", _r(r"\b(delete|remove|archive|trash)\b"),
     {"verbs": ["delete"], "side_effects": "irreversible"}),
    ("verb_export", _r(r"\b(export|download|render)\b"),
     {"verbs": ["export"]}),
    ("verb_execute", _r(r"\b(execute|run|automate|control|launch|trigger|orchestrat|deploy)\b"),
     {"verbs": ["execute"], "side_effects": "irreversible"}),
    # risk modifiers
    ("se_send",     _r(r"\b(send|post|publish|book|order|pay|purchase|reserve|rent|sign|submit|deploy|trade)\b"),
     {"side_effects": "irreversible"}),
    ("se_readonly", _r(r"\b(read.?only|deterministic retrieval|explore public|guidance)\b"),
     {"side_effects": "read"}),
]


def apply_desc_rules(role, fired):
    verbs, se, evidence = set(), None, []
    for rid, rx, contrib in DESC_RULES:
        m = rx.search(role or "")
        if not m:
            continue
        fired[rid] += 1
        verbs.update(contrib.get("verbs", []))
        if contrib.get("side_effects"):
            se = contrib["side_effects"] if se is None else worst(se, contrib["side_effects"])
        evidence.append({"rule": rid, "span": m.group(0)})
    return verbs, se, evidence


# ---------------------------------------------------------------------------
# Capabilities
# ---------------------------------------------------------------------------

def resolve_capabilities(conn, caps_data, researched):
    """Return (capabilities, provenance dict) for one connector."""
    vocab = caps_data["capabilities"]
    arch = conn["archetype"]
    prov = {}
    caps = []
    for c in caps_data["archetype_map"].get(arch, []):
        caps.append(c)
        prov[c] = "archetype:" + arch

    hay = (conn.get("name", "") + " " + conn.get("role", ""))
    for rule in caps_data.get("refine_rules", []):
        w = rule["when"]
        if "archetype_in" in w and arch not in w["archetype_in"]:
            continue
        if "text_matches" in w and not re.search(w["text_matches"], hay, re.I):
            continue
        act = rule["action"]
        if "set" in act:
            caps = []
            prov = {}
            for c in act["set"]:
                caps.append(c)
                prov[c] = "refine:" + rule["id"]
        if "add" in act:
            for c in act["add"]:
                if c not in caps:
                    caps.append(c)
                    prov[c] = "refine:" + rule["id"]

    r = researched.get(conn["id"])
    if r and r.get("capabilities"):
        caps = list(r["capabilities"])
        prov = {c: "researched" for c in caps}

    # keep only known capabilities; guarantee at least one
    caps = [c for c in caps if c in vocab]
    if not caps:
        caps = ["vertical"]
        prov["vertical"] = "fallback"
    # dedupe preserving order
    seen, out = set(), []
    for c in caps:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out, {c: prov.get(c, "archetype:" + arch) for c in out}


# ---------------------------------------------------------------------------
# Per-connector inference
# ---------------------------------------------------------------------------

def clean_role(role):
    role = (role or "").strip()
    return role


def infer_one(conn, vendor, priors, caps_data, researched, fired):
    role = conn.get("role", "")
    prof = {
        "id": conn["id"],
        "name": conn["name"],
        "role": role,
        "archetype": conn["archetype"],
    }
    verb_prov = defaultdict(list)
    evidence = []

    # --- verbs + side effects: description rules ---
    verbs, se, desc_ev = apply_desc_rules(role, fired)
    evidence.extend(desc_ev)
    for v in verbs:
        verb_prov[v].append("description")

    # --- vendor knowledge ---
    vr = vendor.get(conn["id"])
    if vr:
        for v in vr.get("verbs", []):
            if v not in verbs:
                verb_prov[v].append("vendor")
            verbs.add(v)
        if vr.get("side_effects"):
            se = vr["side_effects"] if se is None else worst(se, vr["side_effects"])
        evidence.append({"rule": "vendor:" + conn["id"], "span": vr.get("why", "vendor knowledge")})

    # --- archetype prior fills only what is still empty ---
    prior = priors.get(conn["archetype"], {})
    used_prior = False
    if not verbs:
        for v in prior.get("verbs", []):
            verbs.add(v)
            verb_prov[v].append("archetype_prior")
        used_prior = True
    if se is None:
        se = prior.get("side_effects", "read")
        used_prior = True

    verbs = sorted(verbs) or ["read"]
    verb_side_effects = {v: VERB_SE.get(v, "read") for v in verbs}

    # --- capabilities ---
    caps, cap_prov = resolve_capabilities(conn, caps_data, researched)

    # --- function statement: source + confidence ---
    r = researched.get(conn["id"])
    if r:
        function_text = r["function"]
        source = r.get("source", "researched")
        confidence = "DOCUMENTED"
    elif vr:
        function_text = clean_role(role) or conn["name"]
        source = "vendor_knowledge"
        confidence = vr.get("confidence", "DOCUMENTED")
    else:
        function_text = clean_role(role) or conn["name"]
        source = "directory"
        confidence = "DIRECTORY" if desc_ev else "ASSUMED"

    prof["verbs"] = verbs
    prof["side_effects"] = se
    prof["verb_side_effects"] = verb_side_effects
    prof["capabilities"] = caps
    prof["function"] = {"text": function_text, "source": source}
    prof["confidence"] = confidence
    prof["provenance"] = {
        "verbs": {v: verb_prov.get(v, ["archetype_prior"]) for v in verbs},
        "capabilities": cap_prov,
    }
    prof["evidence"] = evidence
    prof["used_archetype_prior"] = used_prior
    return prof


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_source_registry(explicit):
    """Prefer the skill's full registry; fall back to the committed inferred registry
    (which also carries name/role/archetype) so the engine runs without the skill dir."""
    if explicit and os.path.exists(explicit):
        return load_json(explicit), explicit
    cand = os.path.join(SKILL, "registry_full.json")
    if os.path.exists(cand):
        return load_json(cand), cand
    fallback = os.path.join(DATA, "registry_inferred.json")
    return load_json(fallback), fallback


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "registry_inferred.json"))
    ap.add_argument("--registry", default=None)
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    reg, src = load_source_registry(args.registry)
    priors = load_json(os.path.join(DATA, "archetype_priors.json"))["priors"]
    vendor = load_json(os.path.join(DATA, "vendor_rules.json"))["rules"]
    caps_data = load_json(os.path.join(DATA, "capabilities.json"))
    researched = load_json(os.path.join(DATA, "researched.json"))["entries"]

    fired = Counter()
    profiles = [infer_one(c, vendor, priors, caps_data, researched, fired)
                for c in reg["connectors"]]

    out = {
        "_schema": {
            "generated_by": "engine/infer.py",
            "source_registry": src,
            "vendor_rules_applied": sum(1 for p in profiles
                                        if any(e["rule"].startswith("vendor:") for e in p["evidence"])),
            "researched": len(researched),
            "capability_vocabulary": sorted(caps_data["capabilities"]),
            "note": "Each connector: a function statement (text+source), functional capability "
                    "tags, and per-verb side effects. emits/consumes join keys are intentionally "
                    "absent -- capabilities, not keys, drive use-case composition.",
        },
        "connectors": profiles,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)

    if args.report:
        report(profiles, caps_data, researched, src)
    return 0


def report(profiles, caps_data, researched, src):
    n = len(profiles)
    vocab = caps_data["capabilities"]
    have_fn = sum(1 for p in profiles if p["function"]["text"].strip())
    have_cap = sum(1 for p in profiles if p["capabilities"])
    have_vse = sum(1 for p in profiles if p["verb_side_effects"])
    # a connector is "thin/unresolved" if its function text is uselessly short and not researched
    thin = [p for p in profiles
            if len(p["function"]["text"].strip()) < 12 and p["id"] not in researched]
    src_counts = Counter(p["function"]["source"] for p in profiles)
    conf_counts = Counter(p["confidence"] for p in profiles)

    print(f"source registry          : {src}")
    print(f"connectors               : {n}")
    print(f"have function statement   : {have_fn}/{n}")
    print(f"have >=1 capability       : {have_cap}/{n}")
    print(f"have per-verb side effects: {have_vse}/{n}")
    print(f"researched (terse remainder): {len(researched)}")
    print(f"still thin / unresolved   : {len(thin)}  {[p['name'] for p in thin] or '-- none'}")
    print("\nfunction source:")
    for s, c in src_counts.most_common():
        print(f"  {s:16s} {c:4d}")
    print("\nconfidence:")
    for s, c in conf_counts.most_common():
        print(f"  {s:16s} {c:4d}")

    capc = Counter(c for p in profiles for c in p["capabilities"])
    print(f"\ncapabilities in use: {len(capc)}/{len(vocab)}")
    unused = sorted(set(vocab) - set(capc))
    if unused:
        print(f"  unused: {unused}")
    domc = Counter(vocab[c]["domain"] for p in profiles for c in p["capabilities"])
    print("\nconnectors touching each domain:")
    for d, c in domc.most_common():
        print(f"  {d:12s} {c:4d}")
    print("\ntop capabilities:")
    for c, k in capc.most_common(12):
        print(f"  {c:20s} {k:4d}  {vocab[c]['label']}")


if __name__ == "__main__":
    sys.exit(main())
