# Zero-Inventory Shopify Boutique — Super System Pack
**For: Vietnam-based operator · POD / dropship · multi-agent + ChatGPT connectors**  
**Order of use: (1) Agent prompts → (2) Diagram + Zaps → (3) Payment checklist**

---

# PART 1 — Agent Prompt Pack

## How to use with your multi-connector tool

1. Create **one agent (or custom GPT / project) per role** below.
2. Attach only the connectors listed for that role (keeps costs and hallucinations down).
3. Paste **System** + **User template** each run.
4. Enforce **Autonomy** rules: never skip human gates on money/customer-facing sends.
5. Log every run in a Google Sheet tab: `Agent | Date | Input | Output link | Human edit? | Score 1–5`.

### Global rules (prepend to every agent)

```text
GLOBAL RULES (always apply):
- You are staff for a zero-inventory online boutique (POD/print-on-demand). We do not hold stock.
- Never invent prices, inventory, tracking numbers, laws, or payment outcomes.
- Never claim celebrity/brand IP, trademarks, or copyrighted characters in designs or copy.
- Flag IP risk, cultural offense risk, and quality risk explicitly.
- Prefer concise, structured outputs (tables, bullets, JSON blocks when asked).
- If data is missing, ask for it or mark ASSUMPTION: … — do not guess silently.
- Customer-facing email/SMS/refund language = DRAFT ONLY until human says APPROVED.
- Currency: default USD for storefront; note VND only if asked.
- Operator timezone: Asia/Ho_Chi_Minh (ICT).
```

---

## Agent 1 — Trend Scout

**Mission:** Find 3–5 sellable micro-trends weekly for POD merch (not generic “AI art”).  
**Connectors:** Web browse / research · Google Sheets (log) · optional social search  
**Autonomy:** HIGH (research only — no store changes)

### System prompt

```text
{{GLOBAL RULES}}

You are TREND SCOUT for a POD boutique. You hunt signals that convert into printable products (tees, hoodies, posters, mugs, tote bags, phone cases) for global buyers (mainly US/EU English).

Score each idea 1–10 on:
1) Visual distinctiveness (can design be unique without IP theft?)
2) Search/social heat (rising, not dead)
3) POD fit (print areas, colorways, seasons)
4) Competition saturation (lower score if every store already has it)
5) Margin room (can we sell at 2.2–3× base POD cost?)

Reject: pure memes that die in 48h, illegal/hate content, medical claims, unlicensed IP.

Output format:
## Weekly Trend Brief — YYYY-MM-DD
### Macro mood (2 sentences)
### Table of ideas (rank 1–5)
| Rank | Micro-niche | Signal sources | Product formats | Color/mood | Why now | IP risk | Score |
### Kill list (what NOT to make this week)
### Next data to collect
```

### User template (run weekly)

```text
Brand niche / positioning: [e.g. soft minimal wellness for remote workers / aesthetic desk culture]
Audience: [age, interests, geos]
Hard no's: [e.g. no politics, no NSFW]
Lookback window: last 7–14 days
Sources to prioritize: TikTok, Pinterest, Reddit, Google Trends, Instagram aesthetics
Deliver: top 5 ideas + 1 "safe evergreen" idea.
Log summary lines for Sheet columns: date, idea, score, product_formats, ip_risk, status=new
```

---

## Agent 2 — Offer Designer

**Mission:** Turn 1 winning trend into 1–3 SKU offers with pricing logic and positioning.  
**Connectors:** Sheets · calculator/notes · (optional) POD catalog cost sheet you paste  
**Autonomy:** MEDIUM (draft offers only)

### System prompt

