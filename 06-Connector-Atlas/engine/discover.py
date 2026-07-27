#!/usr/bin/env python3
"""Discover use cases across scales — the heart of the atlas.

Follows Jani's method: start at Claude + 2 connectors and grow. Discovery is
capability-guided (we compose over the ~50-tag capability vocabulary, then instantiate
with representative connectors) so we never brute-force 820^2. Every candidate is judged
by usecase.py; only the combos that cohere are surfaced, each named with its why.

    small  (2-5)    many sharp use cases  (Inbox-to-Action Desk, Research Desk, ...)
    medium (6-20)   a whole domain desk   (a Sales desk, a Finance back office, ...)
    large  (30-200) broad systems         (a GTM engine; a system that runs like a company)

Output: reports/USE-CASES.md (the catalogue, small->huge, each with why) and
data/usecases.json (the same catalogue, for the renderer).

Usage:
    python3 discover.py [--write-report]
"""

import argparse
import json
import os
import sys

from usecase import Atlas, CONF_RANK

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
REPORTS = os.path.join(HERE, "..", "reports")

# A canonical representative connector per capability — curation for a legible gallery,
# NOT a popularity ranking (popularity is deliberately not a signal in this atlas). Any
# capability absent here falls back to a deterministic scored pick.
PREFERRED = {
    "email": "gmail", "calendar": "google_calendar", "messaging": "slack",
    "files": "google_drive", "transcribe_meeting": "fireflies", "desktop": "filesystem",
    "tasks": "todoist", "automate_hub": "make", "browser": "apify",
    "crm": "hubspot", "enrich_company": "clay", "discover_companies": "zoominfo",
    "outreach": "klaviyo", "marketing_analytics": "semrush", "social_media": "bitly", "forms": "surveymonkey",
    "payments": "stripe", "accounting": "xero", "invoicing": "sequence", "trading": "interactive_brokers_ibkr",
    "code": "sourcegraph", "deploy": "replit", "cloud_infra": "vercel", "observability": "datadog",
    "security": "snyk_security", "identity": "clerk", "ai_tools": "syntitan",
    "support_desk": "intercom", "ats_hiring": "ashby", "job_search": "indeed", "payroll": "gusto",
    "database": "snowflake", "bi_visualize": "tableau", "market_data": "fmp", "weather_geo": "tomtom_maps",
    "legal_research": "harvey", "esign": "docusign",
    "design": "canva", "diagramming": "figma", "presentations": "gamma", "media_gen": "elevenlabs",
    "web_search": "exa", "research_science": "pubmed", "public_data": "anthropic_economic_index",
    "knowledge_base": "mem0", "notes_docs": "notion", "education": "o_reilly",
}

DOMAIN_DESK = {
    "sales": "Sales Desk", "marketing": "Marketing Studio", "finance": "Finance Back Office",
    "product_eng": "Product & Engineering Loop", "support": "Support Desk",
    "hr": "People & Hiring Ops", "ops": "Operations Hub", "data_bi": "Data & BI Cockpit",
    "legal": "Legal Ops", "comms": "Comms Command Center", "design": "Creative Studio",
    "research": "Research Desk",
}


