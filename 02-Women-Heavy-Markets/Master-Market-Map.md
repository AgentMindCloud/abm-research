# Women-Heavy Markets & Unmet Needs – 2026-07-26

**Author of this pass:** Claude (Opus) · **Version:** 1.0 (first full draft)
**Raw evidence log:** `99-Raw-Extractions/Women-Markets-Claude-2026-07-26.md`
**Companion map:** `01-AI-Capabilities/Master-Capability-Map.md` (same date)

**Purpose.** Identify industries, products and services disproportionately used, bought or
operated by women, and locate high-friction digital opportunities inside them — before any
product invention, per `00-Meta/ABM-Project-Continuity.md` §2.

**Exclusions applied throughout (Continuity §3, restated as hard filters):** no childcare
for small children · no clinical health expertise or medical claims · no supplements · no
high-stakes financial, legal or real-estate services · no food products · nothing carrying
significant physical-safety or large-financial-loss risk. Every candidate in §6 has been
tested against all six.

**Confidence convention:** **High** = government statistics or primary institutional
research · **Medium** = consistent multi-source reporting, or a checkable claim ·
**Low** = single source, vendor self-report, or market-sizing projection.

---

### Two source-quality warnings that shape this entire map

**(i) The occupation data is excellent; the consumer-spending data is folklore.**
Government labour statistics are reliable. The ubiquitous "women control 85% of consumer
spending / $31.8 trillion" family of claims traces through a chain of marketing blogs to no
identifiable primary study. It appears in this map **once**, labelled **Low**, and is never
used to size anything. *(Direct observation of the citation chain, this pass — **High**.)*

**(ii) Every operational metric in the small-service-business space is published by a
vendor selling the fix.** No-show rates, retention rates and "hours saved" figures come
almost exclusively from booking-software companies and their affiliates. The specific
numbers are unreliable. **But the fact that a dozen commercially competing vendors
independently name the same four problems — forgotten appointments, lost rebooking, lapsed
clients, fragmented inbound messages — is itself strong evidence that those problems are
real and unsolved.** That is how the vendor data is used here: as a convergence signal,
not as measurement. *(**Medium** for the pattern, **Low** for any percentage.)*

---

## 1. Executive Summary

**The core finding, in one sentence:** there is a large, structurally under-served band of
female-majority, appointment-and-relationship-based micro-businesses whose central
operational problem is **memory and coordination**, not clinical skill, not capital, and
not booking software — and the measurable attention of the AI industry is pointed almost
entirely elsewhere.

Seven findings:

**1. The female-majority occupation base is large, digital-adjacent, and administratively
heavy.** BLS 2025 shows hairdressers/hairstylists/cosmetologists at **92% women (747,000
US workers)**, secretaries and administrative assistants at **91.9% (1.49M)**, receptionists
at **89.6% (1.25M)**, executive assistants at **93.5% (249,000)**, skincare specialists at
~95–100% **(113,000)**. *(BLS CPS, 2025 annual averages — **High** for shares, **Medium**
for exact counts pending a direct table re-read.)* The overlap of "female-majority" and
"work is largely scheduling, records, follow-up and client memory" is very high — and that
overlap is precisely what §2.2, §2.6 and §2.8 of the Capability Map say AI does well.

**2. AI attention is measurably not going there.** The Anthropic Economic Index
(CC BY 4.0, period 2026-05-01) shows **Computer & Mathematical at 23.8%** of observed usage
against **Personal Care & Service at 1.23%** and **Healthcare Support at 0.62%**. At
occupation level, tasks commonly done by hairdressers/cosmetologists account for **0.02%**
of observed usage (**rank 318 of 718** published occupations); skincare specialists
**0.04%** (rank 250); exercise trainers and group fitness instructors **0.07%** (rank 203).
The entire Personal Care & Service category receives less observed AI attention than
Architecture & Engineering alone. *(**High** for the numbers.)*
**Two caveats that must travel with this finding:** the publisher states plainly that this
measures *usage of tasks*, not people or jobs, and cannot support claims about employment
or displacement; and occupations with narrow, physical task catalogs will match fewer
conversations for reasons unrelated to attention. So read it as **suggestive evidence of a
supply-of-attention gap, not proof of one** *(**Medium** for the interpretation)*. Even
discounted, a ~1,000× ratio between one category's share and another's is hard to explain
away entirely.

**3. Women make or influence the majority of purchasing in exactly these categories.**
Personal services, beauty and wellness, pet care, gifting, events and household
coordination are majority-female purchase categories, and Vietnam's own "heavy shopper"
e-commerce segment is majority female and concentrated in fashion, beauty and personal
care. *(TGM Research — **Medium**; the "85% of all consumer spending" framing — **Low**,
direction only.)* This matters for a *buyer-side* product too, but §6 will argue the
operator-side is the better entry.

**4. The booking layer is saturated and defended; the layer above it is empty.** Five
platforms — Vagaro, Booksy, Mindbody, StyleSeat, Fresha — account for a reported ~76% of
online salon booking traffic, priced from free to ~$30/month for solos and $129–175 for
mid-market. Switching costs run **~$3,500–6,000** for a six-staff single-location salon
including migration and downtime. *(**Low–Medium** — competitor estimates and a
switching-focused vendor blog, but the direction is consistent everywhere.)*
**Conclusion: do not build a booking system.** Build the layer that sits beside the
incumbent, reads from it, and is sold on a recovered-revenue outcome rather than a seat.

**5. The two most actionable numbers found in the entire domain both point at memory.**
**62% of no-shows are attributed to the client simply forgetting**, and **68% occur within
24 hours of the appointment**. *(Vendor-sourced — **Low** for precision, **Medium** for the
mechanism, which recurs independently across competing vendors.)* This says the problem is
not pricing, not intent, and not demand — it is *last-minute coordination and recall*. That
is a Capability-Map §2.6 (monitoring) plus §2.8 (templated outbound) problem: two of the
highest-maturity, lowest-risk capabilities available.

