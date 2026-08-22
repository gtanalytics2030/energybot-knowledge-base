# GERC Forecasting, Scheduling, DSM Procedure - Part 02: Day-to-Day Requirements and Post-Facto Procedures

---

## Chunk 10: Day-to-Day Forecasting and Scheduling Submission Requirements

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsection 2.1

**PROVISION:** Section 2.1 – Day-to-Day Scheduling Submission

**TITLE:** Daily and Weekly Schedule Submission for Forecasting and Scheduling

**SUMMARY:**
Every RE generator or QCA must submit day-ahead schedules in 15-minute time blocks (96 blocks total covering 00:00 to 24:00 hours) and week-ahead schedules in hourly intervals by 9 AM every day. These schedules must be submitted for each pooling station or generator to enable SLDC to plan grid operations, balance supply and demand, manage system constraints, and coordinate with other market participants. Day-ahead schedules cover the entire following day; week-ahead schedules cover the following 7 days to support medium-term operational planning.

**KEY TOPICS:** Day-Ahead Schedule, Week-Ahead Schedule, 15-Minute Time Block, Hourly Schedule, 96 Blocks, Scheduling Deadline (9 AM), Pooling Station, RE Generator, QCA, Forecasting Submission

**TEXT:**
2.1 Every RE generator or QCA shall require to submit day ahead (15-minute time block) and week ahead schedule (hourly) by 9 AM every day for each pooling station / generator, as the case may be, from 00:00 hrs. to 24:00 hrs. for the next day as well as for the next week.

**REFERENCED PROVISIONS:** EASS Software scheduling requirements, Regulation 5.1 of GERC FSM Notification 2019

**CROSS-REFERENCES:** Section 2.2 (Available Capacity and Forecast Data Format), Section 2.3 (Wind Generator Revision Procedures), Section 2.4 (Solar Generator Revision Procedures), Section 2.5 (Day-Ahead and Week-Ahead Forecast Submission)

---

## Chunk 11: Available Capacity and Forecast Submission in EASS

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsection 2.2

**PROVISION:** Section 2.2 – Available Capacity (AvC) and Total DC/Forecast Submission

**TITLE:** EASS Software Data Submission – Available Capacity and Forecast Format

**SUMMARY:**
Every RE generator or QCA must submit day-ahead available capacity (AvC) and total DC/Forecast data via EASS software in 15-minute intervals covering all 96 time blocks (24 hours) using unique login credentials provided by SLDC. The https://www.sldcguj.org/lodestar/ccs/ portal provides the interface for this mandatory submission. Available capacity represents the maximum power the plant can generate in each time block; DC/Forecast represents the scheduled or predicted generation output. This data enables SLDC to optimize unit commitment, manage deviation settlement, and coordinate real-time grid operations.

**KEY TOPICS:** Available Capacity (AvC), DC/Forecast, Total DC, EASS Software, 15-Minute Interval, 96 Blocks, Login Credentials, SLDC Portal, Unique ID, Password, Generation Forecast, Capacity Forecast

**TEXT:**
2.2 Every RE generator or QCA shall require to submit day ahead "available capacity (AvC)" and "Total DC / Forecast" in 15 minute interval for 96 blocks in the EASS software as per link https://www.sldcguj.org/lodestar/ccs/ by using unique ID and password, which is provided by SLDC to RE generator or QCA as further visually elaborated by screen shot in Annexure 2.

**REFERENCED PROVISIONS:** EASS Software specifications, SLDC Portal access requirements, Annexure 2 (Screen shot and visual elaboration of EASS portal)

**CROSS-REFERENCES:** Section 2.1 (Schedule Submission Timing), Section 2.3-2.4 (Revision Procedures for Wind and Solar), Annexure 2 (EASS Portal screenshot showing Available Capacity and Forecast submission interface)

---

## Chunk 12: Wind Generator Forecast Revision Procedures – Maximum 16 Revisions

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsection 2.3

**PROVISION:** Section 2.3 – Wind Generator Forecast Revision – Conditions and Procedures

**TITLE:** Wind Generator Intraday Forecast Revision Procedures with ±2% Change Threshold

