#!/usr/bin/env python3
"""Validate the discovery — evidence that the judgments are sound.

Not precision/recall on join keys (that machinery is gone). Instead:

  1. Coherence spot-checks  -- hand-labelled combos (makes a use case / doesn't); the engine
                               must agree, and its 'why' must be inspectable.
  2. Membership checks      -- a redundant connector must not raise a combo's rating and must
                               be labelled a fallback; a complementary one must extend it;
                               dropping a redundant member must not lower the use case.
  3. Coverage sanity        -- a 'runs like a company' system really spans most domains; a
                               small system is tight, with no dead members.
  4. Per-verb side effects  -- a read-only use case over a send-capable connector reports read;
                               a use case that actually sends/pays incurs irreversible.

Writes reports/VALIDATION.md and exits non-zero if anything fails.

Usage:
    python3 validate.py
"""

import os
import sys

from usecase import Atlas
from discover import Discover

HERE = os.path.dirname(os.path.abspath(__file__))
REPORTS = os.path.join(HERE, "..", "reports")
RANK = {"non": 0, "partial": 1, "strong": 2}


class Checks:
    def __init__(self):
        self.rows = []

    def ok(self, category, name, passed, detail):
        self.rows.append((category, name, bool(passed), detail))

    def passed(self):
        return all(r[2] for r in self.rows)


def run():
    a = Atlas()
    c = Checks()

    # -- 1. coherence spot-checks -------------------------------------------
    makes = [
        (["Gmail", "Todoist"], "inbox -> tasks"),
        (["Fireflies", "Todoist"], "meeting -> follow-ups"),
        (["Exa", "Notion"], "research -> written brief"),
        (["Slack", "Todoist"], "chat -> tasks"),
        (["Stripe", "Xero"], "payments -> books"),
        (["HubSpot", "Klaviyo"], "CRM -> outbound"),
        (["Shopify", "Stripe"], "store -> payments"),
    ]
    doesnt = [
        (["Gmail", "Interactive Brokers"], "inbox vs. a brokerage"),
        (["CoCounsel Legal", "MSCI"], "case law vs. a markets feed"),
        (["Gmail", "PubMed"], "inbox vs. a biomedical database"),
        (["Figma", "Interactive Brokers"], "whiteboard vs. a brokerage"),
    ]
    for names, label in makes:
        r = a.evaluate(names)
        c.ok("coherence", f"MAKES: {label}", r["rating"] in ("strong", "partial"),
             f"{names} → {r['rating'].upper()} — {r['why_short']}")
    for names, label in doesnt:
        r = a.evaluate(names)
        c.ok("coherence", f"DOESN'T: {label}", r["rating"] == "non",
             f"{names} → {r['rating'].upper()} — {r['why_short']}")

    # -- 2. membership checks -----------------------------------------------
    base = a.evaluate(["Gmail", "Todoist"])
    add_redundant = a.evaluate(["Gmail", "Todoist", "Asana"])
    fb = [d for d in add_redundant["dropped"] if d["status"] == "fallback"]
    c.ok("membership", "redundant add does not raise the rating",
         RANK[add_redundant["rating"]] <= RANK[base["rating"]],
         f"Gmail+Todoist={base['rating']} → +Asana={add_redundant['rating']}")
    c.ok("membership", "redundant connector is labelled a fallback",
         len(fb) == 1,
         f"dropped as fallback: {[d['name'] for d in fb]}")

    add_comp = a.evaluate(["Gmail", "Todoist", "Google Calendar"])
    c.ok("membership", "complementary add extends the use case",
         add_comp["scale"] > base["scale"] and RANK[add_comp["rating"]] >= RANK[base["rating"]],
         f"Gmail+Todoist core={base['scale']} → +Calendar core={add_comp['scale']} "
         f"({add_comp['rating']})")

    drop_red = a.evaluate(["Gmail", "Asana"])  # the 3-combo minus its redundant member
    c.ok("membership", "dropping a redundant member does not lower the use case",
         RANK[drop_red["rating"]] >= RANK[add_redundant["rating"]],
         f"+Asana combo={add_redundant['rating']} → drop redundant → Gmail+Asana={drop_red['rating']}")

    # -- 3. coverage sanity -------------------------------------------------
    cat = Discover().run()
    company = next((u for u in cat if u["name"] == "Runs like a company"), None)
    c.ok("coverage", "'runs like a company' spans most domains",
         company is not None and company["n_domains"] >= 10,
         f"n_domains={company['n_domains'] if company else 'MISSING'}/12, "
         f"scale={company['scale'] if company else '?'}")
    small = a.evaluate(["Gmail", "Todoist"])
    c.ok("coverage", "a small system is tight (no dead members)",
         len(small["dropped"]) == 0 and small["scale"] == 2,
         f"Gmail+Todoist core={small['scale']}, dropped={len(small['dropped'])}")

    # -- 4. per-verb side effects -------------------------------------------
    obs = a.evaluate(["Gmail", "Notion"], mode="observe")
    act = a.evaluate(["Gmail", "Notion"])
    gmail_se = act["side_effects"]["per_connector"].get("gmail")
    c.ok("side_effects", "read-only use case over a send-capable connector reports read",
         obs["side_effects"]["headline"] == "read" and gmail_se == "read",
         f"observe headline={obs['side_effects']['headline']}, Gmail(send-capable) used as "
         f"source={gmail_se}")
    sends = a.evaluate(["HubSpot", "Klaviyo"])
    c.ok("side_effects", "a use case that actually sends incurs irreversible",
         sends["side_effects"]["headline"] == "irreversible" and sends["side_effects"]["observe"] == "read",
         f"HubSpot+Klaviyo headline={sends['side_effects']['headline']}, "
         f"read-only footprint={sends['side_effects']['observe']}")

    return c


def write_report(c, path):
    total = len(c.rows)
    npass = sum(1 for r in c.rows if r[2])
    lines = ["# Connector Atlas — validation",
             "",
             f"**{npass}/{total} checks pass.** Evidence that the use-case discovery is sound — "
             "coherence, membership, coverage and per-verb side effects. No held-out precision on "
             "join keys (that is not what this atlas measures); the honest test of a judgment model "
             "is whether its calls match hand labels and its reasoning is inspectable.",
             ""]
    cats = {}
    for cat, name, passed, detail in c.rows:
        cats.setdefault(cat, []).append((name, passed, detail))
    titles = {"coherence": "## 1. Coherence spot-checks",
              "membership": "## 2. Membership checks",
              "coverage": "## 3. Coverage sanity",
              "side_effects": "## 4. Per-verb side effects"}
    for cat in ("coherence", "membership", "coverage", "side_effects"):
        lines += ["", titles[cat], ""]
        for name, passed, detail in cats.get(cat, []):
            mark = "✅" if passed else "❌"
            lines.append(f"- {mark} **{name}**  \n  {detail}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    c = run()
    total = len(c.rows)
    npass = sum(1 for r in c.rows if r[2])
    cur = None
    for cat, name, passed, detail in c.rows:
        if cat != cur:
            print(f"\n[{cat}]")
            cur = cat
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
        if not passed:
            print(f"        {detail}")
    os.makedirs(REPORTS, exist_ok=True)
    write_report(c, os.path.join(REPORTS, "VALIDATION.md"))
    print(f"\n{npass}/{total} checks pass. wrote reports/VALIDATION.md")
    return 0 if c.passed() else 1


if __name__ == "__main__":
    sys.exit(main())
