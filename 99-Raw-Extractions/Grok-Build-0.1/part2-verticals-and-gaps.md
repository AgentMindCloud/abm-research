# Part 2: Vertical Decision Brief + Gap Research
**As of late July 2026 · Companion to the accessible AI landscape report**

---

## A. Vertical deep-dives (decision brief)

Three SMB patterns dominate women-led and lifestyle service businesses. Choose by **revenue model**, not by “best AI.”

| Vertical | Revenue model | Primary pain | Stack philosophy |
|----------|---------------|--------------|------------------|
| **Salon / spa / beauty pro** | Appointments + retail | Empty chairs, no-shows, rebooking, IG DMs | One vertical ops OS + light social AI |
| **Shopify boutique** | Product DTC | Copy, ads, email, inventory, agentic discovery | Platform AI (Sidekick) + email/SMS + creative |
| **Freelance services** | Projects + retainers | Proposals, contracts, follow-up, scheduling | Client CRM OS + general chat AI |

---

### 1. Salon / spa / independent beauty stack

**Who it’s for:** Solo stylists, booth renters, salons up to ~10 staff, spas; also medspa once EMR matters.

#### Core ops (pick one)

| Tool | Entry price (annual billing) | AI / automation | Why pick it |
|------|------------------------------|-----------------|-------------|
| **GlossGenius** | Standard **$24/mo**, Gold **$48**, Platinum **$148** (monthly: $28 / $56 / $168) | AI Marketing Assistant; Growth Analyst (limited → unlimited by plan); **Reception by GlossGenius** (24/7 call/text booking) **Coming soon** | Beauty-first UX; flat **2.6%** processing; packages/memberships; AI marketing on all plans with trial limits on Standard |
| **Square Appointments** | Free (solo) → Plus ~$49 → Premium ~$149 | Strong booking/reminders; less beauty-native AI marketing than GlossGenius | Already in Square payments ecosystem; free solo start |
| **Vagaro** | Competitive free/low entry (verify live) | Broad marketplace + marketplace discoverability | Multi-service (salon + fitness + more); fee structure can stack |

**GlossGenius AI detail (verified July 2026 pricing page):**
- **AI Marketing Assistant** — drafts email/text campaigns (limited trial on Standard; fuller on higher tiers).
- **Growth Analyst** — limited trial / 20 queries/mo / unlimited by plan; surfaces revenue opportunities and peer comparisons.
- **Reception** — marketed as 24/7 call + text receptionist that books into calendar; **not generally available yet** (Coming soon). Do not build ops plans around it until GA.

#### Recommended salon stack (solo → small team)

| Layer | Tool | Approx. monthly |
|-------|------|-----------------|
| Ops + POS + booking | GlossGenius Gold | $48 |
| Chat / copy | Claude Free or Pro | $0–20 |
| Short-form video | CapCut | Free–Pro |
| Design | Canva Free/Pro | $0–15-ish |
| Instagram DM funnels | Manychat Free → Pro | $0–~29+ |
| Optional inbox AI | Lindy Plus | ~$50 |

**Realistic all-in for a serious solo beauty pro:** **~$50–120/mo** software (excluding ad spend and card processing %).

**Do this first (30-day plan):**
1. Move booking + deposits + reminders into GlossGenius (or Square if payments already live there).
2. Turn on AI Marketing Assistant for rebooking + “haven’t visited in 60 days” texts.
3. CapCut + Canva for before/after + Reels; post consistently.
4. Manychat Free: auto-reply Instagram DMs with booking link.
5. Only add Lindy/Reception-class tools when calendar is already full and missed calls hurt revenue.

**Avoid:** Stacking three booking systems; waiting for Reception instead of fixing no-show policies and card-on-file now.

---

### 2. Shopify boutique (fashion / beauty / lifestyle DTC)

**Who it’s for:** Product brands on Shopify; Instagram-led boutiques; freelancers who also sell inventory.

#### Core AI (platform-native)

