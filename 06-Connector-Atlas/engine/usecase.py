#!/usr/bin/env python3
"""The core question: does Claude + {connectors} make a use case, and why?

Claude sits at the hub. For any subset of connectors this decides whether their
capabilities cohere into a workflow Claude can orchestrate, names the use case in one
plain sentence, explains why each connector earns its place, says which are dropped
(redundant / unrelated) and why, and reports the side effects of only the verbs the use
case actually uses.

No join keys. Coherence is judged on functional capabilities (data/capabilities.json):
whether the jobs the connectors do connect — through Claude — into a source -> action ->
output a person would actually want.

Usage:
    python3 usecase.py "Gmail" "Todoist"
    python3 usecase.py "Gmail" "Interactive Brokers"
    python3 usecase.py --json "Fireflies" "Todoist" "Notion"
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

SIDE_EFFECT_ORDER = ["read", "create", "mutate", "irreversible"]
READ_VERBS = {"read", "search", "export"}
VERB_SE = {"read": "read", "search": "read", "export": "read",
           "create": "create", "update": "mutate", "delete": "irreversible",
           "execute": "irreversible"}
CONF_RANK = {"DOCUMENTED": 3, "VERIFIED": 3, "DIRECTORY": 2, "ASSUMED": 1}


def worst(a, b):
    return a if SIDE_EFFECT_ORDER.index(a) >= SIDE_EFFECT_ORDER.index(b) else b


def load_json(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Naming patterns: sharp names for common shapes; generic fallback otherwise.
# A pattern matches when the combo's capabilities hit >=1 alternative in every group.
# ---------------------------------------------------------------------------

PATTERNS = [
    {"name": "Inbox-to-Action Desk", "need": [["email", "messaging", "support_desk", "forms"], ["tasks"]],
     "why": "Claude reads what comes in via {a} and turns it into tracked work in {b}."},
    {"name": "Meeting Follow-through", "need": [["transcribe_meeting"], ["tasks", "crm", "notes_docs", "email"]],
     "why": "Claude turns {a} into follow-ups and records in {b}."},
    {"name": "Research Desk", "need": [["web_search", "research_science", "public_data", "market_data"], ["notes_docs", "knowledge_base"]],
     "why": "Claude gathers evidence from {a} and writes a durable brief in {b}."},
    {"name": "Data-to-Dashboard", "need": [["database", "market_data", "public_data", "marketing_analytics"], ["bi_visualize"]],
     "why": "Claude queries {a} and builds the dashboard in {b}."},
    {"name": "Outbound Sales Desk", "need": [["discover_companies", "enrich_company"], ["crm", "outreach"]],
     "why": "Claude sources and enriches leads via {a} and runs outbound through {b}."},
    {"name": "Pipeline Cockpit", "need": [["crm"], ["outreach", "email", "calendar"]],
     "why": "Claude keeps the pipeline in {a} moving through {b}."},
    {"name": "Ship-it Dev Loop", "need": [["code"], ["deploy", "cloud_infra"]],
     "why": "Claude reads the repo in {a} and ships it via {b}."},
    {"name": "Incident War-room", "need": [["observability"], ["messaging", "tasks", "code"]],
     "why": "Claude watches {a} and drives the response through {b}."},
    {"name": "Finance Back Office", "need": [["payments", "accounting", "invoicing"], ["notes_docs", "bi_visualize", "email", "tasks", "database"]],
     "why": "Claude reconciles money movement in {a} and reports it through {b}."},
    {"name": "Storefront Ops", "need": [["ecommerce"], ["payments", "support_desk", "marketing_analytics", "shipping"]],
     "why": "Claude runs the store in {a} end to end with {b}."},
    {"name": "Content Studio", "need": [["design", "media_gen", "presentations", "diagramming"], ["social_media", "notes_docs", "files"]],
     "why": "Claude produces creative in {a} and ships it through {b}."},
    {"name": "Support Desk", "need": [["support_desk"], ["crm", "knowledge_base", "tasks"]],
     "why": "Claude resolves tickets in {a} with context from {b}."},
    {"name": "Recruiting Pipeline", "need": [["ats_hiring", "job_search"], ["email", "calendar", "esign", "payroll"]],
     "why": "Claude sources and screens in {a} and moves candidates through {b}."},
    {"name": "Legal Ops", "need": [["legal_research"], ["esign", "notes_docs"]],
     "why": "Claude researches and drafts from {a} and routes for signature via {b}."},
    {"name": "Trading Desk", "need": [["market_data"], ["trading"]],
     "why": "Claude researches markets in {a} and manages the book in {b}."},
    {"name": "Daily Brief", "need": [["email", "calendar", "messaging"], ["notes_docs", "knowledge_base"]],
     "why": "Claude assembles a brief from {a} into {b}."},
    {"name": "Knowledge Hub", "need": [["files", "notes_docs", "knowledge_base"], ["web_search"]],
     "why": "Claude keeps a living knowledge base in {a}, refreshed from {b}."},
]


class Atlas:
    def __init__(self):
        self.caps = load_json(os.path.join(DATA, "capabilities.json"))
        self.doms = load_json(os.path.join(DATA, "domains.json"))["domains"]
        reg = load_json(os.path.join(DATA, "registry_inferred.json"))
        self.CAP = self.caps["capabilities"]
        self.connectors = reg["connectors"]
        self.by_id = {c["id"]: c for c in self.connectors}
        self.by_name = {}
        for c in self.connectors:
            self.by_name.setdefault(c["name"].lower(), c)
        self.by_cap = {}
        for c in self.connectors:
            for cap in c["capabilities"]:
                self.by_cap.setdefault(cap, []).append(c)

    # --- capability linking -------------------------------------------------
    def domains_adjacent(self, d1, d2):
        return d2 in self.doms[d1]["adjacent"] or d1 in self.doms[d2]["adjacent"]

    def cap_link(self, a, b):
        """Do two capabilities connect, through Claude, into one workflow?"""
        if a == b:
            return False
        ca, cb = self.CAP[a], self.CAP[b]
        if b in ca.get("pairs_with", []) or a in cb.get("pairs_with", []):
            return True
        # Glue attaches broadly. Work/knowledge glue (reaches_specialist) reaches anything.
        # Communication glue (email/chat/calendar) reaches operational work but NOT the pure
        # data/knowledge islands (a brokerage, a markets feed, case-law, a research DB) — you
        # coordinate operational systems over chat, you don't casually email a data feed.
        if ca.get("glue") and (ca.get("reaches_specialist") or not cb.get("island")):
            return True
        if cb.get("glue") and (cb.get("reaches_specialist") or not ca.get("island")):
            return True
        if not ca.get("glue") and not cb.get("glue"):
            if ca.get("specialist") or cb.get("specialist"):
                return ca["domain"] == cb["domain"]
            if ca["domain"] == cb["domain"]:
                return True
            if self.domains_adjacent(ca["domain"], cb["domain"]):
                return True
        return False

    def conn_link(self, c1, c2):
        return any(self.cap_link(a, b) for a in c1["capabilities"] for b in c2["capabilities"])

    # --- resolution ---------------------------------------------------------
    def resolve(self, query):
        q = query.strip().lower()
        if q in self.by_name:
            return self.by_name[q]
        if q in self.by_id:
            return self.by_id[q]
        hits = [c for c in self.connectors if q in c["name"].lower()]
        if hits:
            hits.sort(key=lambda c: len(c["name"]))
            return hits[0]
        hits = [c for c in self.connectors if q in c["id"].lower()]
        return hits[0] if hits else None

    # --- helpers ------------------------------------------------------------
    def sink_score(self, conn):
        s = 0
        for cap in conn["capabilities"]:
            roles = self.CAP[cap]["roles"]
            s += ("output" in roles) + ("store" in roles) - ("input" in roles)
        return s

    def provides_input(self, conn):
        return any("input" in self.CAP[cap]["roles"] for cap in conn["capabilities"])

    def provides_output(self, conn):
        return any(("output" in self.CAP[cap]["roles"] or "store" in self.CAP[cap]["roles"])
                   for cap in conn["capabilities"])

    def connectors_by_component(self, conns):
        """Connected components under conn_link."""
        idx = {c["id"]: i for i, c in enumerate(conns)}
        parent = list(range(len(conns)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(len(conns)):
            for j in range(i + 1, len(conns)):
                if self.conn_link(conns[i], conns[j]):
                    union(i, j)
        comps = {}
        for c in conns:
            comps.setdefault(find(idx[c["id"]]), []).append(c)
        return list(comps.values())

    def conn_se_as(self, conn, role, mode):
        """Side effect of using a connector as 'source' or 'sink'. mode='observe' forces read.

        A source is read-only. A sink incurs only the write the workflow performs: creating
        or updating an output. A connector's ability to delete is not counted unless deleting
        is its only write. Sending / posting / paying / trading is irreversible even though it
        is technically a create — that nuance rides on the capability's irreversible_output."""
        if mode == "observe" or role == "source":
            return "read"
        verbs = conn["verbs"]
        se = "read"
        if "create" in verbs:
            se = worst(se, "create")
        if "update" in verbs:
            se = worst(se, "mutate")
        if se == "read" and ("execute" in verbs or "delete" in verbs):
            se = "create"  # a write of some kind, not auto-irreversible
        if any(self.CAP[cap].get("irreversible_output") for cap in conn["capabilities"]):
            se = worst(se, "irreversible")
        return se

    # --- naming -------------------------------------------------------------
    def _cap_conn_names(self, members, cap_group):
        names = []
        for m in members:
            if any(cap in cap_group for cap in m["conn"]["capabilities"]):
                names.append(m["conn"]["name"])
        return names

    def name_and_why(self, core_members, core_caps, domains, rating):
        best, best_score = None, 0
        for pat in PATTERNS:
            if all(any(c in core_caps for c in group) for group in pat["need"]):
                score = len(pat["need"]) + sum(1 for g in pat["need"] for c in g if c in core_caps) * 0.1
                if score > best_score:
                    best, best_score = pat, score
        if best:
            groups_named = []
            for group in best["need"]:
                ns = self._cap_conn_names(core_members, group)
                groups_named.append(", ".join(dict.fromkeys(ns)) or "them")
            why = best["why"]
            for i, letter in enumerate(["a", "b", "c", "d"]):
                if i < len(groups_named):
                    why = why.replace("{" + letter + "}", groups_named[i])
            return best["name"], why
        # generic name from dominant domain + shape
        dlabel = self.doms[domains[0]]["label"] if domains else "Cross-domain"
        srcs = [m["conn"]["name"] for m in core_members if m["role"] == "source"]
        snks = [m["conn"]["name"] for m in core_members if m["role"] == "sink"]
        if snks and srcs:
            name = f"{dlabel} workflow"
            why = f"Claude turns {', '.join(srcs)} into {', '.join(snks)}."
        elif not snks:
            name = f"{dlabel} research"
            why = f"Claude synthesises {', '.join(srcs) or 'these sources'} and answers in chat."
        else:
            name = f"{dlabel} desk"
            why = f"Claude drives {', '.join(m['conn']['name'] for m in core_members)}."
        return name, why

    # --- the evaluation -----------------------------------------------------
    def evaluate(self, queries, mode="act"):
        resolved, unresolved = [], []
        for q in queries:
            c = self.resolve(q)
            (resolved if c else unresolved).append(c or q)
        # dedupe
        seen, conns = set(), []
        for c in resolved:
            if c["id"] not in seen:
                seen.add(c["id"])
                conns.append(c)

        result = {"input": list(queries), "unresolved": unresolved,
                  "resolved": [c["id"] for c in conns]}

        if len(conns) < 2:
            result.update(rating="non", name="—",
                          why_short="A combo needs at least two connectors for Claude to bridge.",
                          members=[], core=[], dropped=[], domains=[], n_domains=0, scale=len(conns),
                          why_long=[], side_effects={"headline": "read", "observe": "read", "per_connector": {}},
                          capabilities_covered=[])
            return result

        # 1. components -> keep the largest coherent one; the rest are unrelated
        comps = self.connectors_by_component(conns)
        comps.sort(key=lambda cc: (len(cc), any(self.provides_input(c) for c in cc) and
                                    any(self.provides_output(c) for c in cc)), reverse=True)
        main = comps[0]
        unrelated = [c for cc in comps[1:] for c in cc]

        # 2. redundancy: greedy set-cover by capability, best provider first
        def score(c):
            return (CONF_RANK.get(c["confidence"], 1), len(c["capabilities"]), -len(c["name"]))
        ordered = sorted(main, key=score, reverse=True)
        covered, core, redundant = set(), [], []
        for c in ordered:
            new = [cap for cap in c["capabilities"] if cap not in covered]
            if new:
                covered.update(c["capabilities"])
                core.append(c)
            else:
                redundant.append(c)

        # 3. roles (source/sink) over the core. Rank each connector by flow position:
        # pure-output (a campaign tool) leans sink, pure-input (a data feed) leans source, dual
        # systems (a CRM, a task list) sit between — sink-score breaks ties (a store leans sink).
        # A connector that produces output is the sink when some connector below it feeds in.
        def flow(c):
            return ((1 if self.provides_output(c) else 0) - (1 if self.provides_input(c) else 0),
                    self.sink_score(c))
        combined = {c["id"]: flow(c) for c in core}
        inputs = [c for c in core if self.provides_input(c)]
        min_src = min((combined[c["id"]] for c in inputs), default=None)
        members = []
        for c in core:
            is_sink = self.provides_output(c) and (min_src is None or combined[c["id"]] > min_src)
            role = "sink" if is_sink else ("source" if self.provides_input(c) else "sink")
            members.append({"conn": c, "role": role, "status": "core"})

        core_caps = sorted(covered)
        core_domains = []
        for cap in core_caps:
            d = self.CAP[cap]["domain"]
            if d not in core_domains:
                core_domains.append(d)
        core_domains.sort(key=lambda d: -sum(1 for cap in core_caps if self.CAP[cap]["domain"] == d))

        # 4. rating: strong = a full source -> act -> output pipeline across >=2 connectors;
        # partial = coheres but is read-only synthesis or missing a stage; non = no combo.
        sources = [m for m in members if m["role"] == "source"]
        sinks = [m for m in members if m["role"] == "sink"]
        has_input = any(self.provides_input(m["conn"]) for m in members)
        if len(core) < 2:
            rating = "non"
        elif has_input and sources and sinks:
            rating = "strong"
        else:
            rating = "partial"

        name, why_short = self.name_and_why(members, core_caps, core_domains, rating)
        if rating == "non":
            name, why_short = "—", "These connectors don't share a workflow Claude can bridge — they're separate use cases."

        # 5. side effects over verbs actually used
        per_conn, headline, observe = {}, "read", "read"
        for m in members:
            se = self.conn_se_as(m["conn"], m["role"], mode)
            per_conn[m["conn"]["id"]] = se
            headline = worst(headline, se)

        # assemble why_long + member records
        why_long = []
        member_out = []
        for m in members:
            c = m["conn"]
            caplabels = ", ".join(self.CAP[cap]["label"] for cap in c["capabilities"])
            why_long.append(f"{c['name']} — {caplabels} ({m['role']}): {c['function']['text']}")
            member_out.append({"id": c["id"], "name": c["name"], "capabilities": c["capabilities"],
                               "status": "core", "role": m["role"], "side_effect": per_conn[c["id"]]})
        dropped = []
        for c in redundant:
            dup = [cap for cap in c["capabilities"] if cap in covered]
            dropped.append({"id": c["id"], "name": c["name"], "capabilities": c["capabilities"],
                            "status": "fallback",
                            "reason": f"redundant: {', '.join(dup)} already covered — kept only as a fallback."})
        for c in unrelated:
            dropped.append({"id": c["id"], "name": c["name"], "capabilities": c["capabilities"],
                            "status": "unrelated",
                            "reason": "no capability links into this use case's workflow."})

        closing = self._closing(members, rating)
        result.update(
            rating=rating, name=name, why_short=why_short, why_long=why_long + [closing],
            members=member_out, core=[c["id"] for c in core], dropped=dropped,
            domains=core_domains, n_domains=len(core_domains), scale=len(core),
            side_effects={"headline": headline, "observe": observe, "per_connector": per_conn},
            capabilities_covered=core_caps)
        return result

    def _closing(self, members, rating):
        if rating == "non":
            return ""
        srcs = [m["conn"]["name"] for m in members if m["role"] == "source"]
        snks = [m["conn"]["name"] for m in members if m["role"] == "sink"]
        if srcs and snks:
            return (f"Claude is the brain in the middle: it reads {', '.join(srcs)}, reasons over it, "
                    f"and acts through {', '.join(snks)}.")
        return "Claude is the brain in the middle, reading these sources and reasoning across them in chat."


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_report(r):
    print(f"\n  {'='*66}")
    print(f"  USE CASE:  {r['name']}   [{r['rating'].upper()}]")
    print(f"  {'='*66}")
    if r["unresolved"]:
        print(f"  ! not found: {r['unresolved']}")
    print(f"  why: {r['why_short']}\n")
    if r["rating"] != "non":
        print(f"  members ({r['scale']} core, spans {r['n_domains']} domain(s): "
              f"{', '.join(r['domains'])}):")
    for m in r["members"]:
        print(f"    + {m['name']:26s} [{m['role']:6s}] {', '.join(m['capabilities'])}  ({m['side_effect']})")
    for d in r["dropped"]:
        tag = "fallback" if d["status"] == "fallback" else "dropped"
        print(f"    - {d['name']:26s} [{tag}] {d['reason']}")
    print()
    for line in r["why_long"]:
        if line:
            print(f"    · {line}")
    se = r["side_effects"]
    print(f"\n  side effects (verbs actually used): {se['headline'].upper()}   "
          f"| read-only footprint: {se['observe']}")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("connectors", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--observe", action="store_true", help="read-only footprint (no acting)")
    args = ap.parse_args()
    atlas = Atlas()
    r = atlas.evaluate(args.connectors, mode="observe" if args.observe else "act")
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        print_report(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