**SUMMARY:**
Wind generators or QCAs can revise forecasts up to a maximum of 16 revisions per day from 00:00 to 24:00 hours with the mandatory condition that the proposed schedule change must exceed ±2% from the previously submitted schedule in the affected time block. The revision becomes effective from the 4th time block after submission; no revision is implemented before the 4th time block even if the ±2% threshold is met. Wind generators can submit their first revision from 23:15 hours for the next day. This procedure prevents frivolous revisions, allows generators to adapt to changing wind conditions, and provides adequate lead time for SLDC grid operations planning.

**KEY TOPICS:** Wind Forecast Revision, Intraday Revision, 16 Revisions Maximum, ±2% Change Threshold, Schedule Revision, 4th Time Block Effectiveness, First Revision at 23:15, Revision Condition, Available Capacity Revision

**TEXT:**
2.3 Wind generators or QCA can revise forecast up to maximum 16 revisions from 00:00 hrs. to 24:00 hrs. for the same day with a condition of more than ± 2% change in "Schedule" / "Available capacity".

If QCA / RE Generators intents to revise its schedule, than the proposed schedule shall be more than ± 2% than that of previously given schedule of respective block.

To clarify further, the illustration is as below:

Suppose Revised DC is Updated at Block No: 12

| Current Schedule | Proposed DC For Next Revision | | |
|---|---|---|---|
| Block No | Schedule / DC (MW) | Block No | Schedule / DC (MW) |
| 15 | 50 | 15 | 49 |
| 16 | 45 | 16 | 45 |
| 17 | 40 | 17 | 40 |
| 18 | 50 | 18 | 50 |
| ... | ... | ... | ... |
| 96 | 50 | 96 | 50 |

The above revision cannot be submitted in the EASS because of change in time block No. 15 is not more than ± 2%.

Suppose Revised DC is Updated at Block No: 12

| Current Schedule | Proposed DC For Next Revision | | |
|---|---|---|---|
| Block No | Schedule / DC (MW) | Block No | Schedule / DC (MW) |
| 15 | 50 | 15 | 48 |
| 16 | 45 | 16 | 45 |
| 17 | 40 | 17 | 40 |
| 18 | 50 | 18 | 50 |
| ... | ... | ... | ... |
| 96 | 50 | 96 | 50 |

The above revision can be submitted and will be approved from 4th time block as change in 15th time block is more than ± 2%.

Such revision shall be effective from 4th time block of submission and no revision shall be implemented before 4th time block even though change is more than ± 2%.

Any wind generators / QCA can submit its first revision from 23:15 hrs. for the day for the next day.

**REFERENCED PROVISIONS:** Revision submission standards, EASS Software revision acceptance rules

**CROSS-REFERENCES:** Section 2.2 (AvC and Forecast Submission), Section 2.4 (Solar Generator Revision – similar procedure with different limits), Section 2.5 (Day-Ahead Forecast Procedures), Section 2.7 (Curtailment procedures requiring schedule adjustments)

---

## Chunk 13: Solar Generator Forecast Revision Procedures – Maximum 9 Revisions

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsection 2.4

**PROVISION:** Section 2.4 – Solar Generator Forecast Revision – Conditions and Procedures

**TITLE:** Solar Generator Intraday Forecast Revision with ±2% Threshold – Limited to 9 Revisions

**SUMMARY:**
Solar generators or QCAs can revise forecasts up to a maximum of 9 revisions per day from 05:30 to 19:00 hours (daylight operating period) with the mandatory condition that the proposed schedule change must exceed ±2% from the previously submitted schedule in the affected time block. The revision becomes effective from the 4th time block of submission; no revision is implemented before the 4th time block. Solar generators can submit their first revision from 23:15 hours for the next day. The lower revision limit (9 vs 16 for wind) and restricted timeframe (05:30-19:00) reflect solar generation's daylight-dependent nature and more predictable diurnal variation compared to wind generation.

**KEY TOPICS:** Solar Forecast Revision, Intraday Revision, 9 Revisions Maximum, ±2% Change Threshold, 05:30-19:00 Hour Window, 4th Time Block Effectiveness, Schedule Revision, First Revision at 23:15, Available Capacity Revision

**TEXT:**
2.4 Solar generators / QCA can revise forecast up to maximum 9 revisions from 05:30 hrs. to 19:00 hrs. for the same day with a condition of more than ± 2% change in "Schedule" / "Available capacity".