**Shopify Sidekick** — included with Shopify plans (limits vary by plan). Not a separate AI subscription.

What it does well in 2026 (merchant-facing + Winter/Spring ’26 evolution):
- Store design, product copy, photo edits, discounts, campaigns
- Performance Q&A against **real store data** (ShopifyQL for performance/payments; fulfillments/payouts queries expanded)
- Flow automation generation (Q1 2026: ~half of Flow automations AI-generated in the quarter)
- Custom app building via natural language (12k+ apps built in Q1 2026)
- **Spring ’26 App Extensions** — Sidekick talks to partner apps (launch partners included **Klaviyo, Loop, Smile, Judge.me, Yotpo** and others)
- **Agentic storefronts** — control brand presence in ChatGPT / Perplexity / Copilot-style discovery surfaces

Merchant signal: weekly active Sidekick shops **~385% YoY** (Shopify Q1 2026 earnings).

#### Recommended boutique stack

| Layer | Tool | Role |
|-------|------|------|
| Commerce OS + agent | **Shopify + Sidekick** | Ops, catalog, campaigns, Flow |
| Email/SMS | **Klaviyo** (Sidekick extension partner) | Lifecycle, abandoned cart, segments |
| Social chat sales | **Manychat** | IG/TikTok DM automation |
| Creative | **Canva + CapCut** | UGC-style product content |
| Generative product art | Midjourney or Canva Magic | Mood boards, ads (watch commercial terms) |
| Optional try-on | **YouCam / Perfect Corp** | Beauty/fashion virtual try-on (B2B often sales-led) |
| Reviews/loyalty | Judge.me, Smile (Sidekick-aware) | Social proof + retention |

**Realistic all-in (beyond Shopify plan):** Klaviyo (usage-based) + Canva Pro + Manychat Pro ≈ **$50–200+/mo** depending on list size and order volume.

**Do this first (30-day plan):**
1. Use Sidekick daily for product descriptions, discount tests, and “what sold last 30 days by margin.”
2. One Klaviyo flow set: welcome, abandoned cart, post-purchase.
3. CapCut product Reels + Manychat “comment keyword → DM product link.”
4. Ask Sidekick to draft Flow for low-stock alerts and VIP tags.
5. Only then add Jasper/Midjourney for scale content—not day one.

**Avoid:** Buying a second “AI commerce suite” that duplicates Sidekick; ignoring agentic storefront settings as AI shopping agents grow.

---

### 3. Freelance services (coaches, photographers, planners, consultants)

**Who it’s for:** Project-based and retainer services without heavy inventory.

#### Client OS comparison (2026)

| Tool | Annual-ish entry | Strength | AI angle |
|------|------------------|----------|----------|
| **HoneyBook** | Starter **~$29/mo** annual ($36 monthly); Essentials **~$49** annual; Premium **~$109** annual | Polished client experience, payments, portal; strong for NA freelancers | HoneyBook AI on higher tiers (emails, notes, tasks, scheduling help); Essentials commonly cited as automation + AI sweet spot |
| **Dubsado** | Starter **~$35/mo**, Premier **~$55** (often cheaper annual) | Deep workflow automation, highly customizable | Less “chat AI product,” more form/workflow automation power |
| **17hats** | From ~**$13–25/mo** annual tiers (sources vary; verify live) | Lowest-cost client management | Fewer modern AI marketing features vs HoneyBook |

**Rule of thumb:**
- Want fastest beautiful client path + AI help → **HoneyBook Essentials**
- Want max automation control and will invest setup time → **Dubsado Premier**
- Need cheapest contracts/invoices → **17hats**, then bolt on Claude

#### Recommended freelance stack

| Layer | Tool | Approx. |
|-------|------|---------|
| CRM / proposals / payments | HoneyBook Essentials | ~$49/mo annual |
| Daily writing / strategy | Claude Pro or ChatGPT Plus/Go | $8–20 |
| Scheduling edge cases | Built-in + Calendly if needed | $0–12 |
| Cross-app glue | Zapier Free → Pro (~$20+) | $0–30 |
| Optional personal agent | Lindy | ~$50 |

