# AI Capability Map – 2026-07-27

**Version:** 1.1 — Claude foundation plus independent ChatGPT evidence audit
**Scope:** Production-relevant AI agents and systems available by July 2026
**Not in scope:** Product ideation or crossing capabilities with market needs

## Evidence and rating conventions

- **Maturity 1–3:** experimental; unsuitable for unattended business outcomes.
- **Maturity 4–6:** useful with a bounded task, instrumentation, and routine
  human or deterministic review.
- **Maturity 7–8:** production-capable for well-specified use cases with
  conventional software controls and exception handling.
- **Maturity 9–10:** commodity-level reliability across varied environments.
  No generative-agent category earns this rating in this map.
- **Reliable without human?** means repeated completion of the stated business
  outcome, not plausible text or a successful demonstration.
- **High confidence** normally means a primary official source, peer-reviewed
  paper, or official benchmark with inspectable methods. **Medium confidence**
  normally means a current preprint or vendor observational/deployment report.
  **Low confidence** is reserved for marketing or evidence that has not been
  independently validated.
- Product availability, price, and model names are a dated **2026-07-27
  snapshot**. A platform having a feature is not evidence that applications
  built with it are reliable.
- Sources from 2024 are retained only when they remain foundational and are
  marked as older under the project’s source rules.

## 1. Executive Summary

### The production reality

AI systems are already useful production components, but the reliable product
is usually a **controlled workflow containing model calls**, not a general
autonomous worker. The strongest systems narrow the task, expose state, limit
permissions, verify outputs, checkpoint progress, and escalate exceptions.
This conclusion is consistent across field evidence, benchmarks, security
research, and current platform guidance.

The best cross-domain production study available in this audit reports 20 case
studies and 86 practitioners across 26 domains. Sixty-eight percent of deployed
agents execute no more than 10 steps before human intervention; 70% primarily
prompt off-the-shelf models; 74% rely mainly on human evaluation; and
reliability is the leading deployment challenge [S03, 2026-06-04, **High**].
This is widespread use of **bounded autonomy**, not evidence of an unattended
general workforce.

Capability and reliability are different variables. A 2026 ICML study evaluates
15 models using 12 measures of consistency, robustness, predictability, and
safety and finds that recent capability gains produce much smaller reliability
gains [S04, 2026-06-02, **High**]. A system can therefore become more impressive
at its best while remaining too inconsistent for an unverified recurring
process.

Long-horizon computer use remains a hard boundary. OSWorld 2.0 contains 108
realistic workflows with median human duration around 1.6 hours and an average
318 tool calls. Its strongest reported configuration completes only 20.6% of
tasks under a strict binary measure, although partial completion reaches 54.8%.
Common failures include losing constraints, ignoring new information, guessing
instead of asking, skipping verification, and misreading hidden state [S06,
2026-07-13, **Medium-High**]. A more terminal-oriented benchmark reaches 65.8%
on 120 tasks, reinforcing that explicit, machine-readable interfaces are
materially easier than GUI state, but still not generally unattended [S07,
2026-06, **Medium**].

Tool use is strongest when it is short, typed, observable, reversible, and
low-risk. The April 2026 Berkeley Function-Calling Leaderboard reports a top
multi-turn score of 68.38 compared with 88.58 for single-turn tasks [S08,
2026-04-12, **High**]. That gap is the practical distance between “the model can
call a function” and “the system can manage a business process.”

Security is not solved by telling the model to be careful. MCPTox evaluates 45
live MCP servers, 353 tools, 1,348 cases, and 20 agent settings; it observes an
attack-success rate as high as 72.8%, with many popular settings above 60%
[S10, 2026-03-14, **High**]. MCP-SafetyBench finds overall attack success of
29.8–48.16%, an 81.94% average for host-side attacks, and 100% identity-injection
success across 13 tested models [S11, 2026, **High**]. Any agent that reads
untrusted content and holds consequential permissions needs architectural
isolation, not just prompt guardrails.

Multi-agent systems are conditionally useful, not an automatic upgrade. Across
180 configurations, centralized multi-agent systems improve parallelizable
tasks by as much as 80.9%, but all tested multi-agent variants degrade
sequential tasks by 39–70%; decentralized systems amplify independent errors
17.2 times versus 4.4 times for centralized systems [S29, 2026-01-28,
**Medium-High**]. The right rule is: use multiple agents only when subtasks can
be independently executed, objectively checked, and deterministically merged.

### What can be trusted today

With the controls specified in this map, current systems are production-capable
for:

- drafting, rewriting, classification, translation, and summarization;
- evidence collection and first-pass synthesis with inspected citations;
- schema-constrained extraction from bounded document classes, with field-level
  validation and exception queues;
- short tool workflows over typed APIs with explicit postconditions;
- monitoring in which deterministic collectors find events and models
  summarize, cluster, or prioritize;
- bounded code changes in a sandbox, gated by strong tests and review;
- grounded customer-service triage and routine support, with verified
  transactions and escalation;
- task decomposition and routing under a clear goal and known constraints;
- evaluation where a deterministic oracle or task-specific checker exists; and
- parallel specialist work whose dependencies are represented in a DAG and
  whose outputs can be independently scored.

They should not be trusted without human or deterministic control for:

- general long-horizon GUI operation;
- self-certifying completion or quality;
- high-impact action after reading untrusted web, email, or document content;
- model memory acting as the business system of record;
- open-ended strategic judgment, negotiation, or relationship ownership;
- open multi-agent swarms;
- regulated advice or irreversible financial, legal, medical, or safety
  decisions; or
- any workflow whose failure is difficult to detect, reverse, or compensate.

### The system design implication

The most dependable pattern is:

`typed input -> explicit state -> short model step -> restricted tool ->
deterministic check -> durable checkpoint -> risk gate -> observable outcome`

The model supplies probabilistic judgment. Ordinary software owns identity,
authorization, state transitions, invariants, money movement, audit logs,
idempotency, and proof of completion. This is the same “bounded,
process-aware autonomy” conclusion reached in the project’s previous synthesis
[S02, 2026-07, **High** for internal synthesis].

## 2. Core Capability Categories

### 2.1 Research & synthesis

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Search-plan generation, query expansion, and source discovery | 8 | Yes for discovery; no for final source selection | Search drift, duplicated sources, popularity bias, missed local-language material | Search APIs plus a model-driven query loop; commercial “deep research” modes | Cheap compared with analyst time, but tool calls and long contexts accumulate; cap queries and deduplicate | [S15, 2025-06, **Medium**]; [S16, 2025-06, **Medium**] |
| Bounded-corpus summarization and comparison | 8 | Usually, when every statement must map to supplied evidence | Omission, compression of disagreement, lost qualifiers, citation attached to the wrong clause | Long-context models, retrieval with stable document IDs, claim-to-evidence tables | Batch processing is economical; quality rises when the corpus is pre-cleaned and segmented | [S17, 2026, **High**]; [S31, 2024-12-19, **Medium-High**, older] |
| Open-web research with citations | 6 | No for consequential claims | Source fabrication, citation laundering, stale evidence, temporal errors, selective synthesis | Deep-research agents with frozen evidence snapshots, browser traces, citation checkers | One answer can require dozens of searches and large contexts; pay for verified claims, not generated pages | [S15, 2025-06, **Medium**]; [S16, 2025-06, **Medium**]; [S17, 2026, **High**] |
| Cross-lingual and local-market research | 5 | No | Translation changes entity names and qualifiers; lower retrieval recall; English/US source bias | Multilingual search, native-language queries, bilingual evidence review | Requires more queries, human spot checks, and local primary sources; Vietnam evidence is thinner | [S18, 2026-06, **Medium**]; project source rules |
| Final decision-grade synthesis | 5 | No | Fluent narrative hides unsupported inference, conflicting evidence is averaged away, static judges approve polished errors | Claim ledger, contradiction table, independent reviewer with tools, human sign-off | Verification can cost as much as first-pass research; this is appropriate for major decisions | [S17, 2026, **High**]; [S27, 2026-06-01, **Medium**] |