**6. Retention concentration makes the economics work at micro scale.** Reported: **42% of
clients who visit more than once a year drive 80% of revenue**; businesses with loyalty
programmes grew revenue **14% YoY vs 7% industry average**; in boutique fitness, retention
rises to **84% at 3+ visits/week** versus much lower at low frequency. *(**Low**
individually; **Medium** for "visit frequency is the dominant retention predictor", which
recurs independently and is mechanically plausible.)* A product that moves a handful of
clients from lapsed to active pays for itself immediately at a small business's scale —
which is what makes outcome-based pricing viable rather than aspirational.

**7. Vietnam is a good place to build from and a difficult place to sell into first.**
Women own **17%** of Vietnamese companies and lead **27%** *(ADB — **High**)*. Vietnam has
~**11,752** aesthetic-service establishments per Ministry of Health data (late 2023), of
which only a single-digit percentage are formally licensed *(**Medium** for the count,
**Low** for the licensing split, which the secondary reporting contradicts itself on)* — an
enormous, high-friction, near-zero-software sector. But it is informal, cash-and-Zalo, with
low willingness to pay in USD and no reliable subscription billing rails. Meanwhile
Vietnam's own observed AI usage is thin (Anthropic Usage Index **0.53**, rank 84/121) and
pointed at code and content rather than operations *(**High**)*. **Recommended posture:
operate from Vietnam, sell to Western independents first, treat Vietnam/SEA as a later
localisation with a different pricing model.**

**The single strongest opportunity zone**, developed in §6: an **outcome-priced retention
and coordination layer for female-majority, appointment-based independent service
businesses** — beauty/esthetics/nails/lash/brow, boutique fitness and Pilates, pet
grooming, and independent creative-service providers (photography, events) — that owns
*client memory, lapse detection, gap-filling and templated outbound*, reads from whatever
booking tool the business already has, and never touches clinical judgement, money
movement, or an unreviewed free-composed message. This both confirms and sharpens the
prior lead candidate recorded in Continuity §5.

---

## 2. Female-Majority Occupations & Industries

### 2.1 The base data (BLS CPS, 2025 annual averages — **High** for shares)

Grouped by relevance to a digital, low-liability, coordination-shaped product.

**Group A — Personal care and appearance services** *(direct service, appointment-based,
relationship-driven, high repeat frequency)*

| Occupation | % women | US employed |
|---|---:|---:|
| Skincare specialists | ~95–100%¹ | 113,000 |
| Hairdressers, hairstylists, cosmetologists | 92.0% | 747,000 |
| Manicurists and pedicurists | ~80%+² | — |
| Massage therapists | ~70%+² | — |

¹ BLS reports 100.0%, almost certainly a small-cell rounding artifact — treat as ~95–100%,
**Medium**. ² Not captured in this pass's extraction; consistent with multi-year BLS
patterns — **Medium**, flagged as a verification debt.

**Group B — Administrative and coordination roles** *(the work itself is memory,
scheduling and follow-up)*

| Occupation | % women | US employed |
|---|---:|---:|
| Executive secretaries / executive assistants | 93.5% | 249,000 |
| Secretaries and admin assistants (exc. legal/medical/exec) | 91.9% | 1,491,000 |
| Receptionists and information clerks | 89.6% | 1,247,000 |
| Bookkeeping, accounting and auditing clerks | ~85%² | — |
| Event / meeting and convention planners | ~75%² | — |
| Travel agents | ~70%² | — |
| Human resources workers | ~70%² | — |

**Group C — Education and instruction** *(school-age and adult; small-children childcare is
excluded by project rules)*

| Occupation | % women | US employed |
|---|---:|---:|
| Preschool and kindergarten teachers | 97.1% | 644,000 |
| Elementary and middle school teachers | ~80%² | — |
| Librarians | ~80%² | — |
| Speech-language pathologists | 97.3% | 203,000 |

**Group D — Health-adjacent** *(listed for completeness; the clinical core is excluded, and
in most cases the surrounding administration is too regulated or too clinically entangled to
separate cleanly — see §6 exclusion notes)*

| Occupation | % women | US employed |
|---|---:|---:|
| Registered nurses | 87.3% | 3,528,000 |
| Licensed practical / vocational nurses | 89.9% | 545,000 |
| Dental hygienists | 95.0% | 203,000 |
| Occupational therapists | 92.4% | 138,000 |
| Dietitians and nutritionists | 91.7% | 136,000 |

**Group E — Adjacent female-heavy service industries with no clean BLS occupation row**
*(all **Medium** or lower; flagged as verification debts)*
- **Pet grooming.** Widely understood to be female-majority; BLS proxies (animal
  caretakers, veterinary technicians) are strongly female-majority. **No credible
  ownership statistic found — verification debt.** Global market ~**$17.9bn in 2025**, US
  services **$11.5bn** *(**Low** — market-research abstracts)*.
- **Boutique fitness and Pilates instruction.** Exercise trainers and group fitness
  instructors are the relevant occupation; studio *ownership* skews female in the
  Pilates/barre/yoga segment. **Verification debt.**
- **Independent creative services** — wedding and portrait photography, floristry, event
  design, interior decorating. Strongly female-majority in the wedding segment; an entire
  cottage industry of "Dubsado specialists" and "virtual assistants for wedding creatives"
  exists, which is itself evidence about the population *(**Medium**)*.
- **Nonprofit and association administration.** Female-majority workforce; membership,
  volunteer and donor coordination are the operational core.

### 2.2 What the occupation list has in common

Across Groups A, B, C and E, the same operational shape recurs:

- **Appointment- or engagement-based**, with a repeat cadence measured in weeks.
- **Relationship-dependent** — the client returns to a *person*, not a brand.
- **Client memory is the product's substrate**: preferences, history, what was done last
  time, what was said, what is due next.
- **The operator is also the practitioner.** There is no back office. Administration
  happens between clients, at night, or not at all.
- **Revenue is lost through omission**, not error: the follow-up that never went out, the
  rebooking never asked for, the lapsed client never noticed, the DM never answered.
