# Raw Extraction – AI Capabilities (Claude pass, 2026-07-26)

Purpose: raw source log behind `01-AI-Capabilities/Master-Capability-Map.md`.
Contains the evidence as collected, including contradictions and rejected sources.
Do not treat this file as a conclusion — it is the audit trail.

---

## A. Source-quality triage note (important)

Web search for "2026 AI agent" topics returns a very high proportion of
**SEO content-farm pages** that publish confident-looking benchmark numbers with no
methodology and, in several cases, model names that do not verifiably exist.

Examples encountered and **rejected or downgraded**:

| Claim found | Source type | Disposition |
|---|---|---|
| "Claude Mythos 5 … 95.5% on SWE-bench Verified" | SEO leaderboard aggregator (leaderboard.steel.dev summary) | **Rejected.** Unverifiable model name; no primary confirmation. |
| "Coasty scored 82% on OSWorld vs OpenAI 38% / Anthropic 22%" | coasty.ai (vendor blog, own product) | **Rejected.** Vendor self-report; internally inconsistent with all other OSWorld reporting. |
| "89% of enterprise AI agent implementations never reach production" | aibusinessweekly.net / theaiconsultingnetwork.com, attributed to Stanford AI Index 2026 | **Downgraded to Low.** Directionally consistent with the AI Index's "agentic deployment remains limited" framing, but the specific 89% figure is not traceable to the Index itself. Treat as folklore, not data. |
| "Fin resolution rate 76% in 2026" vs "51% average" vs "67% across 7,000+ customers" | multiple competitor/vendor blogs | **Kept as a range, Low–Medium.** The spread itself is the finding. |
| "AI agents succeed on 66.3% of real computer tasks, within 6pp of human baseline" | Stanford AI Index 2026 as reported by secondary press | **Medium.** Widely and consistently reported; refers to original OSWorld, not OSWorld 2.0. |

Rule applied in the Master map: any number sourced only to a content farm is either
omitted or labelled **Low confidence** with the disagreement shown.

---

## B. Primary / high-trust sources used

### B1. METR — Task-Completion Time Horizons
- URL: https://metr.org/time-horizons/ (fetched 2026-07-26; page last updated **2026-05-08**)
- URL: https://metr.org/notes/2026-01-22-time-horizon-limitations/
- URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Original method paper: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

**Verbatim-level caveats from METR's own page (High confidence, this is the publisher speaking):**
- "Measurements above 16 hrs are unreliable with our current task suite."
- Horizons apply primarily to "software engineering, machine learning, or cybersecurity tasks."
- Human baseline = "a low-context person (such as a new hire or a remote internet contractor)",
  **not** a domain expert.
- Tasks are "well-specified, algorithmic tasks" — explicitly **not** jobs requiring
  interpersonal interaction or holistic success criteria.
- Coverage is incomplete; "not a complete record of the most capable models."

**Figures (Medium confidence — the live numbers sit in an interactive chart that the
text fetch did not expose; the values below come from secondary reporting of METR
and Epoch AI and should be re-verified against the interactive chart):**
- Doubling time ~7 months over 2019–2025; ~4–4.3 months over 2024–2026.
- Feb 2026: Claude Opus 4.6 top at 50%-horizon ≈ 14h30m.
- Mid-2026 frontier estimates ≈ 16–20h on the 50% horizon — i.e. **at or past METR's own
  stated reliability ceiling for the task suite**, which is the single most important
  caveat for this project.
- 80%-horizon is roughly 4–5× shorter than the 50%-horizon in METR's fitted curves.

**Interpretation for ABMs:** the 50% horizon is a *coin-flip* horizon. For a business
process you need the 80%+ horizon, which is on the order of **1–3 hours** of
low-context-human-equivalent work, on well-specified algorithmic tasks only.

### B2. OSWorld 2.0 (computer-use agents, long-horizon)
- Repo note: `05-Previous-Research/Individual-Papers/2606.29537v2.md` (already in this project)
- PDF: https://s46486.pcdn.co/wp-content/uploads/2022/01/OSWorld2.0.pdf (2026-06-26)
- Headline: best configuration (Claude Opus 4.8, max thinking, batched tool calls)
  completes **20.6%** of tasks, **54.8%** partial score. GPT-5.5 plateaus ~13%.
- Original OSWorld: 12% (Apr 2024) → ~66% (2026). Human baseline on original OSWorld
  reported as **72.36%**.