**Production boundary.** Research agents are reliable assistants when the
deliverable exposes sources, dates, uncertainty, and unresolved conflicts.
They are not reliable authorities. “Citation present” is not the same as
“claim entailed”: ACL 2026 describes a mirage in which fluent, citation-aligned
reports still obscure factual and reasoning defects [S17, 2026, **High**].

**Recommended control stack.** Freeze or archive decisive source passages;
record the query trail; require claim-level citations; use a separate checker
that can open sources; and send high-impact or conflicting claims to a human.

### 2.2 Structured data extraction

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Typed JSON/schema compliance from clean text | 9 | Yes for syntax; not automatically for values | Valid JSON containing wrong, missing, or normalized-away values | Native structured outputs, JSON Schema, constrained decoding | Very low retry cost; schema validation should be mandatory | [S19, 2026-04-28, **Medium**] |
| Exact field extraction from bounded clean text | 8 | Yes for low-risk fields with validation | Negation errors, unit conversion, entity confusion, silent null filling | Schema-constrained LLM plus regex/rules and source-span capture | Best benchmark exact leaf-value result is 83.0%; reconciliation is still needed for critical fields | [S19, 2026-04-28, **Medium**] |
| Repeated semi-structured documents from a known template | 8 | Often, with template checks and exceptions | Template drift, OCR errors, column association, headers/footers copied as data | Hybrid template inference, targeted LLM extraction, OCR, deterministic parsers | Hybrid systems can be dramatically faster and cheaper than applying a vision model to every page | [S20, 2025, **High**]; [S21, 2025-05-15, **Medium-High**] |
| Heterogeneous PDFs, scans, tables, and forms | 5 | No | Reading-order loss, merged cells, handwriting, low-resolution OCR, layout-dependent relationships | Document AI parsers, multimodal models, page images plus field validators | Best reported exact leaf-value accuracy on document images is 67.2%; exception handling dominates operating cost | [S19, 2026-04-28, **Medium**]; [S20, 2025, **High**] |
| Audio/transcript-to-record extraction | 4 | No | Speaker confusion, numbers and names misheard, inferred facts, missing context | ASR plus diarization plus schema extraction and confirmation | Best reported exact leaf-value accuracy is only 23.7% in the cited benchmark | [S19, 2026-04-28, **Medium**] |
| High-stakes record creation | 3 | No | Plausible but wrong values pass format validation; provenance lost | Dual extraction, deterministic reconciliation, source-span review, human approval | Human review cost is justified when one wrong field creates legal, financial, or safety exposure | [S19, 2026-04-28, **Medium**]; [S14, 2024/2026, **High**] |

**Critical distinction.** Near-perfect schema compliance is not near-perfect
extraction. A 2026 benchmark over 21 models reports best exact leaf-value
accuracy of 83.0% for text, 67.2% for document images, and 23.7% for audio even
when output format is usually correct [S19, 2026-04-28, **Medium**].

**Production boundary.** A robust extractor returns the value, the supporting
span or page, field-level confidence, validation results, and an explicit
exception—not merely a JSON object.

### 2.3 Long-horizon multi-step workflows

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Predefined workflow with short model nodes and durable state | 8 | Yes for low-risk processes with deterministic gates | Bad routing, unhandled exception, non-idempotent retry | State machines, Temporal/DBOS/Restate/Dapr, LangGraph checkpoints, OpenAI Agents SDK | Workflow overhead is modest; the value comes from resumption and controlled retries | [S31, 2024, **Medium-High**, older]; [S34, 2026-07-27, **High**]; [S35, 2026-07-27, **High**] |
| Ten-or-fewer step bounded agent loop | 7 | Sometimes | Tool error, instruction drift, premature stopping, retry loops | Agent harness with step budget, postconditions, and escalation | This matches the dominant production pattern: 68% intervene by 10 steps | [S03, 2026-06-04, **High**] |
| Long terminal workflow with tests and machine-readable feedback | 6 | No for arbitrary tasks; sometimes for narrow recurring tasks | Environment setup, dependency conflict, stale state, hidden credentials | Coding agents in containers, terminal tools, test runners | Terminal interaction is materially stronger than GUI, but best cited broad score is 65.8% | [S07, 2026-06, **Medium**]; [S22, 2026-03-14, **High**] |
| General browser/desktop workflow | 3 | No | Hidden state, focus changes, modal dialogs, timing, lost constraints, skipped verification | Computer-use models, Playwright where DOM access exists | OSWorld 2.0 strict completion is 20.6% for the strongest reported configuration; long runs are token-heavy | [S06, 2026-07-13, **Medium-High**] |
| Unattended cross-application business process | 3 | No | Compounding errors, partial side effects, inconsistent permissions, no recovery path | Only defensible after conversion into typed API steps and compensating transactions | Expected cost must include failures, cleanup, duplicate side effects, and supervision | [S03, 2026-06-04, **High**]; [S04, 2026-06-02, **High**] |
| Open-ended “work until done” autonomy | 2 | No | No measurable finish state, circular work, budget exhaustion, destructive action | Research prototypes only | Unbounded token/tool spend and unbounded downside | [S05, 2026-05-08, **High**]; [S06, 2026-07-13, **Medium-High**] |

**Production boundary.** Duration is not the same as autonomy. A workflow can
run for days reliably if durable software owns the state and each model call is
short. Conversely, a 90-minute opaque GUI task can be unreliable because the
agent must remember hundreds of observations and infer hidden application
state.

METR’s time-horizon measure is useful but should not be over-read: it estimates
the duration of human-completable software tasks at a specified success
probability over 100+ tasks, and METR explicitly warns that estimates above 16
hours are unreliable [S05, updated 2026-05-08, **High**]. It does not establish
safe, economic autonomy in an arbitrary business environment.

### 2.4 Tool use & connector orchestration

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Single typed read-only function call | 9 | Usually | Wrong tool among similar options, wrong enum/entity, missing prerequisite | Native function calling, strict schema, deterministic validation | Low latency and cost; cache reads where freshness permits | [S08, 2026-04-12, **High**]; [S09, 2025, **High**] |
| Short sequence of read-only tools | 8 | Often, with step/postcondition checks | State forgotten between calls, redundant calls, stale result | Agents SDKs, MCP clients, explicit scratch/state object | Multi-turn performance is materially below single-turn; set budgets | [S08, 2026-04-12, **High**]; [S09, 2025, **High**] |
| Reversible write action | 6 | Only with scoped authorization and receipt verification | Wrong record, duplicate write, stale precondition, partial update | Preview/commit pattern, idempotency key, version check, audit receipt | Verification API call adds cost but prevents expensive cleanup | [S32, 2026, **Medium-High**]; [S35, 2026-07-27, **High**] |
| Irreversible or high-impact tool action | 3 | No | Misinterpreted intent, prompt injection, excessive scope, non-reversible loss | Human approval, two-person rule, separate credentials, policy engine | Human latency is a safety feature; do not optimize it away | [S14, 2024/2026, **High**]; [S32, 2026, **Medium-High**] |
| Connector use over trusted data | 7 | Sometimes | Schema drift, permission mismatch, pagination, rate limits | MCP/function tools with typed contracts, allowlists, integration tests | Operational reliability is often dominated by the API, not the model | [S09, 2026, **High**]; [S34, 2026-07-27, **High**] |
| Tool use after ingesting untrusted content | 2 | No | Indirect prompt injection, identity spoofing, malicious tool metadata or output | Separate trust zones, taint tracking, content isolation, no ambient authority | Security controls and review outweigh token cost | [S10, 2026, **High**]; [S11, 2026, **High**]; [S12, 2024, **High**, older] |

