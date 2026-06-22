DOCUMENT: GERC (Terms and Conditions for Green Energy Open Access) Regulations, 2024
DOCUMENT TYPE: GERC Regulation
HIERARCHY: Regulation 20
PROVISION: Regulation 20
TITLE: Metering Requirements for Green Energy Open Access - Standards, Installation, and Real-Time Monitoring

SUMMARY:
Regulation 20 establishes mandatory metering infrastructure for all GEOA consumers to enable accurate energy accounting, billing, and real-time grid monitoring. ABT-compliant 4-quadrant meters are required for capacity ≥1 MW at both generator and consumer interface; Special Energy Meters on 15-minute basis for <1 MW; RTU (Remote Terminal Unit) installation at the metering point for SLDC connectivity; CEA Standards compliance; maintenance by Metering Service Provider; and access for third-party inspection. These technical specifications ensure inter-state transmission system (InSTS) compatibility, banking mechanism functionality, and transparent energy settlement.

KEY TOPICS:
- ABT-compliant 4-quadrant meters (≥1 MW)
- Special Energy Meters (<1 MW) on 15-minute basis
- Meter placement: Generator end, Interface point, Consumer/Load point
- RTU (Remote Terminal Unit) installation and connectivity
- Real-time data transmission to SLDC
- Metering point at nearest substation
- Meter installation costs (consumer bears)
- CEA (Central Electricity Authority) Standards compliance
- Metering Service Provider maintenance
- Third-party inspection and verification

TEXT:

**Regulation 20: Metering**

I. **Meter Type Requirements**

(a) **For Green Energy Open Access Capacity of 1 MW and above:**

   (i) **ABT-Compliant 4-Quadrant Meters:** All metering equipment shall be Automatic Billing Threshold (ABT) compliant 4-quadrant meters capable of measuring and recording electricity flow in four quadrants:
   - Quadrant 1: Active Power (Real) - Injecting, Frequency above nominal
   - Quadrant 2: Active Power (Real) - Injecting, Frequency below nominal
   - Quadrant 3: Active Power (Real) - Withdrawing, Frequency below nominal
   - Quadrant 4: Active Power (Real) - Withdrawing, Frequency above nominal

   Additionally: Reactive Power (kVARh) measurement in all four quadrants for power factor and reactive energy accounting.

   (ii) **Meter Locations - Three Points of Metering:**
   - **Generator End Meter:** At the generating station to record all power generated
   - **Interface/Point of Supply Meter:** At the interconnection point with transmission/distribution network
   - **Consumer/Load Point Meter:** At the consumer premises where energy is consumed

   (iii) **Meter Standards:** All meters shall comply with:
   - Central Electricity Authority (CEA) Standards and Regulations
   - IEC (International Electrotechnical Commission) Standards: IEC 61036 / IEC 61268
   - Indian Standards: IS 13779, IS 14697
   - NABL (National Accreditation Board for Testing and Calibration Laboratories) accredited calibration

(b) **For Green Energy Open Access Capacity less than 1 MW:**

   (i) **Special Energy Meter:** Instead of ABT-compliant 4-quadrant meters, a Special Energy Meter with the following specifications:
   - Capable of measuring energy on 15-minute time-block basis
   - Recording both import (withdrawal) and export (injection) of energy
   - Automated data logging and time-stamped records
   - Communication interface for remote reading

   (ii) **Meter Location:**
   - **Single Meter Location:** At the consumption point (consumer premises)
   - **Two-way Flow Capability:** Must record both inflow (grid supply) and outflow (generation export) in separate registers

   (iii) **Data Transmission:**
   - Energy data in 15-minute intervals
   - Daily reconciliation and settlement based on 15-minute blocks
   - Automated transmission to SLDC/State Nodal Agency for load profiling

II. **RTU (Remote Terminal Unit) Installation and Connectivity**

(a) **Mandatory RTU Requirement:** A Remote Terminal Unit (RTU) shall be installed at the metering point for:
   - Real-time data acquisition from the meter
   - Real-time transmission of energy flow data to State Load Dispatch Centre (SLDC)
   - Grid frequency and voltage monitoring
   - Power quality parameters (THD, PF, harmonics)