- **Digital inputs and outputs**, but scattered across four or five unconnected tools.

That list is a near-exact match for the buildable zone in the Capability Map: bounded,
digital, verifiable, reversible, short-horizon, API-mediated. **The market shape and the
capability shape agree.** *(**High** — this is a comparison of two documented lists.)*

### 2.3 Vietnam and the geographic picture

- Women own **17%** of all Vietnamese companies and lead **27%** *(ADB, *Financial Access of
  Women-Owned SMEs in Viet Nam* — **High**)*. IFC estimates Vietnam's gender financing gap
  at **$1.19bn** *(**Medium**)*. ADB's 2025–2030 programme targets up to 2,200 new
  women-owned SME borrowers, and its $100M HDBank facility directs ≥40% to women-owned
  MSMEs *(**High**)*.
- Formal company registration substantially *understates* female business activity in
  Vietnam, because much of it sits in household businesses (*hộ kinh doanh*) outside the
  company register. GSO household-business data is the right source and has not yet been
  read — **verification debt.**
- **Vietnam's aesthetic-services sector: ~11,752 establishments** (Ministry of Health, late
  2023) covering salons, spas, massage, nail and hair; HCMC ~7,087 and Hanoi ~2,044. Only a
  single-digit percentage hold formal MoH licences. *(**Medium** for establishment counts,
  **Low** for the licensing split — the secondary reporting contradicts itself on whether
  598 licensed refers to HCMC or the whole country.)*
- Vietnam salon-service market projected at **9.2% CAGR 2026–2032** *(**Low**)*.

---

## 3. High-Frequency Products & Services Women Buy or Manage

Ranked by *frequency* and *coordination load*, since those are what create software
opportunity — not by market size, which is unreliable in this domain.

### 3.1 Very high frequency (weekly to monthly), high coordination load

| Category | Purchase/management cadence | Why it generates friction | Confidence |
|---|---|---|---|
| **Hair services** | 4–8 weeks, lifelong relationship with one stylist | Formula/service history, rebooking at the chair, colour-correction continuity, cancellation chains | **High** (BLS occupation base) |
| **Nails, lashes, brows** | 2–4 weeks — the highest repeat frequency in personal services | Very high appointment volume per client per year; a single lapsed client is a large annual loss | **Medium** |
| **Skincare / facials / esthetics** | 4–6 weeks, often on a package or course | Package balance tracking, course completion, non-clinical intake, product reorder timing | **High** (occupation), **Medium** (operations) |
| **Boutique fitness / Pilates / yoga** | 1–4× per week | Attendance frequency drives retention; class-pass and membership balances; waitlists | **Medium** |
| **Pet grooming** | 4–8 weeks | Breed/coat-specific instructions, temperament notes, pickup coordination, no-shows | **Medium** |
| **Massage / bodywork (non-clinical)** | 2–6 weeks | Preference memory, package balances, rebooking | **Medium** |
| **Household and family coordination** (appointments, gifts, school calendars, renewals) | Continuous | Invisible administrative load carried disproportionately by women; the most under-tooled category of all | **Medium** for the disproportion, **Low** for any quantification |

### 3.2 Medium frequency, very high per-engagement coordination load

| Category | Cadence | Friction | Confidence |
|---|---|---|---|
| **Weddings and events** (photography, planning, floristry, venues) | Once per client, 6–18 month engagement | Quote → contract → deposit → timeline → vendor coordination → delivery. Reported baseline of **90–120 minutes of admin per booking** before automation *(**Low** — vendor testimonial, worth validating)* | **Medium** |
| **Portrait / family / brand photography** | 1–2× per year per client | Session prep, gallery delivery, reorder prompts, annual re-engagement | **Medium** |
| **Independent instruction and coaching** (music, tutoring, languages, crafts) | Weekly, term-based | Roster management, make-up lessons, term rebooking, parent communication | **Medium** |
| **Nonprofit / association membership and volunteers** | Annual with continuous touchpoints | Lapse detection, renewal chasing, volunteer scheduling, recurring-donor attrition | **Medium** |

### 3.3 Purchase-side categories (buyer, not operator)

Majority-female purchase categories: beauty and personal care, fashion, gifting, pet
supplies and services, home goods and décor, wellness services, travel planning, children's
goods (excluding childcare services), health and beauty e-commerce. Vietnam's "heavy
shopper" e-commerce segment is majority female and concentrated in fashion, beauty and
personal care *(TGM Research — **Medium**)*.

The general claim that women make or influence the majority of household purchasing is
uncontroversial and adequate for *targeting*. The specific "85% / $31.8 trillion" figures
are **Low** and are not used here for anything. *(See §Warning (i).)*

**§6 argues for the operator side over the buyer side.** The reasons are structural:
operators have a measurable revenue problem, a budget line for software, and a small
addressable population reachable without paid acquisition. Consumers have none of those and
require consumer-scale marketing — which a solo operator cannot fund.

---

## 4. Existing Software Landscape in These Areas

### 4.1 Beauty / wellness booking — saturated, price-anchored, defended

| Platform | Position | Reported price | Recurring complaints |
|---|---|---|---|
| **Fresha** | Newer / budget-conscious salons globally | from $19.95/mo solo; $14.95 per bookable team member; **20% one-time commission** on marketplace-sourced new clients | Marketplace commission model; upsell pressure |
| **Vagaro** | Highest adoption among US independents and solos | ~$24–30/mo solo | Payment and client-profile glitches; support leans on help articles |
| **Booksy** | Strong in barbering/beauty, marketplace-led | mid | Marketplace dependency |
| **StyleSeat** | US independents, marketplace-led | mid | Commission model |
| **Mindbody** | Mid-market fitness/wellness | ~$129/mo base, escalating | **Year-long contracts; onboarding up to 8 weeks; difficulty cancelling; dated UI; buggy mobile app; slow support** |
| **Mangomint** | Mid-market salons | ~$165/mo up to 10 staff | Price |
| **Boulevard** | Premium salons/spas | ~$175/mo base | Price |
| **Zenoti / Phorest** | Multi-location, enterprise | custom | Enterprise complexity |
| **Square Appointments** | Free tier for single user | free–low | Thin vertical depth |
| **GlossGenius** | Solo-focused | ~$24–30/mo | Thin vertical depth |