- **The 66% vs 20.6% gap is the benchmark-saturation story**: the moment tasks get
  longer and more realistic, success collapses by ~3×.
- Confidence: High for the direction, Medium for exact percentages.

### B3. MAST — Why Do Multi-Agent LLM Systems Fail?
- https://arxiv.org/abs/2503.13657 ; NeurIPS 2025 poster; https://github.com/multi-agent-systems-failure-taxonomy/MAST
- 14 failure modes in 3 clusters: **system design issues, inter-agent misalignment,
  task verification**.
- Built from 150 hand-annotated traces, inter-annotator κ = 0.88; MAST-Data extends to
  1,600+ traces across 7 MAS frameworks.
- Key line: "many failures stem from poor system design, not model performance," and
  MAS gains on popular benchmarks "are often minimal."
- Confidence: High (peer-reviewed, primary).

### B4. Agent security — prompt injection / MCP tool poisoning
- AgentDojo (already in project corpus): `2406.13352v3.md`
- MCPTox (AAAI): https://ojs.aaai.org/index.php/AAAI/article/view/40895/44856
  — 45 live MCP servers, 353 authentic tools, poisoned descriptions;
  **attack success >60%, up to 72%** on many popular agents.
  Most-resistant model in the study refused poisoned tool calls **<3%** of the time.
- InjecAgent: 1,054 cases; GPT-4 vulnerable **24%** baseline → **47%** with enhanced
  attack prompts.
- MCP-SafetyBench: 20 attack types / 5 domains; host-side attacks **>80%** success avg.
- Supply-chain incident, **May 2026**: OX Security disclosed a systemic vulnerability in
  MCP implementations across multiple languages — reported supply chain of
  >150M downloads, ~200k vulnerable instances. (Secondary reporting: itecsonline.com,
  practical-devsecops.com. **Medium confidence** — the incident is widely reported;
  the exact instance count is a vendor estimate.)
- Real-world 2025 case: Supabase/Cursor support-ticket agent — attacker-supplied ticket
  text executed as SQL, exfiltrating integration tokens. Pattern =
  **privileged access + untrusted input + outbound channel**. (Medium.)
- Confidence overall: High that this is an unsolved structural problem.

### B5. Anthropic Economic Index (primary, CC BY 4.0)
- https://www.anthropic.com/economic-index — accessed via MCP 2026-07-26.
- Latest period **2026-05-01**, snapshot modified 2026-06-24. 121 countries,
  22 job categories, 923 occupations tracked / 718 published.
- Global headline: augmentation **51.38%** vs automation **48.62%**;
  work **43.36%** / personal **40.2%** / coursework **16.45%**.
- **Critical methodological limit stated by the publisher:** this is observed Claude
  usage matched to *task* catalogs. It is NOT a measure of jobs, the labour market, or
  who the users are. The correct phrasing is "AI is used for tasks commonly done by
  [occupation]". It cannot support displacement claims and has no trend series.
- Job-category shares of usage (2026-05):
  Computer & Mathematical 23.8 · Arts/Design/Media 13.55 · Educational Instruction &
  Library 12.79 · Sales 9.14 · Office & Admin Support 7.89 · Management 5.9 ·
  Business & Financial Ops 5.77 · Life/Physical/Social Science 4.51 ·
  Architecture & Engineering 3.56 · Healthcare Practitioners 3.31 ·
  Community & Social Service 2.57 · **Personal Care & Service 1.23** · Production 1.04 ·
  Legal 1.02 · Installation/Maint/Repair 0.62 · **Healthcare Support 0.62** ·
  Food Prep 0.48 · Transportation 0.34 · Protective Service 0.33 ·
  Building & Grounds 0.13 · Construction 0.10 · Farming 0.04.
- Note re: "Task success rates are not currently available for the latest dataset."

### B6. Anthropic Economic Index — Vietnam (VNM), period 2026-05-01
- Anthropic Usage Index **0.53** (usage per working-age population = ~half the global
  average); rank **84 of 121**.
- Use case: work **53.13%** (global 43.36), personal 26.5 (40.2), coursework 20.38 (16.45).
- Automation **51.38%** vs augmentation 48.62 — the mirror image of the global split.
- Top request topics vs global baseline: Content Creation & Copywriting 24.91 (22.72);
  Software Development 18.01 (11.51); Education & Learning 14.54 (13.23);
  Research & Intelligence 8.11 (10.94); Document Processing & Extraction 5.31 (4.32).