**Production boundary.** Tool reliability requires four independent properties:
the model selected the right tool, supplied correct arguments, had appropriate
authorization, and verified the real postcondition. A successful API response
does not prove the intended business outcome.

**Security rule.** The component that interprets untrusted content should not
also possess ambient write authority. Use least-privilege, task-scoped
credentials; allowlisted tools; data-flow separation; preview and approval for
consequential actions; and immutable receipts.

### 2.5 Content generation + revision

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Drafting from a supplied brief and facts | 9 | Yes for internal drafts | Generic tone, missed constraint, unsupported flourish | Frontier or efficient models with templates and brand examples | Small/fast models are sufficient for many first drafts; batch for volume | [S31, 2024, **Medium-High**, older]; [S38–S40, 2026, **High** for pricing] |
| Rewrite, shorten, classify, translate, reformat | 9 | Usually for low-risk use | Meaning drift, dropped negation, locale mismatch | Structured output, diff view, glossary, examples | Among the highest-value low-cost uses; deterministic format checks | [S03, 2026, **High**]; [S18, 2026, **Medium**] |
| Brand-consistent content with revision loop | 8 | Yes for draft production; no for final public claim set | Style imitation without substance, repetitive patterns, outdated product facts | Retrieval of approved claims, style rubric, generator-critic loop | Two-pass drafting is inexpensive; do not confuse self-critique with fact-checking | [S31, 2024, **Medium-High**, older]; [S17, 2026, **High**] |
| Factual public content | 6 | No | Hallucinated facts, stale links, citation mismatch, exaggerated claims | Grounded generation, approved-claim library, link checker, human editor | Verification often costs more than generation | [S15–S17, 2025–2026, **Medium-High**] |
| High-volume personalization | 7 | Only within approved factual/ethical boundaries | Creepy inference, sensitive-attribute use, inconsistent offer, reputational harm | Segmentation rules plus model copy variation; compliance filters | Unit cost is low; governance and review sampling are the real cost | [S14, 2024/2026, **High**] |
| Regulated or consequential claims | 3 | No | Fabricated authority, omitted disclaimers, unlicensed advice | Approved templates and expert review only | Liability overwhelms automation savings | Project exclusions; [S14, 2024/2026, **High**] |

**Production boundary.** Generative models are mature as drafting engines. They
are not mature as publishers of new factual claims. The most reliable design
restricts factual content to an approved, versioned claim library and makes
creative variation happen around those facts.

### 2.6 Monitoring + alerting

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Deterministic collection and rule-based alerting | 10 | Yes | Bad source, threshold design, missing telemetry | Schedulers, webhooks, database queries, observability platforms | Use ordinary software; no model required for detection | Standard software practice |
| Summarizing and prioritizing known alerts | 9 | Usually | Severity inversion, omitted anomaly, unsupported cause | LLM over bounded event payload plus source links | Small models can handle most events; reserve frontier calls for ambiguous cases | [S31, 2024, **Medium-High**, older] |
| Clustering and deduplicating noisy alerts | 8 | Yes with measurable fallback | Semantically different incidents merged, recurring incident split | Embeddings plus deterministic keys and review sampling | Can reduce human load substantially; maintain golden incident sets | [S37, 2026, **Medium-High**] |
| Detecting semantic change in known sources | 7 | Sometimes | Cosmetic change treated as material, dynamic page noise, missed visual change | DOM diff, extraction rules, screenshot comparison, model classifier | Two-stage deterministic diff then LLM interpretation controls cost | [S31, 2024, **Medium-High**, older] |
| Open-web novelty or weak-signal monitoring | 5 | No | Coverage gaps, rumor amplification, source duplication, language bias | Search feeds, curated source lists, human review queue | Cost grows with source breadth and frequency; precision/recall trade-off is unavoidable | [S15, 2025, **Medium**]; [S18, 2026, **Medium**] |
| Automatic consequential action from an alert | 3 | No unless action is reversible and tightly bounded | False positive triggers write, adversarial input, feedback loop | Policy engine, cooldown, preview, approval, compensating transaction | Value must be net of false-action cleanup | [S10–S14, 2024–2026, **High**] |

**Production boundary.** Let deterministic systems decide that an event
occurred whenever possible. Let the model explain, cluster, or prioritize it.
If a model-detected condition can trigger a write, require a separate
postcondition and risk gate.

### 2.7 Code generation & maintenance

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Localized change with clear acceptance tests | 8 | Yes in sandbox; no for merge/deploy by default | Test gaming, hidden regression, misunderstood convention | Claude Code, Codex, Gemini CLI, OpenHands; lint/type/test gates | Often strong ROI; cost is dominated by repo exploration and test loops | [S22, 2026, **High**]; [S23, 2026, **High**]; [S07, 2026, **Medium**] |
| Test, documentation, migration, and mechanical maintenance | 8 | Often with deterministic gates | Brittle tests, incorrect mocks, stale docs, unsafe migration assumption | Repository-aware agents plus CI and disposable databases | Excellent for parallel low-risk queues if reviews remain independent | [S22, 2026, **High**]; [S23, 2025, **High**] |
| Multi-file feature in a familiar repository | 6 | No | Architectural drift, partial implementation, missed integration path | Coding agent in isolated worktree, task plan, full test suite, reviewer | Several model/tool loops; success strongly depends on human expertise | [S23, 2026, **High**]; [S24, 2026-06-16, **Medium**] |
| Repository-scale refactor or unfamiliar environment | 5 | No | Environment setup, dependency mismatch, false green tests, incomplete migration | Containerized environment, incremental commits, strengthened tests | GitTaskBench best cited result is 48.15%; more than half of failures are mundane setup/environment issues | [S22, 2026-03-14, **High**] |
| Vulnerability/security repair | 5 | No | Symptom patch, new attack surface, missed call path, unsafe dependency | Static analysis, security tests, human security review, agent for candidate patch | High review cost is justified; require adversarial tests | [S14, 2024/2026, **High**] |
| Unattended merge and production deployment | 3 | No except trivial low-blast-radius canaries with rollback | False test oracle, secrets/config mismatch, irreversible migration, outage | Protected branches, staged rollout, canary, automated rollback, human gate | Deployment risk—not token price—sets the control level | [S23, 2025, **High**]; [S27, 2026, **Medium**] |

**Production boundary.** Coding agents are most reliable when the repository is
the environment, the task has executable acceptance criteria, the agent works
in isolation, and CI plus a reviewer can reject the result. They are less
reliable when success depends on unwritten architecture, production-only state,
or inadequate tests.

Benchmark pass rates can be false assurance. UTBoost identifies 36 tasks with
insufficient tests and 345 erroneous patches labeled as passed, changing
rankings for 40.9% of SWE-bench Lite and 24.4% of SWE-bench Verified entries
[S23, 2025, **High**]. The verifier is part of the product.

### 2.8 Customer communication

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| FAQ answer grounded in an approved knowledge base | 9 | Usually, with citations and abstention | Wrong document version, answer beyond policy, tone mismatch | RAG, policy retrieval, answer citations, confidence/escalation | Low per interaction; review a stratified sample rather than every answer | [S25, 2025, **High**]; [S26, 2026, **Medium**] |
| Intent classification, triage, and routing | 9 | Yes with fallback | Multi-intent messages, urgency missed, language variation | Structured classification, priority rules, CRM/ticket connector | Small models often sufficient; measure route accuracy and reopen rate | [S03, 2026, **High**] |
| Routine conversational support with read-only account context | 8 | Often | Hallucinated policy, failed identity boundary, premature resolution | Policy-grounded support agents, tool receipts, handoff summary | High-volume deployments can improve self-service, but company evidence is not universal | [S25, 2025, **High**]; [S26, 2026-06-07, **Medium**] |
| Transactional support with reversible writes | 6 | No without deterministic checks and scoped authority | Wrong account/action, incomplete transaction, user-agent coordination failure | Preview/confirm/commit, receipt validation, escalation | Repeated reliability is much lower than single success; include failure recovery in unit economics | [S25, 2025, **High**]; [S26, 2026, **Medium**] |
| Voice support | 5 | No for consequential actions | ASR error, interruption, identity ambiguity, latency, emotional escalation | Grounded voice agents with narrow tools and immediate handoff | Audio processing and low-latency models add cost; transcripts need privacy controls | [S19, 2026, **Medium**] |
| Complaint, negotiation, retention, or vulnerable-customer interaction | 4 | No | False empathy, manipulation, failure to recognize exception, reputational damage | Human-led workflow with AI brief, next-best-action suggestions | Relationship value exceeds automation savings | [S14, 2024/2026, **High**] |

