#!/usr/bin/env python3
"""Scored composition engine over the inferred connector profiles.

Replaces the boolean "do these two share a key" edge, which fired for 73% of all
820x819 ordered pairs and therefore carried almost no information, with a score in
[0,1] built from key specificity, direction fit, confidence tier and side-effect risk.

Pathfinding is Dijkstra over -log(score), so the existing bridge search behaviour is
preserved: a high-scoring edge is a short edge.

Usage:
    python3 compose.py path "Gmail" "Todoist"
    python3 compose.py edges "Gmail" --top 15
    python3 compose.py hubs --top 20
    python3 compose.py density
"""

import argparse
import heapq
import json
import math
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

WEAK = {"person", "vendor_id", "handle"}

# Qualifier keys align records that are ALREADY joined; they do not identify anything.
# Two connectors that share only a timestamp are not composable in any useful sense --
# "both of these have dates on them" is true of most of the directory. Treating timestamp
# as a primary join let Todoist -> Oxford Economics outscore real compositions.
QUALIFIER = {"timestamp"}
QUALIFIER_ONLY_PENALTY = 0.15

TIER_WEIGHT = {"VERIFIED": 1.0, "DOCUMENTED": 0.9, "DIRECTORY": 0.7, "ASSUMED": 0.5}

# Verbs that mean "this connector can hand a value outward"
OUT_VERBS = {"read", "search", "export"}
# Verbs that mean "this connector can take a value inward and act on it"
IN_VERBS = {"create", "update", "delete", "execute"}

SIDE_EFFECT_RISK = {"read": 0.0, "create": 0.10, "mutate": 0.20, "irreversible": 0.35}

# Wildcard bridges: they connect to everything, so an unpenalised path through them is
# always "shortest" and always useless. Same stance as the skill's atlas.py.
HUB_IDS = {"zapier", "make", "n8n", "ifttt", "workato", "tray_ai", "tines", "natoma"}
FALLBACK_IDS = {"control_chrome", "kapture_browser_automation", "desktop_commander",
                "control_your_mac", "remote_desktop_commander", "filesystem", "apify"}


def load(path=None):
    path = path or os.path.join(DATA, "registry_inferred.json")
    with open(path, encoding="utf-8") as fh:
        reg = json.load(fh)
    return reg["connectors"]


def specificity(conns):
    """1 - prevalence. A key almost everyone emits is nearly worthless as a join."""
    n = len(conns)
    emit = Counter()
    for c in conns:
        emit.update(c["emits"])
    spec = {}
    for k, v in emit.items():
        spec[k] = 1.0 - (v / n)
    return spec


# Keys whose content Claude can author from prose. If b consumes one of these and a can
# emit anything readable, the pair composes through Claude as adapter even with no shared
# key -- the INFERRED hop of composition.md. It is lossy and belongs in output labelled as
# such, which is why it is capped well below a real key join rather than omitted.
AUTHORABLE = {"project", "rows:tabular", "file:ref", "file:blob", "email", "code", "image"}
INFERRED_BASE = 0.30


def score_edge(a, b, spec):
    """Score a directed composition a -> b. Returns (score, detail) or (0, None).

    detail["mode"] is "direct" (a real shared identifying key), "qualifier" (the only
    shared key merely aligns records, e.g. a timestamp) or "inferred" (no shared key;
    Claude adapts prose into what b accepts).
    """
    shared = sorted(set(a["emits"]) & set(b["consumes"]))
    if not shared:
        return _inferred_edge(a, b)

    # Direction fit: a must be able to read something out, b must be able to take it in.
    a_out = bool(set(a["verbs"]) & OUT_VERBS)
    b_in = bool(set(b["verbs"]) & IN_VERBS)
    b_read = bool(set(b["verbs"]) & OUT_VERBS)
    if a_out and b_in:
        direction = 1.0
    elif a_out and b_read:
        direction = 0.55        # b can only look the value up, not act on it
    else:
        direction = 0.25

    # Key contribution: best key dominates, extra keys add a little corroboration.
    best_key, best_val = None, 0.0
    for k in shared:
        v = spec.get(k, 0.5)
        if k in WEAK:
            # Opaque ids and handles only join within a vendor or via a crosswalk table.
            v *= 0.25
        if v > best_val:
            best_key, best_val = k, v
    corroboration = 1.0 + 0.06 * (len(shared) - 1)
    key_component = min(1.0, best_val * corroboration)

    # If every shared key is a qualifier there is no identifying join. Fall back to the
    # inferred-adapter route and keep whichever reading is stronger, so a pair like
    # Gmail -> Todoist is scored as the lossy adapter hop it actually is rather than as a
    # spurious timestamp join.
    mode = "direct"
    if all(k in QUALIFIER for k in shared):
        key_component *= QUALIFIER_ONLY_PENALTY
        mode = "qualifier"
        inf_score, inf_detail = _inferred_edge(a, b)
    else:
        inf_score, inf_detail = 0.0, None

    tier = min(TIER_WEIGHT.get(a["confidence"], 0.5), TIER_WEIGHT.get(b["confidence"], 0.5))
    risk = SIDE_EFFECT_RISK.get(b["side_effects"], 0.2)

    score = key_component * direction * tier * (1.0 - risk)

    if b["id"] in HUB_IDS or a["id"] in HUB_IDS:
        score *= 0.35
    elif b["id"] in FALLBACK_IDS or a["id"] in FALLBACK_IDS:
        score *= 0.6

    detail = {
        "mode": mode,
        "keys": shared,
        "join_key": best_key,
        "specificity": round(best_val, 3),
        "direction": direction,
        "tier": min(a["confidence"], b["confidence"], key=lambda t: TIER_WEIGHT.get(t, 0.5)),
        "side_effects": b["side_effects"],
        "score": round(score, 4),
    }
    if inf_score > score:
        return inf_score, inf_detail
    return score, detail


