# Connector Atlas — the use-case catalogue

> Claude is the brain in the centre. Each entry below is a **working** combination: Claude + a set of connectors that cohere into a use case a person would actually want. We surface only what works, name it, and say **why**. Ordered small → huge.


## Small — Claude + 2–5 connectors

### ● Inbox-to-Action Desk  ·  potential 74/100 · 2 connectors · 2/12 domains · strong

*Claude reads what comes in via Gmail and turns it into tracked work in Todoist.*

> potential 74/100 — applicability 25 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Gmail** — email · *source* · uses: read
- **Todoist** — tasks · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Meeting Follow-through  ·  potential 74/100 · 2 connectors · 2/12 domains · strong

*Claude turns Fireflies into follow-ups and records in Todoist.*

> potential 74/100 — applicability 25 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Todoist** — tasks · *sink* · uses: mutate
- **Fireflies** — transcribe_meeting · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Daily Brief  ·  potential 74/100 · 2 connectors · 2/12 domains · strong

*Claude assembles a brief from Gmail into Notion.*

> potential 74/100 — applicability 25 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Gmail** — email · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Knowledge Hub  ·  potential 74/100 · 2 connectors · 2/12 domains · strong

*Claude keeps a living knowledge base in Google Drive, refreshed from Exa.*

> potential 74/100 — applicability 25 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Exa** — web_search · *source* · uses: read
- **Google Drive** — files · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Research Desk  ·  potential 73/100 · 2 connectors · 1/12 domains · strong

*Claude gathers evidence from Exa and writes a durable brief in Notion.*

> potential 73/100 — applicability 25 · leverage 21 · reach 2 · tightness 25

Connectors, and why each earns its place:

- **Exa** — web_search · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Incident War-room  ·  potential 71/100 · 2 connectors · 2/12 domains · strong

*Claude watches Datadog and drives the response through Slack.*

> potential 71/100 — applicability 18 · leverage 25 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Slack** — messaging · *sink* · uses: irreversible
- **Datadog** — observability · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Pipeline Cockpit  ·  potential 70/100 · 2 connectors · 2/12 domains · strong

*Claude keeps the pipeline in HubSpot moving through Klaviyo.*

> potential 70/100 — applicability 18 · leverage 25 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **HubSpot** — crm · *source* · uses: read
- **Klaviyo** — outreach · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Finance Back Office  ·  potential 70/100 · 2 connectors · 2/12 domains · strong

*Claude reconciles money movement in Stripe and reports it through Notion.*

> potential 70/100 — applicability 21 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Stripe** — payments · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Ship-it Dev Loop  ·  potential 69/100 · 2 connectors · 1/12 domains · strong

*Claude reads the repo in Sourcegraph and ships it via Replit.*

> potential 69/100 — applicability 18 · leverage 25 · reach 2 · tightness 25

Connectors, and why each earns its place:

- **Replit** — deploy · *sink* · uses: irreversible
- **Sourcegraph** — code · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Storefront Ops  ·  potential 67/100 · 2 connectors · 2/12 domains · strong

*Claude runs the store in Shop end to end with Stripe.*

> potential 67/100 — applicability 14 · leverage 25 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Shop** — ecommerce · *sink* · uses: irreversible
- **Stripe** — payments · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Recruiting Pipeline  ·  potential 67/100 · 2 connectors · 2/12 domains · strong

*Claude sources and screens in Ashby and moves candidates through Gmail.*

> potential 67/100 — applicability 18 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Ashby** — ats_hiring · *sink* · uses: mutate
- **Gmail** — email · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Content Studio  ·  potential 66/100 · 2 connectors · 2/12 domains · strong

*Claude produces creative in Canva and ships it through Bitly.*

> potential 66/100 — applicability 18 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Canva** — design · *sink* · uses: mutate
- **Bitly** — social_media · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Outbound Sales Desk  ·  potential 65/100 · 2 connectors · 1/12 domains · strong

*Claude sources and enriches leads via ZoomInfo and runs outbound through HubSpot.*

> potential 65/100 — applicability 18 · leverage 21 · reach 2 · tightness 25

Connectors, and why each earns its place:

- **ZoomInfo** — enrich_company, discover_companies · *source* · uses: read
- **HubSpot** — crm · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● Legal Ops  ·  potential 63/100 · 2 connectors · 1/12 domains · strong

*Claude researches and drafts from Harvey and routes for signature via Docusign.*

> potential 63/100 — applicability 11 · leverage 25 · reach 2 · tightness 25

