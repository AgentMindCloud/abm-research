# AI Capability Map – 2026-07-26

**Author of this pass:** Claude (Opus) · **Version:** 1.0 (first full draft)
**Raw evidence log:** `99-Raw-Extractions/AI-Capabilities-Claude-2026-07-26.md`
**Scope:** what AI agents and systems can *reliably* do in production as of July 2026,
and where the hard walls are, judged against the constraints in
`00-Meta/ABM-Project-Continuity.md` (solo operator, low regulation, digital-first).

**Confidence convention:** every claim carries **High / Medium / Low**.
- **High** = primary source (paper, publisher's own docs, government or CC-licensed dataset), or multiple independent primaries agreeing.
- **Medium** = consistent secondary reporting of a primary, or a checkable vendor claim.
- **Low** = single unverified source, vendor self-report, or market-sizing projection. Used only where the *direction* matters and the magnitude does not.

**A warning about the 2026 information environment.** Searching "AI agent benchmark 2026"
returns a large volume of SEO content-farm pages that publish confident benchmark tables
with no methodology, and in several cases cite model names that cannot be verified to
exist. This map rejects those sources by name in the raw log (§A of the raw file). Where
numbers conflict, the conflict is shown rather than averaged away. **Confidence (High)** —
this was directly observed across ~20 searches in this pass.

---

## 1. Executive Summary

**The one-sentence state of the art:** in July 2026, AI systems are extremely strong at
*bounded, verifiable, digital transformations of text and structured data*, moderately
strong at *tool-mediated action inside a narrow permission surface*, and still
fundamentally unreliable at *open-ended, long-horizon, multi-application work without
supervision*. Nothing in the last twelve months has changed that shape — the numbers moved,
the shape did not.

Eight findings that should govern every design decision in this project:

**1. The autonomy horizon is real, measurable, and much shorter than the headlines.**
METR's task-completion time-horizon work puts frontier 50%-reliability horizons in the
14–20 hour range by mid-2026, with doubling time compressing from ~7 months (2019–2025) to
~4 months (2024–2026). But METR itself states that "measurements above 16 hrs are
unreliable with our current task suite," that the horizons apply to *software
engineering, ML and cybersecurity* tasks, that the human baseline is a **low-context new
hire or contractor** rather than an expert, and that tasks are **well-specified and
algorithmic** — explicitly excluding work with interpersonal or holistic success criteria.
*(METR, page last updated 2026-05-08 — **High** for the caveats, **Medium** for the
figures.)* The 50% horizon is a coin-flip horizon. **A business process needs the 80%
horizon, which in METR's fitted curves runs roughly 4–5× shorter — order of 1–3 hours.**

**2. Benchmark saturation is masking the collapse on realistic work.** Computer-use agents
went from 12% (April 2024) to ~66% on the *original* OSWorld — reported as within ~6
points of the 72.4% human baseline. On **OSWorld 2.0**, which lengthens and realises the
same task family, the best configuration (Claude Opus 4.8, maximum thinking, batched tool
calls) completes **20.6%** of tasks at a 54.8% partial score; the next model plateaus near
13%. *(OSWorld 2.0, 2026-06-26 — **High** for direction, **Medium** for exact figures.)*
**A ~3× drop from one benchmark revision is the single most important number in this
document.** Any product plan that assumes "computer use works now" is planning against
the saturated benchmark.

**3. Adoption is broad; agentic autonomy is not.** The Stanford AI Index 2026 reports 88%
of organisations using AI in at least one business function and 78% of the Fortune 500
deployed at scale — while finding that **agentic deployment remains limited across most
business functions**, with governance, validation and readiness lagging badly. The
described current phase is "augmentation within existing operating models."
*(**Medium** — consistent secondary reporting; primary PDF not yet fetched, flagged as a
verification debt.)* This is good news for a solo operator: the constraint is not model
capability, it is *process design*, which is exactly where a single well-organised person
can compete with an enterprise.

**4. Multi-agent complexity is a liability, not an asset.** MAST — 14 failure modes in 3
clusters (system-design issues, inter-agent misalignment, task verification), built from
150 expert-annotated traces at κ = 0.88 and extended to 1,600+ traces across 7 frameworks
— finds multi-agent gains on popular benchmarks "often minimal" and concludes that **many
failures stem from poor system design, not model performance**. *(NeurIPS 2025 —
**High**.)* Independently, minimal coding scaffolds (mini-swe-agent) reach near-SOTA,
which says scaffold sophistication is not the bottleneck. *(**Medium**.)*
**Design implication: one competent agent with excellent tools and an explicit state
machine beats a crew.**

**5. Connector security is unsolved and is the project's largest existential risk.**
MCPTox (AAAI) tested 45 live MCP servers and 353 authentic tools against poisoned tool
descriptions: **attack success above 60%, up to 72%** on many popular agents, and the
most-resistant model refused poisoned tool calls **less than 3%** of the time.
InjecAgent: GPT-4 vulnerable 24% at baseline, 47% under enhanced attacks.
MCP-SafetyBench: host-side attacks over 80% success on average. In May 2026 OX Security
disclosed a systemic vulnerability across multiple MCP implementations. *(**High** that
the problem is structural; **Medium** for the incident's scale.)* The recurring real-world
shape — attested by the 2025 Supabase/Cursor support-ticket breach — is
**privileged access + untrusted input + an outbound channel**. Any ABM that reads
customer-supplied text and holds write credentials contains this pattern by construction.

**6. Cost is no longer a design constraint for text work; it is one for long-horizon
work.** Mid-tier frontier-adjacent models sit around $1–$3 per million input tokens and
$6–$15 output, with batch APIs at a flat 50% discount across all major providers, and
prices at a constant capability tier having fallen sharply year over year.
*(**Medium** for the band, **Low** for the ~80% reduction magnitude.)* Voice is at roughly
$0.07/minute *(**Medium**, checkable vendor pricing)* — a 4-minute booking call costs
about $0.28. **Cost only bites where token consumption is superlinear in horizon length:
long-context re-reading, retry storms, and multi-agent chatter.**

**7. Where the tooling attention is *not* going is measurable — and it is exactly the
territory this project has chosen.** The Anthropic Economic Index (CC BY 4.0, period
2026-05-01) shows observed Claude usage matched to task catalogs, by job category:
**Computer & Mathematical 23.8%**, Arts/Design/Media 13.6%, Educational Instruction &
Library 12.8%, Office & Administrative Support 7.9% — versus **Personal Care & Service
1.23%** and **Healthcare Support 0.62%**. At occupation level, tasks commonly done by
Hairdressers/Hairstylists/Cosmetologists account for **0.02%** of usage (rank 318 of 718
published occupations) and Skincare Specialists **0.04%** (rank 250). *(**High** —
primary, publisher-licensed dataset.)* **Important framing constraint stated by the
publisher: this measures usage of tasks, not people, and cannot support any claim about
employment or displacement.** Read correctly, it is a *supply-of-attention* signal:
AI capability is being pointed at technical and creative desk work, and almost not at
personal-care service operations. That is the whitespace hypothesis, now with a number
attached.

**8. Vietnam-specific: local usage is thinner, more technical, and more
automation-styled.** Vietnam's Anthropic Usage Index is **0.53** — usage per working-age
person about half the global average — ranking 84 of 121 covered countries. Its
conversations skew to work (53.1% vs 43.4% global), automation-style over
augmentation-style (51.4% vs 48.6% — the mirror of the global split), Software Development
(18.0% vs 11.5%) and Content Creation (24.9% vs 22.7%), while "advice or recommendation"
artifacts are half the global rate (5.5% vs 10.7%). *(**High** — primary.)* Practical
read: building *from* Vietnam for Western service-business buyers is not competing against
a saturated local AI-services market, but local talent and habit are pointed at
code and content, not at operations tooling.

**What this means for the next stage of the project.** The Master Synthesis' conclusion —
bounded autonomy with progressive delegation — survives the 2026 evidence intact and is
if anything better supported than when it was written. The buildable zone in July 2026 is:
**short-horizon (minutes to ~1 hour), single-domain, API-mediated (not GUI-mediated),
objectively verifiable, reversible workflows, with deterministic state held outside the
model, one agent rather than several, and a human gate on anything that moves money,
sends unreviewed messages to third parties, or writes to a system of record.**

---

## 2. Core Capability Categories

Maturity is scored 1–10 for **production reliability in a solo-operated business**, not
for demo impressiveness or benchmark score. A 7 means "you can build a product on this if
you design the failure path." A 4 means "it will work in your tests and fail with
customers."

"Reliable without human?" is answered for a *bounded, well-specified* instance of the
capability — not the general case.

---

### 2.1 Research & synthesis

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Retrieval + summarisation over a **defined corpus** (docs you supply) | **8/10** | **Yes**, with citation-back requirement and refusal-on-missing-evidence | Confident interpolation between sources; silent dropping of a source that contradicts the emerging narrative; over-weighting the first document read | Claude/GPT/Gemini long-context + RAG; Claude Agent SDK for tool loops | Cheap. A 50-page corpus synthesis is a few cents to low tens of cents at mid-tier pricing. Batch API at 50% off for non-interactive runs | Project corpus `2403.08399v2` (multi-agent SLR decomposition); pricing aggregators July 2026 — **Medium** |
| Open-web research with source discovery | **6/10** | **No** — needs a human or a deterministic checker on source *quality* | Cites SEO content farms as authoritative (directly observed in this pass); fabricates plausible URLs; treats vendor blogs as neutral; date-blind (2023 numbers presented as current) | Search-enabled models; deep-research modes | Moderate. Long research runs consume 100k+ tokens; superlinear in the number of pages read | Direct observation, this pass — **High**; Master Synthesis "confabulation" — **High** |
| Comparative / structured analysis across sources | **7/10** | Partially — reliable at *assembling* the comparison, unreliable at *adjudicating* conflicts | Averages away contradictions instead of surfacing them; invents a middle number that appears in no source | Same, with an explicit "show disagreement, do not resolve it" instruction | Cheap | This pass, §A of raw log — **High** |

**Verdict for ABMs.** Productised research and monitoring remains the single highest
autonomizability category (consistent with the Master Synthesis ranking). The reliable
version is **closed-corpus**: the customer's own documents, a curated source allowlist, or
a monitored set of URLs. Open-web research sold as a product inherits the 2026 web's
source-quality collapse and needs a human editor — which is fine for a solo operator whose
stated role includes quality gates, but it caps the margin.

---

### 2.2 Structured data extraction

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Simple fields from semi-structured docs (totals, names, dates, IDs) | **8/10** | **Yes** at 99%+ per field, with schema validation + confidence routing | Format normalisation errors (dates, currencies, thousands separators); hallucinating a plausible value rather than returning null | Gemini / GPT / Claude vision + JSON-schema-constrained output; LlamaParse-class parsers | Very cheap per document; batch discount applies | Invoice-OCR benchmarks 2026 — **Medium** for pattern, **Low** for any single figure |
| Complex fields (line items, multi-row tax tables, nested structures) | **6/10** | **No** for financial straight-through processing | 95–97% field accuracy vs a cited 99.9% STP threshold for financial/identity fields; row misalignment; dropped or duplicated rows; silent truncation of long tables | Same, plus deterministic post-validation (totals must reconcile) | Cheap per doc, expensive per *error* | Same — **Medium** |
| Extraction from poor-quality inputs (phone photos, faxes, handwriting) | **4/10** | **No** | Accuracy degrades sharply and *without a corresponding drop in stated confidence* — the most dangerous property in the whole category | Preprocessing + human queue | — | OCR accuracy comparisons 2026 — **Medium** |
| Unstructured text → structured records (emails, chat, notes → CRM fields) | **7/10** | **Yes** for low-stakes fields, **No** for anything that triggers an action | Over-extraction (inventing fields that were only implied); entity confusion across multiple people in one thread | Function-calling / structured-output modes | Cheap | Project corpus + this pass — **Medium** |

**Verdict for ABMs.** This is the most under-rated buildable category. The trick is that
**arithmetic and cross-field consistency are checkable deterministically** — if line items
must sum to a stated total, you get a free verifier, and a free confidence signal that is
actually calibrated. A workflow with a deterministic verifier can run at genuinely high
autonomy. A workflow without one cannot, regardless of model quality. **Design rule:
never ship an extraction product where the output cannot be checked by code.**

---

### 2.3 Long-horizon multi-step workflows

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| 3–10 step workflow, single domain, explicit state, API tools | **7/10** | **Yes** with per-step validation, idempotent steps, and a bounded retry policy | Step skipping when an intermediate output is ambiguous; retry storms; state drift between model belief and system of record | LangGraph (durable execution, checkpointing); Temporal/Inngest-class durable workflow engines; n8n for the glue | Predictable, roughly linear in steps | LangGraph production positioning — **Medium**; project corpus `2501.07834v2` (Flow, dynamic task graphs) — **High** |
| 10–50 step workflow with branching | **5/10** | **No** — needs checkpoints and a human-visible run log | Cascading local errors; loss of the original goal by mid-run; plan-repair loops that never terminate | Same + explicit task-graph decomposition and replanning bounds | Superlinear cost: context re-reading dominates | `2501.07834v2` (bounded replanning) — **High**; OSWorld 2.0 — **High** |
| Open-ended "achieve this outcome" over hours, multi-application | **3/10** | **No.** Do not build on this | **20.6% completion on OSWorld 2.0** at the frontier; the 50%-reliability horizon is a coin flip and METR flags measurements above 16h as unreliable at all | — | Very expensive per successful completion; the failed runs still cost full price | OSWorld 2.0 2026-06-26 — **High**; METR 2026-05-08 — **High** for caveats |

**Verdict for ABMs.** The gap between rows 1 and 3 is where nearly all failed AI startups
of 2025–2026 live. **Build in row 1. Sell the *outcome* of row 3 by composing row-1 units
behind a state machine you own.** Concretely: a durable workflow engine holds the state,
each node is a short bounded model call with a validator, and the customer sees a
long-horizon result. This is the "framed autonomy" of the Master Synthesis, expressed as
architecture.

---

### 2.4 Tool use & connector orchestration

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Calling 1–10 well-documented, typed APIs | **8/10** | **Yes** | Parameter hallucination on optional fields; wrong tool when two tools overlap semantically; ignoring an error response and proceeding as if it succeeded | Provider-native function calling; MCP for standardised tool surfaces | Cheap; tool schemas consume input tokens on every turn — keep the toolset small | Project corpus `a-practical-guide-to-building-agents` (tool risk tiers) — **High** |
| Calling 20+ tools / large MCP surfaces | **5/10** | **No** | Tool-selection accuracy degrades with surface size; schema tokens crowd the context; silent capability drift when a server updates | Tool search / progressive disclosure; namespacing; per-task tool subsets | Large surfaces raise per-turn cost materially | This pass + framework docs — **Medium** |
| Acting on **untrusted external content** while holding credentials | **2/10** | **No. This is the hard no of the entire map** | **MCPTox: >60%, up to 72% attack success across 45 live MCP servers and 353 real tools; the most-resistant model refused poisoned tool calls <3% of the time.** InjecAgent: 24%→47%. MCP-SafetyBench host-side attacks >80% | Nothing available in July 2026 makes this safe by itself. Mitigations are architectural: privilege separation, no outbound channel in the same context as untrusted input, allowlisted actions, human gate | Security failure cost is unbounded — it is not a cost line, it is a business-ending event | MCPTox (AAAI) — **High**; AgentDojo `2406.13352v3` — **High**; OX Security May 2026 — **Medium** |
| GUI / browser automation of third-party web apps without an API | **4/10** | **No** | Brittle to UI change; 20.6% on realistic long-horizon computer use; a failed run can leave the third-party system in a partial state | Playwright + vision as a *last resort*, ideally read-only | High cost per successful run | OSWorld 2.0 — **High** |

**Verdict for ABMs.** Connectors are the value and the risk in the same object. The
architectural rule that follows from the evidence is **the two-context rule**: a context
that reads untrusted input must not hold write credentials or an outbound channel, and a
context that acts must only receive *validated, typed, enumerated* instructions from the
first. Guardrails and prompt instructions do not substitute for this — the Master
Synthesis already lists "guardrails alone secure connectors" under *not supported*, and
the 2026 numbers make it emphatic.

---

### 2.5 Content generation + revision

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Transforming existing content between formats/lengths/registers | **9/10** | **Yes** | Voice drift over long batches; quiet factual insertion during "polish"; over-smoothing that removes distinctiveness | Any frontier or mid-tier model; cheap models are sufficient here | Very cheap; the best margin/quality ratio in the whole map | Master Synthesis (structured content transformation ranked high) — **High** |
| Generating net-new content from a brief | **7/10** | Partially | Generic register; unrequested claims; SEO-slop convergence — everyone's output looks the same because everyone's prompt is the same | Frontier models + strong style grounding on the customer's own prior work | Cheap | Anthropic Economic Index: Content Creation & Copywriting is the **largest global request topic at 22.7%** — **High** |
| Content requiring domain claims (health, legal, financial) | **3/10** | **No** | Confabulated specifics stated fluently; liability transfers to the operator | — | — | Master Synthesis: confabulation; project exclusions in Continuity §3 — **High** |
| Multi-turn revision against critique | **7/10** | Partially | Sycophantic agreement with bad critique; oscillation between two versions; "improvement" that changes meaning | Explicit rubric + diff-constrained edits | Cheap | LLM-judge bias literature 2026 — **Medium** |

**Verdict for ABMs.** Content Creation & Copywriting is simultaneously the **largest**
observed usage category globally (22.7% of requests) and therefore the **most
commoditised**. Generic content generation is not a business in July 2026. Content
*transformation embedded in a workflow with proprietary input* is — the defensibility
lives in the input (a specific customer's client history, service records, past messages),
not in the generation.

---

### 2.6 Monitoring + alerting

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Watching defined sources for defined change conditions | **8/10** | **Yes** | Alert fatigue from loose thresholds; missed change when source structure shifts silently; duplicate alerts on the same underlying event | Scheduled jobs + diffing + a model only for classification/summary of the delta | Very cheap — the model sees only the delta, not the corpus | Master Synthesis (productised monitoring ranked highest) — **High** |
| Judging whether a change **matters** to a specific customer | **6/10** | Partially | Miscalibrated importance; no memory of what was already flagged last week; over-alerting to look useful | Per-customer rubric + explicit suppression state | Cheap | This pass — **Medium** |
| Anomaly detection over business metrics | **7/10** | **Yes** for statistical detection, **No** for causal explanation | Confident spurious causation ("bookings fell because of the weather") | Deterministic stats for detection, model for narration only | Cheap | Project corpus `2603.18916v3` (APM: actionability and explanation) — **High** |

**Verdict for ABMs.** Monitoring is the highest-autonomy, lowest-risk, best-margin
capability available to a solo operator, for three structural reasons: the model handles
only the delta (cheap), errors are *omissions and noise* rather than destructive actions
(reversible), and the value is recurring by nature (subscription-shaped). **Separate
detection from explanation** — do detection in code, narration in the model — and the
failure surface stays small.

---

### 2.7 Code generation & maintenance

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Writing/modifying code in a repo with tests | **8/10** | **Yes** within a review gate; **No** for unattended deploy | Tests that pass while missing the bug (UTBoost shows SWE-bench suites are insufficiently rigorous, so reported scores are optimistic); plausible-but-wrong API usage; silent scope creep | Claude Agent SDK / Claude Code; OpenAI Codex-class; Gemini CLI; mini-swe-agent | Highest-value token spend available to a solo founder. This is the capability that makes the whole project feasible | SWE-bench Verified ~80–81% April 2026 cluster — **Medium**; UTBoost `2506.09289` — **High** |
| Long-running autonomous maintenance (dependency upgrades, refactors) | **6/10** | Partially, with CI as the verifier | Large diffs that pass CI and break behaviour; migration half-applied | Durable agent runs + CI gates + small-diff policy | Moderate | Terminal-Bench 2.0 / LongCLI-Bench 2026 — **Medium** |
| Greenfield systems from a spec | **6/10** | **No** | Architecture that works at demo scale and not at 100 customers; security defaults omitted | Human architectural decisions, agent implementation | Cheap relative to hiring | Project corpus `2308.00352v7` (MetaGPT SOPs), `2307.07924v5` (ChatDev maker/reviewer/tester) — **High** |

**Verdict for ABMs.** This is the strongest capability in the map *and* the reason a
solo operator can attempt any of this. It is also the most saturated market — the Economic
Index shows Computer & Mathematical at **23.8%** of all observed usage, ~1.75× the next
category. **Use coding capability as leverage; do not sell it as the product.**

---

### 2.8 Customer communication

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Answering questions from a defined knowledge base | **7/10** | **Yes** within a narrow, high-structure intent set | Confident answers outside the knowledge base; failure to escalate; policy invention ("we can refund that") | Intercom Fin, Decagon, Sierra, Lorikeet; or own build on a frontier model | Cheap per ticket | Vendor and third-party resolution data — **Medium** for the band |
| Autonomous resolution rate, realistic expectation | — | — | Vendor published averages span **51% / 67% / 76%** across sources; vendor's own case studies cluster **42–50%**; an independent 500-ticket small-business test landed at **38%**; B2B runs **17–25 points below** vendor benchmarks | — | — | Multiple 2026 sources, mutually inconsistent — **Low** individually, **Medium** for the 40–70% band |
| Outbound messages to customers (reminders, follow-ups, rebooking) | **7/10** | **Yes** for templated + variable-filled; **No** for free-composed | Wrong recipient; wrong appointment detail; tone mismatch; duplicate sends; sending during quiet hours | Deterministic templates with model-selected variables and a model-written single variable field | Very cheap | This pass — **Medium** |
| Voice / inbound phone handling | **6/10** | Partially | >800ms latency causes caller talk-over; ~80% first-attempt intent recognition in one 400-call test; accent and background-noise degradation; no graceful failure without an explicit fallback | Retell-class platforms (~600ms end-to-end, ~$0.07/min, native calendar booking) | **~$0.28 for a 4-minute booking call** — cheap enough to be transformative for single-location service businesses | Latency threshold recurs independently — **Medium**; intent figure single-tester — **Low** |

**Verdict for ABMs.** The decisive variable in the resolution-rate spread above is not
model quality — it is **intent-mix structure**. A narrow, high-structure intent set
(appointment change, price question, hours, directions, rebooking) reaches the top of the
band; open-ended B2B support does not. **Sell the narrow intent set.** And note the
asymmetry that makes outbound the better first product: an unsent reminder costs a missed
appointment; a wrongly-sent one costs trust. Templated outbound with model-selected
variables keeps the blast radius at "slightly awkward" rather than "wrong information
stated as policy."

---

### 2.9 Planning & task decomposition

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Decomposing a known process into steps | **8/10** | **Yes** | Plausible-but-wrong ordering; missing the error path entirely; omitting the step that requires information the model does not have | Explicit SOP/task-graph patterns | Cheap | `2308.00352v7` (SOPs), `2501.07834v2` (AOV graphs) — **High** |
| Planning in a novel domain | **5/10** | **No** | Confidently generic plans; the "jagged frontier" — same workflow, some steps helped, some harmed | Human-authored plan, agent execution | Cheap | `dell-acqua-et-al-2026` (jagged frontier, causal) — **High** |
| Dynamic replanning mid-run | **5/10** | **No** without bounds | Non-terminating repair loops; goal drift; each replan compounds context length and cost | Bounded replanning with a hard step budget and a fail-to-human exit | Cost grows fast | `2501.07834v2` — **High**; MAST — **High** |

**Verdict for ABMs.** **Author the process yourself; let the agent execute it.** The
jagged-frontier result is causal evidence that delegation must be decided *per task*, not
per role — which means the operator's real intellectual product is the task graph, and
that is a durable asset that does not depreciate when the model changes.

---

### 2.10 Memory & state management

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| State in an external system of record (DB, ledger) | **9/10** | **Yes** — this is ordinary software, and that is the point | Only the usual engineering failure modes | Postgres/Supabase; durable workflow checkpoints | Negligible | Master Synthesis: "model memory should not replace a system of record" — **High** |
| Within-task context (short-term memory) | **8/10** | **Yes** | Mid-context neglect; instruction decay over long contexts; earlier constraints quietly dropped | Compaction, explicit re-statement of constraints, structured scratchpads | Long contexts are the main cost driver in agent runs | Project corpus + this pass — **Medium** |
| Cross-session semantic memory (agent "remembers the customer") | **5/10** | **No** | Stale facts asserted as current; no invalidation on change; sycophantic memory drift (MemSyco-Bench, 2026); retrieval that only succeeds after background processing completes | Mem0, Zep, Letta, LangMem | Mem0 reports ~6,900 tokens/query; Zep's footprint reported >600k tokens/conversation — a 100× spread | Vendor self-reports, publicly disputed between vendors — **Low** |

**Verdict for ABMs — and this is a finding worth stating plainly.** *Every published
agent-memory number in July 2026 is a vendor number, and the two leading vendors publicly
dispute each other's methodology on the same benchmark (Mem0 reporting 65.99% for Zep;
Zep claiming 75.14% corrected).* There is no credible independent benchmark. Therefore:
**treat "agent memory" as an unbenchmarked layer and do not build a product whose core
promise is memory quality.** Put durable facts in a database with explicit schemas and
invalidation rules, and use the memory layer only for retrieval convenience. For a
customer-retention product — the project's prior lead candidate — this is decisive: the
"memory" that a client prefers a certain treatment must be a *typed database field with a
last-confirmed date*, not a vector recollection.

---

### 2.11 Evaluation & self-critique

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| Deterministic verification (schema, arithmetic, API echo, diff, test suite) | **9/10** | **Yes** | Only what you forgot to check | Plain code. Always prefer this | Negligible | Master Synthesis — **High** |
| LLM-as-judge on a fixed rubric, used as a **regression detector** | **7/10** | **Yes** for relative comparison over time | Systematic position bias across 15 judges / ~150k instances — **not random**, varies by judge and task; verbosity and self-preference bias | Frontier judge + fixed rubric + randomised option order + repeated sampling | Moderate: judging costs real tokens at volume | `arXiv 2606.19544` (2026-06) — **High**; RAND 2026 via secondary — **Low–Medium** |
| LLM-as-judge as an **absolute quality certifier** | **3/10** | **No** | Reliability without validity — consistent scores that do not track truth. Strong judges reach κ>0.80 on well-structured tasks but no judge is uniformly reliable across benchmarks | — | — | Same — **High** |
| Agent self-critique / self-correction | **5/10** | **No** | Cannot detect its own confabulations; "I have verified this" without verifying; confidence unchanged by error | Independent reviewer *with different tools and a separate context* | Doubles inference cost | `2307.07924v5` (maker/reviewer/tester), MAST verification cluster — **High** |

**Verdict for ABMs.** The title of the 2026 judge paper — *Reliability without Validity* —
is the whole lesson. Build the evaluation ladder in this order and never skip a rung:
**(1) deterministic checks, (2) a small hand-labelled golden set, (3) an LLM judge on a
fixed rubric for regression only, (4) sampled human review of production traffic.** The
Master Synthesis' instruction to build measurement *before* expanding authority is now
directly supported by measurement of the measurers.

---

### 2.12 Multi-agent coordination

| Capability | Maturity | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---|---|---|---|---|---|
| One agent, many tools, explicit state machine | **8/10** | **Yes** for bounded workflows | Covered in §2.3/§2.4 | LangGraph; Claude Agent SDK; durable workflow engines | Predictable | MAST — **High**; mini-swe-agent near-SOTA with minimal scaffold — **Medium** |
| Pipeline of specialised agents with typed handoffs (maker → reviewer → tester) | **7/10** | **Yes** where each handoff is a validated artifact | Reviewer rubber-stamps; error propagates because the handoff was prose rather than a typed object | MetaGPT/ChatDev-style SOP pipelines; LangGraph subgraphs | Cost multiplies by stage count | `2308.00352v7`, `2307.07924v5` — **High** |
| Peer agents negotiating a shared goal | **3/10** | **No** | The MAST 14: specification/design violations, inter-agent misalignment (information withholding, derailment, reasoning-action mismatch), verification failures. Gains on benchmarks "often minimal" | — | Worst cost/benefit ratio in the map: token spend multiplies, reliability falls | MAST (NeurIPS 2025) — **High** |
| Open agent swarms / emergent org structures | **2/10** | **No** | Everything above, unbounded | — | — | MAST — **High**; Master Synthesis "not yet supported" — **High** |

**Verdict for ABMs.** **Do not build a crew.** Build one agent, or a pipeline whose
handoffs are typed artifacts that a validator can inspect. The evidence that MAS gains are
minimal while MAS failure surface is large has now been replicated across 1,600+ traces
and 7 frameworks. Multi-agent architecture in 2026 is a marketing aesthetic, not an
engineering advantage, outside of narrow well-studied pipelines.

---

## 3. Agent Architecture Patterns That Actually Work in Production

Five patterns, ordered by evidence strength. Each is a *composition* rule, not a product.

### P1. Durable state machine with short model calls at the nodes
The workflow engine (LangGraph, Temporal, Inngest, or plain Postgres + a job runner) owns
the truth: current step, inputs consumed, outputs produced, retry count. Each node is a
short, well-specified model call with a validator. The model never holds the plan.
**Why it works:** it converts a 3/10 capability (§2.3 row 3) into a composition of 7–8/10
capabilities. It also makes every run auditable, which is the precondition for
progressively removing human gates. *(**High** — this is the operationalisation of the
Master Synthesis conclusion, and matches both LangGraph's production positioning and the
Flow/MetaGPT task-graph findings.)*

### P2. Deterministic verifier attached to every autonomous step
If an output cannot be checked by code — schema valid, totals reconcile, API echoed the
expected state, tests pass, diff within bounds — the step does not get to be autonomous.
It gets a human queue.
**Why it works:** it is the only mechanism in the map with 9/10 maturity, and it produces
a *calibrated* confidence signal, which no model self-report does. **This is the single
highest-leverage design rule in this document.** *(**High**.)*

### P3. The two-context rule (privilege separation around untrusted input)
Context A reads untrusted external content (customer emails, tickets, web pages, uploaded
documents) and has **no credentials and no outbound channel**. It emits a typed,
enumerated, validated object. Context B acts on that object with credentials but **never
sees the raw untrusted text**.
**Why it works:** the MCPTox/InjecAgent/MCP-SafetyBench results show injection resistance
at the model level is effectively absent (<3% refusal for poisoned tools in the most
resistant model tested). If resistance cannot be bought, the attack must be made
structurally unprofitable. Every real-world incident in the record follows the
privileged-access + untrusted-input + outbound-channel pattern; breaking any one leg
breaks the chain. *(**High**.)*

### P4. Risk-tiered gates with progressive removal
Tier 0 (read-only, internal) → autonomous from day one.
Tier 1 (reversible external writes: draft created, internal note, tag applied) → autonomous
after a measured period.
Tier 2 (irreversible external effects: message sent to a customer, record written to a
system of record, schedule changed) → human gate until per-workflow accuracy is measured
on real traffic, then sampled review.
Tier 3 (money movement, contractual commitments, anything the exclusions list touches) →
permanent human gate, or do not build it.
**Why it works:** it makes "autonomy %" an *earned, measured* quantity per workflow rather
than a product claim, which is exactly the success metric in Continuity §8. *(**High** —
project corpus: practical guide tool-risk tiers, NIST AI 600-1, APM controlled adaptation.)*

### P5. Independent review with a different context and different tools
Where a human gate is being removed, the reviewer must be a *separate* invocation with a
separate context and, ideally, different tools — not the same agent asked to double-check.
Self-critique is 5/10; independent review with typed artifacts is 7/10.
**Why it works:** MAST's third failure cluster is task verification, and ChatDev/MetaGPT's
measured gains come specifically from role separation with structured intermediate
artifacts. *(**High**.)*

### Anti-patterns, stated explicitly
- **Agent swarms / peer negotiation.** 2–3/10. Cost up, reliability down. *(MAST — High.)*
- **Long-horizon GUI automation as the core mechanism.** 20.6% on realistic tasks. *(High.)*
- **Model memory as the system of record.** Unbenchmarked, vendor-disputed, no invalidation
  semantics. *(High that the evidence is absent.)*
- **Guardrails/prompts as a security boundary.** Explicitly in the Master Synthesis'
  not-supported list; the 2026 injection numbers close the case. *(High.)*
- **LLM judge as the only quality gate.** Reliability without validity. *(High.)*
- **"We'll add evaluation later."** Authority granted before measurement is the failure
  mode that ends businesses rather than sprints. *(High.)*

---

## 4. Hard Limits (critical section)

These are the walls. Each is stated as a constraint on what can be *sold*, with the
evidence and the design consequence.

### L1. Long-horizon autonomy on realistic multi-application work
**The wall:** 20.6% task completion at the frontier on OSWorld 2.0; ~66% on the earlier,
easier OSWorld revision against a 72.4% human baseline. A single benchmark revision toward
realism cut success roughly 3×. METR's 50%-reliability horizons (14–20h) are *coin-flip*
horizons on *well-specified algorithmic software tasks* judged against a *low-context* human,
and METR states measurements above 16h are unreliable with its current task suite.
*(OSWorld 2.0 2026-06-26 — **High**; METR 2026-05-08 — **High** for caveats, **Medium**
for figures.)*
**Consequence:** you cannot sell "the agent runs your operation." You can sell "the agent
runs these eleven named steps, and here is the log." The extrapolation that horizons double
every ~4 months is real but must not be built into a business plan: the doubling is measured
on the narrow task family above, and the metric's own ceiling has been reached.

### L2. Prompt injection and connector security
**The wall:** >60% (up to 72%) attack success across 45 live MCP servers and 353 real tools;
most-resistant model refuses poisoned tool calls <3% of the time; host-side MCP attacks >80%;
a systemic multi-language MCP vulnerability disclosed May 2026. *(**High**; scale **Medium**.)*
**Consequence:** this is not a residual risk to be documented — it is a **design
constraint that dictates architecture** (see P3). For a solo operator with no security team
and personal liability, any product where a customer's counterparty can write text that
reaches a credentialed agent must be architected on the two-context rule or not built.

### L3. Calibration — models do not know when they are wrong
**The wall:** extraction accuracy degrades sharply on poor inputs *without a corresponding
drop in stated confidence*; self-critique cannot detect the model's own confabulations;
LLM judges show reliability without validity. *(**High** across §2.2, §2.11.)*
**Consequence:** confidence scores from models are not routing signals. Only deterministic
checks produce trustworthy confidence. **If you cannot verify it in code, you cannot
automate it.** This single sentence eliminates the majority of superficially attractive AI
product ideas, and doing that elimination early is the point of this map.

### L4. The jagged frontier — capability is not uniform within a role
**The wall:** causal experimental evidence that AI helps on some tasks and *harms*
performance on others inside the same workflow, and that lower-performing users can be
harmed by generic AI advice on difficult problems. *(dell'Acqua et al. 2026; Kenyan
entrepreneurs RCT — both in project corpus — **High**.)*
**Consequence:** delegate per task, never per role. "AI [job title]" as a product framing
is contradicted by the strongest causal evidence available. Also: an AI advisor product
aimed at less-experienced operators can make their outcomes *worse* — directly relevant if
this project targets small-business owners.

### L5. Multi-agent coordination
**The wall:** 14 failure modes, 1,600+ annotated traces, 7 frameworks; benchmark gains
"often minimal"; failures traced to system design rather than model quality.
*(MAST — **High**.)*
**Consequence:** architectural simplicity is a competitive advantage, not a compromise.

### L6. Cross-session memory has no trustworthy evidence base
**The wall:** every number is a vendor number; the two leading vendors publicly dispute
each other on the same benchmark; a 100× spread in reported token footprint; documented
retrieval-latency behaviour that breaks real-time use; sycophantic memory drift newly
identified (MemSyco-Bench, 2026-07). *(**High** that independent evidence is absent.)*
**Consequence:** durable customer facts go in a typed database with last-confirmed
timestamps and invalidation rules. Memory frameworks are a retrieval convenience only.

### L7. Regulatory, liability and exclusion boundaries (project-specific)
The Continuity constraints exclude clinical health expertise, childcare for small children,
supplements, high-stakes legal/financial products, food, and anything with significant
injury or large-financial-loss risk. The capability evidence *independently* reaches the
same place: confabulation makes domain-claim generation 3/10 (§2.5), and irreversible
high-stakes action is exactly where verification is weakest. **The constraints and the
capabilities agree, which is a good sign the constraints are well-chosen.** *(**High**.)*

### L8. Economic limits, stated honestly
- Token cost is negligible for §2.1, 2.2, 2.5, 2.6 and material only where consumption is
  superlinear in horizon: long-context re-reading, retry storms, multi-agent chatter,
  judge-at-volume. **Cost discipline is horizon discipline.**
- **Failed runs cost full price.** At 20.6% completion, an open-ended long-horizon product
  pays ~5× per delivered outcome, before support cost.
- The genuinely new economic fact of 2026 is **voice at ~$0.07/min** *(**Medium**)* —
  cheap enough that inbound-call capture becomes viable for a single-location business,
  which was not true two years ago.

### L9. The measurement gap between benchmarks and production
**The wall:** UTBoost shows SWE-bench test suites are insufficiently rigorous, making
reported scores optimistic; the AI Index reports broad adoption alongside limited agentic
deployment; the Anthropic Economic Index notes task success rates are *not published* for
the current period. *(**High**, **Medium**, **High** respectively.)*
**Consequence:** benchmark numbers set an *upper bound*, never an expectation. Your own
golden set on your own workflow is the only number that matters — and building it is cheap
and is the thing almost nobody does.

---

## 5. Tool & Platform Landscape (July 2026)

Confidence on this section is **Medium** overall: the landscape is well-reported but almost
entirely by vendors and vendor-adjacent media. Prices and positioning must be re-checked
against vendor pages before any commitment (raw log §C, debt 3).

### 5.1 Models
| Tier | Reported price /1M tok (in/out) | Where it fits in an ABM |
|---|---|---|
| Frontier | ~$5 / $25–30 | Planning, hard reasoning, judge-of-record, novel-situation handling. Use sparingly, at named nodes |
| Strong mid-tier | ~$1–2.50 / $6–15 (one flagship mid-tier on promo at $2/$10 until 2026-08-31, reverting to $3/$15) | **The workhorse.** Almost all §2.1/2.2/2.5/2.6 work belongs here |
| Small/cheap | ~$0.10–0.15 / $0.28–0.60 | Classification, routing, extraction of simple fields, high-volume triage |
| Batch APIs | flat **50%** discount, near-universal | Anything not interactive: overnight monitoring sweeps, backfills, judging |

Design note: **tier per node, not per product.** A monitoring workflow that routes with a
$0.10 model and narrates with a mid-tier model costs an order of magnitude less than one
frontier call per item, at equal output quality — because the expensive judgement is a
small fraction of the tokens.

### 5.2 Orchestration
- **LangGraph** — reported 34.5M monthly downloads and positioned as the production default
  for stateful, durable, auditable graphs, with first-class human-in-the-loop; named
  enterprise deployments include Klarna, Uber, LinkedIn, BlackRock, JPMorgan, Replit.
  *(**Medium**.)* Best fit for P1 and P4.
- **Claude Agent SDK** (renamed from Claude Code SDK, early 2026) — provider-native;
  reported as the most robust error handling, prioritising reliability and safety defaults
  over raw speed. *(**Medium**.)* Best fit where the operator is also the developer.
- **OpenAI Agents SDK** — the productionised successor to Swarm, with sandboxed execution
  and a harness system. *(**Medium**.)*
- **Google ADK**, **CrewAI**, **AutoGen/AG2**, **smolagents**, **Pydantic AI**, **DSPy** —
  the independent/portable tier. CrewAI and AutoGen are the crew-shaped frameworks that
  §2.12 and MAST advise against for new builds.
- **Durable execution** (Temporal, Inngest, or Postgres + job runner) — the unglamorous
  option that satisfies P1 and P4 with no agent framework at all. Genuinely worth
  considering as the default for a solo operator: fewer moving parts, no framework churn.
- **The structural split to keep in mind:** provider-native SDKs (one model family, best
  defaults, lock-in) vs independent frameworks (portable, more glue to maintain). For a
  solo operator, framework churn is a real cost; prefer the option you can still understand
  in twelve months.

### 5.3 Connectors and tool surfaces
- **MCP** is the de facto standard tool boundary in 2026. It is a *convenience* standard,
  not a trust standard — MCP connectivity establishes nothing about permissioning
  (Master Synthesis glossary, and now MCPTox). *(**High**.)*
- **n8n / Make / Zapier** — the low-code glue layer. The project's own corpus
  (`2606.29116v2`) characterised real n8n LLM workflows as having **tight action coupling
  and missing reliability controls** — i.e. the fast path to a working demo and the fast
  path to L2/L3 exposure. Usable for Tier-0/Tier-1 work; not for credentialed action on
  untrusted input. *(**High** for the corpus finding.)*
- **Practical rule:** small hand-curated tool surfaces beat large MCP surfaces (§2.4 row 2).

### 5.4 Vertical / applied platforms relevant to this project
- **Customer support:** Intercom Fin, Decagon, Sierra, Lorikeet. Realistic autonomous
  resolution **40–70%**, driven by intent-mix structure; B2B runs 17–25 points lower.
  *(**Medium** for the band.)*
- **Voice:** Retell-class platforms — ~600ms end-to-end, ~$0.07/min, native Cal.com and
  Google Calendar booking; >800ms causes caller talk-over. *(**Medium**.)* The most
  commercially interesting new primitive for service businesses.
- **Document extraction:** frontier vision models plus LlamaParse-class parsers; 97–99% on
  simple fields, 95–97% on line items, against a 99.9% straight-through-processing
  threshold for financial fields. *(**Medium**.)*
- **Memory:** Mem0, Zep, Letta, LangMem — see L6. Use with a database underneath.
- **Observability/eval:** LangSmith, Braintrust, Phoenix/Arize, Langfuse. Under-adopted
  relative to their importance; this is where the P2/P4 evidence trail lives, and it is
  cheap to set up on day one and expensive to retrofit.

### 5.5 Market context (Low confidence, direction only)
Agent-platform market reported at $7.84B (2025) projected to $52.62B (2030) at 46.3% CAGR;
Gartner projecting 40% of enterprise applications to feature task-specific agents by
end-2026, up from <5% in 2025. *(**Low** — analyst projections with unverifiable
methodology.)* Included only to note that the tooling layer is consolidating fast, which
argues for building on boring, replaceable infrastructure rather than on a specific
framework's abstractions.

---

## 6. Open Gaps & Research Frontiers

Ordered by value to this project. Each of these is simultaneously a knowledge gap and a
potential source of advantage — a gap in the public evidence base is a gap in every
competitor's plan too.

**G1. Injection-resistant architectures for small operators.** The literature documents the
attack thoroughly and the defence barely. There is no widely-adopted reference pattern for
"a two-person business safely lets an agent read customer email and write to its CRM."
P3 is the right shape; a tested, documented implementation of it would be a genuine asset.
**Highest-value gap for this project.**

**G2. Independent agent-memory benchmarking.** L6 is a hole in the public record, not a
finding about capability. Anyone who measures memory systems credibly on a real business
workload — a service business's client history, say — would be first.

**G3. Per-workflow autonomy measurement for micro-businesses.** The reliability literature
(`2602.16666v3`, `2512.04123v4`) is written for enterprises with platform teams. There is
no published methodology for a solo operator to measure and safely expand autonomy on
a single workflow. Continuity §8 requires exactly this instrumentation (≥70% task autonomy
with cost, success rate, intervention frequency). **Building it is a prerequisite, and it
may be productisable in its own right.**

**G4. The tooling-attention asymmetry, quantified.** The Economic Index numbers in §1.7
(Personal Care & Service 1.23% of usage; hairdressing tasks 0.02%, rank 318/718; against
Computer & Mathematical 23.8%) are the strongest quantitative whitespace signal found in
this pass. They need careful handling — the dataset measures *usage of tasks*, not people
or jobs, and cannot speak to employment — but as a measure of where AI attention is
*pointed*, the asymmetry is stark and directly serves Map 2. **Carry this into
`04-Cross-Analysis/`.**

**G5. Reliability of outbound customer communication.** §2.8 has a good evidence base for
*inbound* resolution and almost none for *outbound* correctness (right person, right
detail, right time, no duplicates). Outbound is the better first product for the reasons
given, and the metric that matters is unpublished. Measure it yourself.

**G6. Cost per *delivered outcome*, not per token.** No source found reports cost per
successfully completed workflow including failed retries. At 20.6% completion on hard
tasks, this is a ~5× multiplier that no published pricing analysis accounts for.

**G7. Verification-first task taxonomy.** L3 implies the decisive question for any candidate
workflow is "can a program check the output?" A systematic taxonomy of business tasks by
*verifiability* would be a better idea-generation instrument than the capability list in
§2. Suggest building it in `04-Cross-Analysis/` as the screening filter before scoring
micro-ABMs.

**G8. Model-independence as a design goal.** Algorithmic monoculture is named in the
Master Synthesis glossary as correlated-failure exposure, and 2026's price and capability
churn (a mid-tier flagship's price changing on 2026-08-31 mid-project) makes provider
lock-in a live operational risk. Unstudied for solo operators; cheap to design for now,
expensive later.

---

## Verification debts carried forward

Recorded in full at `99-Raw-Extractions/AI-Capabilities-Claude-2026-07-26.md` §C. The four
that most affect this map:
1. Pin exact METR 50%/80% horizons from the interactive chart (the §1.1 figures are Medium,
   not High, only because of this).
2. Fetch the Stanford AI Index 2026 primary PDF; replace all §1.3 secondary citations.
3. Re-verify all §5.1 pricing against vendor pages.
4. Find any non-vendor agent-memory benchmark, or state its absence as a finding (L6).

---

## Sources

Primary and high-trust:
- [METR — Task-Completion Time Horizons](https://metr.org/time-horizons/) (page updated 2026-05-08); [Clarifying limitations of time horizon](https://metr.org/notes/2026-01-22-time-horizon-limitations/); [Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/); [original method paper](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://s46486.pcdn.co/wp-content/uploads/2022/01/OSWorld2.0.pdf) (2026-06-26); project note `05-Previous-Research/Individual-Papers/2606.29537v2.md`
- [Why Do Multi-Agent LLM Systems Fail? (MAST)](https://arxiv.org/abs/2503.13657), NeurIPS 2025; [MAST repo](https://github.com/multi-agent-systems-failure-taxonomy/MAST)
- [MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers](https://ojs.aaai.org/index.php/AAAI/article/view/40895/44856), AAAI
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models](https://arxiv.org/abs/2606.19544) (2026-06)
- [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://arxiv.org/abs/2506.09289)
- [Anthropic Economic Index](https://www.anthropic.com/economic-index) — CC BY 4.0, period 2026-05-01, snapshot 2026-06-24; accessed 2026-07-26
- [MemSyco-Bench: Benchmarking Sycophancy in Agent Memory](https://arxiv.org/pdf/2607.01071) (2026-07)
- [SWE-bench Verified](https://www.swebench.com/verified.html)
- Project corpus (`05-Previous-Research/`): `2506.17339v2` AI Is the Strategy · `2502.00009v1` The Solo Revolution · `2512.04123v4` Measuring Agents in Production · `2602.16666v3` Science of AI Agent Reliability · `2603.18916v3` Agentic BPM · `2605.10291v1` GenAI Fuels Solo Entrepreneurship · `dell-acqua-et-al-2026` Jagged Technological Frontier · `2308.00352v7` MetaGPT · `2501.07834v2` Flow · `2406.13352v3` AgentDojo · `2606.29116v2` n8n workflow characterization · `2403.08399v2` Multi-agent SLR · `a-practical-guide-to-building-agents` · `NIST.AI.600-1` · `chatgpt-kenyan-entrepreneurs` · `2307.07924v5` ChatDev

Secondary (Medium confidence, verification debts noted):
- Stanford AI Index 2026 via [Forbes, 2026-04-14](https://www.forbes.com/sites/stevenwolfepereira/2026/04/14/stanfords-ai-report-card-agents-are-ready-companies-are-not/) and [SAPinsider](https://sapinsider.org/blogs/stanford-ai-index-2026-enterprise-ai-readiness-governance-risk/)
- Pricing aggregators, July 2026: [TLDL](https://www.tldl.io/resources/llm-api-pricing), [Morph](https://www.morphllm.com/llm-api), [Developers Digest](https://www.developersdigest.tech/blog/frontier-model-api-pricing-june-2026)
- Support-automation benchmarks: [Lorikeet, 2026](https://www.lorikeetcx.ai/articles/resolution-rate-ai-customer-support-benchmarks-2026)
- Document extraction: [aimultiple invoice OCR benchmark](https://research.aimultiple.com/invoice-ocr/), [Vellum](https://www.vellum.ai/blog/document-data-extraction-llms-vs-ocrs)
- Voice latency and pricing: [Trillet latency benchmarks](https://trillet.ai/blogs/voice-ai-latency-benchmarks), [Retell AI](https://www.retellai.com/blog/best-ai-voice-platforms-virtual-receptionists)
- Memory vendor claims (Low, disputed): [Mem0 2026 benchmark report](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- Framework landscape: [Morph agent frameworks 2026](https://www.morphllm.com/ai-agent-framework), [Firecrawl open-source frameworks](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks)
- MCP security incident reporting: [Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-vulnerabilities/), [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026)

Rejected sources are listed by name with reasons in `99-Raw-Extractions/AI-Capabilities-Claude-2026-07-26.md` §A.