**Realistic all-in:** **~$50–100/mo** for a serious solo.

**Do this first (30-day plan):**
1. Template: inquiry form → proposal → contract → invoice → thank-you (HoneyBook or Dubsado).
2. Claude project with brand voice + service packages for proposals and emails.
3. Zapier: new lead → CRM + Slack/email self-alert.
4. CapCut/Canva for portfolio content.
5. Lindy only if inbox volume is the bottleneck, not sales process design.

**Avoid:** Paying for Premium CRM tiers before you have a repeatable offer and pipeline.

---

### Vertical pick matrix

| If you… | Choose | First AI win |
|---------|--------|--------------|
| Sell time in a chair / treatment room | **Salon stack (GlossGenius Gold)** | Rebooking + marketing texts via AI Marketing Assistant |
| Sell physical product online | **Shopify + Sidekick + Klaviyo** | Sidekick product copy + abandoned-cart Flow |
| Sell projects / packages | **HoneyBook Essentials + Claude** | Proposal/email drafting + automated client pipeline |
| Sell mostly via Instagram DMs | Add **Manychat** to any of the above | Keyword auto-reply → book/buy link |
| Need phone answered 24/7 | Plan for **Reception (GG)** or **Playground Camber** (childcare) or generic voice agents—verify GA | Don’t overbuy until call volume justifies it |

**Cross-vertical constants (always worth it at low cost):**
1. Claude or ChatGPT for writing  
2. CapCut for short video  
3. Canva for static design  
4. Human approval before AI sends client-facing money/legal messages  

---

## B. Gap research: Tutoring

### Market context
AI tutors market cited ~**$2.1B (2025)** → **$2.7B (2026)** with high CAGR estimates through 2033 (treat absolute $ as order-of-magnitude). Two different product classes matter:

1. **Student-facing AI tutors** (Khanmigo, NotebookLM, YouLearn, etc.) — often **compete with** human tutors for homework help.  
2. **Tutoring business ops** (TutorCruncher, Teachworks) — run a human tutoring company.  
3. **Teacher productivity AI** (MagicSchool, free Khanmigo for teachers) — lesson planning for educators who also tutor.

### Student / learner AI (not a tutoring business OS)

| Product | Pricing (approx.) | Fit for independent tutors |
|---------|-------------------|----------------------------|
| **Khanmigo** (Khan Academy) | **Free for US teachers**; parents/learners **~$4/mo or $44/yr**; family can enable up to ~10 children; district custom | Use as **homework companion** students already know; tutors should position human sessions as accountability + gaps AI can’t fill |
| **MagicSchool AI** | Free tier; Plus ~**$8.33–12.99/user/mo** | Lesson plans, scaffolds, differentiation for teacher-tutors |
| **Google NotebookLM** | Free / Google AI tiers | Upload PDFs/notes → study guides, audio overviews for custom curricula |
| **Jotform AI Tutor / YouLearn / Knowt / Penseum** | Varies; freemium common | Student self-study; weak as business systems |
| **ibl.ai** | Starter from ~$16/mo; Pro from ~$250/mo (institutional lean) | Institutions more than solo tutors |
| **Varsity Tutors Live+ AI** | Platform-side hybrid (Nov 2025 announcement) | Marketplace model—not your brand OS |

### Tutoring **business** software (the gap fill for operators)

| Product | Pricing | Notes |
|---------|---------|-------|
| **TutorCruncher** | Pay-as-you-go **~$30/mo**; Startup **~$80/mo**; Enterprise custom | Scheduling, invoicing, tutor payouts; card fees ~3.5–3.85% on lower plans |
| **Teachworks** | Starter **~$16.49/mo + ~$0.32/student-lesson**; Growth ~$48 + lower per-lesson; Premium ~$188 + ~$0.065 | Usage-based; many integrations; predictable if lesson volume known |