If QCA / RE Generators intents to revise its schedule, than the proposed schedule shall be more than ± 2% than that of previously given schedule of respective block.

To clarify further, the illustration is as below:

Suppose Revised DC is Updated at Block No: 40

| Current Schedule | Proposed DC For Next Revision | | |
|---|---|---|---|
| Block No | Schedule / DC (MW) | Block No | Schedule / DC (MW) |
| 45 | 50 | 45 | 51 |
| 46 | 45 | 46 | 45 |
| 47 | 40 | 47 | 40 |
| 48 | 50 | 48 | 50 |
| ... | ... | ... | ... |
| 96 | 50 | 96 | 50 |

The above revision cannot be submitted in the EASS because of change in time block No. 45 is not more than ± 2%.

Suppose Revised DC is Updated at Block No: 40

| Current Schedule | Proposed DC For Next Revision | | |
|---|---|---|---|
| Block No | Schedule / DC (MW) | Block No | Schedule / DC (MW) |
| 45 | 50 | 45 | 52 |
| 46 | 45 | 46 | 45 |
| 47 | 40 | 47 | 40 |
| 48 | 50 | 48 | 50 |
| ... | ... | ... | ... |
| 96 | 50 | 96 | 50 |

The above revision can be submitted and will approve from 4th time block as change in 45th time block is more than ± 2%.

Such revision shall be effective from 4th time block of submission and no revision shall be implemented before 4th time block even though change is more than ± 2%.

Any solar generators / QCA can submit its first revision from 23:15 hrs. for the day for the next day.

**REFERENCED PROVISIONS:** Solar generation forecasting standards, EASS revision acceptance criteria

**CROSS-REFERENCES:** Section 2.3 (Wind Generator Revision – similar structure with different parameters), Section 2.2 (AvC and Forecast Data), Section 2.5 (Day-Ahead Forecast Submission), Section 2.7-2.8 (Curtailment procedures)

---

## Chunk 14: Day-Ahead and Week-Ahead Forecast Submission Procedures

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsections 2.5 and 2.6

**PROVISION:** Section 2.5-2.6 – Day-Ahead and Week-Ahead Forecasting

**TITLE:** Day-Ahead Forecast and Week-Ahead Forecast Submission Channels and Timelines

**SUMMARY:**
Every RE generator or QCA must submit day-ahead forecasts using EASS software. Wind generators can submit revisions from 00:00 to 24:00 hours; solar generators only from 05:30 to 19:00 hours. Week-ahead forecasts must be submitted by each RE generator or QCA to SLDC through designated email addresses (provided by SLDC) for operational and planning purposes, giving visibility into power availability for the following 7 days. Day-ahead forecasts in EASS enable detailed 15-minute scheduling and real-time coordination; week-ahead forecasts submitted via email support broader grid planning, reserve management, and coordination with neighboring states.

**KEY TOPICS:** Day-Ahead Forecast, Week-Ahead Forecast, EASS Software, Email Submission, Revision Window, Wind Generator Hours (00:00-24:00), Solar Generator Hours (05:30-19:00), 7-Day Outlook, Operational Availability, Planning Availability

**TEXT:**
2.5 Every RE generator / QCA shall submit in the existing EASS software "Day ahead" forecast, be used for smooth forecasting and scheduling of RE generators. Wind Generators can submit revision from 00:00 hrs. to 24:00 hrs. and Solar Generators from 5:30 hrs. to 19:00 hrs. only.

2.6 "Week ahead" forecast shall be submitted by every RE generator / QCA to SLDC through e-mail ids (e-mail ids will be provided by SLDC) for operational & planning availability of power for next 7 (seven) days.

**REFERENCED PROVISIONS:** EASS Software submission procedures, SLDC email communication protocols

**CROSS-REFERENCES:** Section 2.1 (Submission deadlines – 9 AM), Section 2.2 (EASS portal data format), Section 2.3-2.4 (Revision procedures by generator type), Section 2.7-2.8 (Curtailment and dispatch coordination)

---

## Chunk 15: Curtailment Procedures – Emergency and Planned

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsections 2.7 and 2.8

**PROVISION:** Section 2.7-2.8 – Curtailment Procedures (Emergency and Planned)

