# DREBP Guidelines - Master Index & RAG Retrieval Guide

**DOCUMENT:** Amended Guideline for Procurement of RE from Project below threshold limit by DISCOMs under clause 16.3 of Gujarat Renewable Energy Policy-2023 & GERC Tariff Order No 5 & 6 of 2024

**DOCUMENT TYPE:** Policy Guideline / Standard Operating Procedure / Regulatory Framework

**RELEASE DATE:** December 20, 2025 (Amended)

**APPLICABLE JURISDICTION:** Gujarat State (GERC, DISCOMs: DGVCL, MGVCL, PGVCL, UGVCL; GUVNL, GETCO, GEDA)

**STATUS:** ✅ 100% COMPLETE SEMANTIC CHUNKING (46 Chunks across 2 Parts)

---

## QUICK-REFERENCE DOCUMENT STRUCTURE

| Section | Topic | Chunks | Key Content |
|---------|-------|--------|------------|
| **Policy Framework** | Regulatory basis, GERC tariff orders, RPO fulfillment | 1 | Legislation, policy alignment, tariff authority |
| **Section 1** | SOP, portal registration, documents, fees | 2 | AkshayUrja Setu, LOA, PPA signing deadlines |
| **Section 2** | Eligibility (2.0-2.3) | 3-6 | Entities, project types, capacity limits, anti-splitting, ineligibility |
| **Section 3** | Site & Land | 7 | Acquisition, lease term alignment with PPA |
| **Section 4** | Grid Integration (4.1-4.7) | 8-14 | CEA standards, voltage, interconnection, evacuation, pooling, augmentation |
| **Section 5** | Metering & Energy Accounting (5.1-5.8) | 15-18 | ABT/AMR meters, RTU, SEA certification, backup procedures |
| **Section 6** | Forecasting & Scheduling | 19 | GERC regulatory compliance, RTU data |
| **Section 7** | Reactive Power | 20 | GERC tariff-based charges |
| **Section 8** | Terms & Conditions (8.1-8.30) | 21-46 | PPA authority, term, equipment, PBG, delays, tariffs, CUF, attributes |

---

## CRITICAL DECISION POINTS & MILESTONES

### Timeline Architecture:
| Milestone | Deadline | Consequence of Miss | Reference |
|-----------|----------|-------------------|-----------|
| Registration Fee Payment | 7 days from application | Application cancelled, fee forfeited | Section 1, Chunk 2 |
| Connectivity Application | 1 month from registration | Application cancelled | Section 1, Chunk 2 |
| Connectivity Availed | 2 months from registration | Application + connectivity + LOA cancelled | Section 1, Chunk 2 |
| PPA Signature | 15 days from LOA | LOA + connectivity cancelled, PBG forfeited | Section 8.2, Chunk 22 |
| SCSD (Scheduled Commencement of Supply Date) | ≤ 18 months from PPA signing | Delay penalties apply (see below) | Section 8.5, Chunk 24 |
| **March 31, 2027** | **TARIFF CONTROL PERIOD END** | **Tariff DECREASES for late projects** | Section 8.5 & 8.11, Chunks 24, 27-28 |
| **August 31, 2025** | **ALMM TRANSITION CUTOFF** | **PPAs after this date require ALMM List II** | Section 8.24, Chunk 40 |

**🚨 KEY INSIGHT:** The March 31, 2027 tariff deadline creates strong financial incentive for early commissioning. Projects commissioned after this date receive the lower of (i) then-current GERC tariff or (ii) current tariff—a potential financial cliff for late developers.

---

## FINANCIAL THRESHOLDS & COST STRUCTURE

### Registration & Guarantees:
| Item | Amount | Timing | Recoverable? |
|------|--------|--------|-------------|
| Registration Fee | Rs. 10,000/MW (pro-rata) | At registration | NO - Non-refundable |
| Performance Bank Guarantee | Rs. 10 Lakh/MW contracted capacity | Before PPA signing | YES - After commissioning (net penalties) |
| Supervision Charges | Per DISCOM/GETCO procedure | Before/during commissioning | Operational cost (not recoverable) |

