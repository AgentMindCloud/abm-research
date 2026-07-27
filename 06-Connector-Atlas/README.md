# Connector Atlas — capability inference from descriptions and vendors

## Why this exists

The premise it corrects is mine. I had claimed that connector knowledge was "capped at
whatever the session is connected to (11 of 820)" — that without a live MCP connection and
a harvested tool schema, a connector was unknowable. Jani's correction: the number of
connectors currently connected is irrelevant. A connector's directory description, plus
knowledge of the company on the other end, tells you what it does, what it joins on, and
what it cannot do. Then it is a matter of doing the math and simulating situations.

He was right, and the shipped registry proves how much was being left on the floor:

| | shipped registry | after inference |
|---|---|---|
| connectors whose profile differs from their archetype default | **0 / 820** | **820 / 820** |
| peak key prevalence (`url` before, `timestamp` after) | **91%** | **31%** |
| ordered pairs registering an edge | **490,299 (73%)** | 153,904 with any shared key |
| actionable edges (score ≥ 0.30) | n/a — boolean | **62,202 (9.3%)** |

All 53 `market_data` connectors previously shared one byte-identical emit-set. Every
"A composes with B" answer was an archetype answer wearing a connector's name.

## What it does

1. **`engine/infer.py`** — builds a per-connector capability profile from three ordered
   evidence sources, each recording *why* it fired:
   - **description rules** (~35 ordered regexes over the directory `role` text)
   - **vendor rules** (`data/vendor_rules.json`, 259 hand-authored entries) — the layer
     that resolves terse entries like `Backlog | "MCP Server"`, `Telgani | "Rent a Car"`,
     or Japanese/French-only blurbs where no English rule can fire
   - **archetype prior** (`data/archetype_priors.json`) — fills only what the first two
     left empty, and is tagged `archetype_prior` so it is never mistaken for evidence

2. **`engine/compose.py`** — scores directed compositions instead of asserting boolean
   edges, and labels each with a **mode**:
   - `direct` — a real shared identifying key
   - `qualifier` — the only shared key merely *aligns* records (a timestamp). Two
     connectors that both have dates on them are not composable.
   - `inferred` — no shared key; Claude adapts prose into what the target accepts. Lossy
     by construction, capped well below a key join, and the correct place for a human check.

3. **`engine/simulate.py`** — runs 40 concrete situations end to end and checks the
   proposed composition's mode, join keys and side-effect profile.

4. **`engine/eval.py`** — rebuilds the evaluation discipline that was lost with a previous
   container: held-out precision/recall against a hand-labeled set, a baseline comparison,
   dead-rule detection, and a mode regression.

## Key vocabulary

Finer than the shipped registry's 18 keys, because the coarse ones manufactured edges:
`url` was emitted by 91% of connectors and generated 218,832 candidate pairs by itself.

`url` splits into `url:permalink` / `url:artifact` / `url:auth`; `rows` into
`rows:tabular` / `rows:timeseries`; `money` into `money:txn` / `money:amount`; `geo` into
`geo:point` / `geo:region`; `file` into `file:blob` / `file:ref`.

**`text` is deliberately not a key.** Free text is Claude-as-adapter — the one lossy join
in `composition.md` — so it is modelled as the `inferred` mode with its own cost rather
than as an edge that silently creates paths.

## Honest limits

- **Vendor rules are my knowledge, not documentation.** They are tagged `DOCUMENTED` where
  the product is well known and stable, `ASSUMED` where extrapolated from the brand. They
  are never used for tool parameter names or result field shapes — those stay unknowable
  without a live schema, and no amount of description reasoning recovers them.
- **Arm B is an upper bound, not an unbiased score.** The held-out labels and the vendor
  rules come from the same head. Arm A withholds vendor rules for every held-out connector
  precisely so the headline number measures generalization instead of self-consistency.
  Arm A is the number to trust; arm B shows the ceiling if vendor knowledge is correct.
- **Side effects are per-connector worst case, not per-verb.** This is why three scenarios
  flag a violation for merely *reading* Gmail: Gmail can send, so its worst case is
  `irreversible`. `composition.md` already prescribes the fix ("sending is irreversible;
  drafting is not — keep them separate hops"); implementing per-verb side effects is the
  single highest-value next change.
- **Scores are ordinal, not calibrated.** The only claim made about the scoring function is
  the mode regression: the engine must never assert a key join that does not exist. No
  absolute score should be read as a probability.

## Running it

```bash
cd engine
python3 infer.py --report          # build profiles, print gates
python3 eval.py --write-report     # metrics -> ../reports/EVALUATION.md
python3 simulate.py --write-report # scenarios -> ../reports/SCENARIOS.md

python3 compose.py path "Gmail" "Todoist"
python3 compose.py edges "Shopify" --top 15
python3 compose.py hubs
python3 compose.py density
```

`data/registry_inferred.json` is the production artifact (arm B, all knowledge available).
`data/registry_inferred_armA_eval_only.json` exists solely for measurement — do not ship it.

## Files

```
engine/infer.py       description + vendor + prior inference, with provenance
engine/compose.py     scored composition, mode classification, Dijkstra bridge search
engine/simulate.py    40-scenario harness
engine/eval.py        held-out metrics, baseline delta, dead rules, mode regression
data/heldout_labels.json          60 hand labels, written BEFORE any rule existed
data/vendor_rules.json            259 vendor profiles
data/archetype_priors.json        47 priors, retyped and narrowed
data/registry_inferred.json       820 profiles (production)
scenarios/scenarios.json          40 situations
reports/EVALUATION.md             metrics
reports/SCENARIOS.md              scored scenario report
```

Source registry: `/root/.claude/skills/connector-atlas/scripts/registry_full.json`
(820 connectors scraped from the official directory). Stdlib only, no network at runtime.