**Production boundary.** A support agent needs policy grounding, identity and
authorization outside the model, a verified receipt for every transaction,
and an escalation path the user can invoke. “Conversation ended” is not
“problem solved.”

Repeated success is the relevant metric. In τ-bench, GPT-4o is below 50% task
success and retail pass^8 is below 25% [S25, 2025, **High**]. Company-authored
Nubank evidence shows that carefully engineered deployments can deliver real
benefits—one A/B test reports +37 percentage points transactional NPS and +29
points self-service—but this is evidence for a specific controlled system, not
general autonomy [S26, 2026-06-07, **Medium**].

### 2.9 Planning & task decomposition

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Decompose a clear goal into a checklist | 9 | Usually | Redundant steps, missed local constraint, bad order | Frontier models, templates, examples, dependency labels | Cheap; validate prerequisites before execution | [S31, 2024, **Medium-High**, older] |
| Build a dependency-aware DAG for known operations | 8 | Often with schema validation | Hidden dependency, circular graph, incorrect parallelization | Planner plus typed task schema and graph validator | Planning cost is small; parallelism can reduce wall time when real | [S29, 2026, **Medium-High**]; [S30, 2026, **Medium**] |
| Replan from explicit tool feedback | 7 | Sometimes | Thrashing, repeating failed action, discarding earlier constraint | Bounded agent loop, retry taxonomy, failure memory, escalation threshold | Cap retries; repeated calls can exceed the value of the task | [S03, 2026, **High**]; [S31, 2024, **Medium-High**, older] |
| Estimate time, cost, and risk | 5 | No | Confident but uncalibrated estimates, ignored tail risk, unknown environment | Reference-class data, deterministic cost model, model explanation | Use observed run distributions rather than model intuition | [S04, 2026, **High**]; [S05, 2026, **High**] |
| Open-ended strategy under uncertain goals | 4 | No | Optimizes a proxy, invents assumptions, averages incompatible priorities | Scenario generation and decision memo for human owner | Valuable for option generation; unsuitable for final authority | [S02, 2026-07, **High** internal]; [S14, 2024/2026, **High**] |
| Plan and execute without a separate verifier | 3 | No | Plan errors become action errors; self-review shares blind spots | Not recommended | Cheap up front, expensive in cleanup | [S27, 2026, **Medium**]; [S28, 2025, **Medium-High**] |

**Production boundary.** Planning is useful when goals, available actions, and
finish conditions are explicit. It becomes speculative as hidden constraints,
value judgments, and unknown environments increase. A plan should be a typed,
inspectable artifact that a runtime validates—not private model reasoning.

### 2.10 Memory & state management

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Explicit transactional workflow state | 9 | Yes | Application bug, stale version, incomplete migration | Relational/event store, state machine, checkpoint ID, optimistic locking | Ordinary database cost; this should be the source of truth | [S34, 2026-07-27, **High**]; [S35, 2026-07-27, **High**] |
| Short-term session context | 8 | Usually within a bounded run | Truncation, attention dilution, wrong conversation branch | Session object, compact state summary, scoped context | Long context has token and latency cost; store facts once, retrieve selectively | [S35, 2026-07-27, **High**]; [S39–S40, 2026, **High**] |
| Retrieval of prior facts from a curated memory store | 7 | Sometimes | Wrong entity, stale fact, retrieval miss, no provenance | Typed records plus semantic search and source/date metadata | Embedding retrieval is cheap; freshness and invalidation are not | [S37, 2026, **Medium-High**] |
| Automatic memory writing and consolidation | 5 | No | Stores inference as fact, duplicate/conflicting memories, privacy leakage | Candidate-memory queue, schema, provenance, human/rule approval | Review only high-value memory; retention has privacy and deletion cost | [S14, 2024/2026, **High**]; [S37, 2026, **Medium-High**] |
| Cross-session preference memory | 6 | No for sensitive or consequential preferences | Context collapse, consent ambiguity, obsolete preference | User-visible profile, edit/delete controls, explicit scope | Small storage cost; governance is the dominant requirement | [S14, 2024/2026, **High**] |
| Model context or vector memory as business system of record | 2 | No | Fabrication, stale retrieval, silent overwrite, no transaction isolation | Not recommended | Apparent simplicity creates reconciliation and liability cost | [S04, 2026, **High**]; [S34, 2026-07-27, **High**] |

**Production boundary.** “Memory” is several different systems. Workflow state
belongs in a transactional store. Documents belong in a versioned repository.
Preferences need provenance and user controls. Semantic retrieval is an access
method, not a source of truth. The model should receive a task-specific view of
state rather than own state.

### 2.11 Evaluation & self-critique

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Deterministic outcome evaluation | 10 | Yes if the oracle is valid | Incomplete test, wrong metric, stale expected value | Unit/integration tests, schema checks, database postconditions, checksums | Usually cheaper and more reliable than an LLM judge | [S23, 2025, **High**]; [S27, 2026, **Medium**] |
| Task-specific statistical/anomaly detector | 9 | Often | Dataset shift, threshold drift, label leakage | Lightweight classifier, retrieval comparison, calibrated threshold | One cited TF-IDF detector outperforms all tested LLM judges and is ~3,300 times lower latency | [S27, 2026-06-01, **Medium**] |
| Rubric-based LLM judge for subjective quality | 7 | No as sole gate | Position/style bias, shared blind spot, prompt sensitivity | Multiple criteria, pairwise comparison, reference examples, disagreement sampling | Useful for triage; periodically anchor to human labels | [S04, 2026, **High**]; [S37, 2026, **Medium-High**] |
| Independent model review with source/tool access | 7 | No for highest-impact decisions | Correlated model error, incomplete evidence, deference to fluent output | Different context/model, adversarial checklist, ability to inspect artifacts | Adds a model call but can cheaply reject obvious defects | [S17, 2026, **High**]; [S28, 2025, **Medium-High**] |
| Self-critique in the same context | 5 | No | Rationalizes prior answer, fails to notice missing premise, cosmetic revision | Reflection pass only as one signal | Low incremental cost; low independence | [S27, 2026, **Medium**] |
| Self-reported task success | 2 | No | False success, reward hacking, unverified side effect | Never use as the only completion signal | False success can dominate observed failures | [S27, 2026-06-01, **Medium**] |

**Critical distinction.** A judge evaluates an artifact; a verifier establishes
an outcome. For operational tasks, completion should be proven by external
state: the record exists with the correct version, the message was accepted by
the intended endpoint, the tests exercise the intended behavior, or the
customer explicitly confirms resolution.

In one 2026 analysis, false success represents 45–48% of failures in
single-control τ2 and 75.8% of AppWorld self-assessed success. No tested LLM
judge exceeds AUROC 0.65 on τ2 or 0.54 on AppWorld, while a task-specific
TF-IDF detector reaches 0.83 and 0.95 [S27, 2026-06-01, **Medium**]. Simple
verifiers can beat sophisticated self-reflection.

### 2.12 Multi-agent coordination