**TITLE:** SLDC Curtailment Procedures for Grid Stability and System Constraints

**SUMMARY:**
SLDC may curtail RE generator injection schedules immediately from the very next time block if system constraints, grid stability concerns, or emergency situations arise. Curtailment instructions are conveyed to RE generators through SLDC/Sub-SLDC via best-effort communication; SLDC simultaneously updates the injection schedule in EASS. It is the RE generator's responsibility to check EASS for schedule updates and follow SLDC instructions. For planned curtailment in specific time blocks, SLDC revises and displays the updated injection schedule in EASS in advance. RE generators must check EASS regularly and strictly comply with revised schedules issued by SLDC for grid operations coordination.

**KEY TOPICS:** Curtailment, Emergency Curtailment, Planned Curtailment, Injection Schedule, System Constraint, Grid Stability, Grid Security, EASS Update, SLDC Instruction, Generator Responsibility, Emergency Response

**TEXT:**
2.7 For curtailment in the injection schedule of RE generators, if any due to system constraint or for grid stability / security or any emergency, SLDC will update the injection schedule of RE generator from very next time block in the EASS, also curtailment instruction shall be conveyed through SLDC / Sub SLDC on best effort basis. It is responsibility of RE generator to check the injection schedule in EASS and strictly follow the instruction of SLDC.

2.8 For planned curtailment, in certain time blocks of the day, injection schedule of RE generator will be revised and displayed by SLDC in the EASS. It is responsibility of RE generator / QCA to check the injection schedule in EASS and strictly follow the instruction of SLDC.

**REFERENCED PROVISIONS:** CERC Deviation Settlement Mechanism Regulations, Grid Code emergency procedures

**CROSS-REFERENCES:** Section 2.1-2.2 (Schedule management), Section 2.9 (Interstate RE generator procedures), Section 3.5 (Deviation Settlement procedures)

---

## Chunk 16: Interstate RE Generator Scheduling and Revision Procedures

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 2 / Subsection 2.9

**PROVISION:** Section 2.9 – Interstate RE Generator Forecasting and Scheduling

**TITLE:** Forecasting and Scheduling Procedures for Interstate Renewable Energy Generators

**SUMMARY:**
Wind and solar generators connected to the State grid and selling power outside Gujarat must follow CERC (Deviation Settlement Mechanism and Forecasting) Regulation 2014 (as amended) for forecasting and scheduling. Interstate RE generators submit day-ahead forecasts to the appropriate RLDC (Western RLDC for Gujarat) in 15-minute time blocks (00:00-24:00 hours) and simultaneously to SLDC-Gujarat with available capacity and forecast data for the same 96 time blocks. Interstate generators can revise schedules by advance notice to both WRLDC and SLDC-Gujarat, effective from the 4th time block of notice with one revision allowed per 1.5-hour time slot, subject to a maximum of 16 revisions per day. Individual available capacity and forecast data must be submitted to SLDC-Gujarat for 15-minute time blocks to enable state-level deviation tracking and settlement accounting.

**KEY TOPICS:** Interstate Generator, CERC Regulation, State Boundary Scheduling, RLDC (WRLDC), 15-Minute Time Block, Day-Ahead Forecast, Available Capacity, Forecast Submission, Schedule Revision, 1.5-Hour Time Slot, 4th Time Block Effectiveness, Regional Coordination, State Level Tracking

**TEXT:**
2.9 The Wind and Solar generators which are connected to State grid and selling power outside the Gujarat state, the forecasting and scheduling procedure is as per the CERC (Deviation Settlement Mechanism and Forecasting ) Regulation 2014 as be amended time to time. 

The Scheduling for interstate RE generator is to be done at state boundary by appropriate RLDC (WRLDC) through SLDC.

The interstate RE generator has to submit the day ahead forecast to appropriate RLDC (WRLDC) for every 15 minutes time block for the next day which is from 00:00 hrs. to 24:00 hrs., also submit the same to SLDC- Gujarat with "available capacity" and "Forecast" for every 15 minutes time block for 96 blocks.

Interstate RE generator can revise their Schedule by advance notice to WRLDC as well as SLDC-Gujarat, as the case may be. Such revision may be effective from 4th time block, the first being the time block in which notice given. There may be one revision for each time slot of one and half hours starting from 00:00 hours of a particular day subject to maximum of 16 revisions during the day.  