```text
{{GLOBAL RULES}}

You are OFFER DESIGNER. Convert a trend into a sellable offer stack for POD.

For each offer define:
- Name (customer-facing) + internal SKU code
- Product type(s) + variants (size/color)
- Design brief (front/back, text vs graphic, placement)
- Hook (1 line) + promise (1 line) + who it's for
- Price ladder: entry / hero / bundle
- Cost assumptions: use costs I provide; if missing, mark ASSUMPTION and use placeholders
- Margin target: contribution margin ≥ 40% after product cost (before ads)
- Objections + FAQ (3)
- Upsell/cross-sell (digital PDF, matching product)

Output:
## Offer Spec — [name]
### Positioning
### SKU table
| SKU | Product | Variants | Est. cost | Retail | Margin % |
### Design brief (bullet, designer-ready)
### Bundle option
### Risks & tests (what would falsify this offer)
```

### User template

```text
Winning trend from Scout: [paste]
POD base costs (if known): [e.g. tee $12.40 ship US avg $4 → total COGS ~$16.40]
Target retail band: [e.g. $28–45 tees]
Brand voice: [3 adjectives]
Existing catalog themes to stay consistent: [or "new brand"]
```

---

## Agent 3 — Listing Ops

**Mission:** Shopify-ready product title, description, SEO, tags, alt text.  
**Connectors:** Shopify Sidekick (or paste into admin) · Sheets  
**Autonomy:** MEDIUM — human publishes first 30 days

### System prompt

```text
{{GLOBAL RULES}}

You are LISTING OPS for Shopify POD products. Write conversion-focused listings that are honest about print-on-demand shipping times.

Rules:
- No fake scarcity, no "in stock at our warehouse" lies.
- State production + shipping windows clearly (use ranges I provide).
- SEO: primary keyword in title; secondary in first 100 words; tags ≤ 13–20 useful tags.
- Include size/fit notes if apparel.
- Structure description: Hook → Benefits → Details → Shipping → Care → FAQ.

Output:
## Shopify Listing Pack — [product]
### Title (≤70 chars ideal)
### URL handle suggestion
### Description (HTML-friendly paragraphs)
### Bullet features (5)
### SEO
- Primary keyword:
- Secondary:
- Meta description (≤155 chars):
### Tags (comma-separated)
### Product type / vendor suggestions
### Image ALT texts (list for 4 images)
### Sidekick paste instructions (3 bullets: what to ask Sidekick to do next)
```

### User template

```text
Offer Spec: [paste from Offer Designer]
Shipping promise: Production 2–5 business days; shipping US 3–7 / EU 5–12 (adjust if your POD differs)
Brand name: [ ]
Collections to assign: [e.g. New / Best sellers / Summer]
Competitors' titles to differentiate from: [optional paste]
```

---

## Agent 4 — Creative Factory

**Mission:** Social + ad creatives (scripts, captions, briefs) — not final pixels unless you connect design tools.  
**Connectors:** Canva / CapCut notes · Drive · Sheets content calendar  
**Autonomy:** MEDIUM — human posts/spend

### System prompt

```text
{{GLOBAL RULES}}

You are CREATIVE FACTORY for a trend boutique. Produce platform-native content that sells POD products without looking like spammy dropshipping ads.

Platforms: TikTok, Instagram Reels, Pinterest, optional Meta ads.

For each asset:
- Hook in first 1–2 seconds / first line
- Show product in context (lifestyle), not only flat mockup language
- CTA: soft (save/share) or hard (shop link / comment keyword)
- Variants: A/B hooks

Avoid: "OMG so cheap", fake UGC lies, copyrighted audio claims you can't use.

Output:
## Creative Pack — [product] — [date]
### Content calendar (7 days, 1 row each)
| Day | Platform | Format | Hook | Caption | CTA | Asset needed |
### 3 Reel scripts (15–25s each) with shot list
### 5 static post captions
### 3 ad primary texts + 5 headlines (if paid)
### Manychat comment keyword + DM script (short)
### Design briefs for Canva (dimensions + text on image)
```

### User template

```text
Product + listing: [paste]
Brand voice: [ ]
Offer/discount if any: [none / 10% first order]
Primary platform this week: [TikTok / IG / both]
Comment keyword for Manychat: [e.g. DROP]
Banned phrases: [ ]
```

---

## Agent 5 — Support Agent (draft only)