**Neither is primarily an “AI tutor.”** Pair with Claude for lesson planning and parent updates.

### Recommended **independent tutoring** stack

| Layer | Tool | Role |
|-------|------|------|
| Ops | Teachworks (low volume) or TutorCruncher (payouts to many tutors) | Schedule, bill, payroll-ish |
| Lesson design | Claude Pro + MagicSchool or NotebookLM | Plans, worksheets, differentiation |
| Delivery | Zoom / Google Meet + shared Drive | Sessions |
| Student AI policy | Allow Khanmigo/NotebookLM **outside** paid hour for practice; human hour = Socratic + accountability | Avoid “AI does homework” reputation risk |
| Client CRM alternative | HoneyBook if you sell packages more than hourly lessons | Good for premium 1:1 coaching-style tutoring |

**30-day plan for a tutoring SMB:**
1. Pick Teachworks or TutorCruncher; stop spreadsheet booking.  
2. Claude project: subject, grade band, curriculum standards, parent email templates.  
3. Publish a clear AI policy for students/parents (what AI may/may not do).  
4. Productize: diagnostic session + package of 8 sessions (HoneyBook or ops tool invoices).  
5. Optional: Manychat/WhatsApp for trial-lesson booking.

**Still thin in public data:** vertical AI that jointly does **tutoring pedagogy + multi-tutor payroll + parent CRM** as one product. Stack remains the reality.

---

## C. Gap research: Caregiving

Split into **family caregivers** vs **care businesses** (home care agencies, daycare/preschool).

### 1. Family eldercare coordination

| Product | Pricing | AI / features |
|---------|---------|----------------|
| **Caring Village** | Free core; **Circle ~$14.99/mo**; **Village ~$24.99/mo** (also annual App Store SKUs) | Shared calendar, meds, tasks, docs, messaging; **Julia** AI virtual caregiver 24/7 for guidance, resources, next steps (**not** medical/legal/crisis care) |
| **CaringBridge** | Freemium consumer | Updates/journals more than ops |
| **ACL Caregiver AI Prize Challenge** (US HHS ACL, 2026) | Prize / innovation program | Signals public investment in caregiver AI and workforce-extending tools—watch winners for future products |

**Julia positioning:** practical Q&A, insurance navigation hints, local resources, emotional support framing—**not** a clinician.

### 2. Childcare / daycare / preschool businesses

| Product | AI | Pricing notes |
|---------|-----|---------------|
| **Playground (tryplayground.com) + Camber** | **Camber** = AI “employee”: after-hours **voice agent**, enrollment Q&A (pricing, voucher vs private pay, availability), lead capture to CRM, staff queries, marketing help, predictive enrollment themes | **Sales-led / custom pricing** for platform; Camber voice agent marketed in beta/rollout—book demo |
| Generic LLM | ChatGPT for handbook drafts, parent newsletters | Free–$20; no enrollment CRM |

**Wisconsin Early Childhood-style guidance (sector PDFs):** ChatGPT remains the default free tool for providers for writing and planning—not a compliance system.

### 3. Direct care workforce / agency ops
Public consumer pricing is still thin for agency-grade AI scheduling + EVV + caregiver matching. Practical 2026 approach for a small home-care operator:
- Scheduling/payroll: existing home-care software (vertical; demo-led)
- Admin AI: Claude/ChatGPT Business for care-plan drafts (**HIPAA**: use Business/Enterprise tiers, BAAs where required—not consumer chat)
- Family coordination: Caring Village for family side of sandwich generation clients
- Voice intake: generic voice agents or Lindy-class tools only with strict scripts and human escalation

### Recommended stacks

**Family caregiver (consumer):**  
Caring Village Free → Circle if multi-member → Julia for questions; Claude only for non-PHI general research.

**Daycare director:**  
Playground + Camber for enrollment calls; CapCut/Canva for parent marketing; Claude for handbook/policy drafts (human legal review).

**Small home-care agency:**  
Keep certified vertical software for compliance; add **ChatGPT Business / Claude Team** for admin writing; do **not** put client PHI in consumer AI.

