# AI Capability Evidence Audit — ChatGPT — 2026-07-27

## Purpose and scope

This is the independent ChatGPT research layer used to strengthen
`01-AI-Capabilities/Master-Capability-Map.md`. It is intentionally an evidence
audit, not an opportunity or product-ideation document.

The governing project documents were read before research:

- `00-Meta/ABM-Project-Continuity.md`
- `05-Previous-Research/Master-Synthesis.md`

The project boundary is production reality as of July 2026. A model doing a
task once in a demo is not evidence that a system can perform the task
repeatedly, recover from failures, respect permissions, and deliver a
verifiable business outcome at acceptable cost.

## Method

1. Prefer official documentation, peer-reviewed proceedings, official
   benchmarks, government/standards sources, and papers with inspectable
   methods.
2. Separate model capability from system reliability. A production system may
   be reliable because deterministic software constrains and verifies an
   unreliable model.
3. Separate one-shot success from repeated success. For a workflow that must
   work every day, pass-at-1 is insufficient.
4. Treat vendor observational studies and company-authored deployment reports
   as useful but not independent evidence.
5. Treat 2026 preprints as current evidence with Medium confidence until
   peer-reviewed or independently reproduced.
6. Record material corrections to the inherited master rather than silently
   preserving attractive but weak claims.

## Material corrections and upgrades

| Item in the inherited draft | Audit result | Master treatment |
|---|---|---|
| “Measuring Agents in Production” surveyed 306 practitioners | The current arXiv v4 abstract reports **86 practitioners**, 20 case studies, and 26 domains. The 68% / 70% / 74% findings remain supported. | Correct sample size and cite the current version. |
| Agent Reliability Science evaluated 14 models | Current v3 reports **15 models** across two benchmarks and 12 metrics. | Correct to 15. |
| Precise METR frontier time horizon of 14–20 hours | METR’s live page supports the definition, the 50% and 80% measures, 100+ software tasks, and warns that estimates above 16 hours are unreliable. The exact 14–20-hour value was not exposed in inspectable text. | Remove the precision; retain the definition and the >16-hour measurement caveat. |
| Structured extraction can be “99%+” reliable | Schema compliance can be near-perfect while exact leaf-value accuracy is much lower. A 2026 benchmark reports best accuracy of 83.0% for text, 67.2% for document images, and 23.7% for audio. | Split format compliance from factual extraction accuracy. |
| “One competent agent beats a crew” | Too absolute. A 2026 scaling study finds large gains on parallelizable tasks but 39–70% degradation on sequential tasks; decentralized systems amplify independent errors. | State a conditional rule: multi-agent only when decomposition and merging are genuinely parallel and observable. |
| Model pricing from aggregators | Current official pricing pages are available for OpenAI, Anthropic, and Google. | Replace with an official July 2026 price snapshot and emphasize cost per verified outcome. |
| Stanford AI Index 2026 was a verification debt | Stanford’s official report supports 88% organizational AI adoption and says agent use remains early. | Close the debt using the primary source. |
| Benchmark scores equal production readiness | τ2-bench required a later “verified” task set; UTBoost found erroneous patches labeled passed in SWE-bench-style evaluation. | Add benchmark-validity and false-success limits. |

## High-value evidence ledger

Confidence is about the claim supported by the source, not about every
interpretation in this file.

### Production deployment and reliability

**E01 — Measuring Agents in Production**
Source: Chen et al., arXiv:2512.04123 v4, 2026-06-04; accepted as an ICML 2026
Oral.
URL: https://arxiv.org/abs/2512.04123
Findings: 20 case studies and 86 practitioners across 26 domains; 68% of
deployed agents execute at most 10 steps before human intervention; 70% use
prompting of off-the-shelf models; 74% primarily use human evaluation;
reliability is the leading challenge.
Confidence: **High**.

**E02 — Towards a Science of Agent Reliability**
Source: arXiv:2602.16666 v3, 2026-06-02; accepted at ICML 2026.
URL: https://arxiv.org/abs/2602.16666
Findings: evaluates 15 models with 12 metrics spanning consistency, robustness,
predictability, and safety; capability gains translate into much smaller
reliability gains.
Confidence: **High**.

