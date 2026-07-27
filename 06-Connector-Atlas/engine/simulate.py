#!/usr/bin/env python3
"""Simulation harness.

Runs concrete situations through the scored engine and checks that what comes back
survives inspection: a route exists, its mode is at least as strong as the situation
needs, and no forbidden side effect appears anywhere in the chain.

A scenario failing is informative, not fatal -- the exit code is non-zero only when a
side-effect ban is violated, because that is the one failure that would matter in the
real world.

Usage:
    python3 simulate.py [--write-report]
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
SCEN = os.path.join(HERE, "..", "scenarios")
REPORTS = os.path.join(HERE, "..", "reports")

import compose  # noqa: E402

MODE_STRENGTH = {"none": 0, "qualifier": 1, "inferred": 2, "direct": 3}
SE_ORDER = ["read", "create", "mutate", "irreversible"]


def run_scenario(conns, spec, sc):
    hops = []
    unresolved = []
    resolved = []
    for name in sc["chain"]:
        try:
            resolved.append(compose.resolve(conns, name))
        except SystemExit:
            unresolved.append(name)
    if unresolved:
        return {"id": sc["id"], "status": "UNRESOLVED", "unresolved": unresolved,
                "hops": [], "weakest_mode": "none", "score": 0.0, "violations": []}

    for a, b in zip(resolved, resolved[1:]):
        s, d = compose.score_edge(a, b, spec)
        hops.append({
            "from": a["name"], "to": b["name"],
            "score": round(s, 3),
            "mode": (d or {}).get("mode", "none"),
            "join_key": (d or {}).get("join_key", "-"),
            "side_effects": b["side_effects"],
        })

    weakest = min((h["mode"] for h in hops), key=lambda m: MODE_STRENGTH[m]) if hops else "none"
    total = min((h["score"] for h in hops), default=0.0)

    violations = []
    for c in resolved:
        for banned in sc.get("forbid", []):
            if SE_ORDER.index(c["side_effects"]) >= SE_ORDER.index(banned):
                violations.append(f"{c['name']} is {c['side_effects']}, scenario forbids {banned}")

    want = sc.get("expect_mode", "any")
    if weakest == "none":
        status = "NO ROUTE"
    elif violations:
        status = "SIDE-EFFECT VIOLATION"
    elif want == "any" or MODE_STRENGTH[weakest] >= MODE_STRENGTH.get(want, 0):
        status = "OK"
    else:
        status = "WEAKER THAN EXPECTED"

    return {"id": sc["id"], "status": status, "hops": hops, "weakest_mode": weakest,
            "score": round(total, 3), "violations": violations, "unresolved": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-report", action="store_true")
    args = ap.parse_args()

    conns = compose.load()
    spec = compose.specificity(conns)
    with open(os.path.join(SCEN, "scenarios.json"), encoding="utf-8") as fh:
        blob = json.load(fh)
    scenarios = blob["scenarios"]
    by_id = {s["id"]: s for s in scenarios}

    results = [run_scenario(conns, spec, s) for s in scenarios]

    out = []
    def emit(line=""):
        out.append(line)
        print(line)

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    emit("# Scenario simulation")
    emit()
    emit(f"{len(results)} situations run through the scored engine "
         "(20 generic, 20 from Jani's ABM / HCMC-funnel / women-heavy-markets context).")
    emit()
    emit("| status | n |")
    emit("|---|---|")
    for k in sorted(counts, key=lambda x: -counts[x]):
        emit(f"| {k} | {counts[k]} |")
    emit()
    emit("`direct` = a real shared identifying key. `inferred` = no shared key; Claude "
         "adapts prose into what the target accepts (lossy, and the right place for a "
         "human check). `qualifier` = the only shared key merely aligns records.")
    emit()

    for r in results:
        sc = by_id[r["id"]]
        emit(f"### {r['id']} — {sc['need']}")
        emit()
        emit(f"*pattern:* {sc['expected_pattern']} · *status:* **{r['status']}** · "
             f"*weakest hop:* {r['weakest_mode']} · *min score:* {r['score']}")
        emit()
        if r["unresolved"]:
            emit(f"Not in the directory: {', '.join(r['unresolved'])}")
            emit()
            continue
        emit("| hop | mode | join | score | target side effects |")
        emit("|---|---|---|---|---|")
        for h in r["hops"]:
            emit(f"| {h['from']} → {h['to']} | {h['mode']} | `{h['join_key']}` | "
                 f"{h['score']} | {h['side_effects']} |")
        if r["violations"]:
            emit()
            for v in r["violations"]:
                emit(f"- **side-effect violation:** {v}")
        emit()

    violated = [r for r in results if r["status"] == "SIDE-EFFECT VIOLATION"]
    emit("## Outcome")
    emit()
    emit(f"- routes found: {sum(1 for r in results if r['weakest_mode'] != 'none')}/{len(results)}")
    emit(f"- every hop a real key join: {sum(1 for r in results if r['weakest_mode'] == 'direct')}")
    emit(f"- side-effect violations: {len(violated)}")

    if args.write_report:
        os.makedirs(REPORTS, exist_ok=True)
        with open(os.path.join(REPORTS, "SCENARIOS.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(out) + "\n")

    return 1 if violated else 0


if __name__ == "__main__":
    sys.exit(main())