def _inferred_edge(a, b):
    """Claude-as-adapter hop: no shared key, but b accepts something Claude can author."""
    targets = sorted(set(b["consumes"]) & AUTHORABLE)
    if not targets:
        return 0.0, None
    if not (set(a["verbs"]) & OUT_VERBS):
        return 0.0, None
    if not (set(b["verbs"]) & IN_VERBS):
        return 0.0, None
    tier = min(TIER_WEIGHT.get(a["confidence"], 0.5), TIER_WEIGHT.get(b["confidence"], 0.5))
    risk = SIDE_EFFECT_RISK.get(b["side_effects"], 0.2)
    score = INFERRED_BASE * tier * (1.0 - risk)
    if b["id"] in HUB_IDS or a["id"] in HUB_IDS:
        score *= 0.35
    elif b["id"] in FALLBACK_IDS or a["id"] in FALLBACK_IDS:
        score *= 0.6
    detail = {
        "mode": "inferred",
        "keys": [],
        "join_key": "claude-adapter -> " + "/".join(targets[:3]),
        "specificity": 0.0,
        "direction": 1.0,
        "tier": min(a["confidence"], b["confidence"], key=lambda t: TIER_WEIGHT.get(t, 0.5)),
        "side_effects": b["side_effects"],
        "score": round(score, 4),
        "lossy": True,
    }
    return score, detail


def build_index(conns):
    return {c["id"]: c for c in conns}


def resolve(conns, query):
    q = query.strip().lower()
    for c in conns:
        if c["id"] == q or c["name"].lower() == q:
            return c
    hits = [c for c in conns if q in c["name"].lower() or q in c["id"]]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        raise SystemExit(f"no connector matches {query!r}")
    raise SystemExit(f"{query!r} is ambiguous: " + ", ".join(h["name"] for h in hits[:10]))


def out_edges(conns, spec, a, threshold=0.02):
    res = []
    for b in conns:
        if b["id"] == a["id"]:
            continue
        s, d = score_edge(a, b, spec)
        if s >= threshold:
            res.append((s, b, d))
    res.sort(key=lambda t: -t[0])
    return res


def shortest_path(conns, spec, src, dst, k=3, beam=25):
    """Dijkstra over -log(score), beam-limited per node to keep 820 nodes tractable."""
    adj_cache = {}

    def neighbours(node):
        if node["id"] not in adj_cache:
            adj_cache[node["id"]] = out_edges(conns, spec, node)[:beam]
        return adj_cache[node["id"]]

    pq = [(0.0, [src["id"]], [])]
    best = {}
    found = []
    seen_paths = set()
    while pq and len(found) < k:
        cost, path, details = heapq.heappop(pq)
        cur = path[-1]
        if cur == dst["id"]:
            t = tuple(path)
            if t not in seen_paths:
                seen_paths.add(t)
                found.append((cost, path, details))
            continue
        if len(path) > 4:
            continue
        if best.get(cur, 1e9) < cost - 1e-9 and cur != src["id"]:
            continue
        best[cur] = min(best.get(cur, 1e9), cost)
        idx = build_index(conns)
        for s, b, d in neighbours(idx[cur]):
            if b["id"] in path:
                continue
            heapq.heappush(pq, (cost - math.log(max(s, 1e-6)), path + [b["id"]], details + [d]))
    return found


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------