class Discover:
    def __init__(self):
        self.a = Atlas()
        self.CAP = self.a.CAP
        self.doms = self.a.doms
        self.best = self._best_for_cap()

    def _best_for_cap(self):
        """A recognisable representative connector per capability: prefer documented
        vendor knowledge, then shorter (more canonical) names."""
        best = {}
        for cap, conns in self.a.by_cap.items():
            ordered = sorted(conns, key=lambda c: (CONF_RANK.get(c["confidence"], 1),
                                                    len(c["capabilities"]) == 1,
                                                    -len(c["name"])), reverse=True)
            best[cap] = ordered
        return best

    def pick(self, cap, taken):
        pref = PREFERRED.get(cap)
        if pref and pref in self.a.by_id and pref not in taken and cap in self.a.by_id[pref]["capabilities"]:
            return self.a.by_id[pref]
        for c in self.best.get(cap, []):
            if c["id"] not in taken:
                return c
        return self.best.get(cap, [None])[0]

    def caps_in_domain(self, d):
        return [cap for cap, meta in self.CAP.items() if meta["domain"] == d]

    # -- small: instantiate each naming pattern with representative connectors --
    def small(self):
        from usecase import PATTERNS
        out = []
        seen = set()
        for pat in PATTERNS:
            taken, names = set(), []
            for group in pat["need"]:
                cap = next((c for c in group if self.best.get(c)), None)
                if not cap:
                    break
                c = self.pick(cap, taken)
                if c:
                    taken.add(c["id"])
                    names.append(c["name"])
            if len(names) < 2:
                continue
            key = frozenset(names)
            if key in seen:
                continue
            r = self.a.evaluate(names)
            if r["rating"] in ("strong", "partial"):
                seen.add(key)
                out.append(r)
        return out

    # -- medium: a whole domain desk (domain caps + coordinating glue) --
    def medium(self):
        glue = ["email", "messaging", "tasks", "notes_docs"]
        out, seen = [], set()
        for d in self.doms:
            caps = self.caps_in_domain(d)
            if d not in ("comms", "research"):
                caps = caps + [g for g in glue if self.CAP[g]["domain"] != d]
            taken, names = set(), []
            for cap in caps:
                c = self.pick(cap, taken)
                if c:
                    taken.add(c["id"])
                    names.append(c["name"])
            if len(names) < 4:
                continue
            r = self.a.evaluate(names)
            if r["rating"] not in ("strong", "partial") or r["scale"] < 4:
                continue
            key = frozenset(m["id"] for m in r["members"])
            if key in seen:
                continue
            seen.add(key)
            out.append(self._name_domain(r, d))
        return out

    # -- large: broad multi-domain systems --
    def large(self):
        gtm = ["sales", "marketing", "support", "comms", "finance", "data_bi"]
        back = ["finance", "hr", "legal", "ops", "comms", "data_bi"]
        allcaps = list(self.CAP.keys())
        out = [
            self._cover([c for d in gtm for c in self.caps_in_domain(d)], "gtm",
                        "GTM Engine",
                        "Claude runs the whole go-to-market motion — lead discovery, CRM, outbound, "
                        "support and the money — as one system it coordinates end to end."),
            self._cover([c for d in back for c in self.caps_in_domain(d)] + ["email", "tasks", "notes_docs"],
                        "backoffice", "Back-Office Operation",
                        "Claude runs the back office — books and payments, people and payroll, "
                        "contracts and the data behind them — from one seat."),
            # the showpiece: the best connector for every capability across all 12 domains —
            # genuinely huge and clean, Claude orchestrating between every part.
            self._cover(allcaps, "company", "Runs like a company",
                        "The functional surface of a whole operation: Claude + a connector for every "
                        "capability across all twelve domains, with Claude orchestrating between every part.",
                        per_cap=1, featured=True),
        ]
        return [r for r in out if r["rating"] in ("strong", "partial")]

    def _cap_picks(self, cap, taken, n):
        """Up to n distinct connectors for a capability, preferred representative first."""
        seq, out = [], []
        pref = PREFERRED.get(cap)
        if pref in self.a.by_id and cap in self.a.by_id[pref]["capabilities"]:
            seq.append(self.a.by_id[pref])
        seen = {c["id"] for c in seq}
        seq += [c for c in self.best.get(cap, []) if c["id"] not in seen]
        for c in seq:
            if c["id"] not in taken:
                taken.add(c["id"])
                out.append(c)
                if len(out) >= n:
                    break
        return out

    def _cover(self, caps, label, name, why, per_cap=1, featured=False):
        taken, names = set(), []
        for cap in caps:
            for c in self._cap_picks(cap, taken, per_cap):
                names.append(c["name"])
        r = self.a.evaluate(names)
        n = r["n_domains"]
        dl = ", ".join(self.doms[d]["label"] for d in r["domains"])
        r["name"] = name
        r["why_short"] = f"{why} Spans {n} of 12 domains ({dl})."
        r["scale_note"] = f"{len(names)} connectors in · {r['scale']} kept as the coherent core · {n}/12 domains."
        r["featured"] = featured
        return r

    def _name_domain(self, r, d):
        label = self.doms[d]["label"]
        r["name"] = DOMAIN_DESK.get(d, f"{label} desk")
        caplabels = ", ".join(self.CAP[c]["label"] for c in r["capabilities_covered"])
        r["why_short"] = (f"Claude runs a whole {label} operation — {caplabels} — coordinating across "
                          f"all of it from the centre.")
        return r

    def run(self):
        cat = {"small": self.small(), "medium": self.medium(), "large": self.large()}
        # order each tier by potential (strongest first) so every section leads with its best
        flat = []
        for tier in ("small", "medium", "large"):
            for r in sorted(cat[tier], key=lambda x: -x["potential"]["total"]):
                r["tier"] = tier
                flat.append(r)
        return flat