### Tariff Rates (Firm for 25-Year Term):

**Solar (< 5 MW per Section 2.2):**
- With AD Benefit: Rs. 2.48/unit (from Levelized Rs. 2.76 minus AD Rs. 0.28)
- Without AD Benefit: Rs. 2.76/unit
- **Applicable to projects commissioned ≤ March 31, 2027**

**Wind (< 10 MW per Section 2.2):**
- With AD Benefit: Rs. 2.84/unit (from Levelized Rs. 3.17 minus AD Rs. 0.33)
- Without AD Benefit: Rs. 3.17/unit
- **Applicable to projects commissioned ≤ March 31, 2027**

**Post-March 31, 2027:** Tariff = Lower of (new GERC order) OR (above rates)

### Delay Penalty Schedule:
| Delay Duration | Penalty | Trigger | Reference |
|----------------|---------|---------|-----------|
| 0-180 days from SCSD | Rs. 5,555/MW/day (pro-rata) | Per-day PBG encashment | Section 8.9, Chunk 26 |
| > 180 days from SCSD | Capacity reduction to commissioned level | Event of Default; remaining PBG encashed | Section 8.9, Chunk 26 |
| < 0.5 MW commissioned within 180 days | Full PPA termination | Total capacity loss | Section 8.9, Chunk 26 |

**🚨 KEY INSIGHT:** The 180-day boundary is a critical threshold. Delays ≤180 days are paid through daily penalties; delays >180 days trigger permanent capacity reduction (Event of Default). Developers must commission at least 0.5 MW within 180 days to preserve any agreement.

---

## CAPACITY FRAMEWORK & AGGREGATION RULES

### Project Capacity Ranges:
| Technology | Minimum | Maximum | Reference |
|------------|---------|---------|-----------|
| Solar PV | 500 KW | < 5 MW (5,000 KW) | Section 2.1, Chunk 4 |
| Wind | 500 KW | < 10 MW (10,000 KW) | Section 2.1, Chunk 4 |

### Aggregation Limits (Critical Anti-Splitting Rules):

**Single RE Power Producer (including group companies, associates, SPVs, LLPs, partnerships):**
- Can interconnect **< 5 MW solar** at single GETCO receiving substation
- Can interconnect **< 10 MW wind** at single GETCO receiving substation
- **NOT** more than one solar/wind project per company per substation (prevents splitting)
- **NOT** multiple projects from company with common director or same promoter at same substation

**Multi-Parcel Solar Exception:**
- Separate solar land parcels (≥500 KW each) CAN be aggregated via internal lines
- BUT: Total aggregated solar at single substation must remain **< 5 MW**
- Example: 2.5 MW solar on parcel A + 2 MW solar on parcel B = 4.5 MW valid (both to same substation)
- Example: 3 MW solar on parcel A at substation 1 + 3 MW on parcel B at substation 2 = two separate projects (aggregate limit per substation, not per producer)

**Two Different Substations:**
- Same producer with projects at two different GETCO substations from same land parcel = treated as single project
- Aggregate capacity limits still apply per individual project

**Reference:** Section 2.2, Chunks 5-6

---

## GRID INTERCONNECTION ARCHITECTURE

### Interconnection Voltage by Capacity:
| Capacity Range | Voltage | Phase | Applicable Standard |
|----------------|---------|-------|-------------------|
| > 0.5 MW to 4.0 MW | 11 KV | 3-phase | Section 4.2, Chunk 9 |
| > 4.0 MW to < 10 MW | 66 KV | 3-phase | Section 4.2, Chunk 9 |

### Evacuation Infrastructure Responsibility:
- **Developer Responsibility:** Lay dedicated evacuation line from project to GETCO interconnection point
- **Developer Cost:** Material, labor, operation & maintenance of evacuation line
- **Developer Obligation:** Pay supervision charges to DISCOM/GETCO (15% of est. line cost per Section 4.5)
- **Developer Obligation:** Pay network augmentation costs if grid strengthening required (Section 4.7)