**E03 — METR time horizons**
Source: METR, updated 2026-05-08.
URL: https://metr.org/time-horizons/
Findings: defines a time horizon as the duration of human-completable software
tasks a model can complete at a specified reliability; reports 50% and 80%
measures over 100+ tasks; explicitly warns that measurements above 16 hours
are unreliable.
Confidence: **High** for the method and caveat.

**E04 — OSWorld 2.0**
Source: arXiv:2606.29537 v2, 2026-07-13.
URL: https://arxiv.org/abs/2606.29537
Findings: 108 long-horizon computer workflows, median human duration about 1.6
hours, and an average 318 tool calls. The strongest reported system, Claude
Opus 4.8 with maximum thinking and batching, achieves 20.6% binary completion
and 54.8% partial completion. Failures include losing constraints, ignoring
mid-task information, guessing instead of asking, skipping verification, and
misreading hidden state.
Confidence: **Medium-High** (current benchmark preprint with inspectable tasks).

**E05 — TUA-Bench**
Source: arXiv:2606.28480, 2026-06.
URL: https://arxiv.org/abs/2606.28480
Findings: 120 real terminal and UI tasks; strongest Claude Code/Opus 4.8 result
is 65.8%. Terminal interaction is materially more effective than GUI
interaction, but neither supports general unattended operation.
Confidence: **Medium** (preprint).

### Tool use, workflow control, and security

**E06 — Berkeley Function-Calling Leaderboard v4**
Source: UC Berkeley Gorilla, updated 2026-04-12.
URL: https://gorilla.cs.berkeley.edu/leaderboard
Findings: top overall score 77.47; top multi-turn score 68.38 versus 88.58 for
single-turn. Tool selection and argument construction are substantially more
reliable in short contexts than in stateful interaction.
Confidence: **High** for the published leaderboard snapshot.

**E07 — Berkeley Function-Calling Leaderboard paper**
Source: Patil et al., ICML 2025, PMLR 267.
URL: https://proceedings.mlr.press/v267/patil25a.html
Findings: single-turn function calling is comparatively strong; memory,
dynamic decisions, and long-horizon execution remain open challenges.
Confidence: **High**.

**E08 — MCP-AgentBench**
Source: AAAI 2026 proceedings, published 2026-03-14.
URL: https://ojs.aaai.org/index.php/AAAI/article/view/40347
Findings: evaluates agents over 33 operational MCP servers, 188 tools, and 600
queries across six categories, using outcome-oriented evaluation.
Confidence: **High** for benchmark scope.

**E09 — MCPTox**
Source: AAAI 2026 proceedings, published 2026-03-14.
URL: https://ojs.aaai.org/index.php/AAAI/article/view/40895
Findings: 45 live MCP servers, 353 tools, 1,348 test cases, and 20 agent
settings; one setting reached 72.8% attack success, many popular configurations
exceeded 60%, and even the highest-refusal tested model refused fewer than 3%
of toxic tool responses.
Confidence: **High**.

**E10 — MCP-SafetyBench**
Source: ICLR 2026 / arXiv:2512.15163.
URLs: https://openreview.net/forum?id=7XYjeL46co and
https://arxiv.org/abs/2512.15163
Findings: five domains and 20 attack types; overall attack success ranges from
29.8% to 48.16%; host-side attacks average 81.94%; identity injection reaches
100% across 13 tested models.
Confidence: **High**.

**E11 — AgentDojo**
Source: Debenedetti et al., arXiv:2406.13352, 2024-06-19.
URL: https://arxiv.org/abs/2406.13352
Findings: 97 realistic tasks and 629 security test cases demonstrate indirect
prompt-injection risk through untrusted tool output; available defenses remain
incomplete.
Confidence: **High**, but flagged as a 2024 source.

**E12 — NIST Generative AI Profile**
Source: NIST AI 600-1, published 2024-07-26, updated 2026-04-08.
URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
Finding: risk controls belong across design, deployment, monitoring, and
incident response; a prompt-level guardrail is not a complete control system.
Confidence: **High**.