The same revised forecast/schedule is to be submitted to SLDC-Gujarat with individual "available Capacity" and "Forecast" for 15 minutes time block.

**REFERENCED PROVISIONS:** CERC (Deviation Settlement Mechanism and Forecasting) Regulation 2014 and amendments, WRLDC operating procedures, State boundary coordination protocols

**CROSS-REFERENCES:** Section 2.1-2.4 (Intrastate forecasting and revision procedures), Section 3.5 (Deviation Settlement accounting), Related to CERC regulations on interstate power flows

---

## Chunk 17: Post-Facto Procedure – Payment Based on Actual Generation

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 3 / Subsection 3.1

**PROVISION:** Section 3.1 – Commercial Payment Mechanism for RE Generators

**TITLE:** Post-Facto Tariff Payment for Actual Generation – State Energy Account Certification

**SUMMARY:**
Wind or solar generators connected to the State grid and selling power within the State are paid by the power purchase agreement (PPA) buyer based on actual generation at the tariff rate agreed in the PPA or wheeling agreement. The actual generation of all eligible RE generators under this regulation is certified monthly in the State Energy Account (SEA), which serves as the official record for billing and payment settlement. This post-facto settlement mechanism ensures that generators are remunerated for actual output rather than scheduled output, with the SEA certification providing regulatory verification of generation figures.

**KEY TOPICS:** Actual Generation, Payment Settlement, PPA Tariff, Wheeling Agreement, Power Purchase Agreement, State Energy Account (SEA), Monthly Certification, Post-Facto Payment, Buyer Payment, Tariff Rate

**TEXT:**
3.1 The wind or solar generators connected to the State grid and selling power within the State shall be paid by the buyer as per actual generation at the tariff agreed in the power purchase agreement or wheeling agreement. The actual generation of all eligible RE generators under this regulation shall be certified in monthly State Energy Account (SEA).

**REFERENCED PROVISIONS:** Power Purchase Agreement terms and conditions, Wheeling Agreement specifications, GERC Tariff Regulations

**CROSS-REFERENCES:** Section 3.2-3.3 (QCA authorization and de-pooling requirements), Section 3.5 (Deviation Settlement mechanisms), Related to PPA implementation and commercial arrangements

---

## Chunk 18: QCA Authorization and De-Pooling Responsibility

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 3 / Subsections 3.2 and 3.3

**PROVISION:** Section 3.2-3.3 – QCA Authorization and De-Pooling Obligations

**TITLE:** QCA Authorization Requirements and De-Pooling Liability Among Pooling Station Members

**SUMMARY:**
If a QCA receives authorization for forecasting and scheduling of a pooling station or windfarm/solar plant from its member generators but the authorization ratio does not cover 100% of installed pooling station capacity, the QCA must obtain written consent from all pooling station members (100% of capacity) to proceed. Even when authorization is below 100%, the QCA must submit the entire pooling station forecast as a consolidated entity and must de-pool (allocate) the deviation settlement (DSM) charges proportionally among all windfarm/solar generators of the pooling station. The QCA must collect DSM liability from all pool members up to 100% aggregate capacity and set off collected amounts with the DSM pool account. This procedure ensures all generators participate in settlement calculations and prevents any pool member from avoiding DSM liability obligations.

**KEY TOPICS:** QCA Authorization, Pooling Station, 100% Capacity Coverage, Unanimous Consent, De-Pooling, DSM Allocation, Deviation Settlement, Pool Member Liability, Collective Forecasting, Settlement Responsibility

**TEXT:**
3.2 If any QCA gets authorization for forecasting and scheduling of a particular windfarm / Solar Plant Pooling Station from its member, but the ratio of authorization is not 100% of Pooling Station installed capacity then it is responsibility of QCA to get the consent of all Pooling Station members (100% of Pooling Station).

3.3 Even though the authorization for forecasting and scheduling from wind / solar generators is not up to 100% of Pooling Station, the QCA has to submit the forecast of that Pooling Station as whole and QCA has to de- pool the DSM amount with all wind/solar generators of that Pooling Station and set off with DSM pool account by collecting amount up to 100% means from all wind / solar generators of that particular Pooling Station.

