# Raw Extraction – Women-Heavy Markets & Unmet Needs (Claude pass, 2026-07-26)

Purpose: raw source log behind `02-Women-Heavy-Markets/Master-Market-Map.md`.
Includes contradictions, extraction caveats, and rejected material. Audit trail, not conclusion.

---

## A. Source-quality triage note

Two distinct quality problems in this domain:

**A1. Occupation data is good; consumer-spending data is folklore.**
Government labour statistics (BLS CPS, GSO Vietnam, ILO) are solid primary sources.
The widely-repeated "women control 85% of consumer spending / $31.8 trillion" family of
claims traces back through a chain of marketing blogs to no identifiable primary study.
Treated as **Low confidence, directional only**, and *never* used to size a market.

**A2. Every operational metric in the service-business space is published by a vendor
selling the fix.** No-show rates, retention rates, and "hours saved" figures come almost
exclusively from booking-software companies and their affiliates. The *numbers* are
unreliable; the *fact that every vendor independently identifies the same problems* is
itself the useful signal. Recorded as **Medium for the existence and rough magnitude of
the problem, Low for any specific percentage.**

Rejected / heavily downgraded:

| Claim | Source type | Disposition |
|---|---|---|
| "Women control 85% of consumer spending" / "$31.8 trillion in 2025" | Marketing blogs citing each other (girlpowermarketing, financebuzz, electroiq, passivesecrets) | **Low.** Direction only. No primary. |
| "91% of women are responsible for buying new homes" | Same chain | **Rejected.** Implausible on its face; also lands in an excluded category (real estate). |
| "GroomGrid — reduce no-shows 80%" | Vendor homepage | **Rejected.** Pure marketing. |
| Nail-salon / pet-grooming market-size forecasts to 2032–2035 | Paid market-research report abstracts | **Low.** Directional only; methodology unavailable. |
| "Fresha/Vagaro/Booksy/Mindbody/StyleSeat = ~76% of online booking traffic" | Vendor-adjacent comparison blog (zenoti) | **Low–Medium.** Plausible and consistent with observation, but a competitor's estimate. |

---

## B. Primary / high-trust sources

### B1. BLS — Current Population Survey, employed persons by detailed occupation and sex
- https://www.bls.gov/cps/cpsaat11.htm (annual averages; retrieved 2026-07-26, reported year 2025)

Extracted rows (female share of employment, total employed):

| Occupation | % women | Total employed |
|---|---:|---:|
| Speech-language pathologists | 97.3% | 203,000 |
| Preschool and kindergarten teachers | 97.1% | 644,000 |
| Dental hygienists | 95.0% | 203,000 |
| Executive secretaries / executive administrative assistants | 93.5% | 249,000 |
| Childcare workers | 93.2% | 1,106,000 |
| Occupational therapists | 92.4% | 138,000 |
| **Hairdressers, hairstylists, and cosmetologists** | **92.0%** | **747,000** |
| Secretaries and administrative assistants (exc. legal/medical/exec) | 91.9% | 1,491,000 |
| Dietitians and nutritionists | 91.7% | 136,000 |
| Licensed practical and licensed vocational nurses | 89.9% | 545,000 |
| Receptionists and information clerks | 89.6% | 1,247,000 |
| Registered nurses | 87.3% | 3,528,000 |
| Skincare specialists | ~100% (see caveat) | 113,000 |
| Medical secretaries and administrative assistants | 98.4% | 103,000 (see caveat) |

**Extraction caveats (important):**
- "Skincare specialists 100.0%" is almost certainly a rounding/suppression artifact of a
  small cell. Treat as "≈95–100%", **Medium**.
- "Medical secretaries 103,000" is implausibly low against other BLS series for that
  occupation (typically several hundred thousand). Likely a mis-parse. **Do not cite the
  count**; the ~98% female share is consistent with all other years and is safe.
- Everything else is consistent with the multi-year BLS pattern → **High** for shares,
  **Medium** for exact counts pending a direct table re-read.

Occupations *not* captured in this extraction but reliably female-majority in BLS series
and relevant here (flagged for next-pass verification, currently **Medium**):
manicurists and pedicurists (~80%+), massage therapists (~70%+), bookkeeping/accounting/
auditing clerks (~85%), medical records specialists, human resources workers (~70%+),
event planners / meeting-convention planners (~75%+), travel agents (~70%+),
veterinarians and veterinary technicians (vet techs ~90%+), social workers (~80%+),
elementary and middle school teachers (~80%), librarians, florists, interior designers,
fundraisers, real-estate *brokers/agents* (~55%, and excluded by project rules anyway).