Connectors, and why each earns its place:

- **Harvey** — legal_research · *source* · uses: read
- **Docusign** — esign · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Data-to-Dashboard  ·  potential 62/100 · 2 connectors · 1/12 domains · strong

*Claude queries Snowflake and builds the dashboard in Tableau.*

> potential 62/100 — applicability 18 · leverage 18 · reach 2 · tightness 25

Connectors, and why each earns its place:

- **Tableau** — bi_visualize · *source* · uses: read
- **Snowflake** — database · *sink* · uses: create

**Side effects** (only the verbs this use case actually uses): **create**  ·  read-only footprint: read

### ● Trading Desk  ·  potential 58/100 · 2 connectors · 2/12 domains · strong

*Claude researches markets in FMP and manages the book in Interactive Brokers (IBKR).*

> potential 58/100 — applicability 5 · leverage 25 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **FMP** — market_data · *source* · uses: read
- **Interactive Brokers (IBKR)** — trading · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ◐ Support Desk  ·  potential 44/100 · 2 connectors · 2/12 domains · partial

*Claude resolves tickets in Intercom with context from HubSpot.*

> potential 44/100 — applicability 18 · leverage 8 · reach 3 · tightness 15

Connectors, and why each earns its place:

- **HubSpot** — crm · *source* · uses: read
- **Intercom** — support_desk · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **read**  ·  read-only footprint: read


## Medium — Claude + a whole domain desk

### ● Support Desk  ·  potential 80/100 · 5 connectors · 4/12 domains · strong

*Claude runs a whole Support operation — Email, Chat / messaging, Notes & docs, Support desk, Tasks & projects — coordinating across all of it from the centre.*

> potential 80/100 — applicability 24 · leverage 25 · reach 6 · tightness 25

Connectors, and why each earns its place:

- **Gmail** — email · *source* · uses: read
- **Slack** — messaging · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate
- **Intercom** — support_desk · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Marketing Studio  ·  potential 78/100 · 8 connectors · 4/12 domains · strong

*Claude runs a whole Marketing operation — Email, Forms & surveys, Marketing analytics, Chat / messaging, Notes & docs, Outbound campaigns, Social publishing, Tasks & projects — coordinating across all of it from the centre.*

> potential 78/100 — applicability 21 · leverage 25 · reach 7 · tightness 25

Connectors, and why each earns its place:

- **Bitly** — social_media · *sink* · uses: irreversible
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Notion** — notes_docs · *sink* · uses: mutate
- **Klaviyo** — outreach · *sink* · uses: irreversible
- **Semrush** — marketing_analytics · *source* · uses: read
- **Todoist** — tasks · *sink* · uses: mutate
- **SurveyMonkey** — forms · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Product & Engineering Loop  ·  potential 78/100 · 11 connectors · 5/12 domains · strong

*Claude runs a whole Product & Engineering operation — AI models & agents, Cloud & infrastructure, Code & repos, Database / warehouse, Build & deploy, Email, Identity & compliance, Chat / messaging, Notes & docs, Observability, Security & trust, Tasks & projects — coordinating across all of it from the centre.*

> potential 78/100 — applicability 19 · leverage 25 · reach 9 · tightness 25

Connectors, and why each earns its place:

- **Syntitan** — ai_tools, database · *sink* · uses: mutate
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Replit** — deploy · *sink* · uses: irreversible
- **Vercel** — cloud_infra · *sink* · uses: irreversible
- **Notion** — notes_docs · *sink* · uses: mutate
- **Datadog** — observability · *source* · uses: read
- **Todoist** — tasks · *sink* · uses: mutate
- **Sourcegraph** — code · *sink* · uses: read
- **Snyk Security** — security · *source* · uses: read
- **Clerk** — cloud_infra, identity · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Comms Command Center  ·  potential 78/100 · 6 connectors · 1/12 domains · strong

*Claude runs a whole Comms & Collaboration operation — Calendar, Local machine / OS, Email, Files & storage, Chat / messaging, Meeting transcription — coordinating across all of it from the centre.*

> potential 78/100 — applicability 25 · leverage 25 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Fireflies** — transcribe_meeting · *source* · uses: read
- **Filesystem** — desktop · *sink* · uses: mutate
- **Google Drive** — files · *sink* · uses: mutate
- **Google Calendar** — calendar · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Legal Ops  ·  potential 77/100 · 6 connectors · 4/12 domains · strong