| Capability | Maturity (1-10) | Reliable without human? | Typical failure modes | Best current tools/examples | Cost/performance notes | Sources |
|---|---:|---|---|---|---|---|
| Parallel independent research or generation with centralized merge | 7 | Sometimes | Duplicate work, inconsistent assumptions, weak merge rubric | Manager-worker, map-reduce, shared source ledger, deterministic dedupe | Can improve coverage; token cost rises roughly with workers | [S29, 2026, **Medium-High**] |
| Parallel tasks represented by a valid DAG | 7 | Sometimes with objective checks | Hidden dependency, premature merge, inconsistent state | Central scheduler, specialist agents, per-node verifier | Specific computer-use results improve 3.4–25.5% and wall time about 1.5x | [S30, 2026, **Medium**] |
| Generator plus independent critic/verifier | 7 | Yes for low-risk rejection/routing, not final authority | Correlated errors, critic lacks tools, endless revision | Separate prompts/models/context, deterministic stop rule | Often a better second-agent use than simulated personas | [S17, 2026, **High**]; [S28, 2025, **Medium-High**] |
| Centralized manager over tool-using specialists | 6 | No for consequential work | Manager bottleneck, summary information loss, worker state conflict | Hierarchical agent system with shared typed state | Centralization limits error amplification but adds latency | [S28, 2025, **Medium-High**]; [S29, 2026, **Medium-High**] |
| Sequential multi-agent handoffs | 4 | No | Information loss, incompatible assumptions, error propagation | Prefer one agent with explicit state unless expertise boundary is real | All tested multi-agent variants degrade sequential tasks by 39–70% in one broad study | [S29, 2026, **Medium-High**] |
| Decentralized open-ended swarm | 2 | No | Independent error amplification, circular debate, no owner, runaway cost | Research only | Independent error amplification reaches 17.2x in the cited study | [S28, 2025, **Medium-High**]; [S29, 2026, **Medium-High**] |

**Production boundary.** “More agents” is not a capability category by itself.
Use multiple agents when the work has real parallel structure, roles have
distinct information or tools, every output has a contract, and one component
owns the state and merge. Otherwise, extra agents increase interfaces,
latency, correlated hallucination, and cost.

## 3. Agent Architecture Patterns That Actually Work in Production

### Pattern 1 — Deterministic workflow shell with bounded model nodes

Ordinary software owns the workflow graph, state transitions, timeouts, retries,
and finish conditions. The model performs narrow semantic steps such as
classify, extract, draft, compare, or select among allowed next actions.

**Why it works:** Most production deployments already intervene within 10
steps, and workflows exchange flexibility for predictability [S03, 2026,
**High**; S31, 2024, **Medium-High**, older].

**Required controls:**

- typed input and output at every node;
- explicit maximum steps, retries, tokens, time, and spend;
- durable checkpoint before and after any side effect;
- deterministic routing for known conditions;
- an exception state rather than forced completion; and
- an observable postcondition for “done.”

### Pattern 2 — Read, propose, verify, commit

Split consequential activity into four phases:

1. **Read:** collect current state with read-only credentials.
2. **Propose:** generate a structured action plan or diff.
3. **Verify:** independently check identity, scope, constraints, and expected
   effect.
4. **Commit:** execute with a task-scoped credential and capture a receipt.

**Why it works:** It prevents a single misinterpretation from becoming an
immediate side effect and creates a natural human approval point. It also makes
retries safer.

**Use for:** CRM updates, outbound messages, publishing, refunds, schedule
changes, repository merges, and any external write.

### Pattern 3 — Tool contracts plus least privilege

Expose small task-specific tools instead of a general shell or broad connector.
Make required parameters explicit; reject unknown fields; validate entity IDs
and versions; and return a typed receipt.

**Required controls:**

- separate read and write tools;
- allowlisted destinations and action types;
- task-scoped, short-lived authorization;
- idempotency key and optimistic concurrency for writes;
- dry-run/preview output;
- reversible operation or compensating transaction; and
- server-side policy enforcement independent of the model.

**Why it works:** Tool calling is comparatively mature in short, typed
interactions, while multi-turn state and untrusted tool content remain weak
[S08–S12, 2024–2026, **High**].

### Pattern 4 — Durable execution with idempotent side effects

Checkpoint the graph so a process can pause for approval, survive a crash, and
resume. Durable runtimes and current agent SDKs expose this as a first-class
primitive [S34–S36, 2026-07-27, **High** for product features].

**Important caveat:** replay may re-execute model nodes and API calls. A
checkpoint is not exactly-once execution. External writes still need
idempotency keys, version checks, and reconciliation [S34, 2026-07-27,
**High**].

### Pattern 5 — Deterministic collector, probabilistic interpreter

Let schedulers, APIs, database queries, webhooks, and diffs detect that
something changed. Give the bounded event payload to the model to summarize,
classify, cluster, or recommend. Do not ask a language model to continuously
“watch” what conventional software can measure exactly.

**Why it works:** It uses the model for semantic judgment while preserving
coverage, timing, and deduplication in ordinary software.

### Pattern 6 — Independent verification by the cheapest valid oracle

Choose evaluation in this order:

1. deterministic invariant or exact postcondition;
2. task-specific statistical detector;
3. reference comparison or retrieval check;
4. independent model judge with tools;
5. human review.

Use human review immediately when consequences are high, criteria are
value-laden, or no valid oracle exists.

**Why it works:** Task-specific verification can be more accurate and thousands
of times cheaper than an LLM judge [S27, 2026, **Medium**]. Independence matters:
same-context self-critique is not an external control.

### Pattern 7 — Risk-tiered autonomy

Classify actions using at least:

- read versus write;
- reversible versus irreversible;
- private versus public;
- known destination versus open destination;
- financial/legal/safety impact;
- exposure to untrusted input;
- confidence and evidence quality; and
- detectability and recoverability of failure.

Example policy:

- **Tier 0:** draft only.
- **Tier 1:** autonomous read and internal classification.
- **Tier 2:** reversible write with deterministic verification and sampling.
- **Tier 3:** preview plus human approval.
- **Tier 4:** prohibited from autonomous execution.

This follows current OpenAI, Anthropic, and NIST guidance and the project’s
governance constraint [S01–S02; S13–S14; S32–S33].

### Pattern 8 — Centralized multi-agent work only for real parallelism

A coordinator owns the shared typed state and decomposes only independent
subtasks. Workers receive minimal context, produce contracted artifacts, and
cannot directly mutate shared external state. The coordinator validates and
merges their outputs.

**Use when:** independent source searches, candidate generation, isolated test
creation, or distinct specialist analyses can run in parallel.

**Do not use when:** each step depends on the full output and hidden reasoning
of the previous step, or when workers share mutable external state. Sequential
tasks show 39–70% degradation in the cited scaling study [S29, 2026,
**Medium-High**].

### Pattern 9 — Observability, replay, and a production evaluation loop

Record:

- prompt/config/model and tool versions;
- input provenance and trust level;
- state transitions and tool arguments;
- approvals, refusals, and escalations;
- external receipts and postcondition results;
- token, latency, tool, and human-review cost;
- user correction and business outcome; and
- privacy-appropriate trace retention.

Maintain a golden set from real failures, run it before changes, deploy canaries,
and compare outcome distributions rather than a few polished transcripts.
Adoption without this loop creates a reactive production system; 74% of the
cited production sample still rely mainly on human evaluation [S03, 2026,
**High**].

## 4. Hard Limits (critical section)

### Limit 1 — Stochastic output and repeated reliability

A model may succeed often while still being unsuitable for a recurring process.
If a step succeeds with probability 0.95 and ten independent steps must all
succeed, the simple compounded probability is about 0.60. Real errors are not
independent and can cascade, so this is only an illustration.