### B2. Anthropic Economic Index (CC BY 4.0), period 2026-05-01
Accessed via MCP 2026-07-26. https://www.anthropic.com/economic-index

**Publisher's binding methodological constraint:** this is *observed Claude usage matched to
occupational task catalogs*. It is **not** a measure of jobs, the labour market, or who the
users are. Correct phrasing: "AI is used for tasks commonly done by [occupation]". No trend
series exists; it cannot support displacement or job-security claims. **Any use of these
numbers in the Master map must carry that frame.**

Job-category shares of global usage:

| Category | % of usage |
|---|---:|
| Computer and Mathematical | 23.80 |
| Arts, Design, Entertainment, Sports, Media | 13.55 |
| Educational Instruction and Library | 12.79 |
| Sales and Related | 9.14 |
| Office and Administrative Support | 7.89 |
| Management | 5.90 |
| Business and Financial Operations | 5.77 |
| Life, Physical, and Social Science | 4.51 |
| Architecture and Engineering | 3.56 |
| Healthcare Practitioners and Technical | 3.31 |
| Community and Social Service | 2.57 |
| **Personal Care and Service** | **1.23** |
| Production | 1.04 |
| Legal | 1.02 |
| Installation, Maintenance, Repair | 0.62 |
| **Healthcare Support** | **0.62** |
| Food Preparation and Serving | 0.48 |
| Transportation and Material Moving | 0.34 |
| Protective Service | 0.33 |
| Building and Grounds Cleaning | 0.13 |
| Construction and Extraction | 0.10 |
| Farming, Fishing, Forestry | 0.04 |

Personal Care and Service drill-down (usage share of global total; rank of 718 published
occupations; augmentation/automation split):

| Occupation | usage share % | rank | aug% | auto% |
|---|---:|---:|---:|---:|
| Locker Room / Coatroom / Dressing Room Attendants | 0.56 | 44 | 35.5 | 64.5 |
| Recreation Workers | 0.11 | 157 | 46.3 | 53.7 |
| Residential Advisors | 0.10 | 167 | 59.3 | 40.8 |
| Childcare Workers | 0.09 | 174 | 43.9 | 56.1 |
| Exercise Trainers and Group Fitness Instructors | 0.07 | 203 | 58.0 | 42.0 |
| Animal Caretakers | 0.04 | 250 | 41.5 | 58.5 |
| **Skincare Specialists** | **0.04** | **250** | 41.5 | 58.5 |
| Tour Guides and Escorts | 0.03 | 279 | 35.9 | 64.1 |
| **Hairdressers, Hairstylists, and Cosmetologists** | **0.02** | **318** | 55.9 | 44.1 |
| Barbers | 0.01 | 374 | 52.5 | 47.5 |
| Concierges | 0.01 | 374 | 23.2 | 76.8 |

**The headline asymmetry.** Cross-referencing B1 and B2:
- Hairdressers/hairstylists/cosmetologists: **92% female, 747,000 US workers**,
  **0.02% of observed AI usage**, rank 318/718.
- Computer & Mathematical as a whole: **23.8% of observed AI usage.**
- The whole Personal Care & Service category (1.23%) receives less observed AI attention
  than Architecture & Engineering alone (3.56%).
- Caveat that must travel with this: occupation ranking reflects how often conversation
  content matches an occupation's *task catalog*, and occupations with broad catalogs can
  rank high for reasons unrelated to who is using the tool. Personal-care task catalogs are
  narrow and physical, which partly explains low matching independently of attention.
  **So this is suggestive evidence of an attention gap, not proof of one.** Confidence
  **Medium** for the interpretation, **High** for the underlying numbers.

### B3. Anthropic Economic Index — Vietnam (VNM), 2026-05-01
- Anthropic Usage Index **0.53** (share of usage ÷ share of working-age population;
  1.0 = global average). Rank **84 of 121**.
- Work 53.13% / personal 26.50% / coursework 20.38% (global: 43.36 / 40.20 / 16.45).
- Automation-style 51.38% vs augmentation 48.62% (global: 48.62 / 51.38 — exact mirror).
- Request topics vs global: Content Creation & Copywriting 24.91 (22.72);
  Software Development 18.01 (11.51); Education & Learning 14.54 (13.23);
  Research & Intelligence 8.11 (10.94); Document Processing & Extraction 5.31 (4.32).