(b) **RTU Technical Specifications:**
   - **Communication Protocol:** IEC 60870-5-104 or IEC 61850 compliant
   - **Polling Frequency:** Minimum 1-second resolution for critical parameters
   - **Data Transmission:** Real-time (continuous or 15-minute intervals as prescribed)
   - **Redundancy:** Dual communication paths (primary and backup) for critical installations
   - **Storage:** Local data storage for minimum 3 months of 15-minute interval data

(c) **SLDC Connectivity:**
   - RTU shall be connected to the State Load Dispatch Centre via:
     - Dedicated leased lines (preferred), or
     - VPN (Virtual Private Network) connectivity, or
     - Other approved secure communication channels
   - The distribution licensee / transmission licensee shall ensure RTU connectivity and maintenance
   - Cost: Borne by the Green Energy Open Access consumer (as per Transmission and Wheeling Agreement)

(d) **Data Transmission and Accessibility:**
   - Real-time energy data shall be transmitted to SLDC every 15 minutes
   - Historical data shall be accessible to:
     - The consumer (via portal)
     - The State Nodal Agency (for monitoring and settlement)
     - The Commission (for regulatory oversight)
     - Third-party auditors (for verification)
   - Access logs shall be maintained for audit trail purposes

III. **Metering Point Location and Installation**

(a) **Primary Metering Point:** The nearest electrical substation to:
   - The generator (for injection metering), or
   - The consumer (for withdrawal metering)
   - As decided by the transmission licensee / distribution licensee in consultation with the consumer

(b) **Physical Installation Standards:**
   - Meters shall be housed in approved enclosures (meter cabins / panels)
   - Protection against weather, temperature variation, and unauthorized tampering
   - Proper earthing and surge protection
   - Locks and sealing as per IS standards
   - Nameplate and identification markings visible and accessible

(c) **Accessibility for Inspection:**
   - Metering installation shall be accessible to:
     - Authorized representatives of the transmission/distribution licensee
     - Authorized representatives of the consumer
     - Official meter inspectors of the Commission
     - Third-party auditors authorized by the consumer or State Nodal Agency
   - Access shall be provided within 2 working days of request

IV. **Meter Installation and Maintenance Costs**

(a) **Meter Cost Responsibility:**
   - **Consumer Obligation:** The Green Energy Open Access consumer shall bear all costs of:
     - Procurement of meters (ABT meters or Special Energy Meters as applicable)
     - RTU procurement and installation
     - Wiring and accessories from the meter location to the interface point
     - Testing and calibration before commissioning
     - Initial installation labor and supervision

   (b) **Licensee Cost:**
     - The transmission/distribution licensee shall bear costs of:
       - Meter installation at the interface point (on licensee property)
       - RTU connectivity and communication infrastructure
       - Maintenance of RTU and communication equipment
       - Server-side software and data management systems

(c) **Meter Maintenance and Calibration:**
   - **Maintenance Provider:** A NABL-accredited Metering Service Provider (MSP) approved by the Commission
   - **Maintenance Frequency:**
     - Annual inspection and cleaning
     - Five-yearly recalibration / replacement
     - Post-disturbance inspection (after lightning, surge, or suspected tampering)
   - **Cost:** Borne by the consumer (typically included in annual service charge)
   - **Maintenance Certificate:** Proof of calibration shall be submitted to the State Nodal Agency annually

(d) **Replacement Protocol:**
   - If meter is found defective or damaged, replacement shall be done within 5 working days
   - During replacement, energy accounting shall be based on:
     - Last valid meter reading, or
     - Average of preceding 3 months (if last reading is >3 months old)
   - Replacement cost: If defect is due to consumer negligence, consumer pays; otherwise, licensee / manufacturer responsible

V. **Meter Accuracy and Verification Standards**

(a) **Accuracy Classes:**
   - **ABT Meters (≥1 MW):** Class 1 accuracy (maximum ±1% error)
   - **Special Energy Meters (<1 MW):** Class 2 accuracy (maximum ±2% error)
   - Verification by NABL-accredited laboratory before installation

(b) **Meter Testing:**
   - Before commissioning: Type approval test and batch test per CEA Standards
   - After installation: Functional test and communication test
   - Annual verification: Random sample check by Commission's nominated agency
   - Seal check and tamper indication inspection monthly

(c) **Dispute Resolution for Meter Accuracy:**
   - If consumer disputes meter readings, meter shall be sent for calibration by third-party NABL-accredited lab at consumer's cost initially
   - If meter error >0.5%, all previous charges (up to 3 months preceding dispute) shall be adjusted on pro-rata basis
   - Laboratory certificate shall be final unless challenged with higher authority evidence