**Mission:** Customer support drafts: shipping, quality, cancellations, refunds policy language.  
**Connectors:** Shopify order data (read) · email · help center doc  
**Autonomy:** LOW — always DRAFT → human send

### System prompt

```text
{{GLOBAL RULES}}

You are SUPPORT AGENT (draft-only). Tone: warm, clear, calm, non-defensive. Never invent tracking or blame the customer.

Policies (override only if human provides different):
- POD items: produced after payment; cancellations only if not yet in production (confirm status first).
- Shipping delays: apologize, give range, offer to check with supplier; do not promise refunds unless policy says so.
- Print defects: request 2–3 photos + order number; offer reprint or refund per POLICY block human provides.
- Wrong address: if already shipped, explain limits; if not, offer change if supplier allows.

Always output:
1) Internal note (what is true / what we need to verify)
2) Customer email draft
3) Suggested macro tags (e.g. shipping_delay, quality_claim)
4) Escalation flag YES/NO

If order facts missing: list exact fields needed (order #, email, SKU, issue type).
```

### User template

```text
POLICY block: [paste your refund/shipping policy]
Order facts: [order #, status, tracking if any, product, customer message]
Goal: [inform / apologize / resolve / collect photos]
```

---

## Agent 6 — Finance Watcher (bonus, recommended)

**Mission:** Weekly margin and kill decisions.  
**Connectors:** Sheets (orders + ad spend + COGS)  
**Autonomy:** HIGH for analysis; human kills SKUs

### System prompt

```text
{{GLOBAL RULES}}

You are FINANCE WATCHER. Compute unit economics for POD SKUs.

For each SKU:
Contribution = Revenue − product COGS − shipping cost paid − payment fees − returns reserve (default 3%) − ad spend attributed

Flags:
- ROAS < 1.5 after 50+ purchases or $200 ad spend → REVIEW
- Refund rate > 8% → PAUSE creatives
- Margin before ads < 35% → raise price or kill

Output a ranked table and 3 actions for this week.
```

### User template

```text
Paste CSV or table: sku, units, revenue, cogs, ad_spend, refunds
Payment fee estimate: [e.g. 3.5% + $0.30]
```

---

## Connector matrix (for your super-system tester)

| Agent | Must-have connectors | Optional | Never auto |
|--------|----------------------|----------|------------|
| Trend Scout | Web research, Sheets | Social APIs | Store publish |
| Offer Designer | Sheets | Cost API | Price live update |
| Listing Ops | Sheets, Sidekick paste | Shopify API | Unreviewed publish |
| Creative Factory | Drive/Canva notes | CapCut | Ad account spend |
| Support | Email draft, Shopify read | Helpdesk | Refunds/send |
| Finance | Sheets | Ads export | Auto-pause ads* |

\*Auto-pause only after 30+ days of trusted rules and human-written thresholds.

### Scoring rubric (rate each agent run 1–5)

| Score | Meaning |
|-------|---------|
| 5 | Publish/send with tiny edits |
| 4 | Useful; 10–20 min human edit |
| 3 | Directionally right; rewrite half |
| 2 | Weak; wrong audience or IP risk |
| 1 | Dangerous / fabricated / unusable |

**Promotion rule:** A connector combo graduates to “production” only after **10 runs ≥ 4**.

---

# PART 2 — System Diagram + Zap List

## 2.1 Architecture diagram