**E13 — NIST agent hijacking evaluation**
Source: NIST technical blog, 2025-01-17.
URL: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations
Finding: many agents are vulnerable to indirect prompt injection and need
stronger hijacking evaluations.
Confidence: **High**.

### Research, extraction, and document work

**E14 — DeepResearch Bench**
Source: arXiv:2506.06287, 2025-06.
URL: https://arxiv.org/abs/2506.06287
Findings: 89 tasks with frozen retrospective search evaluate hallucination,
tool use, evidence use, and forgetting.
Confidence: **Medium**.

**E15 — DeepResearchBench**
Source: arXiv:2506.11763, 2025-06.
URL: https://arxiv.org/abs/2506.11763
Findings: 100 PhD-level tasks across 22 fields, with separate report-quality
and citation-quality evaluation.
Confidence: **Medium**.

**E16 — DREAM: The Mirage of Synthesis**
Source: ACL 2026 Long Paper.
URL: https://aclanthology.org/2026.acl-long.448/
Finding: fluent, citation-aligned reports can still obscure factual and
reasoning defects; static evaluators without tools cannot fully validate
temporal or factual claims.
Confidence: **High**.

**E17 — Structured Output Benchmark**
Source: arXiv:2604.25359, 2026-04-28.
URL: https://arxiv.org/abs/2604.25359
Findings: 5,000 text examples, 209 OCR PDFs across seven document types, and
115 audio examples over 21 models. Near-perfect schema compliance coexists with
best exact leaf-value accuracy of 83.0% for text, 67.2% for document images,
and 23.7% for audio.
Confidence: **Medium** (preprint; strong corrective signal).

**E18 — READoc**
Source: Findings of ACL 2025.
URL: https://aclanthology.org/2025.findings-acl.1128/
Finding: 3,576 real documents reveal a continuing gap between document parsing
systems and realistic structured extraction.
Confidence: **High**.

**E19 — TWIX**
Source: UC Berkeley technical report, 2025-05-15.
URL: https://digicoll.lib.berkeley.edu/record/320827
Findings: a hybrid approach combining template inference with targeted LLM use
improves F1 by 25% versus popular extractors and, after template inference, is
reported as 520 times faster and 3,700 times cheaper than a vision-LLM
baseline.
Confidence: **Medium-High**; performance is system- and dataset-specific.

### Code generation and maintenance

**E20 — GitTaskBench**
Source: AAAI 2026 proceedings, published 2026-03-14.
URL: https://ojs.aaai.org/index.php/AAAI/article/view/40533
Findings: 54 realistic repository tasks across seven modalities/domains; best
OpenHands plus Claude 3.7 result is 48.15%; more than half of observed failures
arise from ordinary environment, dependency, and setup problems.
Confidence: **High**.

**E21 — UTBoost**
Source: ACL 2025 / arXiv:2506.09289.
URL: https://arxiv.org/abs/2506.09289
Findings: identifies 36 tasks with insufficient tests and 345 erroneous
patches incorrectly labeled passed; rankings change for 40.9% of SWE-bench Lite
and 24.4% of SWE-bench Verified entries after test strengthening.
Confidence: **High**.

**E22 — Claude Code expertise study**
Source: Anthropic Research, 2026-06-16.
URL: https://www.anthropic.com/research/claude-code-expertise
Findings: about 400,000 sessions from about 235,000 users; verified success is
15% for novice users and 28–33% for intermediate/expert users. Human expertise
remains an important part of system performance.
Confidence: **Medium** (large vendor observational study).

### Customer communication and outcome verification

**E23 — τ-bench**
Source: ICLR 2025.
URL: https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html
Findings: realistic retail and airline tool-agent-user interactions; GPT-4o
achieves under 50% task success, and repeated-success pass^8 is under 25% in
retail.
Confidence: **High**.