Top five account for a reported ~**76% of online booking traffic** (2025).
**Switching cost ~$3,500–6,000** for a six-staff single-location salon; client-data
migration 2–8 hours; staff retraining 1–2 weeks.
*(All **Low–Medium** — vendor and vendor-adjacent sources; see §Warning (ii).)*

**What this landscape means.** Three conclusions, and the third is the important one:
1. **Booking is solved and commoditised.** Entering it means competing on price against a
   free tier, with a distribution disadvantage.
2. **Switching costs protect incumbents from replacement but not from adjacency.** The same
   $3,500–6,000 that stops a salon leaving Mindbody also means it will never migrate to you
   — but it says nothing about whether the salon will add a $79/month layer that makes
   Mindbody more profitable.
3. **The incumbents are systems of record, not systems of action.** They store the
   appointment. They do not notice that a client's 5-week cadence has become 11 weeks, or
   that a cancellation just opened a Saturday slot three people would want, or that a
   client mentioned a preference in a DM eight weeks ago. **That is the empty layer.**

### 4.2 Adjacent verticals

- **Pet grooming:** MoeGo, Animalo, GroomBoard, ZendPaw, Picktime, Teddy. A **thinner,
  younger, less consolidated** field than salon software — closer to a genuine opening, and
  operationally near-identical to beauty. *(**Medium**.)*
- **Boutique fitness:** Mindbody, Mariana Tek, fitDEGREE, WellnessLiving, Momence,
  ClassPass as a demand channel. Retention tooling exists but is largely dashboard-shaped
  (it *reports* churn rather than acting on it). *(**Medium**.)*
- **Creative / event services:** HoneyBook, Dubsado, Studio Ninja, Aisle Planner. Reported
  savings of ~10 hours/week (vendor self-report, **Low**).
  **The most telling artifact in this whole section: a visible cottage industry of
  "Dubsado specialists" and "virtual assistants for wedding creatives" exists purely to
  configure these tools.** That is a market signalling, in cash, that the software is
  valuable enough to want and too complex to adopt unaided. *(**Medium** — inferred from
  the existence and volume of those service businesses.)* An AI product that *configures
  and operates* rather than *provides features* is aimed directly at that gap.
- **Nonprofit / membership:** Bloomerang, Neon, Wild Apricot, Little Green Light. Lapse
  detection is typically a report, not an action.
- **General small-business AI:** the receptionist/voice layer (Retell-class platforms at
  ~$0.07/min, ~600ms latency) is new, cheap and largely un-verticalised. *(**Medium** —
  see Capability Map §5.4.)* This is the newest genuinely open primitive.

### 4.3 The structural gap, stated once

Existing software in these verticals is **transactional and passive**: it records what was
booked, sold and paid. What is missing is **relational and active**: something that holds
the client relationship's state over time, notices when it deviates, and acts within narrow
bounds. Every vertical above has the first and lacks the second. *(**Medium** — synthesised
from the landscape review; the strongest single piece of supporting evidence is that
retention tooling in boutique fitness is dashboard-shaped.)*

---

## 5. Unmet Needs & Friction Points (Most Important)

Twenty-two candidate frictions were collected (raw log §C). Below are the twelve that
survive the exclusions and are plausibly automatable given the Capability Map. Each carries
a **Capability fit** (which Capability Map section applies, and its maturity) and a
**Risk tier** (per Capability Map P4: Tier 0 read-only · Tier 1 reversible write ·
Tier 2 irreversible external effect · Tier 3 do-not-build).

### F1. Lapsed-client detection against the client's *own* cadence — **the strongest single friction**
Businesses know who booked. They do not know who *should have* booked. A nail client on a
3-week cadence at week 9 is a silent, unnoticed loss; a hair client on 8 weeks at week 9 is
fine. A single global "hasn't visited in 90 days" filter — which is what incumbents offer —
is useless because it ignores per-client cadence.
**Evidence:** 42% of clients visiting more than once a year drive 80% of revenue *(**Low**
precision, **Medium** mechanism)*. Retention rises with visit frequency across every source
found *(**Medium**)*.
**Capability fit:** §2.6 monitoring (8/10) + §2.2 extraction (8/10). Detection is
*deterministic statistics*, not model inference — per-client interval, variance, expected
next date. The model only writes the message.
**Risk tier:** 0 to detect, 2 to send. **Verifiable in code — yes** (the arithmetic is the
whole product). This is the highest-quality opportunity in the map.

### F2. Rebooking capture at the moment of service completion
The single highest-conversion moment is the client standing at the desk, and it is missed
constantly because the operator is finishing, cleaning, and greeting the next client.
**Capability fit:** §2.8 templated outbound (7/10) + §2.6. **Risk tier:** 1–2.
**Verifiable:** yes — did a next appointment get created within N hours?

### F3. Client memory as structured, dated records
Preferences, service history, what was discussed, what is due next, what to avoid
(non-clinical). Currently lives in the practitioner's head, a paper card, or a notes app.
**Capability fit:** §2.2 unstructured→structured (7/10). **Critical design constraint from
Capability Map L6:** this must be a **typed database field with a last-confirmed date**, not
a vector recollection — agent memory is an unbenchmarked, vendor-disputed layer.
**Risk tier:** 0–1. **Verifiable:** partially — schema validity yes, truth no; therefore
show provenance ("you said this on 12 May") rather than asserting facts.

### F4. Last-minute gap filling from a waitlist
A Saturday cancellation at 09:00 for a 14:00 slot is pure lost revenue unless someone
contacts the right three people in the right order within minutes. No human operator
mid-service can do this.
**Evidence:** **68% of no-shows occur within 24 hours of the appointment** *(**Low**
precision, **Medium** mechanism)* — the window is short and the work is time-critical, which
is exactly what a machine is for.
**Capability fit:** §2.6 + §2.8. **Risk tier:** 2 (it books people).
**Verifiable:** yes — was the slot filled?