- Job categories vs global index: Computer & Math 29.32 (×1.23);
  Architecture & Engineering 5.17 (×1.45); Sales 6.46 (×0.71);
  Healthcare Practitioners 1.66 (×0.50).
- Reading: Vietnam's observed usage is **more work-oriented, more automation-styled, and
  more technical** than the world average, and *thinner* on advice/consumer-facing use
  (artifact "advice or recommendation" 5.54 vs 10.72 global).

### B7. LLM-as-judge reliability
- "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge
  Models Across Agreement, Consistency, and Bias" — https://arxiv.org/abs/2606.19544 (2026-06)
- Position bias measured across 15 judges / ~150,000 evaluation instances; bias is
  **systematic, not random**, and varies by judge and task.
- Strong judges can reach Cohen's κ > 0.80 vs human raters on well-structured tasks.
- RAND (2026, via secondary): no judge uniformly reliable across benchmarks; frontier
  models exceeded 50% error on hard bias benchmarks. (**Low–Medium** — secondary.)
- Practical rule extracted: LLM judges are usable as **regression detectors** on a fixed
  rubric, not as **absolute quality certifiers**.

### B8. Agent memory
- Mem0 (ECAI 2025 paper + April 2026 algorithm release): LoCoMo **92.5**,
  LongMemEval **94.4**, ~6,900 tokens/query; biggest gains on temporal (+29.6) and
  multi-hop (+23.1). Source: mem0.ai blog — **vendor self-report, Low–Medium.**
- Zep rebuttal: claims corrected LoCoMo **75.14%** vs the 65.99% Mem0 reported for them.
  Independent note: Zep memory footprint >600k tokens/conversation vs Mem0's 1,764;
  post-ingestion retrieval often only succeeds after background graph processing
  completes (hours) — a real-time blocker. (**Low–Medium**, contested.)
- Benchmarks in use: LoCoMo (1,540 questions: single-hop, multi-hop, open-domain,
  temporal), LongMemEval, BEAM.
- **Finding worth keeping:** every published memory number is a vendor number, and the
  two leading vendors publicly dispute each other's methodology. Treat agent memory as
  an *unbenchmarked* layer for production purposes.

### B9. Document extraction accuracy
- research.aimultiple.com invoice OCR benchmark; vellum.ai; llamaindex OCR-accuracy post;
  parsli/zerentry comparisons (mixed quality).
- Consistent pattern across sources (Medium confidence for the pattern, Low for any
  single number):
  - Traditional OCR on structured invoice fields: **85–95%**
  - LLM / hybrid extraction: **97–99%** on simple fields (totals, vendor name: 99%+)
  - **Complex fields — line items, multi-row tax breakdowns: 95–97%**
  - Straight-through-processing threshold for financial/identity fields cited as
    **99.9% field-level** — i.e. above what LLM extraction currently delivers on
    complex fields.
  - Accuracy degrades sharply on low-quality scans/photos.
- Scanned-invoice head-to-head cited: Gemini 94%, GPT+OCR 91%, Claude 90%. (Low.)

### B10. Customer support automation
- Intercom Fin published averages: 51% (with top performers 65–70%) / 67% across
  7,000+ customers / 76% in 2026 — three different figures across sources.
- Counter-evidence: Intercom's own case studies cluster **42–50%**; an independent
  500-ticket small-business test landed at **38%**; B2B deployments run
  **17–25 points below** vendor benchmarks.
- Decagon: no public benchmark; Rippling cited moving chat deflection 38% → 50%+.
- Lorikeet's 2026 benchmark framing: ~two-thirds resolution as median, 70–75% strong,
  80%+ best-in-class **on a high-structure intent mix**.
- Confidence: Medium for the 40–70% band, Low for any single vendor figure.
- **Extracted rule:** resolution rate is a function of *intent-mix structure*, not model
  quality. A narrow, high-structure intent set is where the automation actually lands.