*Claude runs a whole Legal operation — Email, E-signature, Legal research, Chat / messaging, Notes & docs, Tasks & projects — coordinating across all of it from the centre.*

> potential 77/100 — applicability 20 · leverage 25 · reach 6 · tightness 25

Connectors, and why each earns its place:

- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Harvey** — legal_research · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate
- **Docusign** — esign · *sink* · uses: irreversible

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Operations Hub  ·  potential 76/100 · 10 connectors · 3/12 domains · strong

*Claude runs a whole Operations & Logistics operation — Automation hub, Browser automation, E-commerce store, Email, Local services, Chat / messaging, Notes & docs, Tasks & projects, Travel & booking, Vertical platform — coordinating across all of it from the centre.*

> potential 76/100 — applicability 20 · leverage 25 · reach 6 · tightness 25

Connectors, and why each earns its place:

- **G2** — vertical · *source* · uses: read
- **Make** — automate_hub · *source* · uses: read
- **Uber** — travel_booking · *source* · uses: read
- **Shop** — ecommerce · *sink* · uses: irreversible
- **Apify** — browser · *source* · uses: read
- **Gmail** — email · *source* · uses: read
- **Slack** — messaging · *source* · uses: read
- **Strava** — local_services · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Sales Desk  ·  potential 75/100 · 6 connectors · 4/12 domains · strong

*Claude runs a whole Sales operation — CRM, Lead discovery, Email, Company enrichment, Chat / messaging, Notes & docs, Tasks & projects — coordinating across all of it from the centre.*

> potential 75/100 — applicability 22 · leverage 25 · reach 6 · tightness 21

Connectors, and why each earns its place:

- **Clay** — enrich_company, discover_companies · *source* · uses: read
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Notion** — notes_docs · *sink* · uses: mutate
- **HubSpot** — crm · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate

Left out (and why):
- ~~ZoomInfo~~ — redundant: enrich_company, discover_companies already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Data & BI Cockpit  ·  potential 75/100 · 8 connectors · 4/12 domains · strong

*Claude runs a whole Data & BI operation — BI & dashboards, Database / warehouse, Email, Market & financial data, Chat / messaging, Notes & docs, Tasks & projects, Weather & geospatial — coordinating across all of it from the centre.*

> potential 75/100 — applicability 18 · leverage 25 · reach 7 · tightness 25

Connectors, and why each earns its place:

- **FMP** — market_data · *source* · uses: read
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Notion** — notes_docs · *sink* · uses: mutate
- **Tableau** — bi_visualize · *sink* · uses: read
- **Todoist** — tasks · *sink* · uses: mutate
- **Snowflake** — database · *sink* · uses: create
- **TomTom Maps** — weather_geo · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Finance Back Office  ·  potential 74/100 · 7 connectors · 4/12 domains · strong

*Claude runs a whole Finance & Accounting operation — Accounting, Email, Invoicing, Chat / messaging, Notes & docs, Payments, Tasks & projects, Trading & investing — coordinating across all of it from the centre.*

> potential 74/100 — applicability 20 · leverage 25 · reach 7 · tightness 22

Connectors, and why each earns its place:

- **Sequence** — accounting, invoicing · *sink* · uses: irreversible
- **Gmail** — email · *source* · uses: read
- **Slack** — messaging · *source* · uses: read
- **Stripe** — payments · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate
- **Interactive Brokers (IBKR)** — trading · *source* · uses: read

Left out (and why):
- ~~Xero~~ — redundant: accounting already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Creative Studio  ·  potential 74/100 · 8 connectors · 4/12 domains · strong

*Claude runs a whole Design & Creative operation — Design & brand, Diagrams & whiteboards, Email, Media generation, Chat / messaging, Notes & docs, Presentations, Tasks & projects — coordinating across all of it from the centre.*

> potential 74/100 — applicability 21 · leverage 21 · reach 7 · tightness 25

Connectors, and why each earns its place:

- **Canva** — design · *sink* · uses: mutate
- **Figma** — diagramming · *source* · uses: read
- **Gamma** — presentations · *sink* · uses: mutate
- **Gmail** — email · *source* · uses: read
- **Slack** — messaging · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate
- **ElevenLabs** — media_gen · *sink* · uses: mutate

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read

### ● People & Hiring Ops  ·  potential 73/100 · 6 connectors · 4/12 domains · strong

*Claude runs a whole HR & Recruiting operation — Recruiting / ATS / HRIS, Email, Job market, Chat / messaging, Notes & docs, Payroll & benefits, Tasks & projects — coordinating across all of it from the centre.*