**Regulatory caution:** Care and education are high-stakes. AI assistants must escalate emergencies; meds/care plans need licensed human oversight.

---

## D. Gap research: Multi-agent SMB stacks

There is still **no single verified all-in-one** “marketing + sales + ops multi-agent OS” for micro-businesses. What exists is a **layer cake**:

### Layer map

| Layer | Examples | SMB fit |
|-------|----------|---------|
| **Personal agent** | Lindy (~$49.99/mo) | Inbox, calendar, SMS/iMessage; human approve-before-send |
| **Integration agent** | Zapier Agents (platform from ~$19.99/mo annual + task usage) | Best if you already live in Zapier; agents call Zaps as tools |
| **Multi-agent workforce builder** | **Relevance AI** | No-code agent teams with handoffs; GTM/sales heavy |
| **Enterprise low-code agents** | Microsoft Copilot Studio | Best inside M365; 230k+ orgs by Build 2025 |
| **Code-first multi-agent** | CrewAI (OSS; cloud often ~$99+/mo class) | Developers only |
| **Vertical embedded agents** | Shopify Sidekick, GlossGenius AI, Playground Camber, Jasper “100+ agents” | Highest ROI for non-technical owners |

### Relevance AI (primary multi-agent product for ambitious SMBs)

Verified docs pricing (late 2026):

| Plan | Price | Capacity |
|------|-------|----------|
| Free | $0 | 200 Actions/mo; explore marketplace |
| **Pro** | **$19/mo annual** ($29 monthly) | 2,500 Actions/mo; $20 Vendor Credits/mo; 2 build users; BYO LLM; unlimited workforces |
| **Team** | **$234/mo annual** ($349 monthly) | 7,000 Actions/mo; $70 Vendor Credits; calling/meeting agents; 5 build + 45 end users |
| Enterprise | Custom | SSO, RBAC, evals, etc. |
| Top-ups | $80 / 1k Actions; $20 / 10k Vendor Credits | Actions reset; vendor credits roll over while subscribed |

**Fit:** Sales/research/ops sequences (research agent → writer → CRM updater). Overkill for a solo stylist who only needs rebooking texts.

### Practical multi-agent patterns by vertical

| Vertical | Multi-agent pattern that actually works | Tools |
|----------|----------------------------------------|-------|
| Salon | Marketing agent (GG) + DM agent (Manychat) + human stylist | Not Relevance day one |
| Boutique | Sidekick + Klaviyo flows + creative human | Sidekick App Extensions = “agent team” inside Shopify |
| Freelance | Claude for content + HoneyBook automation + Zapier | Lindy if email is the job |
| Tutoring agency | Ops software + Claude lesson agent + human tutors | Relevance only if recruiting/sales is multi-step at volume |
| Daycare | Camber voice + staff AI writing + human director | Playground-native first |
| Growth-stage SMB (sales-led) | Relevance Pro workforce: lead enrich → email draft → human approve | Start Free → Pro |

### When to buy multi-agent platforms vs stay embedded

**Stay embedded (Sidekick / GlossGenius / HoneyBook AI) if:**
- Team < 5  
- Work lives in one vertical system  
- You need reliability over flexibility  

**Add Lindy / Zapier Agents if:**
- Pain is cross-app glue (Gmail ↔ CRM ↔ calendar)  
- You want one assistant, not an agent factory  

**Add Relevance AI (Pro) if:**
- You run repeatable multi-step GTM or ops pipelines  
- You’re willing to design/eval agents and monitor Actions  
- Credit burn is budgeted  

**Avoid CrewAI/Copilot Studio first** unless you have a developer or are already on Microsoft 365 enterprise.

### Governance (Forrester AppGen risk still applies)
- Log every agent that can email/clients  
- Human-in-the-loop for payments, medical, legal, student grades  
- Prefer Business AI tiers for client data  
- Kill zombie Zaps/agents quarterly  