**REFERENCED PROVISIONS:** Pooling station guidelines per GERC Notification No. 1 of 2019, De-pooling procedures, DSM pool account management

**CROSS-REFERENCES:** Section 3.1 (Actual generation payment), Section 3.4 (QCA dispute resolution), Section 3.5 (Deviation Settlement mechanisms), Section 5 (QCA Qualifying Criteria)

---

## Chunk 19: QCA Dispute Resolution and Alternate QCA Selection

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 3 / Subsection 3.4

**PROVISION:** Section 3.4 – Dispute Resolution Between Generators and QCAs

**TITLE:** Mechanism for Dispute Resolution and Alternate QCA Selection

**SUMMARY:**
In case of disputes between generators and existing QCAs regarding forecasting, scheduling, or settlement services, the pooling station association or mutual agreement mechanism shall decide on selecting an alternate QCA. The alternate QCA selection occurs only after all past and current bills or dues are fully settled among disputing parties and with one month advance notice to all pool members. This procedure protects generators' right to change service providers while ensuring financial obligations are met and allowing adequate transition time for operations planning. The pooling station association acts as the neutral arbiter in such disputes.

**KEY TOPICS:** Dispute Resolution, Generator-QCA Dispute, Pooling Station Association, Alternate QCA, Settlement of Dues, One-Month Notice, Service Provider Change, Conflict Resolution, Bill Settlement

**TEXT:**
3.4 In case of dispute between generators and existing QCAs, the association of the pooling station shall decide alternate QCA after settlement of all past and current bills/due and with one-month advance notice.

**REFERENCED PROVISIONS:** Pooling station association bylaws and governance procedures, Settlement and reconciliation standards

**CROSS-REFERENCES:** Section 3.2-3.3 (QCA authorization), Section 5 (QCA Qualifying Criteria), Section 6 (QCA Registration Process)

---

## Chunk 20: Deviation Settlement – ABT Meter Data Collection and DSM Liability

**DOCUMENT:** GERC Notification No.1 2019 Forecasting, Scheduling, DSM & related matters Solar and Wind generation sources regulation 2019. Implementation Procedure

**DOCUMENT TYPE:** Regulation Implementation Procedure

**HIERARCHY:** Section 3 / Subsection 3.5 / Parts 3.5.1 and 3.5.2

**PROVISION:** Section 3.5.1-3.5.2 – Commercial Mechanism and Deviation Settlement

**TITLE:** Deviation Settlement Mechanism – ABT Meter Data Requirements and DSM Liability Framework

**SUMMARY:**
SLDC collects ABT meter data from QCAs, STUs, or distribution companies every Monday covering the previous 10 days of operations. The required data must be downloaded in encrypted format and submitted to SLDC within 48 hours of request. Wind and solar generators (intra-State transactions) that deviate from their submitted schedules are liable for deviation charges according to Table I and Table II of GERC Notification No.1 of 2019, which establishes graduated penalty rates based on absolute error percentages. The ABT meter provides the official measurement of actual generation versus scheduled generation, forming the basis for deviation calculation and financial settlement among market participants.

**KEY TOPICS:** Deviation Settlement, ABT Meter Data, 10-Day Data Collection, Encrypted Data, 48-Hour Submission, Deviation Charges, Schedule Deviation, Absolute Error, Intra-State Transaction, DSM Liability, Financial Settlement

**TEXT:**
3.5.1 SLDC shall require interface ABT meter data for the previous 10 days on the every Monday. QCA / STU / Distribution Company is required to provide downloaded encrypted data by e-mail on requirement from SLDC within 48 hours.

3.5.2. The wind or solar generators (Intra-State transaction) who deviate from its given schedule shall be liable to pay deviation charges as per the Table - I and Table - II of Hon'ble GERC Notification No.1 of 2019.

**REFERENCED PROVISIONS:** GERC Notification No.1 of 2019 Table I and Table II (Deviation Charge Schedules), ABT meter data standards, Encrypted data transmission protocols

**CROSS-REFERENCES:** Section 3.5.3-3.5.6 (Interstate generator deviation settlement, over-injection treatment, DSM pool accounting), Section 3.5.8 (ABT meter specifications), Section 1.2.1(d) (ABT meter technical requirements)

---

