# Connector Atlas — validation

**23/23 checks pass.** Evidence that the use-case discovery is sound — coherence, membership, coverage, per-verb side effects and the potential score. No held-out precision on join keys (that is not what this atlas measures); the honest test of a judgment model is whether its calls match hand labels and its reasoning is inspectable.


## 1. Coherence spot-checks

- ✅ **MAKES: inbox -> tasks**  
  ['Gmail', 'Todoist'] → STRONG — Claude reads what comes in via Gmail and turns it into tracked work in Todoist.
- ✅ **MAKES: meeting -> follow-ups**  
  ['Fireflies', 'Todoist'] → STRONG — Claude turns Fireflies into follow-ups and records in Todoist.
- ✅ **MAKES: research -> written brief**  
  ['Exa', 'Notion'] → STRONG — Claude gathers evidence from Exa and writes a durable brief in Notion.
- ✅ **MAKES: chat -> tasks**  
  ['Slack', 'Todoist'] → STRONG — Claude reads what comes in via Slack and turns it into tracked work in Todoist.
- ✅ **MAKES: payments -> books**  
  ['Stripe', 'Xero'] → STRONG — Claude turns Stripe into Xero.
- ✅ **MAKES: CRM -> outbound**  
  ['HubSpot', 'Klaviyo'] → STRONG — Claude keeps the pipeline in HubSpot moving through Klaviyo.
- ✅ **MAKES: store -> payments**  
  ['Shopify', 'Stripe'] → STRONG — Claude runs the store in Shopify end to end with Stripe.
- ✅ **DOESN'T: inbox vs. a brokerage**  
  ['Gmail', 'Interactive Brokers'] → NON — These connectors don't share a workflow Claude can bridge — they're separate use cases.
- ✅ **DOESN'T: case law vs. a markets feed**  
  ['CoCounsel Legal', 'MSCI'] → NON — These connectors don't share a workflow Claude can bridge — they're separate use cases.
- ✅ **DOESN'T: inbox vs. a biomedical database**  
  ['Gmail', 'PubMed'] → NON — These connectors don't share a workflow Claude can bridge — they're separate use cases.
- ✅ **DOESN'T: whiteboard vs. a brokerage**  
  ['Figma', 'Interactive Brokers'] → NON — These connectors don't share a workflow Claude can bridge — they're separate use cases.

## 2. Membership checks

- ✅ **redundant add does not raise the rating**  
  Gmail+Todoist=strong → +Asana=strong
- ✅ **redundant connector is labelled a fallback**  
  dropped as fallback: ['Todoist']
- ✅ **complementary add extends the use case**  
  Gmail+Todoist core=2 → +Calendar core=3 (strong)
- ✅ **dropping a redundant member does not lower the use case**  
  +Asana combo=strong → drop redundant → Gmail+Asana=strong

## 3. Coverage sanity

- ✅ **'runs like a company' spans most domains**  
  n_domains=12/12, scale=47
- ✅ **a small system is tight (no dead members)**  
  Gmail+Todoist core=2, dropped=0

## 4. Per-verb side effects

- ✅ **read-only use case over a send-capable connector reports read**  
  observe headline=read, Gmail(send-capable) used as source=read
- ✅ **a use case that actually sends incurs irreversible**  
  HubSpot+Klaviyo headline=irreversible, read-only footprint=read

## 5. Potential score sanity

- ✅ **every use case's potential is its four parts summed**  
  mismatched: none
- ✅ **the huge featured system tops operational reach**  
  featured reach=25, max across catalogue=25
- ✅ **a small universal combo maxes applicability (size-independent value)**  
  Gmail+Todoist applicability=25 (max 25), featured applicability=17
- ✅ **a non-use-case scores zero potential**  
  total=0