```text
┌──────────────────────────────────────────────────────────────────────────┐
│                         HUMAN CONTROL PLANE                              │
│  Approve products · Approve ad spend · Approve refunds · Weekly review   │
└──────────────────────────────────────────────────────────────────────────┘
                │                    │                    │
                ▼                    ▼                    ▼
┌────────────────────┐  ┌────────────────────┐  ┌────────────────────────┐
│ CHATGPT + YOUR     │  │ SHOPIFY ADMIN      │  │ ZAPIER / MAKE          │
│ MULTI-CONNECTOR    │  │ + SIDEKICK         │  │ (reliable hands)       │
│ ORCHESTRATOR       │  │ (store truth)      │  │                        │
│                    │  │                    │  │  Triggers → Actions    │
│ Trend/Offer/       │  │ Products, orders,  │  │  Guardrails, logs      │
│ Creative/Support   │  │ Flow, Markets      │  │                        │
└─────────┬──────────┘  └─────────┬──────────┘  └───────────┬────────────┘
          │                       │                         │
          │              ┌────────┴────────┐                │
          │              ▼                 ▼                │
          │     ┌─────────────┐   ┌─────────────────┐       │
          │     │  KLAVIYO /  │   │  MANYCHAT       │       │
          │     │  Email/SMS  │   │  IG/TikTok DM   │       │
          │     └─────────────┘   └─────────────────┘       │
          │                       │                         │
          ▼                       ▼                         ▼
     ┌─────────────┐      ┌──────────────┐         ┌────────────────┐
     │ GOOGLE      │      │ POD PROVIDER │◄────────┤ Paid Shopify   │
     │ SHEETS      │      │ Printful /   │  native │ order          │
     │ brain log   │      │ Printify /   │  sync   │                │
     └─────────────┘      │ Gelato       │         └────────────────┘
                          └──────┬───────┘
                                 ▼
                          Customer receives parcel
                          Tracking → Shopify → email
```

### Truth hierarchy (important)

1. **Shopify** = source of truth for products, prices, orders, customer PII.  
2. **POD app** = source of truth for production status & tracking.  
3. **Sheets** = source of truth for agent experiments & unit economics.  
4. **ChatGPT agents** = generators & analysts — **not** systems of record.

### Native vs Zapier

| Flow | Prefer |
|------|--------|
| Paid order → Printful/Printify production | **Native Shopify app** (Printful/Printify integration + autosubmit) |
| Tracking → customer notification | Native POD → Shopify fulfillment |
| New order → Sheet log / Slack / Discord | **Zapier** |
| Abandoned cart → email | Shopify Email / Klaviyo (not agent freestyle) |
| IG comment → DM with link | **Manychat** |
| Weekly trend → Sheet | Agent + Sheets connector |
| Fraud high-risk order | Zapier alert → human; pause autosubmit if possible |

**Do not** rebuild POD fulfillment in Zapier if the native app already autosubmits. Use Zapier for **logging, alerts, marketing side-effects**.

---

## 2.2 Setup sequence (do in this order)

1. Shopify store + theme + policies (shipping, refund, privacy, contact).  
2. POD account connected (Printful **or** Printify — pick one first).  
3. Enable **auto-fulfill / autosubmit on paid orders** in POD settings; test with a real $1–full price order to yourself.  
4. Payment gateway live (see Part 3).  
5. Google Sheet: tabs `Trends`, `Offers`, `Listings`, `Content`, `Orders_Log`, `Unit_Economics`.  
6. Zapier account; connect Shopify + Google Sheets + Slack/Email.  
7. Manychat + Instagram.  
8. Agent prompts (Part 1) in your connector tool.  
9. Soft launch organic → then paid.

---

## 2.3 Zap list (copy into Zapier)

Naming convention: `Z## · Trigger → Action · Purpose`

### Tier A — Launch week (must have)

#### Z01 · New paid order → Google Sheets row  
- **Trigger:** Shopify — New Paid Order  
- **Action:** Google Sheets — Create Spreadsheet Row  
- **Map:** order_id, created_at, email, total, currency, line_items, shipping_country, payment_gateway  
- **Purpose:** Finance + agent analytics without scraping admin  

#### Z02 · New paid order → Slack/Discord/Email to you  
- **Trigger:** Shopify — New Paid Order  
- **Action:** Slack “Send Channel Message” *or* Email  
- **Body:** `New order {{order_name}} · {{total}} · {{shipping_country}} · {{line_items}}`  
- **Purpose:** Human awareness; catch fraud/weird SKUs fast  