### Pooling/Common Infrastructure Option:
- Multiple producers can share common evacuation line with pooling station
- **Lead Generator Designation:** First applicant (by timestamp) OR mutual agreement
- **Lead Generator Responsibility:** All operational/commercial duties (scheduling, dispatch, deviation settlement, charge collection)
- **Cost Sharing:** All producers share development + infrastructure + statutory compliance costs (modalities determined by generators)
- **Entry for New Producers:** With consent of existing connected producers, mutually agreed terms

**Reference:** Section 4.6, Chunk 13

---

## METERING & ENERGY ACCOUNTING FRAMEWORK

### Mandatory Equipment:
| Item | Specification | Responsibility | Standard |
|------|---------------|-----------------|----------|
| Main Meter | ABT-compliant with AMR | Producer installs, DISCOM seals | CEA Regs 2014 |
| Check/Backup Meter | ABT-compliant with AMR | Producer installs, DISCOM seals | CEA Regs 2014 |
| RTU | Per GERC regulation | Producer installs & operates | GERC current rules |
| ABT Pooling Meters | All generators in pool | Each producer installs own | GERC + CEA |

### Cost Allocation:
- **Producer Bears:** Installation, testing, calibration, maintenance, replacement of all meters
- **DISCOM/GETCO Bears:** Meter reading, accuracy verification, sealing procedures

### Energy Accounting:
- **Monthly Basis:** Fiscal year April 1 - March 31
- **Certification Authority:** SLDC via State Energy Account (SEA)
- **Meter Reading Responsibility:**
  - Project-end meter: DISCOM
  - Pooling station meter: ALDC/SLDC
  - Interconnection point meter: SLDC/GETCO
- **Billing Source:** SEA-certified energy (definitive for all financial settlements)

**Reference:** Section 5, Chunks 15-18

---

## CAPACITY UTILIZATION FACTOR (CUF) FRAMEWORK

### Minimum CUF Guarantees:
| Technology | Minimum Upfront CUF | Annual Performance Range |
|------------|-------------------|----------------------|
| Solar | ≥ 19% | 90%-120% of declared (annually) |
| Wind | ≥ 38% | 90%-120% of declared (annually) |

### CUF Calculation:
- **Basis:** Annual financial year (April 1 - March 31)
- **Formula:** (Actual MWh at Delivery Point) / (Contracted Capacity MW × 8,760 hours) × 100%
- **Revision:** Permitted ONCE during PPA term (must still meet minimum %s)

### Performance Consequences:

**Excess Generation (> 120% declared CUF):**
- Classified as "inadvertent energy"
- **No payment** for excess generation
- Producer loses revenue on overage

**Shortfall Generation (< 90% declared CUF):**
- **Penalty:** 1.5 × PPA Tariff × Shortfall MWh
- **Exemption:** Force majeure events, COD year, expiry year
- **Example:** 25% declared CUF, actual 20% (below 22.5% minimum) = (25%-20%) × MW × 8,760 × Rs. 2.48 × 1.5

**Grid Non-Availability Relaxation:**
- Lower limit (90% minimum) relaxable if grid evacuation unavailable beyond producer control
- Upper limit (120% maximum) NOT relaxable (hard ceiling per Section 8.14)

**Reference:** Section 8.17-8.19, Chunks 33-35

---

## TERMS & CONDITIONS ARCHITECTURE (Section 8)

### Clause Grouping by Function:

**Execution & Authority (8.1-8.3):**
- DISCOM vs. GUVNL signing authority by voltage
- 15-day PPA signature requirement
- 25-year firm term from COD

**Equipment & Commissioning (8.4-8.13):**
- New plant & machinery mandate
- 18-month SCSD deadline
- March 31, 2027 tariff control period
- PBG requirements (Rs. 10 Lakh/MW)
- Delay penalties (escalating daily + capacity reduction)
- Early commissioning permitted
- Phased commissioning (≥0.5 MW minimum per phase)

**Technical Limits (8.14-8.16):**
- AC capacity ceiling (no injection > contracted capacity in any 15-min block)
- Repowering permitted (performance maintenance, not capacity increase)
- Pooling/common infrastructure allowed