Use pass^k or repeated-run consistency in addition to pass@1. τ-bench’s retail
pass^8 below 25% illustrates why a good one-shot transcript is insufficient
[S25, 2025, **High**]. Reliability should be reported across consistency,
robustness, predictability, and safety, not as one benchmark number [S04, 2026,
**High**].

### Limit 2 — Horizon and error accumulation

Long workflows require retaining constraints, interpreting new evidence,
recovering from partial failure, and knowing when to stop. OSWorld 2.0’s 20.6%
strict completion on tasks averaging 318 tool calls is the clearest current
warning [S06, 2026, **Medium-High**].

Mitigation reduces exposure—it does not remove the limit:

- shorten model-controlled segments;
- externalize state;
- checkpoint and verify after each stage;
- stop after repeated failures;
- ask rather than guess; and
- convert GUI work into APIs or terminal operations.

### Limit 3 — Hidden environment state

Models observe partial representations: a screenshot, DOM subset, terminal
window, tool response, or compressed history. They do not inherently know that
a modal opened, a session expired, a write partially succeeded, or another
actor changed the record.

Machine-readable interfaces outperform GUIs because state and errors are more
explicit [S06–S08, 2026, **Medium-High**]. For important processes, query the
source of truth after action rather than infer success from the interface.

### Limit 4 — Prompt injection and confused-deputy risk

An agent can encounter instructions inside webpages, emails, files, tool
descriptions, or tool outputs. If the same model also holds permissions, the
untrusted content can redirect those permissions. Current MCP security results
show high attack success even in leading models [S10–S12, 2024–2026,
**High**].

There is no prompt that solves this. Required controls include trust-zone
separation, least privilege, data-flow restrictions, allowlists, approval for
consequential writes, server-side policy, and adversarial testing.

### Limit 5 — False success and invalid evaluators

Agents frequently claim success when the external task failed. LLM judges can
share the same blind spots, and benchmark tests can be incomplete. False
success constitutes a large share of observed failures in recent analysis
[S27, 2026, **Medium**], while UTBoost finds hundreds of erroneous patches
previously labeled passed [S23, 2025, **High**].

The completion signal must come from an outcome oracle: external state,
customer confirmation, independently strengthened tests, or a task-specific
detector.

### Limit 6 — Memory freshness, provenance, and deletion

Large context is not durable memory. Semantic retrieval can return a related
but stale or wrong-entity fact. Automatic memory may store an inference as a
fact or preserve information that should be deleted.

Keep transactional state in a database; attach source, entity, validity period,
and confidence to retrieved facts; make user preferences visible/editable; and
apply retention and deletion policies outside the model.

### Limit 7 — Benchmark validity and transfer

Benchmarks select tasks, environments, tools, and evaluators. Scores may rise
because tests are weak, tasks leaked, environments simplified, or scaffolds are
benchmark-specific. The corrected τ2 task set and UTBoost results demonstrate
that evaluation definitions themselves can be wrong [S23, **High**; S25,
**High**].

Production decisions need local evaluations on the actual task distribution,
permissions, languages, error costs, and interfaces.

### Limit 8 — Cost and latency variance

Agent costs are distributions, not fixed per-request prices. Long context,
reasoning tokens, retries, search calls, computer-use steps, failed attempts,
verification, and human exception handling can dominate.

Compare:

`cost per verified outcome = (model + tools + infrastructure + review +
failure recovery) / verified successful outcomes`

Do not compare only model price per token. Batch and cached input can reduce
token charges by about 50% on current major platforms, but they do not reduce
failure-recovery or supervision cost [S38–S40, 2026-07-27, **High**].

### Limit 9 — Goals, values, judgment, and relationships

Models optimize the specification they receive. They do not own the
organization’s values, customer relationship, reputation, or risk appetite.
Open-ended strategy and negotiation contain unspoken priorities and exceptions
that are difficult to encode or verify.

Use models to create options, surface evidence, and draft decisions. Keep
authority with a named human for consequential tradeoffs and relationship
ownership.

### Limit 10 — Irreversible, regulated, and physical consequences

Where a failure can cause injury, major financial loss, legal exposure,
clinical harm, or irreversible public action, today’s agents should not be the
final authority. This project additionally excludes clinical health, small-child
childcare, supplements, high-stakes finance/legal/real estate, food products,
and significant physical-safety exposure [S01, 2026-07, **High** internal].

### Limit 11 — Multilingual and geographic evidence gaps

Most benchmarks and production reports are English- and US-heavy. Translated
evidence can degrade retrieval, calibration, and citation quality [S18,
2026-06, **Medium**]. Vietnam-specific interfaces, policy language, naming
conventions, messaging platforms, and data availability require local testing.
An English benchmark score should not be treated as evidence for Vietnamese
production reliability.

## 5. Tool & Platform Landscape (July 2026)

### 5.1 Foundation-model API snapshot

Prices are per million tokens at standard rates unless stated otherwise. They
change frequently and should be rechecked before financial modeling.

| Provider / current tier | Input | Output | Relevant production notes | Source and confidence |
|---|---:|---:|---|---|
| OpenAI GPT-5.6 Sol | $5.00 | $30.00 | High-capability tier; 1.05M context listed; cached input discounted | [S38, accessed 2026-07-27, **High**] |
| OpenAI GPT-5.6 Terra | $2.50 | $15.00 | Mid-tier agentic model | [S38, accessed 2026-07-27, **High**] |
| OpenAI GPT-5.6 Luna | $1.00 | $6.00 | Lower-cost routing/drafting tier | [S38, accessed 2026-07-27, **High**] |
| Anthropic Claude Opus 4.8 | $5.00 | $25.00 | High-capability tier; separate tool/search/runtime costs may apply | [S39, accessed 2026-07-27, **High**] |
| Anthropic Claude Sonnet 5 | $2.00 promotional | $10.00 promotional | Promotion through 2026-08-31; then $3/$15 according to dated page | [S39, accessed 2026-07-27, **High**] |
| Anthropic Claude Haiku 4.5 | $1.00 | $5.00 | Fast, lower-cost classification/routing tier | [S39, accessed 2026-07-27, **High**] |
| Google Gemini 3.5 Flash | $1.50 | $9.00 | Batch $0.75/$4.50; grounded search separately metered after allowance | [S40, updated 2026-07-09, **High**] |

**Selection rule:** use the cheapest model that passes the local evaluation for
that node. Route only ambiguous, high-value cases to frontier models. Expensive
reasoning on every step is rarely the best production architecture.

### 5.2 Agent harnesses and durable runtimes

| Tool/platform | What it provides | Production value | Important limit | Source |
|---|---|---|---|---|
| OpenAI Agents SDK | Function tools, sessions, handoffs, guardrails, tracing, human approval state, durable-runtime integrations | Small set of inspectable primitives; serializable pause/resume | Feature availability does not validate application safety; tracing has data-governance constraints | [S35, 2026-07-27, **High**] |
| Claude Managed Agents | Beta managed sandbox, stateful long-running sessions, versioned configuration, tools/MCP/skills/multi-agent | Reduces harness and sandbox operations | Beta; not ZDR or HIPAA eligible on the dated documentation | [S36, 2026-07-27, **High**] |
| Gemini managed agents | Preview managed harness, tools, long interaction budgets | Reduces infrastructure work; integrated model/tool loop | Preview; documentation itself recommends least privilege and output verification | [S37, 2026-07-27, **High**] |
| LangGraph | Graph/state abstraction, checkpoints, persistence, interrupts, human-in-loop | Explicit state and resumable processes | Replay may re-execute later nodes and side effects; application owns idempotency | [S34, 2026-07-27, **High**] |
| Temporal, DBOS, Restate, Dapr | Durable ordinary-code workflow execution | Strong state, retries, timers, recovery, operational history | Requires explicit integration with model/tool policy and evaluators | [S35, 2026-07-27, **High** for listed integrations] |
| Low-code automation platforms | Deterministic connectors, schedules, triggers, approvals | Good workflow shell for low-risk administrative processes | Connector permissions, schema drift, and opaque retry semantics require review | Vendor features; **Medium** |