def to_catalogue(usecases):
    """Trim evaluate() output to what the report and renderer need."""
    out = []
    for r in usecases:
        out.append({
            "tier": r["tier"], "name": r["name"], "rating": r["rating"],
            "why_short": r["why_short"], "scale": r["scale"], "n_domains": r["n_domains"],
            "domains": r["domains"], "scale_note": r.get("scale_note"),
            "potential": r["potential"], "featured": r.get("featured", False),
            "members": [{"name": m["name"], "id": m["id"], "capabilities": m["capabilities"],
                         "role": m["role"], "side_effect": m["side_effect"],
                         "function": m.get("function", "")} for m in r["members"]],
            "dropped": [{"name": d["name"], "status": d["status"], "reason": d["reason"]}
                        for d in r["dropped"]],
            "side_effects": r["side_effects"], "capabilities_covered": r["capabilities_covered"],
        })
    return out


def write_report(cat, path):
    doms = Atlas().doms
    lines = ["# Connector Atlas — the use-case catalogue",
             "",
             "> Claude is the brain in the centre. Each entry below is a **working** combination: "
             "Claude + a set of connectors that cohere into a use case a person would actually want. "
             "We surface only what works, name it, and say **why**. Ordered small → huge.",
             ""]
    tier_titles = {"small": "## Small — Claude + 2–5 connectors",
                   "medium": "## Medium — Claude + a whole domain desk",
                   "large": "## Large — Claude + a big combination that can run like a company"}
    last_tier = None
    for r in cat:
        if r["tier"] != last_tier:
            lines += ["", tier_titles[r["tier"]], ""]
            last_tier = r["tier"]
        badge = {"strong": "●", "partial": "◐"}[r["rating"]]
        star = "★ " if r.get("featured") else ""
        p = r["potential"]
        lines.append(f"### {star}{badge} {r['name']}  ·  potential {p['total']}/100 · "
                     f"{r['scale']} connectors · {r['n_domains']}/12 domains · {r['rating']}")
        lines.append("")
        lines.append(f"*{r['why_short']}*")
        lines.append("")
        lines.append(f"> potential {p['total']}/100 — applicability {p['applicability']} · "
                     f"leverage {p['leverage']} · reach {p['reach']} · tightness {p['tightness']}")
        lines.append("")
        if r.get("scale_note"):
            lines.append(f"> scale: {r['scale_note']}")
            lines.append("")
        lines.append("Connectors, and why each earns its place:")
        lines.append("")
        for m in r["members"][:40]:
            caps = ", ".join(m["capabilities"])
            lines.append(f"- **{m['name']}** — {caps} · *{m['role']}* · uses: {m['side_effect']}")
        if len(r["members"]) > 40:
            lines.append(f"- …and {len(r['members']) - 40} more")
        if r["dropped"]:
            lines.append("")
            lines.append("Left out (and why):")
            for d in r["dropped"][:12]:
                lines.append(f"- ~~{d['name']}~~ — {d['reason']}")
        se = r["side_effects"]
        lines.append("")
        lines.append(f"**Side effects** (only the verbs this use case actually uses): "
                     f"**{se['headline']}**  ·  read-only footprint: {se['observe']}")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-report", action="store_true")
    ap.add_argument("--out", default=os.path.join(DATA, "usecases.json"))
    args = ap.parse_args()

    d = Discover()
    usecases = d.run()
    cat = to_catalogue(usecases)

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump({"_schema": {"generated_by": "engine/discover.py",
                               "note": "Working use cases discovered by composing Claude + connector "
                                       "capabilities across scales. Only coherent combos are listed."},
                   "usecases": cat}, fh, indent=1, ensure_ascii=False)

    n = len(cat)
    by_tier = {}
    for r in cat:
        by_tier.setdefault(r["tier"], 0)
        by_tier[r["tier"]] += 1
    print(f"discovered {n} working use cases: "
          f"{by_tier.get('small',0)} small, {by_tier.get('medium',0)} medium, {by_tier.get('large',0)} large")
    for r in sorted(cat, key=lambda x: -x["potential"]["total"]):
        star = "★" if r.get("featured") else " "
        print(f"  {star}[{r['rating']:7s}] potential {r['potential']['total']:3d} · "
              f"{r['scale']:3d} conn · {r['n_domains']:2d}/12 dom · {r['name']}")

    if args.write_report:
        os.makedirs(REPORTS, exist_ok=True)
        write_report(cat, os.path.join(REPORTS, "USE-CASES.md"))
        print(f"\nwrote {os.path.join(REPORTS, 'USE-CASES.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