### F5. Reducing forgotten appointments
**62% of no-shows are attributed to the client simply forgetting** *(**Low** precision,
**Medium** mechanism)*. Reminders reduce no-shows 38–50%, more with low-friction
cancellation *(**Low**)*. Salons reportedly lose $1,500–3,000/month to no-shows *(**Low**)*.
**Capability fit:** §2.8 (7/10). **Risk tier:** 2. **Verifiable:** yes.
**Caveat:** most incumbents already send SMS reminders. The unmet part is *escalation
intelligence* — which client, which channel, how many touches, and when to ask for a deposit
— not the reminder itself. Do not sell "reminders."

### F6. Inbound message triage across fragmented channels
Instagram DM, WhatsApp, Zalo, SMS, phone, web form, Facebook. Enquiries are lost in the
gaps between them, and after-hours enquiries are lost entirely.
**Capability fit:** §2.8 inbound (7/10 within a **narrow, high-structure intent set** —
which is what this is: price, availability, hours, location, rebooking) + §2.2.
**Risk tier:** 1 to draft, 2 to send.
**⚠ This is the highest-security-risk friction in the map.** It is exactly the
Capability-Map L2 pattern: untrusted external input reaching a credentialed agent. It must
be built on the **two-context rule (P3)** — the context reading DMs holds no credentials and
emits a typed enumerated intent; a separate context acts. Anything less should not ship.

### F7. Package, membership and class-pass balance tracking
Clients lose track of remaining sessions; businesses lose track of expiring balances.
Unused balances are simultaneously a revenue-recognition problem and a churn predictor.
**Capability fit:** §2.2 + §2.6. Pure arithmetic → **fully verifiable**. **Risk tier:** 0–1.
Underrated: this is the easiest thing in the map to get right and it produces a *reason to
contact the client* that is genuinely welcome.

### F8. Review requests timed to the right client at the right moment
Discovery in these verticals runs on Google and Instagram. Review volume is a growth input,
and asking the wrong client at the wrong time is worse than not asking.
**Capability fit:** §2.6 + §2.8. **Risk tier:** 2. **Verifiable:** partially — sent yes,
appropriate no. Needs a suppression list and a hard cap.

### F9. Non-clinical intake and consent-form chasing
Forms unreturned before an appointment cause delay or cancellation.
**Capability fit:** §2.8 + §2.2. **Risk tier:** 1–2.
**⚠ Scope constraint:** the *chasing* is automatable; the *content* must never involve
clinical interpretation, medical claims, or health advice. Chase the form; never read it as
a clinician. If a vertical's intake is inherently medical, the vertical is excluded.

### F10. Quote → contract → deposit → delivery chasing in project-based creative services
The reported **90–120 minutes of admin per booking** baseline *(**Low** — vendor
testimonial, verification debt)*.
**Capability fit:** §2.3 row 1 (7/10 — a 3–10 step workflow with explicit state, which is
precisely the buildable band) + §2.8. **Risk tier:** 1–2.
**⚠ Money movement (deposit collection) is Tier 2–3** — chase and link, never initiate.

### F11. Cross-tool data fragmentation
The typical operator runs a booking tool, Instagram, a spreadsheet, a notes app and a
payment processor with no shared state. **Nobody is the system of record**, which is why
F1–F4 are impossible for them today.
**Capability fit:** §2.4 (8/10 for 1–10 typed APIs; 5/10 for large surfaces — so integrate
*few* tools well). **Risk tier:** 0–1 read, 2 write.
This is the *enabling* friction: solving F1 requires solving enough of F11 first. It is also
the moat — once you hold the unified relational state, you are hard to remove.