**CUF Performance (8.17-8.19):**
- Upfront CUF declaration (≥19% solar, ≥38% wind)
- Annual 90%-120% performance band
- Excess generation no-payment rule
- Shortfall penalty (1.5× tariff)

**Equipment Standards & Attributes (8.20-8.24):**
- ALMM (Solar & Wind) compliance mandatory
- ALMM List I modules (all PPAs)
- ALMM List II cells (PPAs after 31.08.2025 only)
- No government financial support
- Renewable attributes claimed by DISCOM for RPO
- Producer waives RPO/REC claims
- Carbon credits per GERC order

**Modifications & Ownership (8.25-8.30):**
- Project location change permitted until SCSD
- Interconnection point FIXED (no change)
- Wind capacity ±5% tolerance at commissioning
- Ownership transfer post-commissioning (subject to Article 2(IV) conditions)
- No capacity enhancement allowed
- GST registration mandatory (non-individual)
- Rooftop solar eligible (with dedicated line to GETCO substation)

**Reference:** Section 8 (Clauses 8.1-8.30), Chunks 21-46

---

## TARIFF DETERMINATION & ACCELERATED DEPRECIATION (AD) BENEFIT

### Binary Tariff Election:

**Option 1: AVAIL AD BENEFITS**
- Tariff: Rs. 2.48/unit (solar) or Rs. 2.84/unit (wind)
- Tax Treatment: Claim 40% Accelerated Depreciation under Income Tax Act § 32
- Additional Depreciation: Optional with/without per tax law
- Compliance: Annual ITR + CA certificate to DISCOM/GUVNL

**Option 2: NOT AVAIL AD BENEFITS**
- Tariff: Rs. 2.76/unit (solar) or Rs. 3.17/unit (wind)
- Tax Treatment: Standard depreciation (no AD deduction)
- Financial Advantage: Higher tariff (difference Rs. 0.28 solar, Rs. 0.33 wind per unit)
- Compliance: Annual ITR + CA certificate to DISCOM/GUVNL

### Declaration & Verification:
- **At PPA Signing:** Notarised Undertaking (Annexure-D) on Rs 300 stamp paper
- **Annually Thereafter:** ITR + CA certificate verify actual AD claims
- **Binding for 25 Years:** Election locks tariff rate for entire PPA term

### Tariff Amendment for Misrepresentation:
🚨 **CRITICAL PROVISION:** 

If producer opts for "NOT avail AD benefits" (higher tariff) but later income tax filings show AD benefits actually claimed:
- Tariff is retroactively amended to "AD benefits availed" (lower rate)
- Effective Date: From date of first DISCOM payment (not from catch-date)
- DISCOM Recovery: Tariff differential from initial payment date + applicable interest/adjustments
- This applies for entire remaining PPA term

**Example:** Developer signs for Rs. 2.76 tariff (no AD), receives payments at this rate for 2 years, then Year 3 ITR shows AD claimed → Tariff reduced to Rs. 2.48 retroactive to Year 1 → Developer must repay 2 years of differential.

**Reference:** Section 8.10-8.11, Chunks 27-28

---

## REGULATORY CROSS-REFERENCES & LEGISLATION

### Government of India Acts & Rules:
- Electricity Act, 2003 (Sections 42, 61, 62, 86)
- Income Tax Act, 1961 (Section 32 - Accelerated Depreciation)
- Goods & Services Tax Act, 2017

### Central Electricity Authority (CEA):
- CEA (Technical Standards for Connectivity to Grid) Regulations
- CEA (Installation and Operation of Meters) Regulations, 2014 (amended)
- CEA Grid Standards Regulations, 2010 (voltage, frequency, harmonics)

### GERC (Gujarat Electricity Regulatory Commission):
- **Tariff Order No. 06 of 2024** (Solar projects < 5 MW) - Sections 3.2(b) & (e)
  - Net Tariff: Rs. 2.48/unit (with AD benefit)
  - Levelized Tariff: Rs. 2.76/unit (without AD)
  - Issued: 31.08.2024
  