No harness makes the model reliable. The harness makes state, permissions,
retries, and review points governable.

### 5.3 Tool interfaces

| Interface | Best use | Reliability profile | Guidance |
|---|---|---|---|
| Typed function/API call | Production read/write against known systems | Highest when schemas and postconditions are strict | Default choice |
| MCP server | Standardized discovery and tool/resource integration | Operationally useful; expands trust and injection surface | Curate servers/tools, pin versions, isolate trust, least privilege |
| Terminal | Code, data, and infrastructure tasks with textual feedback | Stronger than GUI; commands can have broad blast radius | Sandbox, allowlist, working-directory boundary, diff/test gates |
| Browser DOM automation | Known web application with stable selectors | Better than pixels, vulnerable to UI/schema change | Prefer official API; assert page state and result |
| Pixel-based computer use | Legacy application or human-only interface | Lowest current long-horizon reliability | Use for assisted operation; frequent checkpoints and approval |

### 5.4 Evaluation and observability stack

A minimum production stack needs:

1. versioned prompt/model/tool configuration;
2. trace IDs across model, tools, and external systems;
3. deterministic postconditions and receipts;
4. a local golden set including real failures and adversarial cases;
5. repeated-run reliability and cost distributions;
6. human-escalation, correction, and override metrics;
7. privacy-aware trace retention and deletion; and
8. canary release and rollback.

Current SDKs and platforms expose tracing and evaluation primitives, but the
team must define valid outcomes. A beautiful trace of an invalid task is still
an invalid evaluation.

### 5.5 Adoption context

Stanford HAI reports organizational AI use at 88% in 2026 while noting that
agent use remains early [S41, 2026, **High**]. This reconciles the apparent
contradiction between rapid AI adoption and weak evidence for general
autonomy: companies broadly use AI, but mature deployments typically constrain
agents to specific processes and retain human evaluation [S03, 2026, **High**].

## 6. Open Gaps & Research Frontiers

### 6.1 Independent longitudinal production evidence

The field lacks neutral datasets tracking real agents over months across
failure frequency, human intervention, rollback, cost, and customer outcome.
Vendor case studies can show possibility, but not base rates or transfer.

**Research need:** anonymized incident and outcome reporting by task class,
risk tier, interface, model, workflow length, and verification method.

### 6.2 Reliability at strict thresholds

Benchmarks emphasize average task success. Business processes often need
99%+ detection and recovery, not 60–80% unverified completion.

**Research need:** pass^k, worst-group performance, tail latency, recovery rate,
false-success rate, and cost per verified outcome.

### 6.3 Execution-control security

Prompt injection remains a fundamental problem when untrusted data and
privileged action share a model context.

**Research need:** information-flow control, capability-secure tool tokens,
provenance/taint tracking, secure content transformation, policy enforcement
outside the model, and standardized adversarial suites for real connectors.

### 6.4 Valid, economical outcome verification

Self-critique and general LLM judges are not sufficient. Many tasks lack an
inexpensive external oracle.

**Research need:** automatically synthesized task-specific verifiers,
postcondition contracts, uncertainty-aware escalation, and methods for proving
that tests measure the intended outcome.

### 6.5 Transactional memory and provenance

Memory benchmarks increasingly test conversational recall, but production needs
entity correctness, freshness, conflict resolution, deletion, provenance, and
transactional update semantics.

**Research need:** long-lived benchmarks where facts change, permissions differ,
users correct the system, and deleted information must not reappear.

### 6.6 Benchmark integrity and contamination

Corrected task sets and strengthened tests show that benchmarks can overstate
progress.

**Research need:** continuously refreshed private test sets, independent
evaluator audits, environment reproducibility, contamination disclosure, and
production-task transfer studies.

### 6.7 Conditional science of multi-agent systems

Recent evidence begins to explain when multiple agents help: genuine
parallelism, centralized state, diversity that adds information, and objective
merge rules.

**Research need:** predictive measures of decomposability, communication cost,
error correlation, and the threshold at which one stronger model is cheaper
and more reliable than several weaker agents.

### 6.8 Multilingual and Vietnam-specific evaluation

Current benchmarks underrepresent Vietnamese language, local software
interfaces, administrative norms, and customer-service expectations.

**Research need:** Vietnamese retrieval and citation benchmarks, mixed
Vietnamese-English entity handling, Zalo/social-commerce workflows, local
document layouts, and culturally appropriate escalation—with the same strict
project exclusions and privacy controls.

### 6.9 Agent unit economics

Token prices are falling, but long contexts, tool calls, retries, verification,
and human exceptions can dominate.

**Research need:** standardized reporting of cost per verified outcome,
supervision minutes, cleanup cost, latency percentiles, and value of failures
prevented.

### 6.10 Human skill and organizational learning

The operator remains part of system performance. A large Anthropic
observational study reports verified coding success of 15% for novice users
versus 28–33% for intermediate/expert users [S24, 2026-06-16, **Medium**].

**Research need:** interfaces that expose uncertainty and state, teach operators
when to intervene, convert corrections into tests, and preserve human expertise
rather than hide it behind an anthropomorphic agent.

### 6.11 Safe communication and relationship continuity

Grounded FAQ and triage are mature, but complaint handling, vulnerable users,
retention, and negotiation remain difficult to verify and reputationally
sensitive.

**Research need:** relationship-preserving escalation, truthful disclosure,
emotion/urgency recognition without sensitive profiling, and longitudinal
customer-outcome measures.

### 6.12 The solo-operator frontier

For a solo ABM, the key metric is not “how autonomous is the agent?” but “how
much verified work can one owner safely supervise?”

**Research need:** an autonomy-adjusted leverage metric incorporating:

- verified outcomes per owner-hour;
- exception and correction rate;
- maximum plausible loss per action;
- detectability and recoverability;
- customer trust and retention;
- total cost per verified outcome; and
- how quickly a failure becomes a reusable test or rule.

The near-term frontier is therefore **supervised leverage**, not ownerless
operation.

## Source Register

### Project governance and synthesis

**[S01]** AgentMindCloud, `00-Meta/ABM-Project-Continuity.md`, updated 2026-07.
Internal primary project document. **Confidence: High** for project constraints.

**[S02]** AgentMindCloud,
`05-Previous-Research/Master-Synthesis.md`, 2026-07. Synthesis of 28 prior
research papers. **Confidence: High** for the recorded project synthesis;
individual external claims retain their original source quality.

### Production, reliability, and long horizon

**[S03]** Chen et al., “Measuring Agents in Production,” arXiv:2512.04123 v4,
2026-06-04; accepted as ICML 2026 Oral.
https://arxiv.org/abs/2512.04123
20 case studies; 86 practitioners; 26 domains; 68% at most 10 steps; 70%
off-the-shelf prompting; 74% human evaluation. **Confidence: High**.

**[S04]** “Towards a Science of Agent Reliability,” arXiv:2602.16666 v3,
2026-06-02; accepted at ICML 2026.
https://arxiv.org/abs/2602.16666
15 models, 12 metrics, two benchmarks. **Confidence: High**.

**[S05]** METR, “Time Horizons,” updated 2026-05-08.
https://metr.org/time-horizons/
Official methodology and measurement caveats. **Confidence: High**.

**[S06]** “OSWorld 2.0,” arXiv:2606.29537 v2, 2026-07-13.
https://arxiv.org/abs/2606.29537
Current long-horizon computer-use benchmark. **Confidence: Medium-High**
(preprint).

**[S07]** “TUA-Bench,” arXiv:2606.28480, 2026-06.
https://arxiv.org/abs/2606.28480
120 real terminal/UI tasks. **Confidence: Medium** (preprint).

### Tool use and security