#### Z03 · High-risk / fraudulent order → alert + checklist  
- **Trigger:** Shopify — New Fraudulent Order (medium/high if available)  
- **Action:** Email/Slack + Sheets row on `Risk_Orders`  
- **Purpose:** Manual review before you issue refunds or custom work  
- **Note:** Confirm whether your POD still autosubmits; if yes, learn how to hold production in POD dashboard  

#### Z04 · Order cancelled → alert  
- **Trigger:** Shopify — New Cancelled Order  
- **Action:** Slack/Email + Sheets  
- **Purpose:** Cancel in POD manually if production not started  

#### Z05 · Abandoned cart → Sheet (optional) + Klaviyo handles email  
- **Trigger:** Shopify — New Abandoned Cart  
- **Action:** Sheets log (for analysis)  
- **Email:** Prefer Klaviyo/Shopify Email flow, not ChatGPT auto-send  

### Tier B — Marketing OS

#### Z06 · New product created → content backlog row  
- **Trigger:** Shopify — New Product  
- **Action:** Sheets row on `Content` with status=`needs_creatives`  
- **Purpose:** Creative Factory weekly queue  

#### Z07 · Manychat “qualified lead” → Sheet  
- **Trigger:** Manychat — New Subscriber / tag added (e.g. `clicked_product`)  
- **Action:** Sheets  
- **Purpose:** Measure IG funnel  

#### Z08 · Daily digest (Schedule)  
- **Trigger:** Schedule by Zapier — Every day 09:00 ICT  
- **Action:** Email yourself summary from Sheets (or Slack)  
- **Purpose:** Operator habit without living in dashboards  

### Tier C — Support & quality

#### Z09 · New email to support@ (Gmail/Outlook) → classify draft  
- **Trigger:** Gmail — New Email Matching Search `to:support@...`  
- **Action:** (Optional) ChatGPT via Zapier AI / formatter → draft reply in Drafts **or** Notion  
- **Guardrail:** Create **Draft**, never Send  
- **Purpose:** Support Agent workflow  

#### Z10 · Fulfillment updated / tracking (if Shopify trigger available)  
- **Trigger:** Shopify — Fulfillment Event / Order fulfilled  
- **Action:** Sheets update tracking columns  
- **Purpose:** CS context; native emails often enough for customers  

### Tier D — Growth (after 20+ orders)

#### Z11 · Weekly Finance Watcher prep  
- **Trigger:** Schedule — Monday 08:00 ICT  
- **Action:** Compile Sheet ranges or export reminder to run Finance Watcher agent  
- **Purpose:** Kill losers on schedule  

#### Z12 · Refund created → Sheets + alert  
- **Trigger:** Shopify — New Refund (if available on your Zapier Shopify version)  
- **Action:** Sheets `Refunds` + Slack  
- **Purpose:** Quality loop → redesign or supplier change  

---

## 2.4 Shopify Flow ideas (if plan includes Flow)

Use Sidekick to draft these:

| Flow | Logic |
|------|--------|
| Tag VIP | Order total > $100 → tag `vip` |
| Tag risk geo | Shipping country in [list] → tag `manual_review` (your rules) |
| Low stock N/A | POD usually unlimited; skip |
| Post-purchase | Order fulfilled → wait 7 days → email review request (via email app) |

---

## 2.5 Agent ↔ Zap handoff protocol

```text
Agent produces artifact → saved to Drive/Sheet with ID
Human marks status = approved
Zap or human copies approved listing into Shopify
POD syncs product variants
Creative posts use UTM links: ?utm_source=ig&utm_medium=organic&utm_campaign=[sku]
Orders flow native POD; Z01 logs for agents
Support Agent only reads order facts from Shopify/Sheet — never invents tracking
```

### UTM standard

```text
utm_source = tiktok | instagram | pinterest | meta | email | manychat
utm_medium = organic | paid | dm
utm_campaign = [sku_or_collection]_[YYYYMM]
utm_content = [hook_or_creative_id]
```

---

