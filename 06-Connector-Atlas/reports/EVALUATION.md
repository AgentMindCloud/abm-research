# Evaluation

Held-out set: 60 connectors hand-labeled before any rule existed (30 rich / 30 terse).

## Profile accuracy (micro-averaged over the held-out set)

| arm | slice | emits P / R / F1 | consumes P / R / F1 | side-effect acc |
|---|---|---|---|---|
| archetype baseline | all (n=60) | 0.480 / 0.668 / 0.559 | 0.253 / 0.590 / 0.354 | 0.583 |
| archetype baseline | rich (n=30) | 0.507 / 0.673 / 0.578 | 0.256 / 0.574 / 0.354 | 0.533 |
| archetype baseline | terse (n=30) | 0.453 / 0.663 / 0.538 | 0.250 / 0.609 / 0.354 | 0.633 |
| inference, arm A (unbiased) | all (n=60) | 0.781 / 0.500 / 0.610 | 0.581 / 0.540 / 0.560 | 0.633 |
| inference, arm A (unbiased) | rich (n=30) | 0.833 / 0.531 / 0.649 | 0.562 / 0.500 / 0.529 | 0.567 |
| inference, arm A (unbiased) | terse (n=30) | 0.723 / 0.465 / 0.566 | 0.600 / 0.587 / 0.593 | 0.700 |
| inference, arm B (upper bound) | all (n=60) | 0.959 / 0.995 / 0.977 | 0.862 / 1.000 / 0.926 | 0.950 |
| inference, arm B (upper bound) | rich (n=30) | 0.958 / 1.000 / 0.978 | 0.857 / 1.000 / 0.923 | 0.933 |
| inference, arm B (upper bound) | terse (n=30) | 0.962 / 0.990 / 0.976 | 0.868 / 1.000 / 0.929 | 0.967 |

**Headline:** emits F1 0.559 (archetype baseline) -> 0.610 (arm A inference), a 9% relative gain, with vendor rules for the held-out connectors withheld entirely.

## Dead rules

Rules that never fired across all 820: **none**

## Key prevalence gate (no key above 35% of connectors)

Peak: `timestamp` at 31%. Over gate: **none**

Shipped registry for comparison: `url` 91%, `text` 65%, `timestamp` 62%, `rows` 52%.

## Mode regression

The engine must never claim a key join that does not exist. `direct` also requires score >= 0.25.

| pair | expected | actual mode | score | |
|---|---|---|---|---|
| Gmail -> Google Drive | direct | direct | 0.555 | PASS |
| Apollo.io -> Lemlist | direct | direct | 0.455 | PASS |
| ZoomInfo -> HubSpot | direct | direct | 0.720 | PASS |
| Shopify -> Xero | direct | direct | 0.535 | PASS |
| Supabase -> Tableau | direct | direct | 0.286 | PASS |
| SurveyMonkey -> Supabase | direct | direct | 0.338 | PASS |
| Stripe -> Xero | direct | direct | 0.588 | PASS |
| Have I Been Pwned -> HubSpot | direct | direct | 0.720 | PASS |
| Gmail -> Todoist | inferred | inferred | 0.168 | PASS |
| Google Calendar -> Todoist | inferred | inferred | 0.168 | PASS |
| Fireflies -> Todoist | inferred | inferred | 0.168 | PASS |
| Todoist -> Oxford Economics | not-direct | qualifier | 0.039 | PASS |
| PubMed -> Stripe | not-direct | inferred | 0.176 | PASS |
| Telgani -> Snyk Security | not-direct | none | 0.000 | PASS |
| Mermaid Chart -> Interactive Brokers (IBKR) | not-direct | none | 0.000 | PASS |
| O'Reilly -> PagerDuty | not-direct | inferred | 0.137 | PASS |
| Courtroom5 -> Shippo | not-direct | none | 0.000 | PASS |

**PASS** — 17/17 pairs

## Gates

| gate | value | threshold | status |
|---|---|---|---|
| connector-level resolution (differ from archetype default) | 100% | >=60% | PASS |
| no key above 35% prevalence | 31% | <=35% | PASS |
| dead rules removed | 0 | 0 | PASS |
| mode regression (never claim a false key join) | 17/17 | all pass | PASS |

**All gates: PASS**
