# Scenario simulation

40 situations run through the scored engine (20 generic, 20 from Jani's ABM / HCMC-funnel / women-heavy-markets context).

| status | n |
|---|---|
| OK | 35 |
| SIDE-EFFECT VIOLATION | 3 |
| NO ROUTE | 2 |

`direct` = a real shared identifying key. `inferred` = no shared key; Claude adapts prose into what the target accepts (lossy, and the right place for a human check). `qualifier` = the only shared key merely aligns records.

### gen01 — Turn the attachments people email me into filed documents I can search later.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.673

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Gmail → Google Drive | direct | `file:blob` | 0.673 | mutate |

### gen02 — Take the leads I pulled from a prospecting database and start an outbound sequence.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.585

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Apollo.io → lemlist | direct | `domain` | 0.585 | irreversible |

### gen03 — Enrich the companies in my CRM with firmographic data.

*pattern:* enrich · *status:* **OK** · *weakest hop:* direct · *min score:* 0.72

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| ZoomInfo → HubSpot | direct | `domain` | 0.72 | mutate |

### gen04 — Reconcile my storefront orders against my accounting ledger.

*pattern:* reconcile · *status:* **OK** · *weakest hop:* direct · *min score:* 0.521

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Shopify → Xero | direct | `rows:tabular` | 0.521 | mutate |

### gen05 — Get payment records into the books without retyping them.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.584

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Stripe → Xero | direct | `money:amount` | 0.584 | mutate |

### gen06 — Turn survey responses into a queryable table.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.423

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| SurveyMonkey → Supabase | direct | `rows:tabular` | 0.423 | irreversible |

### gen07 — Put my warehouse data in front of the team as a dashboard.

*pattern:* materialize · *status:* **OK** · *weakest hop:* direct · *min score:* 0.358

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Supabase → Tableau | direct | `rows:tabular` | 0.358 | read |

### gen08 — Check whether any of my CRM contacts turned up in a breach.

*pattern:* enrich · *status:* **OK** · *weakest hop:* direct · *min score:* 0.72

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Have I Been Pwned → HubSpot | direct | `domain` | 0.72 | mutate |

### gen09 — Turn what was said in my meetings into tasks I will actually do.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* inferred · *min score:* 0.216

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Fireflies → Todoist | inferred | `claude-adapter -> project` | 0.216 | mutate |

### gen10 — Make the emails that need action show up on my task list.

*pattern:* pipeline · *status:* **SIDE-EFFECT VIOLATION** · *weakest hop:* inferred · *min score:* 0.216

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Gmail → Todoist | inferred | `claude-adapter -> project` | 0.216 | mutate |

- **side-effect violation:** Gmail is irreversible, scenario forbids irreversible

### gen11 — Publish an analysis as a shareable page instead of losing it in chat.

*pattern:* materialize · *status:* **OK** · *weakest hop:* direct · *min score:* 0.547

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Supabase → Send | direct | `file:blob` | 0.547 | irreversible |

### gen12 — Take a signed contract and file it where the team can find it.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.635

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Docusign → Box | direct | `file:blob` | 0.635 | mutate |

### gen13 — Get my ad and site metrics into one place I can query.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* inferred · *min score:* 0.176

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Semrush → Google Cloud BigQuery | inferred | `claude-adapter -> code/rows:tabular` | 0.176 | irreversible |

### gen14 — Turn a research question into sourced reading I can cite.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* inferred · *min score:* 0.216

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Exa → Basic Memory Cloud | inferred | `claude-adapter -> file:blob/file:ref` | 0.216 | mutate |

### gen15 — Track shipments against the orders that produced them.

*pattern:* reconcile · *status:* **OK** · *weakest hop:* direct · *min score:* 0.54

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Shopify → Shippo | direct | `geo:point` | 0.54 | irreversible |

### gen16 — Turn customer support volume into something I can chart over time.

*pattern:* digest · *status:* **NO ROUTE** · *weakest hop:* none · *min score:* 0.0

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Intercom → Metabase | none | `-` | 0.0 | read |

### gen17 — Build a deck from numbers rather than rebuilding it by hand each month.

*pattern:* materialize · *status:* **OK** · *weakest hop:* direct · *min score:* 0.729

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Metabase → Gamma | direct | `image` | 0.729 | create |

### gen18 — Watch for errors in production and page a human when it matters.

*pattern:* trigger_action · *status:* **OK** · *weakest hop:* inferred · *min score:* 0.176

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Sentry → PagerDuty | inferred | `claude-adapter -> email` | 0.176 | irreversible |

### gen19 — Turn candidate applications into a reviewable pipeline.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.521

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Teamtailor → Airtable | direct | `rows:tabular` | 0.521 | mutate |

### gen20 — Keep a durable record linking records across two systems so re-runs do not duplicate.

*pattern:* mirror · *status:* **OK** · *weakest hop:* direct · *min score:* 0.552

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Supabase → Airtable | direct | `rows:tabular` | 0.552 | mutate |

### abm01 — Find mid-market Western companies that look like they need AI help, and get them into a CRM.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.72

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Harmonic → Attio | direct | `domain` | 0.72 | mutate |

### abm02 — Enrich those companies with headcount and hiring signals before I decide who to contact.

*pattern:* enrich · *status:* **OK** · *weakest hop:* direct · *min score:* 0.481

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Harmonic → Aura | direct | `domain` | 0.481 | read |

### abm03 — Find the actual decision-maker's email at a company I have only a domain for.

*pattern:* enrich · *status:* **SIDE-EFFECT VIOLATION** · *weakest hop:* direct · *min score:* 0.495

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Apollo.io → ZoomInfo | direct | `domain` | 0.495 | read |

- **side-effect violation:** Apollo.io is irreversible, scenario forbids irreversible

### abm04 — Run cold outreach to a qualified list without sending anything I have not seen.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.585

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Attio → lemlist | direct | `domain` | 0.585 | irreversible |

### abm05 — Track which outreach threads got a reply so I can follow up on the live ones.

*pattern:* reconcile · *status:* **OK** · *weakest hop:* direct · *min score:* 0.615

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| lemlist → Attio | direct | `email` | 0.615 | mutate |

### abm06 — Turn a discovery call into a written brief the HCMC provider can quote against.

*pattern:* materialize · *status:* **OK** · *weakest hop:* direct · *min score:* 0.615

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Fireflies → Google Drive | direct | `email` | 0.615 | mutate |

### abm07 — Give a prospect a credible landing page for the offer without building a site.

*pattern:* materialize · *status:* **OK** · *weakest hop:* direct · *min score:* 0.516

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Gamma → Send | direct | `file:blob` | 0.516 | irreversible |

### abm08 — Let a prospect book a call at a time that works, without me chasing.

*pattern:* trigger_action · *status:* **OK** · *weakest hop:* direct · *min score:* 0.652

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Calendly → Google Calendar | direct | `email` | 0.652 | mutate |

### abm09 — Invoice a Western client from Vietnam and have it land in the books.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.584

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Stripe → Xero | direct | `money:amount` | 0.584 | mutate |

### abm10 — Send the onboarding paperwork for signature and keep the executed copy.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.673

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Docusign → Google Drive | direct | `file:blob` | 0.673 | mutate |

### abm11 — Keep every prospect interaction in one durable store instead of my memory.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.516

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Gmail → Supabase | direct | `file:blob` | 0.516 | irreversible |

### abm12 — Check a target market's economic conditions before I pitch into it.

*pattern:* enrich · *status:* **NO ROUTE** · *weakest hop:* none · *min score:* 0.0

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Oxford Economics → Metabase | none | `-` | 0.0 | read |

### abm13 — Compare how Claude is actually used in a country against where I am selling.

*pattern:* reconcile · *status:* **OK** · *weakest hop:* direct · *min score:* 0.358

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Anthropic Economic Index → Metabase | direct | `rows:tabular` | 0.358 | read |

### abm14 — Turn my research notes into a paper I can hand a client.

*pattern:* materialize · *status:* **OK** · *weakest hop:* inferred · *min score:* 0.243

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Basic Memory Cloud → Gamma | inferred | `claude-adapter -> image` | 0.243 | create |

### abm15 — Find which industries employ mostly women in a given country, from public data.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.423

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Anthropic Economic Index → Supabase | direct | `rows:tabular` | 0.423 | irreversible |

### abm16 — Pull public health and demographic series for a region I am researching.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.423

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| PopHIVE → Supabase | direct | `rows:tabular` | 0.423 | irreversible |

### abm17 — Find software categories women-heavy businesses actually review and rate.

*pattern:* pipeline · *status:* **OK** · *weakest hop:* direct · *min score:* 0.521

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| G2 → Airtable | direct | `rows:tabular` | 0.521 | mutate |

### abm18 — Check whether a market I am researching has real procurement money in it.

*pattern:* enrich · *status:* **OK** · *weakest hop:* direct · *min score:* 0.358

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| JP Bid → Metabase | direct | `rows:tabular` | 0.358 | read |

### abm19 — Keep the whole research corpus searchable without re-reading everything.

*pattern:* enrich · *status:* **OK** · *weakest hop:* direct · *min score:* 0.412

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Google Drive → Glean | direct | `file:ref` | 0.412 | read |

### abm20 — Produce a weekly brief from calendar, inbox and the task list.

*pattern:* digest · *status:* **SIDE-EFFECT VIOLATION** · *weakest hop:* inferred · *min score:* 0.216

| hop | mode | join | score | target side effects |
|---|---|---|---|---|
| Google Calendar → Gmail | direct | `email` | 0.499 | irreversible |
| Gmail → Todoist | inferred | `claude-adapter -> project` | 0.216 | mutate |

- **side-effect violation:** Gmail is irreversible, scenario forbids irreversible

## Outcome

- routes found: 38/40
- every hop a real key join: 31
- side-effect violations: 3