### F12. Pricing and service-menu drift
Services priced years ago, never revisited; discounts that became permanent; loss-making
services nobody has noticed.
**Capability fit:** §2.6 anomaly detection (7/10 for detection, **not** for causal
explanation) + §2.1. **Risk tier:** 0 — advisory only, and it must stay advisory.
**⚠ Capability Map L4 applies directly:** causal RCT evidence shows generic AI advice can
*harm* lower-performing operators on difficult problems. Present the arithmetic ("this
service's average revenue per hour is 40% below your others"); do not present a
recommendation. This constraint is not a nicety — it is the difference between a useful
product and a harmful one.

### 5.1 What unifies F1–F12

Every one is a **memory, coordination or timing** problem: something that should have
happened, did not, and nobody noticed. None requires domain expertise the operator does not
already have. None requires clinical judgement. None moves money autonomously. **Nine of
the twelve are verifiable in code**, which per Capability Map L3 is the precondition for
autonomy. *(**High** — this is an assessment of the list against a stated criterion.)*

### 5.2 What is conspicuously *not* a friction here

Worth stating, because it rules out the obvious ideas:
- **Not content generation.** These operators can post to Instagram; it is not their
  bottleneck, and per Capability Map §2.5 content generation is the single most
  commoditised capability in AI (22.7% of all observed global usage).
- **Not booking.** Solved (§4.1).
- **Not payments.** Solved by Square/Stripe and excluded by risk rules anyway.
- **Not bookkeeping.** Adjacent to the excluded financial category and already served.
- **Not "an AI assistant."** Capability Map L4 — the jagged frontier means role-shaped
  products are contradicted by the strongest causal evidence available. Sell a *named
  workflow*, not a *persona*.

---

## 6. Promising Opportunity Zones (after exclusions)

Each zone is stated with its exclusion clearance, capability fit, and the specific reason
it could work for a solo operator. Ranked.

### Zone 1 — Retention & Coordination Layer for Appointment-Based Personal-Service Micro-Businesses ★ strongest
**Who:** independent and 1–6 chair/room beauty, esthetics, nails, lash/brow, hair and
non-clinical massage businesses. 92% female in the core occupation, ~747,000 US workers in
hairdressing alone plus 113,000 skincare specialists *(BLS 2025 — **High**)*.
**What:** sits *beside* the incumbent booking tool. Owns per-client cadence modelling (F1),
rebooking prompts (F2), structured dated client memory (F3), waitlist gap-filling (F4),
escalation-intelligent no-show reduction (F5), package balances (F7) and timed review
requests (F8).
**Why now:** the Economic Index shows this occupational territory at **0.02% of observed AI
usage, rank 318/718** *(**High** for the number, **Medium** for the attention
interpretation)*. Incumbents are systems of record, not systems of action (§4.3). Voice at
~$0.07/min makes after-hours capture newly affordable *(**Medium**)*.
**Exclusions:** ✅ no childcare · ✅ no clinical claims (memory is preferences and service
history, never diagnosis) · ✅ no supplements · ✅ no financial/legal/RE · ✅ no food ·
✅ no physical-safety or large-loss risk. **All clear.**
**Capability fit:** monitoring 8/10, extraction 8/10, templated outbound 7/10, 3–10 step
workflows 7/10. Detection is deterministic arithmetic. **Verifiable in code: yes.**
**Solo feasibility:** high. Narrow intent set, small tool surface, outcome measurable in
dollars, addressable population reachable without paid acquisition (Instagram, industry
educators, distributor relationships).
**Pricing shape:** flat monthly plus an outcome component tied to recovered bookings. The
retention concentration in §1.6 means a handful of reactivated clients covers the fee, which
makes outcome pricing honest rather than a gimmick.
**Principal risks:** (a) an incumbent ships the same feature — mitigated by being
multi-incumbent and outcome-priced rather than seat-priced; (b) integration availability —
**must be validated first, see §6.1**; (c) low willingness to pay at the solo end — target
2–6 practitioner businesses, not chair-renters.
**This both confirms and sharpens the prior lead candidate in Continuity §5.** The
sharpening is: lead with **retention and coordination**, and drop "margin" from the framing —
margin work drifts toward advisory output, which Capability Map L4 says can actively harm
less-experienced operators.

### Zone 2 — The same layer for Pet Grooming
**Who:** independent groomers and small grooming salons. Female-majority (**verification
debt**). US grooming services ~$11.5bn in 2025 *(**Low**)*.
**Why it may be better than Zone 1:** operationally near-identical (appointment cadence,
client memory, no-shows, rebooking) with a **thinner, younger, less consolidated software
field** *(**Medium**)* — less incumbent risk, and breed/coat/temperament notes are a
naturally structured memory schema.
**Exclusions:** all clear. Animal handling is the *groomer's* physical risk, not the
software's; keep the product away from any health or safety guidance about the animal.
**Capability fit:** identical to Zone 1. **Solo feasibility:** high.
**Why not ranked first:** less evidence collected in this pass, and the female-majority
claim is currently unverified.

### Zone 3 — Client-Journey Operations for Independent Creative-Service Providers
**Who:** wedding and portrait photographers, event planners, florists, designers. Strongly
female-majority in the wedding segment *(**Medium**)*.
**What:** F10 — the quote → contract → deposit-chase → timeline → delivery → reorder
pipeline, as a durable 3–10 step workflow (Capability Map §2.3 row 1, 7/10).
**Why now:** the "Dubsado specialist" cottage industry is a paying market telling you the
existing tools are worth having and too complex to adopt (§4.2). **Sell operation, not
features** — the product configures and runs itself.
**Exclusions:** all clear, provided the product **chases and links** for deposits and never
initiates money movement (Tier 2–3).
**Capability fit:** good. **Verifiable:** yes — each stage transition is a checkable state
change.
**Why not ranked first:** one-shot engagements mean lower repeat frequency and therefore a
weaker recurring-revenue mechanic than Zone 1, and HoneyBook/Dubsado are real incumbents in
a way that Zone 2's field is not.

### Zone 4 — Retention & Attendance Operations for Boutique Fitness / Pilates Studios
**Who:** independent Pilates, barre, yoga and reformer studios. Instructors and owners skew
female. Exercise trainers/group-fitness instructors: **0.07% of observed AI usage, rank
203/718** *(**High** for the number)*.
**What:** attendance-frequency monitoring (the dominant retention predictor — **Medium**),
lapse detection before cancellation, class-pass and membership balances (F7), waitlist
filling (F4).
**Exclusions:** ✅ clear, **provided the product never gives exercise, injury or health
guidance.** It counts attendance and sends coordination messages. Nothing else. This
boundary is easy to state and easy to cross accidentally, so it needs to be enforced in the
product, not just the policy.
**Capability fit:** strong (arithmetic detection). **Risk:** Mindbody, Mariana Tek and
others are closer to this space than salon incumbents are to Zone 1.

### Zone 5 — Membership, Volunteer & Donor Lapse Operations for Small Nonprofits and Associations
**Who:** small nonprofits, professional associations, clubs — female-majority
administrative workforce.
**What:** lapse detection, renewal sequences, volunteer scheduling, recurring-donor
attrition monitoring. Existing tools report; they do not act (§4.2).
**Exclusions:** ✅ all clear. Donation *processing* stays with the existing processor —
the product detects and drafts; it never touches funds.
**Capability fit:** strong, same shape as Zone 1. **Weakness:** notoriously slow
procurement, low budgets, committee decision-making — bad fit for a solo operator's cash
cycle. Ranked last for that reason, not on capability.

### 6.1 Zones deliberately excluded, with reasons

| Candidate | Why excluded |
|---|---|
| Nursing, dental hygiene, therapy, dietetics workflow tools | Occupations are 87–95% female and administratively drowning, but the administration is inseparable from clinical content and is regulated (HIPAA-class). **Continuity §3 clinical exclusion + Capability Map L7.** Highest-friction, highest-liability territory in the whole map. Do not enter. |
| Childcare centre administration | Explicit project exclusion. |
| Post-discharge / care coordination | Clinical exclusion; already deprioritised in Continuity §5. |
| Nutrition, wellness coaching, supplement retail | Supplement and clinical-claim exclusions. |
| Bookkeeping and tax for female-owned businesses | Falls under high-stakes financial exclusion; also well served. |
| Real-estate agent tooling (~55% female) | Explicit real-estate exclusion. |
| Meal planning, catering, food e-commerce | Explicit food exclusion. |
| Teacher lesson-planning tools | Educational Instruction is already **12.79%** of observed AI usage *(**High**)* — one of the most crowded categories, not whitespace. |
| Generic "AI assistant for women entrepreneurs" | Capability Map L4: role-shaped, advice-shaped products are contradicted by causal evidence and can harm lower-performing users. |

### 6.2 The one thing to validate before building anything

**Integration availability, not demand.** Zones 1–4 all depend on reading appointment and
client data out of an incumbent booking platform. If Fresha, Vagaro, Booksy, StyleSeat,
Mindbody and MoeGo do not offer usable read APIs on the plans that small businesses actually
buy, every zone above collapses into either GUI scraping (Capability Map §2.4: **4/10, do
not build on this**) or manual CSV import (viable but changes the product materially).

**This is a two-day desk check and it gates everything else.** Do it before any further idea
generation. If APIs are unavailable, the fallback ranking changes: Zone 3 rises, because
creative-services workflows can own their own state from the start rather than mirroring
someone else's.

---

## 7. Cultural & Geographic Notes (Vietnam vs Western markets)

### 7.1 Vietnam — the operating base

**What is genuinely favourable:**
- **Scale of the target sector.** ~**11,752** aesthetic-service establishments per Ministry
  of Health data, late 2023 — HCMC ~7,087, Hanoi ~2,044 *(**Medium**)*. Salon services
  projected at 9.2% CAGR to 2032 *(**Low**)*.
- **Women's business participation is substantial and institutionally supported.** 17% of
  companies owned, 27% led *(ADB — **High**)*; ADB and IFC actively financing women-owned
  SMEs, with a $1.19bn identified gender financing gap *(**Medium**)*.
- **Social commerce is the dominant commercial channel.** TikTok Shop at **39%** of
  Vietnamese e-commerce in H1 2025 (from 29% in 2024), GMV +69% YoY; four-platform GMV
  **VND 429.7tn (~$16bn)** in 2025 *(**Medium**)*. Businesses here are already
  digitally native in a *chat-and-video* register.
- **Low local competition in AI operations tooling.** Vietnam's observed usage is thin
  (Anthropic Usage Index **0.53**, rank 84/121) and pointed at code and content, not
  operations — Software Development 18.0% vs 11.5% global, "advice or recommendation"
  artifacts at half the global rate *(**High**)*.

**What is genuinely unfavourable — and decisive for sequencing:**
- **Informality.** Only a single-digit percentage of aesthetic establishments hold formal
  licences *(**Low–Medium**, reporting is contradictory)*. Informal businesses do not buy
  SaaS subscriptions, do not have business bank accounts reliably, and do not sign annual
  contracts.
- **Payment rails.** No dependable path to recurring USD-denominated subscription billing
  for a micro-business in this segment. Cash and QR transfer dominate.
- **Willingness to pay.** A $79/month Western price point is not transferable. Local pricing
  would need to be roughly an order of magnitude lower, which changes the entire unit
  economics and support model.
- **Channel and platform dependency.** Zalo is the dominant messaging channel, not
  WhatsApp or SMS. **Zalo OA / Mini App commercial and automation capabilities have not been
  verified and are a hard prerequisite** for any Vietnam-facing version *(verification
  debt)*.
- **Seller consolidation.** Vietnamese platform sellers **fell ~7.5% to 601,800 shops** in
  2025 under competitive pressure *(**Medium**)* — a market squeezing, not expanding, at the
  micro end.
- **Company-register data understates reality.** Much female business activity sits in
  household businesses (*hộ kinh doanh*) outside the company register; GSO data is the right
  source and has not been read *(verification debt)*.

### 7.2 Western markets (US, UK, AU, CA, EU) — the first customers

- **Prices support the model.** Salon software already sells at $24–175/month, so a
  $49–149/month adjacent layer is inside an established budget envelope *(**Medium**)*.
- **Channels are SMS, email, Instagram DM and WhatsApp** — all with mature, documented APIs.
- **Card-on-file and deposits are normalised**, which makes the no-show economics in §5-F5
  real rather than theoretical.
- **Discovery runs on Google reviews and Instagram**, which makes F8 (review timing) a
  growth lever the operator already believes in.
- **Regulatory load is real but bounded and non-clinical:** GDPR/UK-GDPR and US state
  privacy law for client records; TCPA/CASL/PECR-class consent rules for SMS and marketing
  messages. **This is the single most under-appreciated compliance item in the whole map** —
  automated outbound messaging is *directly regulated* in the US, Canada and EU, and a
  product whose core function is sending messages must handle consent, opt-out, quiet hours
  and record-keeping correctly from day one. It is not a blocker; it is a design
  requirement, and getting it right is a competitive advantage over anyone who does not.
  *(**Medium** — well-established law, specifics need a jurisdiction check before launch.)*
- **Cultural fit is good.** Western independent beauty and wellness operators are
  Instagram-native, accustomed to buying tools, and vocal about no-shows and lost rebookings
  in their own professional communities — which is both market research and a distribution
  channel.

### 7.3 Recommended geographic sequencing

1. **Build from Vietnam, sell to Western independents.** Cost base local, revenue in USD,
   product built in English against documented APIs and mature payment rails. This is the
   arbitrage the Continuity constraints were written for.
2. **Beachhead: one vertical, one country, one incumbent integration.** Not "beauty
   businesses globally." The Capability Map's §2.8 finding is decisive here: automation
   quality is a function of *intent-mix narrowness*, so a narrow beachhead is a capability
   decision, not just a go-to-market one.
3. **Vietnam / SEA as a later localisation**, gated on: Zalo automation feasibility, a
   local payment mechanism, and a price point an order of magnitude lower. Treat it as a
   second product, not a translation.
4. **Do not build for both simultaneously.** The channel stack (SMS/email/Instagram vs
   Zalo), the payment rails, the price point, the consent regime and the formality level all
   differ. A solo operator cannot carry two of everything.

### 7.4 A cultural note on framing

The project's own framing — "whitespace not already crowded by technical men building for
technical men" (Continuity §1) — is now supported by a number rather than an intuition:
**Computer & Mathematical 23.8% of observed AI usage vs Personal Care & Service 1.23%**
*(**High**)*. But the framing has a marketing implication worth stating: **the product
should be sold as competent operational software, not as software "for women."** The buyers
in Zones 1–4 are professionals with a revenue problem. Gender is how this project *found*
the market and why it is under-served; it is not the value proposition, and leading with it
would misrepresent what the product does.

---

## Verification debts carried forward

Full list in `99-Raw-Extractions/Women-Markets-Claude-2026-07-26.md` §D. The five that most
affect this map:
1. **Re-read BLS cpsaat11 directly** — pin 2025 shares/counts and add manicurists, massage
   therapists, bookkeeping clerks, event planners, travel agents, HR workers, vet techs.
   Fix the two extraction anomalies flagged in §2.1.
2. **Verify female-ownership share in pet grooming and boutique fitness** — Zone 2 and
   Zone 4 rest on an unverified premise.
3. **Find any non-vendor source for no-show and retention rates** (academic, industry
   association, or payment-processor data). If none exists, state that absence explicitly —
   it is itself a finding, and it would mean §5's magnitudes are all vendor-shaped.
4. **Check integration availability across the incumbent booking platforms** (§6.2) — this
   gates every zone and is a two-day desk check.
5. **Vietnam specifics:** GSO household-business data; Zalo OA/Mini App automation
   feasibility; resolve the MoH licensing contradiction; find the female share of
   Vietnamese platform sellers.

---

## Sources

Primary / high-trust:
- [BLS Current Population Survey — employed persons by detailed occupation and sex](https://www.bls.gov/cps/cpsaat11.htm) (2025 annual averages; retrieved 2026-07-26)
- [Anthropic Economic Index](https://www.anthropic.com/economic-index) — CC BY 4.0, period 2026-05-01, snapshot 2026-06-24; accessed via MCP 2026-07-26. *Usage of tasks, not people or jobs; no trend series; cannot support employment or displacement claims.*
- [ADB — Financial Access of Women-Owned Small and Medium-Sized Enterprises in Viet Nam](https://www.adb.org/sites/default/files/publication/850891/financial-access-women-owned-smes-viet-nam.pdf)
- [IFC — Women-owned enterprises in Vietnam: Perceptions and Potential](https://www.ifc.org/content/dam/ifc/doc/mgrt/market-study-on-women-owned-enterprises-in-vietnam-eng-v1.pdf) (not yet read in full — verification debt)
- [ADB / HDBank $100M MSME and women-owned business facility](https://www.adb.org/news/adb-hdbank-sign-100-million-loan-expand-access-finance-msmes-women-owned-businesses-viet-nam)
- Companion: `01-AI-Capabilities/Master-Capability-Map.md` (2026-07-26); `05-Previous-Research/Master-Synthesis.md`

Secondary (Medium):
- [Shopee and TikTok Shop account for 8 per cent of Vietnam's retail market — Vietnam Investment Review](https://vir.com.vn/shopee-and-tiktok-shop-account-for-8-per-cent-of-vietnams-retail-market-144853.html)
- [Vietnam E-commerce Sector Outlook 2026 — Vietnam Briefing](https://www.vietnam-briefing.com/news/vietnams-e-commerce-sector-outlook-in-2026.html/)
- [Mapping Vietnam's Online Shoppers 2025 — TGM Research](https://tgmresearch.com/vietnam-online-consumer-segments.html)
- [Inside Vietnam's billion-dollar beauty-service landscape — Luma](https://luma.vn/vietnams-billion-beauty-service/) (reports Ministry of Health establishment data)

Vendor / vendor-adjacent (Low individually; used only as convergence evidence — see §Warning (ii)):
- [The real revenue cost of no-shows at salons and spas — Zenoti](https://www.zenoti.com/es/thecheckin/infographic-the-cost-of-a-no-show-how-missed-appointments-impact-your-bottom-line-2); [Beauty & Wellness Industry Statistics 2025 — Zenoti](https://www.zenoti.com/thecheckin/beauty-wellness-industry-statistics-2025)
- [Spa & Salon Retention Statistics 2026 — Jeri Commerce](https://blog.jericommerce.com/resources/spas-salons-medspas-retention-statistics)
- [No-Show Statistics 2026 by Industry — Etisia](https://www.etisia.com/no-show-statistics)
- [Best Salon Software Guide 2026 — The Salon Business](https://thesalonbusiness.com/best-salon-software/); [Salon software cost per month 2026 — heylilo](https://heylilo.co/resources/pricing-switching/salon-software-cost-per-month)
- [Does rebooking reduce no-shows in pet grooming — MoeGo](https://www.moego.pet/blog/does-rebooking-reduce-no-shows-pet-grooming)
- [Boutique fitness retention rate benchmarks 2026 — StudioPulse](https://getstudiopulse.com/blog/boutique-fitness-retention-rate); [45 Pilates industry statistics 2026 — SchedulingKit](https://schedulingkit.com/statistics/pilates-industry-statistics)
- [Best CRM for photographers: Dubsado vs HoneyBook — Colie James](https://coliejames.com/best-crm-for-photographers/)

Low confidence, direction only, not used for sizing:
- [NielsenIQ — Women's impact on the CPG landscape (2024)](https://nielseniq.com/global/en/insights/analysis/2024/shaping-success-a-deep-dive-into-womens-impact-on-the-cpg-landscape/) (best available near-primary on women's purchasing influence; not yet read — verification debt)
- The "women control 85% of consumer spending / $31.8tn" claim family — no traceable primary. Rejected for sizing.

Rejected sources are listed by name with reasons in `99-Raw-Extractions/Women-Markets-Claude-2026-07-26.md` §A.
