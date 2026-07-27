# Connector Atlas — use cases around Claude

**Claude is the brain in the centre.** Take the ~820 connectors in the Claude directory, add
Claude and two connectors — say Gmail + Todoist — and ask: *do they make a use case? which one?
why?* Then grow the combination: more and more connectors, always asking which ones **work
together**, what use case they make, and **why**. We surface only the combos that cohere, name
them, and explain why each connector earns its place.

A connector belongs in a combo if it brings real value to the whole system (Claude + the others).
If it doesn't fit, or it just duplicates a job another connector already does, it's left out — and
we say so.

There are **no join keys**, no popularity, no personal context. Coherence is judged on what each
connector *does* — its functional capabilities — and whether those jobs connect, through Claude,
into a workflow a person would actually want.

---

## The pipeline

```
directory description + vendor knowledge (+ web research where thin)
        │   engine/infer.py
        ▼
data/registry_inferred.json     820 connectors: a function statement, capability tags,
        │                       per-verb side effects — all as knowledge, not guesses
        │   data/capabilities.json   ~50 capability tags → 12 domains, with workflow roles
        │   data/domains.json        the 12 domains + how they connect
        ▼
engine/usecase.py   does Claude + {connectors} make a use case? name it, explain why,
        │           keep vs. drop members, side effects from verbs used, a potential score
        ▼
engine/discover.py  a catalogue of working use cases, small → huge
        │           → reports/USE-CASES.md, data/usecases.json
        ├─ engine/render.py    → atlas.html   (Claude hub + a gallery of use cases)
        └─ engine/validate.py  → reports/VALIDATION.md
```

## What every connector is reduced to

`engine/infer.py` states, for each of the 820 connectors:

- **a function statement** — what it does, in plain language, with a `source`
  (`directory` / `vendor_knowledge` / `researched`) and a confidence tag. The terse minority
  whose blurb was too thin to stand alone (e.g. `Backlog | "MCP Server"`, `IQLand | "iqlandaimcp"`,
  non-English blurbs) were **researched online** and recorded in `data/researched.json` — not left
  blank.
- **capability tags** — the jobs it can do, from a controlled vocabulary of ~50 (`email`, `tasks`,
  `crm`, `payments`, `market_data`, `deploy`, `legal_research`, …). Derived from the archetype and
  refined by keyword rules (so Stripe reads as `payments`, not generic `cloud_infra`; a brokerage
  reads as `trading`, not a `market_data` feed).
- **per-verb side effects** — reading is `read`; only creating/updating/sending/paying/trading
  carries a write. This is what lets a *read-only* use case over a send-capable connector report
  `read`, and only a use case that actually sends incur `irreversible`.

## How a combo is judged (`engine/usecase.py`)

For any connector subset, with Claude at the hub:

- **Coherence.** Each capability has a domain and a workflow role (`input` / `store` / `output`).
  Two capabilities *connect* if they share or bridge a workflow: work/knowledge glue
  (notes, tasks, files, search, automation) attaches to anything; communication glue
  (email, chat, calendar) attaches to operational work but **not** to specialist islands; specialist
  capabilities (a brokerage, case-law, a markets feed) only connect within their domain or via an
  explicit `pairs_with`. If the connectors' capabilities form one connected workflow with a source
  and somewhere for the output to land, the combo **coheres**.
- **Rating** is ordinal and always explained: **strong** (a full source → act → output pipeline),
  **partial** (coheres, but read-only synthesis or a missing stage), **non** (no shared workflow).
- **Membership.** A connector stays if it adds a capability the combo needs and doesn't already
  have. It's dropped as *redundant* (its capability is already covered — kept only as a labelled
  fallback) or *unrelated* (it doesn't link into the workflow).
- **Side effects** = the union of the verbs the use case actually uses. A connector used as a source
  is `read` even if it *can* send.

```
python3 engine/usecase.py "Gmail" "Todoist"
python3 engine/usecase.py "Gmail" "Interactive Brokers"     # → NON, no shared workflow
python3 engine/usecase.py "Fireflies" "Todoist" "Notion" --json
```

## Discovery across scales (`engine/discover.py`)

Capability-guided, never brute-force 820²:

- **small (2–5)** — many sharp use cases (Inbox-to-Action Desk, Research Desk, Outbound Sales Desk…)
- **medium (6–20)** — a whole domain desk (a Sales desk, a Finance back office…)
- **large (30–200)** — broad systems: a GTM engine, a back office, and a **system that runs like a
  company** (best connector per capability across all 12 domains). Scale and domain coverage are
  reported honestly — functional reach, never autonomy.

Every use case carries a **potential** score (0–100) so they can be ranked by value *independent of
size* — a sharp two-connector desk and a whole-company system can each rank near the top for
different, visible reasons. It is a composite of four inspectable 0–25 parts, never a bare number:
**applicability** (how universally runnable the connectors are), **leverage** (does Claude actually
act, not just advise), **reach** (operational span — the only size-weighted part, deliberately a
quarter of the total), and **tightness** (coherence quality with no dead members).

```
python3 engine/discover.py --write-report      # → reports/USE-CASES.md + data/usecases.json
python3 engine/render.py   --out atlas.html    # → the static gallery, Claude in the centre
```

## The atlas (`atlas.html`)

A **static, readable** page (no interactivity — a page you scan and evaluate). Claude is the hub;
it opens with a **"most potential" leaderboard across all sizes**, then features the one **huge**
system that runs like a company (with a domain-by-domain list of which connector fills each
capability), then lists the full catalogue grouped small → medium → large. Every use case plainly
states what it is for and which connectors it uses, with the one-line job each connector does and its
per-use-case side effect. Cinnabar/jade palette; a load-time scaffolding self-check (`CSS1Compat`).

## Validation (`engine/validate.py`)

Not held-out precision on join keys (gone). Instead: coherence spot-checks against hand labels
(Gmail+Todoist = yes; Gmail+Interactive Brokers = no), membership checks (a redundant add never
raises the rating; a complementary one extends it), coverage sanity (a "runs like a company" system
really spans most domains; a small one is tight), per-verb side effects, and potential-score sanity
(the huge system tops reach; a small universal combo maxes applicability; a non-use-case scores zero).
`23/23` pass — see `reports/VALIDATION.md`.

## Files

| Path | What |
|---|---|
| `data/registry_inferred.json` | 820 connectors: function + capabilities + per-verb side effects |
| `data/capabilities.json` | the ~50 capability tags, their domains, roles and link rules |
| `data/domains.json` | the 12 functional domains and their adjacency |
| `data/researched.json` | function knowledge for the terse minority, researched online |
| `data/vendor_rules.json`, `data/archetype_priors.json` | the function-knowledge layer inputs |
| `data/usecases.json` | the discovered catalogue (for the renderer) |
| `engine/infer.py` | function + capability + per-verb side-effect inference |
| `engine/usecase.py` | the coherence engine — does a combo make a use case, and why |
| `engine/discover.py` | multi-scale discovery |
| `engine/render.py` | `atlas.html` — static readable page: potential leaderboard + huge system + catalogue |
| `engine/validate.py` | the checks (coherence, membership, coverage, side effects, potential) |
| `atlas.html` | the atlas: Claude in the centre, use cases ranked by potential, small → huge |
| `reports/USE-CASES.md`, `reports/VALIDATION.md` | the catalogue and the checks |

*The v1 **function knowledge** (verbs, side effects, vendor rules, archetype priors) is kept and
extended. The v1 **join-key composition** — typed emit/consume keys, prevalence gates, direct/
qualifier/inferred modes, dead-rule detection, held-out precision — was off-target and has been
removed.*