- Job categories vs global index: Computer & Math 29.32 (×1.23);
  Architecture & Engineering 5.17 (×1.45); Management 6.19 (×1.05); Sales 6.46 (×0.71);
  Business & Financial Ops 5.05 (×0.88); Healthcare Practitioners 1.66 (×0.50).
- Artifacts: "advice or recommendation" 5.54 vs global 10.72 (×0.52);
  "code fix or debug" 6.06 vs 3.29 (×1.84); "data or spreadsheet" 4.51 vs 3.11.
- **Reading:** Vietnamese observed usage is more work-oriented, more technical, more
  automation-styled, and markedly *less* advisory/consumer-facing than the world average.
  Confidence **High** for the data, **Medium** for the interpretation.

### B4. ADB — Financial access of women-owned SMEs in Viet Nam
- https://www.adb.org/sites/default/files/publication/850891/financial-access-women-owned-smes-viet-nam.pdf
- **Women own 17% of all companies in Vietnam and lead 27% of them.** (**High** — ADB primary.)
- IFC estimate of Vietnam's gender financing gap: **$1.19 billion**. (**Medium**.)
- ADB/HDBank $100M facility, ≥40% directed to women-owned MSMEs; 2025–2030 ADB programme
  targeting up to 2,200 new women-owned SME borrowers. (**High** — press primary.)
- IFC market study: "Women-owned enterprises in Vietnam: Perceptions and Potential" —
  https://www.ifc.org/content/dam/ifc/doc/mgrt/market-study-on-women-owned-enterprises-in-vietnam-eng-v1.pdf
  (Not yet read in depth — **verification debt**.)

### B5. Vietnam beauty/aesthetic services sector
- Vietnamese **Ministry of Health** data, late 2023: **11,752 establishments** offering
  aesthetic services nationwide (beauty salons, spas, massage, nail, hair, remedial massage).
  - Ho Chi Minh City ≈ **7,087** establishments, of which **598** licensed under MoH rules.
  - Hanoi ≈ **2,044**, of which **200** licensed.
  - **Contradiction in the reporting:** one secondary source states 598 of the *national*
    11,752 were licensed, another attributes 598 to HCMC specifically. Either way the
    licensed share is single-digit percent. **Medium** for the establishment count (MoH
    primary via secondary reporting), **Low** for the exact licensing split.
  - Secondary: https://luma.vn/vietnams-billion-beauty-service/
- Separate 2023 report: >6,000 spa businesses nationwide. (**Low**.)
- Vietnam salon-service market projected CAGR **9.2%** 2026–2032. (**Low** — paid report.)
- **Structural implication:** a largely informal, unlicensed, cash-and-Zalo sector. Very
  high friction, very low software penetration, but also low willingness/ability to pay in
  USD and no reliable payment rails for subscription billing. Note for §7.

### B6. Vietnam e-commerce and social commerce
- GMV across Shopee, Lazada, Tiki, TikTok Shop: **VND 429.7 trillion (~$16bn)** in 2025.
- Seller count across those four platforms **fell ~7.5% to 601,800 shops** — consolidation
  under competitive pressure. (**Medium** — Vietnam Investment Review, trade press.)
  https://vir.com.vn/shopee-and-tiktok-shop-account-for-8-per-cent-of-vietnams-retail-market-144853.html
- TikTok Shop share of Vietnamese e-commerce: **39% in H1 2025**, up from 29% in 2024;
  GMV +69% YoY vs Shopee +16.1%. (**Medium**.)
- Shopee + TikTok Shop ≈ **8% of Vietnam's total retail market**. (**Medium**.)
- Consumer segmentation: the "Heavy Shopper" segment is majority female, concentrated in
  fashion, beauty and personal care. (**Medium** — TGM Research.)
  https://tgmresearch.com/vietnam-online-consumer-segments.html
- **Gap:** no source found for the female share of *sellers* on Vietnamese platforms.
  **Verification debt.**

### B7. Salon / spa operational friction (vendor-sourced — see A2)
- No-show rates: **15–20%** of scheduled revenue lost (Zenoti); **15–30%** range across
  sources; **15–25%** for businesses without deposits; **<5%** for top performers with
  deposits + reminders.
- **62% of no-shows are attributed to the client simply forgetting**; **68% occur within
  24 hours of the appointment.** (These two are the most actionable numbers found in the
  whole domain — they say the problem is *memory and last-minute coordination*, not
  pricing or intent.)
- SMS reminders reduce no-shows **38–50%**, up to 60–70% when combined with low-friction
  cancellation.