def cmd_edges(args):
    conns = load()
    spec = specificity(conns)
    a = resolve(conns, args.src)
    print(f"{a['name']}  [{a['archetype']}]  {a['confidence']}")
    print(f"  emits    : {', '.join(a['emits']) or '-'}")
    print(f"  consumes : {', '.join(a['consumes']) or '-'}")
    print(f"  verbs    : {', '.join(a['verbs'])}   side effects: {a['side_effects']}")
    print(f"\ntop {args.top} outbound compositions:")
    for s, b, d in out_edges(conns, spec, a)[:args.top]:
        print(f"  {s:.3f}  -> {b['name'][:34]:36s} via {d['join_key']:14s} "
              f"(spec {d['specificity']:.2f}, {d['side_effects']})")
    return 0


def cmd_path(args):
    conns = load()
    spec = specificity(conns)
    a = resolve(conns, args.src)
    b = resolve(conns, args.dst)
    direct, detail = score_edge(a, b, spec)
    print(f"{a['name']} -> {b['name']}")
    if direct > 0:
        mode = detail["mode"]
        print(f"\n{mode.upper()}  score {direct:.3f}")
        if mode == "inferred":
            print("  no shared key — Claude adapts prose into what the target accepts.")
            print("  LOSSY: label this hop as inferred and put the human check here.")
        elif mode == "qualifier":
            print("  the only shared key aligns records, it does not identify them.")
        print(f"  join keys    : {', '.join(detail['keys']) or '(none)'}")
        print(f"  best key     : {detail['join_key']} (specificity {detail['specificity']})")
        print(f"  direction fit: {detail['direction']}")
        print(f"  weakest tier : {detail['tier']}")
        print(f"  side effects : {detail['side_effects']}")
    else:
        print("\nNo direct edge: nothing this emits is consumed by that.")
    print("\nBRIDGED paths:")
    idx = build_index(conns)
    for cost, path, details in shortest_path(conns, spec, a, b):
        eff = math.exp(-cost)
        names = " -> ".join(idx[p]["name"] for p in path)
        keys = " / ".join(d["join_key"] for d in details)
        print(f"  [{eff:.4f}] {names}")
        print(f"            keys: {keys}")
    return 0


def cmd_hubs(args):
    conns = load()
    spec = specificity(conns)
    scores = []
    for a in conns:
        tot = sum(s for s, _, _ in out_edges(conns, spec, a, threshold=0.15))
        scores.append((tot, a))
    scores.sort(key=lambda t: -t[0])
    print(f"top {args.top} connectors by outbound composition weight (score >= 0.15):")
    for tot, a in scores[:args.top]:
        tag = " (hub)" if a["id"] in HUB_IDS else (" (fallback)" if a["id"] in FALLBACK_IDS else "")
        print(f"  {tot:8.1f}  {a['name'][:36]:38s} [{a['archetype']}]{tag}")
    return 0


def cmd_density(args):
    conns = load()
    spec = specificity(conns)
    n = len(conns)
    total = n * (n - 1)
    buckets = Counter()
    nonzero = 0
    for a in conns:
        for b in conns:
            if a["id"] == b["id"]:
                continue
            s, _ = score_edge(a, b, spec)
            if s > 0:
                nonzero += 1
            if s >= 0.5:
                buckets[">=0.50"] += 1
            elif s >= 0.3:
                buckets["0.30-0.50"] += 1
            elif s >= 0.15:
                buckets["0.15-0.30"] += 1
            elif s > 0:
                buckets["0-0.15"] += 1
    print(f"ordered pairs            : {total:,}")
    print(f"pairs with any shared key: {nonzero:,} ({nonzero*100//total}%)")
    print("score distribution:")
    for k in [">=0.50", "0.30-0.50", "0.15-0.30", "0-0.15"]:
        v = buckets[k]
        print(f"  {k:12s} {v:8,}  {v*100/total:5.1f}%")
    strong = buckets[">=0.50"] + buckets["0.30-0.50"]
    print(f"\nactionable edges (>=0.30): {strong:,} ({strong*100/total:.1f}%)")
    print("baseline for comparison  : 490,299 (73.0%) boolean edges in the shipped registry")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("path"); p.add_argument("src"); p.add_argument("dst"); p.set_defaults(fn=cmd_path)
    p = sub.add_parser("edges"); p.add_argument("src"); p.add_argument("--top", type=int, default=15); p.set_defaults(fn=cmd_edges)
    p = sub.add_parser("hubs"); p.add_argument("--top", type=int, default=20); p.set_defaults(fn=cmd_hubs)
    p = sub.add_parser("density"); p.set_defaults(fn=cmd_density)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