---

## E. Combined “start here” playbooks

### Playbook 1 — Beauty salon (women-led service)
1. GlossGenius Gold  
2. Claude Free/Pro  
3. CapCut + Canva  
4. Manychat Free  
5. Skip multi-agent platforms until Reception GA or call volume is painful  

### Playbook 2 — Fashion boutique on Shopify
1. Shopify Sidekick daily habit  
2. Klaviyo core flows  
3. CapCut + Canva  
4. Manychat for IG  
5. Sidekick ↔ Klaviyo extensions before buying Relevance  

### Playbook 3 — Freelance coach / creative
1. HoneyBook Essentials  
2. Claude Pro  
3. Zapier light  
4. CapCut portfolio  
5. Lindy only if inbox > ~50 actionable threads/day  

### Playbook 4 — Independent tutor
1. Teachworks or TutorCruncher  
2. Claude + NotebookLM for prep  
3. Written student AI policy  
4. Khanmigo as optional student practice, not replacement  
5. HoneyBook if selling premium packages  

### Playbook 5 — Family caregiver (not a business)
1. Caring Village + Julia  
2. Shared meds/calendar discipline  
3. No PHI in consumer ChatGPT  

### Playbook 6 — Daycare / preschool
1. Demo Playground + Camber  
2. Claude for parent comms drafts  
3. Human review on all enrollment promises  

### Playbook 7 — Multi-agent experiment (any vertical, growth stage)
1. Map one pipeline (e.g., lead → research → draft outreach → human send)  
2. Relevance Free prototype → Pro if Actions fit  
3. Or Zapier Agents if stack already on Zapier  
4. Measure hours saved for 2 weeks before expanding agent count  

---

## F. Updated coverage status

| Domain | Status after Part 2 | Residual gaps |
|--------|---------------------|---------------|
| Salon / beauty ops AI | **Strong** | Reception GA date/pricing unknown |
| Shopify boutique AI | **Strong** | Exact Sidekick plan limits vary; verify on plan |
| Freelance client OS + AI | **Strong** | HoneyBook AI feature matrix by tier shifts; verify |
| Tutoring business ops | **Moderate** | Little native AI inside TutorCruncher/Teachworks |
| Student AI tutors | **Moderate** | Crowded; weak business tooling |
| Family caregiving AI | **Moderate** | Caring Village well documented; clinical AI still sparse/publicly cautious |
| Childcare business AI | **Moderate** | Playground/Camber real; list pricing opaque |
| Home-care agency AI | **Weak** | Compliance-heavy; sales-led; not fully mapped |
| Multi-agent SMB platforms | **Stronger** | Relevance + Lindy + Zapier Agents mapped; vertical all-in-ones still stacked |
| Niche styling advisors | **Weak** | Still mostly YouCam + general chat |

---

## G. Source notes (primary / high-value)

- GlossGenius pricing & AI teammates: https://glossgenius.com/pricing  
- Shopify Sidekick: https://www.shopify.com/sidekick (+ Q1 2026 earnings coverage; Spring ’26 app extensions reporting)  
- HoneyBook / Dubsado / 17hats comparisons: vendor blogs & 2026 comparison roundups (verify live pricing)  
- Relevance AI pricing docs: https://relevanceai.com/docs/get-started/pricing  
- Khanmigo pricing: https://www.khanmigo.ai/pricing  
- Caring Village / Julia: https://caringvillage.com/ + App Store IAP tiers  
- Playground Camber: https://www.tryplayground.com/solutions/ai  
- TutorCruncher / Teachworks: vendor pricing & 2026 comparison posts  
- ACL Caregiver AI Prize: https://acl.gov/caregiver-ai-competition  
- Lindy / Zapier Agents: 2026 “best AI agents for SMB” roundups + vendor pricing pages  

**Disclaimer:** Prices and “coming soon” features change quickly. Confirm on vendor sites before purchase. Not medical, legal, or financial advice—especially for care and education use cases.

---

*End of Part 2*