**E24 — τ2-bench and verified task set**
Sources: arXiv:2506.07982 and Amazon AGI GitHub repository, 2025–2026.
URLs: https://arxiv.org/abs/2506.07982 and
https://github.com/amazon-agi/tau2-bench-verified
Finding: dual-control tasks make the user and agent coordinate; performance
drops versus no-user settings. A later corrected task set was necessary because
some original task definitions, actions, and evaluation did not align.
Confidence: **High** for the evaluation caveat; **Medium** for current
performance generalization.

**E25 — Five Nubank production deployments**
Source: arXiv:2606.08867, 2026-06-07.
URL: https://arxiv.org/abs/2606.08867
Findings: five customer-support deployments in a company serving 100M+ users;
one card-delivery A/B test reports +37 percentage points transactional NPS and
+29 points self-service versus prior variants.
Confidence: **Medium** (company-authored deployment report).

**E26 — False success detection**
Source: arXiv:2606.09863, 2026-06-01.
URL: https://arxiv.org/abs/2606.09863
Findings: 9,876 τ2 trajectories and 1,879 AppWorld trajectories; false success
accounts for 45–48% of failures in single-control τ2 and 75.8% of AppWorld
self-assessed success. No tested LLM-judge configuration exceeds AUROC 0.65 on
τ2 or 0.54 on AppWorld, while a task-specific TF-IDF detector reaches 0.83 and
0.95 at far lower latency.
Confidence: **Medium** (preprint); strong support for task-specific verifiers.

### Multi-agent systems

**E27 — MAST**
Source: arXiv:2503.13657, 2025-03-17.
URL: https://arxiv.org/abs/2503.13657
Findings: five frameworks, 150 tasks, and six expert annotators identify 14
failure modes in three clusters; many multi-agent gains are minimal and
coordination failures are common. Inter-annotator kappa is 0.88.
Confidence: **Medium-High**.

**E28 — Towards a Science of Scaling Agent Systems**
Sources: Google Research, 2026-01-28; arXiv:2512.08296.
URLs:
https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
and https://arxiv.org/abs/2512.08296
Findings: 180 configurations across four benchmarks. Centralized multi-agent
systems improve parallelizable tasks by up to 80.9%, but every tested
multi-agent variant degrades sequential tasks by 39–70%. Independent error
amplification is 17.2 times in decentralized systems versus 4.4 times in
centralized systems.
Confidence: **Medium-High** (large current preprint with official research
summary).

**E29 — Multi-Agent Computer Use**
Source: arXiv:2606.01533, 2026-06.
URL: https://arxiv.org/abs/2606.01533
Finding: DAG-managed specialist agents improve selected computer-use
benchmarks by 3.4–25.5% and reduce wall time by about 1.5 times, demonstrating
that observable parallel decomposition can be useful.
Confidence: **Medium** (preprint; narrow conditions).

### Architecture and platform evidence

**E30 — Building Effective Agents**
Source: Anthropic Engineering, 2024-12-19.
URL: https://www.anthropic.com/engineering/building-effective-agents
Findings: simple composable workflow patterns are the most dependable starting
point; workflows trade flexibility for predictability; agent loops need
environmental ground truth, stopping conditions, and extensive sandbox tests.
Confidence: **Medium-High** (vendor engineering guidance; consistent with
independent evidence).

**E31 — OpenAI practical guide to building agents**
Source: OpenAI, current 2026 documentation.
URL: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
Findings: risk-rate tools by read/write access, reversibility, permissions, and
financial impact; use human oversight for high-risk or irreversible actions;
combine model guardrails with authentication, authorization, and strict access
control.
Confidence: **Medium-High** (official implementation guidance).

**E32 — LangGraph documentation**
Source: LangChain, accessed 2026-07-27.
URLs: https://docs.langchain.com/oss/python/langgraph/overview and
https://docs.langchain.com/oss/python/langgraph/persistence
Findings: checkpointing, persistence, human-in-the-loop, and durable execution
are explicit primitives. Replaying from a checkpoint can re-execute later nodes,
including LLM and API calls, so side effects still require idempotency.
Confidence: **High** for product behavior; not evidence of application
reliability by itself.