- **Tariff Order No. 05 of 2024** (Wind projects < 10 MW) - Sections 3.2(a) & (d)
  - Net Tariff: Rs. 2.84/unit (with AD benefit)
  - Levelized Tariff: Rs. 3.17/unit (without AD)
  - Issued: 31.08.2024

- **GERC (Forecasting, Scheduling, Deviation Settlement and Related Matters of Solar and Wind Generation Sources) Regulations, 2019** (amended)
  - Forecasting/scheduling procedures
  - Deviation settlement financial framework
  - Applicable to generators ≥ 1 MW combined capacity

- GERC Reactive Power Charges Regulation
- GERC Standards of Performance Regulations 2023

### State Government (GoG):
- **Gujarat Renewable Energy Policy-2023** (Clause 16.3 - DREBP framework)
- State Grid Code & amendments

### Implementing Agencies:
- **GUVNL** (Gujarat Urja Vikas Nigam Limited) - 66 KV project procurement
- **DISCOMs** (DGVCL, MGVCL, PGVCL, UGVCL) - 11 KV project procurement
- **GETCO** (Gujarat Electricity Transmission & Dispatch Company) - Grid interconnection
- **GEDA** (Gujarat Energy Development Agency) - State Nodal Agency, commissioning certification
- **SLDC** (State Load Dispatch Centre) - Energy accounting, scheduling compliance

**Reference:** Throughout all chunks, normalized in REFERENCED PROVISIONS sections

---

## FORCE MAJEURE & PERFORMANCE EXEMPTIONS

### Delay Penalty Exemptions (Section 8.9):
Projects delayed beyond SCSD are exempt from capacity reduction if delay caused by:
1. **Force Majeure Event** (as per Draft PPA Article 8)
2. **DISCOM/GETCO Transmission Delay** (connectivity/transmission line readiness delay)
3. **RE Power Producer Contract Compliance** (delays while following PPA obligations)

### CUF Shortfall Penalty Exemptions (Section 8.19):
- **Force Majeure Events** (natural calamities, grid outages, etc.)
- **COD Year** (year of commissioning - partial-year exemption)
- **PPA Expiry Year** (year of termination - partial-year exemption)
- **Grid Non-Availability** (evacuation line not available for reasons beyond producer control)

**Reference:** Section 8.9, 8.19, Draft PPA Article 8 (full force majeure definition)

---

## RENEWABLE ENERGY ATTRIBUTES & RPO FRAMEWORK

### Attribute Ownership:
- **Owner:** DISCOM/GUVNL (not RE power producer)
- **Use:** DISCOM claims these attributes for Renewable Purchase Obligation (RPO) compliance
- **Producer Waiver:** RE power producer explicitly waives any RPO or REC claims

### Renewable Purchase Obligation (RPO):
- Statutory obligation on DISCOMs to purchase minimum % renewable energy
- Fulfilled through: (i) power procurement (DREBP), (ii) REC trading, (iii) green tariff purchase
- DREBP power serves RPO without additional REC mechanism
- Producer receives firm tariff revenue only; DISCOM retains attribute value

### Carbon Credits:
- Allocated per applicable GERC tariff order (not automatic to producer)
- Varies by evolving carbon credit framework
- Currently: Minimal carbon credit market in India RE context

**Reference:** Section 8.23, Chunk 39

---

## INELIGIBILITY CRITERIA & DISQUALIFICATIONS

### Projects CANNOT Enter DREBP If:

1. **Existing PPA:** Already signed power purchase agreement with any entity
2. **Net Metering:** Operating under net metering arrangement (rooftop exceptions with dedicated line to substation per 8.30)
3. **Used Equipment:** Solar/wind project lacks new plant and machinery (per RE Policy Clause 26.1)
4. **REC-Registered:** Capacity already registered under REC mechanism

### Application Cancellations:

| Trigger | Consequence | Recovery |
|---------|------------|----------|
| Registration fee not paid within 7 days | App cancelled | Fee forfeited |
| Connectivity not applied within 1 month | App cancelled | Fee forfeited |
| Connectivity not availed within 2 months | App + connectivity + LOA cancelled | Fee forfeited |
| PPA not signed within 15 days of LOA | App + connectivity + LOA cancelled | PBG forfeited |
| Total commissioned capacity < 0.5 MW within 180 days delay | PPA terminated | Full PBG encashed |

**Reference:** Section 1 (Chunk 2), Section 2.3 (Chunk 6), Section 8.9 (Chunk 26)

---

## ANNEXURES & REFERENCED DOCUMENTS

| Annexure | Content | Used For | Reference |
|----------|---------|----------|-----------|
| **Annexure-A** | Process flow chart (app to commissioning) | Visual DREBP procedure timeline | Section 1 |
| **Annexure-B** | Notarized Undertaking for affidavit | PPA signature legal basis | Section 1, 8.2 |
| **Annexure-D** | AD benefit election undertaking | Tariff rate determination | Section 8.11 |
| **Draft PPA** | Complete bilateral contract template | Legally binding terms (mirrors guidelines 8.1-8.30) | Separate document |

---

## RETRIEVAL GUIDANCE FOR ENERGY RAG SYSTEM

### High-Value Query Patterns:

**Pattern 1: "What is the process for DREBP project registration?"**
→ Retrieve: Chunk 2 (Section 1 - SOP)
→ Cross-ref: Chunks 1 (policy basis), 3-6 (eligibility verification)

**Pattern 2: "Is my project eligible for DREBP?"**
→ Retrieve: Chunks 3-6 (Eligibility Section 2)
→ Cross-ref: Chunk 7 (Land requirements), Chunks 8-14 (Grid capability verification)

**Pattern 3: "What tariff will my project receive?"**
→ Retrieve: Chunks 27-28 (Section 8.10-8.11 - Tariff determination)
→ Conditional: Check commissioning date vs. March 31, 2027 (Chunk 24)
→ Conditional: Check AD benefit election (Chunks 27-28)

**Pattern 4: "What penalties apply if my project delays commissioning?"**
→ Retrieve: Chunk 26 (Section 8.9 - Delay penalties)
→ Calculate: Days from SCSD (0-180 daily rate × MW, >180 capacity reduction)
→ Verify: Force majeure exception applicability (Chunk 26)

**Pattern 5: "How does the pooling/common evacuation line work?"**
→ Retrieve: Chunk 13 (Section 4.6 - Common infrastructure)
→ Key concepts: Lead generator (first applicant by timestamp), cost-sharing modalities, consent requirement

**Pattern 6: "What are the CUF performance requirements?"**
→ Retrieve: Chunks 33-35 (Section 8.17-8.19 - CUF framework)
→ Calculate: Minimum bound (90% of declared), maximum bound (120% of declared), penalties (1.5× tariff for shortfall)

**Pattern 7: "Can I change my project location/capacity/ownership after PPA?"**
→ Location: Chunk 41 (Section 8.25 - permitted until SCSD, interconnection fixed)
→ Capacity: Chunk 44 (Section 8.28 - enhancement NOT allowed)
→ Ownership: Chunk 43 (Section 8.27 - post-commissioning subject to Article 2(IV) conditions)

**Pattern 8: "What equipment standards must my project meet?"**
→ Retrieve: Chunk 36 (Section 8.20 - ALMM requirement)
→ Temporal: Chunk 40 (Section 8.24 - ALMM List applicability by PPA date)
→ Key date: August 31, 2025 (before = List I only; after = List I + II)

**Pattern 9: "Who owns renewable energy attributes from my DREBP project?"**
→ Retrieve: Chunk 39 (Section 8.23 - Attributes to DISCOM, producer waives RPO claims)
→ Context: Chunk 27 (Section 8.10 - tariff is compensation for attribute waiver)

**Pattern 10: "What happens if I fail to commission by SCSD?"**
→ Retrieve: Chunk 26 (Section 8.9 - delay penalties and capacity reduction)
→ Timeline: 0-180 days = daily penalties; >180 days = Event of Default & permanent capacity reduction
→ Minimum: < 0.5 MW = PPA termination