> potential 73/100 — applicability 20 · leverage 25 · reach 6 · tightness 21

Connectors, and why each earns its place:

- **Gusto** — ats_hiring, payroll · *sink* · uses: irreversible
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Indeed** — job_search · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate

Left out (and why):
- ~~Ashby~~ — redundant: ats_hiring already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Research Desk  ·  potential 64/100 · 6 connectors · 1/12 domains · strong

*Claude runs a whole Research & Knowledge operation — Learning & courses, Knowledge & memory, Notes & docs, Public / gov data, Scientific research, Web search — coordinating across all of it from the centre.*

> potential 64/100 — applicability 15 · leverage 21 · reach 3 · tightness 25

Connectors, and why each earns its place:

- **Exa** — web_search · *source* · uses: read
- **Mem0** — knowledge_base · *sink* · uses: mutate
- **PubMed** — research_science · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **O'Reilly** — education · *sink* · uses: read
- **Anthropic Economic Index** — public_data · *source* · uses: read

**Side effects** (only the verbs this use case actually uses): **mutate**  ·  read-only footprint: read


## Large — Claude + a big combination that can run like a company

### ★ ● Runs like a company  ·  potential 90/100 · 47 connectors · 12/12 domains · strong

*The functional surface of a whole operation: Claude + a connector for every capability across all twelve domains, with Claude orchestrating between every part. Spans 12 of 12 domains (Product & Engineering, Operations & Logistics, Comms & Collaboration, Research & Knowledge, Finance & Accounting, Data & BI, Design & Creative, Marketing, HR & Recruiting, Sales, Legal, Support).*

> potential 90/100 — applicability 17 · leverage 25 · reach 25 · tightness 23

> scale: 51 connectors in · 47 kept as the coherent core · 12/12 domains.

Connectors, and why each earns its place:

- **Clay** — enrich_company, discover_companies · *source* · uses: read
- **Gusto** — ats_hiring, payroll · *sink* · uses: irreversible
- **Sequence** — accounting, invoicing · *sink* · uses: irreversible
- **Syntitan** — ai_tools, database · *sink* · uses: mutate
- **G2** — vertical · *sink* · uses: read
- **FMP** — market_data · *source* · uses: read
- **Exa** — web_search · *source* · uses: read
- **Make** — automate_hub · *sink* · uses: irreversible
- **Uber** — travel_booking · *sink* · uses: irreversible
- **Shop** — ecommerce · *sink* · uses: irreversible
- **Mem0** — knowledge_base · *sink* · uses: mutate
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Apify** — browser · *sink* · uses: irreversible
- **Bitly** — social_media · *sink* · uses: irreversible
- **Canva** — design · *sink* · uses: mutate
- **Figma** — diagramming · *sink* · uses: create
- **Gamma** — presentations · *sink* · uses: mutate
- **Strava** — local_services · *sink* · uses: irreversible
- **Stripe** — payments · *sink* · uses: irreversible
- **Replit** — deploy · *sink* · uses: irreversible
- **Vercel** — cloud_infra · *sink* · uses: irreversible
- **Indeed** — job_search · *source* · uses: read
- **Harvey** — legal_research · *source* · uses: read
- **PubMed** — research_science · *source* · uses: read
- **Notion** — notes_docs · *sink* · uses: mutate
- **Todoist** — tasks · *sink* · uses: mutate
- **HubSpot** — crm · *sink* · uses: mutate
- **Klaviyo** — outreach · *sink* · uses: irreversible
- **Semrush** — marketing_analytics · *source* · uses: read
- **Datadog** — observability · *source* · uses: read
- **Tableau** — bi_visualize · *sink* · uses: read
- **Intercom** — support_desk · *sink* · uses: irreversible
- **Docusign** — esign · *sink* · uses: irreversible
- **O'Reilly** — education · *sink* · uses: read
- **Fireflies** — transcribe_meeting · *source* · uses: read
- **Filesystem** — desktop · *sink* · uses: mutate
- **ElevenLabs** — media_gen · *sink* · uses: mutate
- **Sourcegraph** — code · *sink* · uses: read
- **TomTom Maps** — weather_geo · *source* · uses: read
- …and 7 more

Left out (and why):
- ~~ZoomInfo~~ — redundant: enrich_company, discover_companies already covered — kept only as a fallback.
- ~~Xero~~ — redundant: accounting already covered — kept only as a fallback.
- ~~Ashby~~ — redundant: ats_hiring already covered — kept only as a fallback.
- ~~Snowflake~~ — redundant: database already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● Back-Office Operation  ·  potential 79/100 · 25 connectors · 7/12 domains · strong