**E33 — OpenAI Agents SDK**
Source: OpenAI, accessed 2026-07-27.
URLs: https://openai.github.io/openai-agents-python/ and
https://openai.github.io/openai-agents-python/human_in_the_loop/
Findings: function tools, sessions, handoffs, tracing, serialized run state,
approval pauses, and durable-runtime integrations are supported primitives.
Confidence: **High** for product features.

**E34 — Claude Managed Agents**
Source: Anthropic documentation, accessed 2026-07-27.
URLs: https://platform.claude.com/docs/en/managed-agents/overview and
https://platform.claude.com/docs/en/managed-agents/agent-setup
Findings: beta stateful long-running agents, managed sandbox, versioned
configuration, tools, MCP, skills, and multi-agent features. The service is not
Zero Data Retention or HIPAA eligible at this date.
Confidence: **High** for product state and constraints.

**E35 — Gemini managed agents**
Source: Google AI for Developers, accessed 2026-07-27.
URL: https://ai.google.dev/gemini-api/docs/agents
Findings: managed agent harness in preview; interaction budgets can run from
100,000 to 3 million tokens; documentation recommends least privilege and
verifying output before deployment.
Confidence: **High** for product state; no implied production reliability.

### Adoption and cost

**E36 — Stanford AI Index 2026**
Source: Stanford HAI, 2026.
URLs: https://hai.stanford.edu/ai-index/2026-ai-index-report and
https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
Findings: 88% of surveyed organizations report AI use, while AI-agent use
remains early. Adoption of AI does not establish autonomous-agent reliability.
Confidence: **High**.

**E37 — OpenAI model pricing**
Source: OpenAI, accessed 2026-07-27.
URL: https://developers.openai.com/api/docs/models/compare
Snapshot: GPT-5.6 Sol $5 input / $30 output per million tokens; Terra $2.50 /
$15; Luna $1 / $6.
Confidence: **High** for the dated price snapshot.

**E38 — Anthropic pricing**
Source: Anthropic, accessed 2026-07-27.
URL: https://platform.claude.com/docs/en/about-claude/pricing
Snapshot: Claude Opus 4.8 $5 / $25; Sonnet 5 promotional $2 / $10 through
2026-08-31 and then $3 / $15; Haiku 4.5 $1 / $5. Batch processing is 50% of
standard token pricing.
Confidence: **High** for the dated price snapshot.

**E39 — Gemini API pricing**
Source: Google, updated 2026-07-09.
URL: https://ai.google.dev/gemini-api/docs/pricing
Snapshot: Gemini 3.5 Flash $1.50 / $9 standard and $0.75 / $4.50 batch per
million tokens; grounded search is separately metered after free allowance.
Confidence: **High** for the dated price snapshot.

## Synthesis used in the master

### What is reliably achievable now

- Drafting, classification, transformation, and summarization when inputs are
  bounded and outputs are reviewed or mechanically validated.
- Research assistance when retrieval is inspectable, citations are opened, and
  consequential claims receive independent verification.
- Structured extraction into typed schemas when the input class is constrained,
  confidence/exception paths exist, and critical fields are reconciled against
  source documents.
- Short tool workflows with typed interfaces, least privilege, explicit state,
  and deterministic postconditions.
- Code changes inside a sandbox when tests, linting, type checks, and human
  review gate merge or deployment.
- Monitoring pipelines where deterministic collectors detect events and the
  model summarizes or prioritizes them.
- High-volume customer triage and routine grounded support with escalation and
  transaction verification.

### What is not reliably achievable without human or deterministic control

- General long-horizon computer use across hidden UI state.
- Autonomous operation over untrusted web/email/document input while holding
  high-impact permissions.
- Self-certification of task success.
- Durable memory based only on model context or semantic retrieval.
- Open-ended multi-agent swarms.
- Unreviewed strategy, negotiation, relationship management, regulated advice,
  irreversible purchases, or high-loss transactions.

### Production design rule

The dependable unit is not “an autonomous agent.” It is a bounded process:

`typed input -> explicit state -> short model step -> restricted tool ->
deterministic check -> durable checkpoint -> risk gate -> observable outcome`

The model supplies probabilistic judgment inside that process. Deterministic
software owns permissions, state, invariants, money movement, and proof of
completion.