- Average salon loses **$1,500–$3,000/month** to no-shows; worked example: 200 monthly
  appointments at $85 average → $2,550–$5,100/month lost.
- Retention: **42% of clients who visit more than once a year drive 80% of revenue**;
  spas with loyalty programmes grew revenue **14% YoY vs 7% industry average**.
- Sources: zenoti.com, blog.jericommerce.com, etisia.com, bookrhub.com, aimi.so —
  **all vendor or vendor-adjacent. Low individually; Medium for the pattern.**

### B8. Salon software landscape
- Top five by online-booking traffic: **Vagaro, Booksy, Mindbody, StyleSeat, Fresha** ≈ 76%
  of booking traffic (2025). (**Low–Medium**, competitor estimate.)
- Positioning: Vagaro + Square Appointments strongest among US independents/solo;
  Fresha strong among newer and budget-conscious salons globally; Zenoti dominant in
  multi-location/enterprise.
- Pricing: free (Square single-user) → **$24–30/mo** solo (GlossGenius, Vagaro) →
  **$129–175/mo** mid-market (Mindbody ~$129 base, Mangomint ~$165/10 staff,
  Boulevard ~$175 base) → custom enterprise (Zenoti, Phorest).
  Fresha from **$19.95/mo** solo, **$14.95 per bookable team member**, plus a **20%
  one-time commission** on new marketplace-sourced clients.
- Recurring complaints (review aggregators, Capterra/G2 summaries):
  - Mindbody: **year-long contracts**, onboarding up to **8 weeks**, difficulty cancelling,
    dated UI, buggy mobile app, slow support.
  - Vagaro: payment and client-profile glitches, support leans on help articles.
- **Switching cost: ~$3,500–6,000 for a 6-staff single-location salon** including data
  migration and staff downtime; client-data migration 2–8 hours; retraining 1–2 weeks.
  (**Low** — from a switching-focused vendor blog, but the *direction* is well-attested.)
- **Strategic conclusion (Medium):** the booking layer is saturated, price-anchored low,
  and defended by high switching costs. **Do not build a booking system.** The opening is a
  *layer that sits beside* the incumbent and reads from it — retention, memory,
  coordination, revenue recovery — sold on outcome rather than seat.

### B9. Creative / event services CRM landscape
- HoneyBook, Dubsado, Studio Ninja, Aisle Planner — the wedding/photography/creative
  services stack. An entire cottage industry of "Dubsado specialists" and
  "virtual assistants for wedding creatives" exists to configure these tools.
  **That cottage industry is the finding**: the software is powerful enough to be worth
  configuring and too complex for the target user to configure alone. (**Medium** —
  inferred from the existence and volume of such service businesses.)
- Reported admin savings: **~10 hours/week** (HoneyBook self-report); one photographer
  reported **90–120 minutes per booking** of manual work before automation;
  a doula/birth photographer reported a year-long client journey compressed to
  **15–20 minutes total** of admin. (**Low** — vendor testimonials. But the *baseline*
  they imply — 90–120 min of admin per booking — is the number worth validating.)
- Dubsado includes time-tracking; HoneyBook is manual-entry only. (**Medium**.)

### B10. Pet grooming
- Global pet-grooming market ~**$17.9bn in 2025** (from ~$14.8bn 2024), projected ~$42.9bn
  by 2035 (~9.1% CAGR). US pet-grooming services crossed **$11.5bn in 2025**, projected
  ~$13bn by end-2026. (**Low** — market-research abstracts.)
- No-shows: typical **5–15%**; **15–25%** without deposits; **<5%** with automated deposits
  and reminders; online self-booking reduces no-shows **30–40%**. (**Low**, vendor.)
- Software: MoeGo, Animalo, GroomBoard, ZendPaw, Picktime — a *thinner, younger* vendor
  field than salon software. Notably less consolidated.
- **No credible statistic found for female ownership share in pet grooming.**
  Occupation-level proxy: BLS "Animal caretakers" and veterinary technicians are strongly
  female-majority; groomers are widely understood to be female-majority but this is
  **unverified — verification debt.**

### B11. Boutique fitness / Pilates
- Boutique studio monthly retention commonly cited at **90–93%** (7–10% monthly churn);
  top studios **95–97%**. Another source cites monthly retention **70–85%** depending on
  membership structure — **these disagree substantially and probably measure different
  things** (member churn vs class-attendance retention).
- Pilates studios reported at lower churn than traditional gyms (gym monthly churn ~18%);
  72% six-month retention, rising to **84% for clients attending 3+ classes/week**.