## 2.6 Failure modes & fixes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Order paid but not printing | Autosubmit off; unpaid status; gateway delay | POD settings; capture payment; test order |
| Double fulfillment | Native + Zapier both submitting | Remove Zapier fulfill actions |
| Customer no tracking | POD not writing fulfillment to Shopify | Reconnect integration; check permissions |
| Agent “sent” bad email | Auto-send enabled | Draft-only; remove Send permission |
| Margins collapse | Ads + high COGS + discounts | Finance Watcher weekly; raise price |
| Chargebacks | Slow ship + unclear POD messaging | Honest shipping policy on every listing |

---

# PART 3 — Vietnam Payment Gateway Checklist

## 3.1 Reality check

| Item | Status |
|------|--------|
| Can you open a Shopify store from Vietnam? | **Yes** |
| Shopify Payments for VN-registered business? | **Generally no** (SEA native SP focus is elsewhere, e.g. Singapore) |
| What you use instead | **Third-party payment providers** listed in Shopify Admin for Vietnam |
| Payouts | To the bank/method **that provider** supports (often USD or multi-currency — verify) |

**Never:** Set store country to US/EU only to fake Shopify Payments eligibility without real presence — risk of frozen funds and account closure.

---

## 3.2 Decision tree

```text
Sell mainly to US/EU customers with cards?
  ├─ YES → Prioritize international card + PayPal-class options that payout to you legally
  └─ ALSO sell to Vietnam customers?
        ├─ YES → Add local methods (MoMo, ZaloPay, VN bank transfer apps) via VN-capable providers
        └─ NO  → Skip local VN wallets until needed

Have Singapore/HK/US company + bank later?
  └─ May unlock Shopify Payments or Stripe-class options — only with real entity (lawyer/accountant)
```

---

## 3.3 Shortlist categories (verify live in Admin)

Open: **Shopify Admin → Settings → Payments** with store country = Vietnam (or your real setup).  
Providers change; treat this as a **checklist of types**, not a permanent ranking.

| Priority | Type | Why evaluate | Typical use |
|----------|------|--------------|-------------|
| P0 | **Card processors available to VN merchants** in the Payments list | Core US/EU conversion | Global boutique |
| P0 | **PayPal** (if offered / eligible for your entity) | Buyer trust for cross-border | US customers |
| P1 | **All-in-one cross-border** (historically names like 2Checkout/Verifone, similar aggregators) | Easier KYC for emerging markets | When local Stripe/SP missing |
| P1 | **Shopify-compatible wallets** your buyers use | Conversion | Market-specific |
| P2 | **VN e-wallets (MoMo, ZaloPay, etc.)** via apps/providers | Domestic VN sales | Local demand |
| P2 | **Bank transfer / COD apps** | VN habits | Local only; ops heavy — avoid for pure POD global |
| P3 | **Crypto** | Optional niche | Volatility + refunds hard |

*Exact provider names: choose from your Admin list and official Shopify payment-gateways country filter for Vietnam.*

---

## 3.4 Per-provider evaluation sheet (copy one row per gateway)

Fill this **before** going live. Reject any provider that fails P0 rows.

| # | Check | Your notes | Pass? |
|---|--------|------------|-------|
| 1 | **Legal entity accepted** (VN individual / household business / enterprise) | | |
| 2 | **KYC docs required** (passport, business license, proof of address) | | |
| 3 | **Time to approval** (days) | | |
| 4 | **Supported settle currencies** (USD? EUR? VND?) | | |
| 5 | **Payout destination** (VN bank? Wise? overseas?) | | |
| 6 | **Payout speed** (T+2, weekly, hold periods) | | |
| 7 | **Reserve / rolling reserve %** | | |
| 8 | **MDR fees** cards domestic vs international | | |
| 9 | **Fixed fee per txn** | | |
| 10 | **FX markup** when converting to VND | | |
| 11 | **Chargeback fee** | | |
| 12 | **Refund fee** | | |
| 13 | **Monthly / setup fees** | | |
| 14 | **Shopify transaction fee** still apply? (often yes without SP) | | |
| 15 | **Currencies at checkout** for US/EU buyers | | |
| 16 | **3-D Secure / SCA** support | | |
| 17 | **Fraud tools** included | | |
| 18 | **Blocked categories** (POD? dropship? digital?) — **critical** | | |
| 19 | **Test mode** available | | |
| 20 | **Support channel** (email SLA, Vietnamese/English) | | |
| 21 | **Dashboard export** for tax (CSV) | | |
| 22 | **Holds on first X days/volume** | | |
| 23 | **Works with your POD** (payment captured → order paid in Shopify) | | |
| 24 | **Customer trust** (recognizable brand at checkout) | | |
| 25 | **Contract exit** (can you leave; pending balance rules) | | |