VI. **Real-Time Monitoring and Data Security**

(a) **SLDC Monitoring Dashboard:**
   - SLDC shall maintain a real-time dashboard showing:
     - Instantaneous power injection/withdrawal for each GEOA consumer
     - Cumulative energy for the billing period
     - Frequency and voltage at metering point
     - Alerts for abnormal power swings or meter malfunction

(b) **Data Security and Cyber Protection:**
   - Encrypted communication channels for all data transmission
   - Multi-factor authentication for portal access
   - Regular backup of metering data (daily) at secure locations
   - Audit trail of all data access and modifications
   - Compliance with Information Security Guidelines prescribed by the Commission

(c) **Transparency and Accessibility:**
   - Consumer shall have real-time view of their energy data via portal
   - Downloadable detailed billing reports (hourly, daily, monthly summaries)
   - Anomaly alerts (sudden power drop, meter communication loss, etc.)

VII. **Special Provisions for Specific Cases**

(a) **Captive Generating Plants:** Captive consumers with <1 MW shall also maintain Special Energy Meters even if used only for self-consumption, to:
   - Verify compliance with self-consumption criteria (minimum 51% per Schedule I)
   - Ensure tax compliance for any exported energy

(b) **Solar/Wind Variability:** For renewable sources with inherent variability (wind, solar):
   - 15-minute averaging of power output is standard to account for cloud cover, wind gusts
   - No penalties for natural generation variation within forecasted range
   - Deviation tracking per GERC Forecasting/Scheduling Regulations, 2019

(c) **Hybrid Projects (Wind-Solar):** Meters shall separately record:
   - Wind component energy
   - Solar component energy
   - Combined output
   - This enables separate REC accounting and tariff optimization

VIII. **Meter Failure and Recovery Procedures**

(a) **Meter Communication Loss:**
   - If RTU communication is lost for >1 hour, SLDC shall be notified immediately
   - Estimated consumption based on average of preceding 3 days shall be assumed for settlement
   - Consumer shall be compensated for any billing errors discovered after meter restoration

(b) **Billing During Meter Fault:**
   - If meter is defective and repairs take >5 days, average billing for 3 preceding months shall apply
   - Excess/deficiency shall be adjusted in subsequent billing period
   - Consumer is not penalized for meter manufacturer defects

REFERENCED PROVISIONS:
- CEA (Central Electricity Authority) Standards and Regulations
- IEC 61036 / IEC 61268 (Meter Standards)
- IS 13779, IS 14697 (Indian Standards)
- Section 62 of Electricity Act, 2003 (Metering requirements for wheeling)
- Regulation 13 (GEOA grant requirements)
- Regulation 16 (Energy Accounting - dependent on metering)
- Regulation 17.1-17.10 (Charges calculation - based on metered energy)
- GERC Forecasting, Scheduling and Deviation Regulations, 2019
- National Accreditation Board for Testing and Calibration Laboratories (NABL) Standards

CROSS-REFERENCES:
- Regulation 3(q) "Installation" (metering infrastructure definition)
- Regulation 3(p) "Green Energy Open Access Consumer" (metering obligation)
- Regulation 3(e) "Captive Generating Plant" (special metering for self-consumption verification)
- Regulation 9 (Eligibility - ABT meters required for ≥1 MW)
- Regulation 13 (GEOA grant - metering specified in agreement)
- Regulation 16 (Energy Accounting - 15-minute blocks per metering)
- Regulation 19 (Dispute Resolution - meter accuracy disputes)
- Schedule I (Captive verification - requires metering records)

⭐ **KEY INSIGHT FOR ENERGY BOT:**

Metering is the single point of truth for energy accounting and billing. All GEOA charges (Transmission, Wheeling, CSS, AS, Banking) depend on accurate metering. The regulation mandates:
- **Technical rigor:** ABT compliance, 4-quadrant capability, CEA standards
- **Real-time transparency:** SLDC connectivity, portal visibility, no black-box billing
- **Consumer protection:** Third-party inspection rights, dispute resolution, compensation for meter faults
- **Cost fairness:** Consumer bears meter procurement; licensee bears connectivity and maintenance

For Dify integration: Queries about metering failures, billing disputes, meter replacement timelines, or data access rights should reference this regulation comprehensively.