*Claude runs the back office — books and payments, people and payroll, contracts and the data behind them — from one seat. Spans 7 of 12 domains (Operations & Logistics, Comms & Collaboration, Finance & Accounting, Data & BI, HR & Recruiting, Legal, Research & Knowledge).*

> potential 79/100 — applicability 17 · leverage 25 · reach 15 · tightness 22

> scale: 29 connectors in · 25 kept as the coherent core · 7/12 domains.

Connectors, and why each earns its place:

- **Gusto** — ats_hiring, payroll · *sink* · uses: irreversible
- **Sequence** — accounting, invoicing · *sink* · uses: irreversible
- **G2** — vertical · *sink* · uses: read
- **FMP** — market_data · *source* · uses: read
- **Make** — automate_hub · *sink* · uses: irreversible
- **Uber** — travel_booking · *sink* · uses: irreversible
- **Shop** — ecommerce · *sink* · uses: irreversible
- **Apify** — browser · *sink* · uses: irreversible
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Asana** — tasks · *sink* · uses: mutate
- **Stripe** — payments · *sink* · uses: irreversible
- **Indeed** — job_search · *source* · uses: read
- **Harvey** — legal_research · *source* · uses: read
- **Strava** — local_services · *sink* · uses: irreversible
- **Notion** — notes_docs · *sink* · uses: mutate
- **Tableau** — bi_visualize · *sink* · uses: read
- **Docusign** — esign · *sink* · uses: irreversible
- **Fireflies** — transcribe_meeting · *source* · uses: read
- **Snowflake** — database · *sink* · uses: create
- **Filesystem** — desktop · *sink* · uses: mutate
- **TomTom Maps** — weather_geo · *source* · uses: read
- **Google Drive** — files · *sink* · uses: mutate
- **Google Calendar** — calendar · *sink* · uses: mutate
- **Interactive Brokers (IBKR)** — trading · *sink* · uses: irreversible

Left out (and why):
- ~~Xero~~ — redundant: accounting already covered — kept only as a fallback.
- ~~Ashby~~ — redundant: ats_hiring already covered — kept only as a fallback.
- ~~Resend~~ — redundant: email already covered — kept only as a fallback.
- ~~Todoist~~ — redundant: tasks already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

### ● GTM Engine  ·  potential 78/100 · 20 connectors · 6/12 domains · strong

*Claude runs the whole go-to-market motion — lead discovery, CRM, outbound, support and the money — as one system it coordinates end to end. Spans 6 of 12 domains (Comms & Collaboration, Finance & Accounting, Data & BI, Marketing, Sales, Support).*

> potential 78/100 — applicability 18 · leverage 25 · reach 12 · tightness 23

> scale: 22 connectors in · 20 kept as the coherent core · 6/12 domains.

Connectors, and why each earns its place:

- **Clay** — enrich_company, discover_companies · *source* · uses: read
- **Sequence** — accounting, invoicing · *sink* · uses: irreversible
- **FMP** — market_data · *source* · uses: read
- **Bitly** — social_media · *sink* · uses: irreversible
- **Gmail** — email · *sink* · uses: irreversible
- **Slack** — messaging · *sink* · uses: irreversible
- **Stripe** — payments · *sink* · uses: irreversible
- **HubSpot** — crm · *sink* · uses: mutate
- **Klaviyo** — outreach · *sink* · uses: irreversible
- **Semrush** — marketing_analytics · *source* · uses: read
- **Tableau** — bi_visualize · *sink* · uses: read
- **Intercom** — support_desk · *sink* · uses: irreversible
- **Fireflies** — transcribe_meeting · *source* · uses: read
- **Snowflake** — database · *sink* · uses: create
- **Filesystem** — desktop · *sink* · uses: mutate
- **TomTom Maps** — weather_geo · *source* · uses: read
- **SurveyMonkey** — forms · *source* · uses: read
- **Google Drive** — files · *sink* · uses: mutate
- **Google Calendar** — calendar · *sink* · uses: mutate
- **Interactive Brokers (IBKR)** — trading · *sink* · uses: irreversible

Left out (and why):
- ~~ZoomInfo~~ — redundant: enrich_company, discover_companies already covered — kept only as a fallback.
- ~~Xero~~ — redundant: accounting already covered — kept only as a fallback.

**Side effects** (only the verbs this use case actually uses): **irreversible**  ·  read-only footprint: read