**[S08]** UC Berkeley Gorilla, “Berkeley Function-Calling Leaderboard v4,”
updated 2026-04-12.
https://gorilla.cs.berkeley.edu/leaderboard
Official live leaderboard snapshot. **Confidence: High**.

**[S09]** Patil et al., “Berkeley Function-Calling Leaderboard,” ICML 2025,
PMLR 267.
https://proceedings.mlr.press/v267/patil25a.html
Peer-reviewed benchmark paper. **Confidence: High**.

**[S10]** “MCPTox,” AAAI 2026, published 2026-03-14.
https://ojs.aaai.org/index.php/AAAI/article/view/40895
45 live MCP servers and 1,348 cases. **Confidence: High**.

**[S11]** “MCP-SafetyBench,” ICLR 2026 / arXiv:2512.15163.
https://openreview.net/forum?id=7XYjeL46co
Five domains and 20 attack types. **Confidence: High**.

**[S12]** Debenedetti et al., “AgentDojo,” arXiv:2406.13352, 2024-06-19.
https://arxiv.org/abs/2406.13352
97 tasks and 629 security cases. **Confidence: High**; **older than preferred
window**.

**[S13]** NIST, “Strengthening AI Agent Hijacking Evaluations,” 2025-01-17.
https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations
Official technical guidance. **Confidence: High**.

**[S14]** NIST AI 600-1, “Artificial Intelligence Risk Management Framework:
Generative Artificial Intelligence Profile,” published 2024-07-26; updated
2026-04-08.
https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
Official risk-management profile. **Confidence: High**; foundational 2024
source.

### Research, synthesis, and extraction

**[S15]** “DeepResearch Bench,” arXiv:2506.06287, 2025-06.
https://arxiv.org/abs/2506.06287
89 tasks with frozen retrospective search. **Confidence: Medium** (preprint).

**[S16]** “DeepResearchBench,” arXiv:2506.11763, 2025-06.
https://arxiv.org/abs/2506.11763
100 PhD-level tasks across 22 fields. **Confidence: Medium** (preprint).

**[S17]** “DREAM: The Mirage of Synthesis,” ACL 2026 Long Paper.
https://aclanthology.org/2026.acl-long.448/
Peer-reviewed evaluation of deep-research outputs. **Confidence: High**.

**[S18]** “Cross-lingual BrowseComp Plus,” arXiv:2606.15345, 2026-06.
https://arxiv.org/abs/2606.15345
Cross-lingual retrieval/citation degradation. **Confidence: Medium** (preprint).

**[S19]** “Structured Output Benchmark,” arXiv:2604.25359, 2026-04-28.
https://arxiv.org/abs/2604.25359
21 models across text, document images, and audio. **Confidence: Medium**
(preprint).

**[S20]** “READoc,” Findings of ACL 2025.
https://aclanthology.org/2025.findings-acl.1128/
3,576 real documents. **Confidence: High**.

**[S21]** UC Berkeley, “TWIX,” technical report, 2025-05-15.
https://digicoll.lib.berkeley.edu/record/320827
Hybrid template-inference/extraction system. **Confidence: Medium-High**.

### Code and outcome evaluation

**[S22]** “GitTaskBench,” AAAI 2026, published 2026-03-14.
https://ojs.aaai.org/index.php/AAAI/article/view/40533
54 realistic repository tasks. **Confidence: High**.

**[S23]** “UTBoost,” ACL 2025 / arXiv:2506.09289.
https://arxiv.org/abs/2506.09289
Strengthens insufficient software-task tests. **Confidence: High**.

**[S24]** Anthropic Research, “How AI assistance impacts the formation of coding
expertise,” 2026-06-16.
https://www.anthropic.com/research/claude-code-expertise
Large vendor observational study. **Confidence: Medium**.

**[S25]** “τ-bench,” ICLR 2025.
https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html
Retail and airline tool-agent-user benchmark. **Confidence: High**.

**[S26]** “Building Effective Customer Support Agents,” arXiv:2606.08867,
2026-06-07.
https://arxiv.org/abs/2606.08867
Five Nubank production deployments. **Confidence: Medium** (company-authored
deployment report).

**[S27]** “Detecting False Success in Tool-Using Agents,” arXiv:2606.09863,
2026-06-01.
https://arxiv.org/abs/2606.09863
9,876 τ2 and 1,879 AppWorld trajectories. **Confidence: Medium** (preprint).

### Multi-agent systems

**[S28]** “MAST: Multi-Agent System Failure Taxonomy,” arXiv:2503.13657,
2025-03-17.
https://arxiv.org/abs/2503.13657
Five frameworks, 150 tasks, 14 failure modes. **Confidence: Medium-High**.

**[S29]** Google Research, “Towards a Science of Scaling Agent Systems,”
2026-01-28; paper arXiv:2512.08296.
https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
180 configurations across four benchmarks. **Confidence: Medium-High**
(large preprint plus official research summary).

**[S30]** “Multi-Agent Computer Use,” arXiv:2606.01533, 2026-06.
https://arxiv.org/abs/2606.01533
DAG-managed specialists on computer-use benchmarks. **Confidence: Medium**
(preprint).

### Architecture, platforms, and pricing

**[S31]** Anthropic Engineering, “Building Effective Agents,” 2024-12-19.
https://www.anthropic.com/engineering/building-effective-agents
Official engineering guidance consistent with independent evidence.
**Confidence: Medium-High**; older than preferred window.

**[S32]** OpenAI, “A Practical Guide to Building AI Agents,” current 2026.
https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
Official implementation guidance. **Confidence: Medium-High**.

**[S33]** Anthropic Research, “Building and evaluating trustworthy agents,”
2026-04-09.
https://www.anthropic.com/research/trustworthy-agents
Official safety framework. **Confidence: Medium-High**.

**[S34]** LangChain, LangGraph overview and persistence documentation, accessed
2026-07-27.
https://docs.langchain.com/oss/python/langgraph/overview
https://docs.langchain.com/oss/python/langgraph/persistence
Official product behavior. **Confidence: High** for features and replay
semantics.

**[S35]** OpenAI Agents SDK documentation, accessed 2026-07-27.
https://openai.github.io/openai-agents-python/
https://openai.github.io/openai-agents-python/human_in_the_loop/
Official product documentation. **Confidence: High** for features.

**[S36]** Anthropic, Claude Managed Agents documentation, accessed 2026-07-27.
https://platform.claude.com/docs/en/managed-agents/overview
https://platform.claude.com/docs/en/managed-agents/agent-setup
Official beta product documentation. **Confidence: High** for features and
eligibility constraints.

**[S37]** Google AI for Developers, “Gemini managed agents,” accessed
2026-07-27.
https://ai.google.dev/gemini-api/docs/agents
Official preview product documentation. **Confidence: High** for features.

**[S38]** OpenAI model comparison/pricing, accessed 2026-07-27.
https://developers.openai.com/api/docs/models/compare
Official dated price snapshot. **Confidence: High**.

**[S39]** Anthropic pricing, accessed 2026-07-27.
https://platform.claude.com/docs/en/about-claude/pricing
Official dated price snapshot. **Confidence: High**.

**[S40]** Google Gemini API pricing, updated 2026-07-09; accessed 2026-07-27.
https://ai.google.dev/gemini-api/docs/pricing
Official dated price snapshot. **Confidence: High**.

**[S41]** Stanford HAI, “2026 AI Index Report” and Economy chapter, 2026.
https://hai.stanford.edu/ai-index/2026-ai-index-report
https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
Official report. **Confidence: High**.

## Audit note

The independent extraction supporting this revision is stored in
`99-Raw-Extractions/AI-Capabilities-ChatGPT-2026-07-27.md`. The prior Claude
extraction remains in `99-Raw-Extractions/` for comparison. This master favors
claims that could be traced to primary sources during the 2026-07-27 audit and
removes attractive precision that could not be verified.