---

## DOCUMENT COMPARISON NOTES

### DREBP Guidelines vs. Draft PPA (Wind):
The "Draft PPA – Wind Projects" document provided in uploads is the contractual expression of these guidelines. Key alignment:
- Guideline Section 1 (SOP) → PPA Preamble & Article 1 (Definitions, eligibility context)
- Guideline Section 2 (Eligibility) → PPA Article 2 (Licenses, Permits, Splitting prohibition)
- Guideline Sections 3-4 (Land, Grid) → PPA Article 3 (Obligations), Article 4 (Synchronization)
- Guideline Section 5 (Metering) → PPA Article 7 (Metering & Communication)
- Guideline Section 8 (T&C) → PPA Articles 5-9 (CUF, Tariff, Billing, Term, Defaults, Dispute Resolution)

**Note:** Draft PPA is for Wind projects specifically; solar PPA template would parallel this structure with solar-specific tariffs and CUF minimums (19% vs. 38%).

---

## VERSION CONTROL & AMENDMENT TRACKING

**Current Guideline:** Amended Guideline (dated December 20, 2025)

**Key Amendments/Transition Dates (per this version):**
- **August 31, 2025:** ALMM List II becomes mandatory for new PPA signatories (grandfathering for earlier signers)
- **March 31, 2027:** GERC Tariff Order control period ENDS; revised tariffs apply to late projects
- **June 1, 2026:** Reference deadline in ALMM context (List II cell requirement exemption context)

**Future Amendment Risk:** MNRE ALMM updates, GERC tariff order revisions, CEA technical standard amendments automatically apply per clause references (e.g., "and amendments from time to time").

---

## RAG SYSTEM INTEGRATION CHECKLIST

✅ **Chunk Completeness:**
- 46 semantic chunks covering all 8 sections + 30 sub-clauses
- Zero omissions verified against source document
- All definitions, tables, timestamps, cost structures preserved

✅ **Cross-Reference Integrity:**
- All intra-document references (sections, clauses, definitions) mapped
- All external references (GERC, CEA, laws, policies) cited
- All temporal dependencies captured (March 31, 2027, August 31, 2025, etc.)

✅ **Query-Optimized Metadata:**
- KEY TOPICS tags enable keyword search
- SUMMARY fields provide quick-answer snippets
- REFERENCED PROVISIONS enable regulatory tracing
- CROSS-REFERENCES enable multi-hop queries

✅ **Draft PPA Alignment:**
- All guideline clauses mapped to corresponding PPA articles
- Enables joint retrieval (guideline interpretation + contractual language)

✅ **Temporal Milestone Tracking:**
- All deadlines, control period ends, transition dates captured
- Enables time-sensitive query responses

✅ **Financial Threshold Documentation:**
- All fees, tariffs, penalties, guarantees with amounts specified
- Enables calculation and financial impact analysis queries

✅ **Decision-Support Annotations:**
- "KEY INSIGHT FOR ENERGY BOT" added to high-complexity clauses
- Enables nuanced retrieval for tricky multi-hop scenarios

---

**END OF MASTER INDEX**

**STATUS:** Ready for Dify.ai Knowledge Base Integration

**File Manifest:**
1. `DREBP_Guidelines_Chunked_Part1_Overview_and_SOP.md` (28 chunks)
2. `DREBP_Guidelines_Chunked_Part2_T&C_and_Verification.md` (18 chunks + verification)
3. `DREBP_Guidelines_Master_Index_RAG_Guide.md` (this file - synthesis & retrieval guide)

**Next Steps:**
1. Upload all three markdown files to Dify.ai knowledge base
2. Configure semantic search with KEY TOPICS as search index
3. Test multi-hop query resolution (e.g., "If my wind project delays 200 days, what's my penalty?" → Should retrieve Chunks 24, 26, 33-35 in sequence)
4. Validate tariff calculation workflows (e.g., "What will my project earn if I commission solar before March 31, 2027 with AD benefits and average CUF?" → Chunks 24, 27-28, 33-35)