- (**Low** individually; **Medium** for "attendance frequency is the dominant retention
  predictor", which recurs independently across sources and is mechanically plausible.)
- Exercise Trainers and Group Fitness Instructors: **0.07% of observed AI usage, rank
  203/718** (B2) — another low-attention, high-frequency, female-heavy category.

### B12. Consumer spending (Low — direction only)
- "Women control ~85% of consumer purchases / influence 70–80% of household purchasing
  decisions / $31.8tn global spend in 2025" — repeated across marketing blogs with no
  traceable primary. **Low.**
- NielsenIQ (2024) has genuine CPG analysis of women's purchasing influence and is the
  best available near-primary in this space — https://nielseniq.com/global/en/insights/analysis/2024/shaping-success-a-deep-dive-into-womens-impact-on-the-cpg-landscape/
  (**Not yet read — verification debt.**)
- **Practical stance:** the directional claim (women make or influence the majority of
  household and personal-services purchasing) is uncontroversial and adequate for
  targeting. It must not be used as a market-size number.

---

## C. Candidate friction points collected (pre-filtering)

Raw list before applying the project's exclusions. Scored later in the Master map.

1. No-shows and late cancellations in appointment-based service businesses.
2. Rebooking / next-appointment capture at the moment of service completion.
3. Client memory: preferences, formula/service history, allergies (non-clinical), notes,
   "what did we do last time", last-confirmed dates.
4. Lapsed-client reactivation — who has not returned in N weeks vs their own cadence.
5. Inbound message triage across Instagram DM / WhatsApp / Zalo / SMS / phone / web form.
6. After-hours inbound enquiries lost to voicemail.
7. Deposit collection and cancellation-policy enforcement without confrontation.
8. Package / membership / class-pass balance tracking and expiry reminders.
9. Review requests timed to the right client at the right moment.
10. Waitlist-to-gap filling when a cancellation opens a slot.
11. Multi-tool data fragmentation (booking tool + Instagram + spreadsheet + notes app).
12. Onboarding/intake paperwork chasing (forms, consent, questionnaires — non-clinical).
13. Quote/proposal/contract/invoice chasing in project-based creative services.
14. Supplier reordering and stock-level tracking for consumables.
15. Staff/renter/contractor scheduling and commission or rent reconciliation.
16. Pricing and service-menu drift — services priced years ago, never revisited.
17. Content production for social channels the business depends on for discovery.
18. Volunteer / committee / membership coordination in nonprofits and associations.
19. Event vendor coordination and timeline management.
20. Recurring-donor and member lapse detection in nonprofits.
21. Class/course roster and communication management for independent instructors.
22. Handover notes between shifts or between an owner and a covering practitioner.

Excluded on sight by project rules (Continuity §3): anything requiring clinical judgement
or medical claims; childcare for small children; supplements; high-stakes legal/financial/
real-estate advice; food products; anything with injury or large-financial-loss exposure.
Note that #12 must be scoped carefully to stay non-clinical, and #7/#15 touch money
*movement* and therefore need Tier-2/Tier-3 gates per the Capability Map's P4.

---

## D. Open verification debts (carry into next pass)

1. **Re-read BLS cpsaat11 directly** and pin exact 2025 shares and counts, including
   manicurists, massage therapists, bookkeeping clerks, event planners, travel agents,
   HR workers, vet techs. Fix the two extraction anomalies noted in B1.
2. Read the **IFC Vietnam women-owned enterprises market study** in full (B4).
3. Read the **NielsenIQ CPG analysis** and replace the Low-confidence consumer-spending
   claims with something citable, or drop the section (B12).
4. Find the **female share of sellers** on Vietnamese e-commerce / social commerce (B6).
5. Find **any non-vendor source** for no-show and retention rates in appointment
   businesses — academic, industry association, or payment-processor data (B7).
   If none exists, say so explicitly in the Master map.
6. Verify **female ownership share in pet grooming** and in boutique fitness studio
   ownership (B10, B11).
7. Check **Vietnamese GSO** data on female-headed household businesses
   (hộ kinh doanh) — likely a much better fit than company-registration data for the
   informal sector described in B5.
8. Resolve the **Vietnam salon licensing contradiction** in B5 against the MoH source.
9. Check **Zalo OA / Zalo Mini App** commercial capabilities and whether third-party
   automation is permitted — decisive for any Vietnam-facing product.
10. Establish whether the ~90–120 min/booking admin baseline in B9 holds up outside
    vendor testimonials.