### B11. Coding agents
- SWE-bench Verified = 500 human-validated instances (https://www.swebench.com/verified.html).
- April 2026 cluster reported at ~**80–81%** (Claude Opus 4.5/4.6, Gemini 3.1 Pro).
  Medium confidence — consistent across several aggregators.
- Broader reality band across configurations/compute budgets: **40–75%**.
- Terminal-Bench 2.0 and LongCLI-Bench (2026) push toward longer CLI horizons.
- UTBoost (https://arxiv.org/abs/2506.09289) finds SWE-bench test suites are
  insufficiently rigorous — reported scores are **optimistic**. High relevance.
- mini-swe-agent: minimal scaffolds reach near-SOTA → **scaffold complexity is not the
  bottleneck**; this argues against elaborate multi-agent designs.

### B12. Cost / pricing (July 2026)
- Aggregators: tldl.io, morphllm.com, costgoat.com, developersdigest.tech (all secondary;
  **Medium** for the band, Low for exact per-model figures — verify against vendor
  pricing pages before budgeting).
- Reported band per 1M tokens (input/output):
  - Frontier: ~$5/$25 to $5/$30
  - Strong mid-tier: ~$1/$6 to $2.50/$15; Claude Sonnet 5 promo $2/$10 (reverting to
    $3/$15 after 2026-08-31)
  - Cheap/small: $0.10–$0.15 in, $0.28–$0.60 out
- Batch APIs at a flat **50%** discount are near-universal (Anthropic, OpenAI, Google,
  Alibaba).
- Claimed ~**80%** industry-wide price reduction 2025→2026 at constant capability tier.
  (Low–Medium; direction is well-supported, magnitude is not.)

### B13. Framework / platform landscape
- LangGraph reported at 34.5M monthly downloads and positioned as the production default
  for stateful, durable, auditable workflows; named deployments include Klarna, Uber,
  LinkedIn, BlackRock, Cisco, Elastic, JPMorgan, Replit. (**Medium** — mostly vendor and
  vendor-adjacent reporting.)
- Anthropic renamed Claude Code SDK → **Claude Agent SDK** in early 2026.
- OpenAI's Swarm → production Agents SDK with sandboxed execution + harness.
- Google ADK; HuggingFace smolagents; CrewAI; AutoGen/AG2; Pydantic AI; DSPy.
- Split that matters: **provider-native SDKs** (single model family, best error handling
  and safety defaults) vs **independent frameworks** (portable, more glue).
- No-code / low-code: n8n, Make, Zapier. n8n workflow characterization already in the
  project corpus (`2606.29116v2`), which found real workflows have **tight action
  coupling and missing reliability controls**.
- Gartner (via secondary): 40% of enterprise applications to feature task-specific agents
  by end-2026, up from <5% in 2025. (**Low** — vendor-quoted analyst projection.)
- Agent market $7.84B (2025) → $52.62B (2030), 46.3% CAGR. (**Low** — market-sizing
  report, unverifiable methodology. Included only as a directional signal.)

### B14. Voice agents
- Latency: >800ms produces caller talk-over; sub-600ms achievable in production;
  some platforms claim <500ms. (Medium for the 800ms threshold — it recurs
  independently across sources and matches human turn-taking research.)
- One tester ran 400+ inbound calls across medical / home services / professional /
  SMB retail; top platforms correctly identified caller intent on first attempt in
  **80%+** of calls. (Low–Medium; single unverified tester.)
- Retell AI cited at ~600ms end-to-end, **$0.07/min**, native Cal.com and Google Calendar
  booking. Pricing is a checkable vendor claim (Medium).
- **Extracted rule:** voice is now cheap enough ($0.07/min ⇒ a 4-minute booking call
  ≈ $0.28) that inbound-call capture is economically viable for a single-location
  service business. Intent recognition at ~80% first-attempt means it needs a
  deterministic fallback, not autonomy.

### B15. Stanford AI Index 2026
- Reported via secondary press (Forbes 2026-04-14; sapinsider; af.net; aiquinta).
- Consistently reported claims: 88% of organizations use AI in ≥1 business function;
  78% of Fortune 500 deployed at scale; agent success ~66.3% on real computer tasks;
  **agentic deployment remains limited across most business functions**;
  governance/validation/readiness lag adoption; current phase = "augmentation within
  existing operating models."
- Confidence: Medium (consistent multi-source secondary reporting of a primary report;
  the primary PDF was not fetched in this pass — **flag for verification**).

---

## C. Open verification debts (carry into next pass)

1. Fetch the METR interactive chart data directly and pin exact 50%/80% horizons per
   model with dates. (Highest value single fix.)
2. Fetch the Stanford AI Index 2026 primary PDF and replace all secondary citations.
3. Verify current vendor pricing pages (Anthropic/OpenAI/Google) rather than aggregators.
4. Find a non-vendor agent-memory benchmark. If none exists, that absence is itself a
   finding to state plainly.
5. Locate a primary source for the "% of agent pilots that never reach production" claim,
   or drop it entirely.
6. Check whether OSWorld 2.0 has posted updated leaderboard numbers since 2026-06-26.