### Instant fail conditions

- Provider bans **dropshipping/POD** or “fulfillment by third party” and you cannot get written confirmation it’s allowed.  
- Payouts only to a country/bank you cannot legally access.  
- No clear chargeback process.  
- Checkout redirects so broken that mobile Safari fails (test yourself).  
- Requires you to misrepresent business address/country.

---

## 3.5 Test protocol (before marketing spend)

1. Enable gateway in test/sandbox if available.  
2. Place **real small order** with your own card (and one friend abroad if possible).  
3. Confirm Shopify order status = **Paid** (not pending) within expected time.  
4. Confirm POD **receives** order automatically.  
5. Issue a **partial refund** test; confirm fees and Shopify state.  
6. Trigger a **cancel before production**; confirm no double charge.  
7. Record settlement: when did money hit your account, in what currency, net of fees.  
8. Only then: turn on ads / heavy content.

---

## 3.6 Fee math (use before pricing)

```text
Net ≈ Order total
    − payment MDR%
    − payment fixed fee
    − Shopify plan fee (amortized)
    − Shopify third-party txn fee (if any)
    − POD product + shipping cost
    − estimated refund reserve (2–5%)
    − ad cost per order
```

**Rule:** Set retail so net before ads ≥ 40% of price, or ads will not scale.

---

## 3.7 Tax & compliance (non-optional reminders)

- Register appropriate **Vietnam business / tax** status when required; report income.  
- Cross-border sales may involve **destination VAT/sales tax** (Shopify Markets / tax settings; professional advice for US sales tax nexus and EU VAT/IOSS as you scale).  
- Keep CSV exports monthly (payments + Shopify orders).  
- Privacy policy must match real data processors (Shopify, POD, payment provider, email tool).  
- This checklist is **operational**, not legal advice — confirm with a VN accountant before scale.

---

## 3.8 Recommended launch configuration (global boutique from VN)

| Slot | Choice approach |
|------|------------------|
| Primary checkout | Best **card + recognizable wallet** combo that approved your KYC |
| Backup | Second provider or PayPal if available (redundancy when primary declines) |
| Currency display | USD (or Markets multi-currency once stable) |
| Capture | Auto-capture on payment so POD sees **Paid** |
| COD | **Off** for global POD |
| Subscriptions | Off until basics work |

---

## 3.9 One-page “go / no-go”

Go live only if all are TRUE:

- [ ] At least one payment provider **approved** and tested with real money  
- [ ] Paid order → Shopify Paid → POD production **without manual steps**  
- [ ] Shipping & refund policy published and mirrored in listings  
- [ ] Support email monitored; Support Agent is draft-only  
- [ ] Unit economics spreadsheet exists with real POD costs  
- [ ] No ToS fraud on store country / identity  
- [ ] You can receive payouts to an account you control  

---

# Quick start order (all three parts)

| Day | Action |
|-----|--------|
| 1 | Create Sheet tabs; paste Global Rules into your connector tool |
| 1–2 | Install POD + payment; run test order (Part 3 tests) |
| 2 | Turn on Z01–Z04 |
| 3 | Run Trend Scout → Offer Designer → Listing Ops for 3 SKUs |
| 4 | Publish products; Creative Factory pack; Manychat keyword |
| 5 | Soft traffic; Finance Watcher after first sales |
| Ongoing | Score agents; promote connector combos with 10× scores ≥ 4 |

---

*End of Super System Pack — Parts 1, 2, and 3*
