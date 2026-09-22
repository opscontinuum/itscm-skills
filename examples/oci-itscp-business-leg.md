# Worked example: the business leg, run end to end

**System:** Oracle E-Business Suite on Exadata, OCI `us-ashburn-1` with regional DR to
`us-phoenix-1`.

**The architecture is not described here.** It lives in
[`opscontinuum/oci-itscp`](https://github.com/opscontinuum/oci-itscp), a separate public
repository, and every file path cited below names a file in *that* repository, not this one.
The three cited most:

- [`docs/01-architecture.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/01-architecture.md) the two-region, two-availability-domain design
- [`docs/02-mtd-tiers.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/02-mtd-tiers.md) the recovery tiers and what each one's replication achieves
- [`checklists/tier-assignment-workshop.md`](https://github.com/opscontinuum/oci-itscp/blob/main/checklists/tier-assignment-workshop.md) the session this example performs

**Role played:** product owner for the program, who came in with three requirements: the system
is operated as realtime, availability is committed at **99.9%**, and data loss is to be **zero
or near zero**.

**Session:** `bia-workshop`, steps 1 through 4. Signatures are assumed for this exercise; the
mechanism that makes a signature bind to content is not yet designed.

This is what a completed business leg looks like. Every number below is the hypothetical
business's, not a default, and a real program replaces all of them.

---

## Step 0: what the product owner asked for, checked against the architecture

Before any process was named, three stated requirements were tested against what
[`docs/02-mtd-tiers.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/02-mtd-tiers.md) says the system can do. Two hold. One needed a correction the product
owner accepted.

### 99.9% and a fifteen minute recovery are compatible. 99.99% would not have been

| Commitment | Downtime allowed | Tier 0 recovery costs | Events the budget permits |
|---|---|---|---|
| 99.9% | 43.8 min/month, 8.8 hr/year | RTO 15 min + WRT 30 min = **45 min** | About **one per month** |
| 99.99% | 4.4 min/month, 52.6 min/year | the same 45 min | About **one per year** |

At 99.99% a single recovery event consumes roughly ten months of the annual budget, which makes
the availability number and the recovery number nearly incompatible: the commitment is really
about never invoking recovery rather than about recovering quickly.

**At 99.9% they are coherent.** One Tier 0 event consumes about one month's allowance, and the
year absorbs roughly eleven. That is a number an operations team can actually be held to, and it
is why 99.9% is the right ask for a system with a fifteen minute RTO.

Recorded as a finding rather than assumed: the product owner's looser availability number is the
more rigorous one.

### Zero RPO is available, and it is available in one direction only

[`docs/02-mtd-tiers.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/02-mtd-tiers.md) and [`docs/01-architecture.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/01-architecture.md) give two replication legs with different
properties:

| Failure | Mechanism | Data loss |
|---|---|---|
| Availability domain, Ashburn AD-1 lost | Oracle Data Guard **SYNC** standby in AD-2, Maximum Availability protection mode | **Zero**, while the standby is synchronized |
| Region, all of Ashburn lost | Active Data Guard **ASYNC** to Phoenix | **Under 30 seconds**, measured transport lag |

So "zero or near zero" maps cleanly onto the design, and the two halves are committed
separately:

- **RPO 0** is committed for an availability domain failure, which is the far likelier event.
- **RPO ≤ 30 seconds** is the commitment for a regional failure, accepted as a residual.

The alternative to that residual is synchronous replication across roughly 3,000 km, which the
write latency makes unusable for an ERP. The product owner accepted this on the record rather
than leaving a zero in a document that the architecture cannot honor in a regional event.

### The correction: RPO is a property of the mechanism, not of the process

The first pass set RPO 0 for the revenue processes and 5 minutes for procurement, on the
reasoning that procurement matters less.

**That is not purchasable.** Procurement runs on the same EBS database as order entry, and a
single synchronous standby protects all of it at once. There is no configuration in which one
schema on one database has a different recovery point from another.

So RPO is stated **per replication boundary**, and every process on the EBS database inherits
the same number. Reporting and BI differs only because it reads the Active Data Guard standby
rather than the primary.

This is the kind of thing that surfaces only when the objectives are written down together.

---

## Step 1: the business processes

Nine, taken from [`checklists/tier-assignment-workshop.md`](https://github.com/opscontinuum/oci-itscp/blob/main/checklists/tier-assignment-workshop.md) §2 and described in the business's
own words.

| Mission/Business process | Description | Owner |
|---|---|---|
| Order entry and booking | Customer orders captured, priced, credit checked and booked. Where revenue becomes recognizable | Commercial |
| Shipping and fulfilment | Pick, pack, ship and inventory transactions, the carrier handoff, and the shipping confirmation that releases invoicing | Operations |
| AR cash application | Incoming customer payments matched to open receivables, including the daily bank file and lockbox intake | Finance |
| Partner and EDI integrations | Continuous machine to machine exchange with customers, suppliers, carriers and the bank | Integration |
| GL and period close | Ledger posting, sub-ledger reconciliation, and the close sequence producing reportable financials | Finance |
| AP payment runs | Scheduled supplier payment batches, file generation and transmission to the bank | Finance |
| Payroll and HR self-service | Payroll calculation and disbursement, plus employee self-service | HR |
| Procurement | Requisition, approval, purchase order issue and receipt | Procurement |
| Reporting and BI | Management reporting, ad-hoc analytics and scheduled extracts | Commercial |

---

## Step 2: the impact scale, then the impacts

The scale is this business's own. NIST prints sample cost figures to show the shape of the
table and they are deliberately not used.

| Impact category | Severe | Moderate | Minimal |
|---|---|---|---|
| **Financial** | Over $500k at risk, or revenue recognition deferred past a reporting boundary | $50k to $500k, recoverable in the same period | Under $50k, absorbed in normal variance |
| **Regulatory and contractual** | A statutory filing or payroll date missed, or a customer service level breached with penalty | A deadline met only by exception handling that must be disclosed internally | No external deadline affected |
| **Customer and operational** | Customers cannot transact and know it; orders are lost rather than delayed | Customers experience delay; work queues and is processed late | Internal inconvenience only |
| **Workforce** | Employees not paid on the scheduled date | Self-service unavailable; payroll unaffected | Reduced convenience |
| **Reputational** | Externally visible failure likely to be reported by customers, partners or press | Partner-visible, handled through account management | Not externally visible |

Impact per process, worst category rather than an average, because a business does not average
a missed payroll:

| Process | Financial | Regulatory | Customer | Workforce | Reputational | **Overall** |
|---|---|---|---|---|---|---|
| Order entry and booking | Severe | Moderate | Severe | Minimal | Severe | **Severe** |
| Shipping and fulfilment | Severe | Moderate | Severe | Minimal | Severe | **Severe** |
| AR cash application | Severe | Moderate | Moderate | Minimal | Minimal | **Severe** |
| Partner and EDI integrations | Moderate | Moderate | Severe | Minimal | Severe | **Severe** |
| GL and period close | Severe | Severe | Minimal | Minimal | Moderate | **Severe** |
| AP payment runs | Moderate | Severe | Moderate | Minimal | Moderate | **Severe** |
| Payroll and HR self-service | Moderate | Severe | Minimal | Severe | Moderate | **Severe** |
| Procurement | Moderate | Minimal | Moderate | Minimal | Minimal | **Moderate** |
| Reporting and BI | Minimal | Minimal | Minimal | Minimal | Minimal | **Minimal** |

**Partner and EDI moved up from the earlier draft**, and the realtime framing is why. When
exchanges were nightly batches, a four hour outage was absorbed by the next run. Operated as
realtime they are continuous, customers see failures directly, and there is no catch-up window,
so the customer and reputational ratings both rise to Severe.

---

## Step 3: MTD, then RTO, then RPO

Asked in that order. MTD is the business's tolerance, RTO is derived to satisfy it, RPO comes
from the replication boundary.

| Process | Condition | MTD | RTO | RPO | What drives the MTD |
|---|---|---|---|---|---|
| Order entry and booking | | 2 hr | 15 min | 0 | Rate of revenue loss, and the point customers order elsewhere |
| Shipping and fulfilment | | 2 hr | 15 min | 0 | Carrier cut-offs and the invoicing they release |
| AR cash application | | 4 hr | 15 min | 0 | Daily bank file cut-off |
| Partner and EDI integrations | | 4 hr | 15 min | 0 | Partner service levels, with no batch window to absorb a miss |
| GL and period close | outside close | 8 hr | 4 hr | 0 | Internal reporting rhythm |
| **GL and period close** | **within close** | **2 hr** | **15 min** | **0** | **Statutory reporting deadline. Inflexible** |
| AP payment runs | outside window | 24 hr | 4 hr | 0 | Supplier terms tolerate a day |
| **AP payment runs** | **within 24 hr of a run** | **4 hr** | **15 min** | **0** | **Bank file submission window. Contractual** |
| Payroll and HR self-service | outside window | 24 hr | 4 hr | 0 | Self-service only |
| **Payroll** | **within 48 hr of disbursement** | **4 hr** | **15 min** | **0** | **Statutory disbursement date. A miss is a regulatory event** |
| Procurement | | 12 hr | 4 hr | 0 | Requisitions queue rather than being lost |
| Reporting and BI | | 24 hr | 12 hr | ≤ 1 hr | Internal convenience |

Every RTO is shorter than its MTD, as NIST SP 800-34 Rev. 1 §3.2.1 requires, with the WRT from
[`docs/02`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/02-mtd-tiers.md) §2 accounting for the difference.

**Three processes carry two rows.** Their tolerance changes with the calendar, and one averaged
number would be far too loose inside the window and needlessly expensive for the other eleven
months. The freeze rules in [`checklists/tier-assignment-workshop.md`](https://github.com/opscontinuum/oci-itscp/blob/main/checklists/tier-assignment-workshop.md) §5 are the operational
expression of these rows.

### Where the margin actually is

Checked against the architecture rather than assumed, and one result is uncomfortably tight.

| Failure | Order entry RTO | plus WRT | Total | Against MTD 2 hr |
|---|---|---|---|---|
| Availability domain | 15 min | 30 min | 45 min | 75 min of margin |
| **Region** | **60 min** | **30 min** | **90 min** | **30 min of margin** |

The 60 minute cross-region figure is itself conditional on EBS logical host names being
preserved, per [`docs/01-architecture.md`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/01-architecture.md) §5.1. Without that, [`docs/02`](https://github.com/opscontinuum/oci-itscp/blob/main/docs/02-mtd-tiers.md) §5 adds three to five
hours for `FND_CONC_CLONE.SETUP_CLEAN` and AutoConfig, and **order entry breaches its MTD in a
regional event.**

Recorded as a business-visible dependency on a technical decision, which is the correct place
for it. The product owner now knows that one configuration practice stands between a 30 minute
margin and a breach.

---

## Step 3b: alternate means of working

Asked explicitly, because NIST wants "none" written down where it is true rather than left
blank.

| Process | While the system is unavailable |
|---|---|
| Order entry and booking | Orders taken by phone and email on a manual log, re-keyed on recovery. Bounded at about 4 hours before the backlog exceeds same-day re-keying |
| Shipping and fulfilment | Pick lists printed from the last extract; confirmations recorded manually. Carrier handoff continues |
| AR cash application | **None.** Bank files accumulate and are applied on recovery |
| Partner and EDI integrations | **None required.** Inbound files land in replicated Object Storage and replay; outbound transmission is a separate replayable step |
| GL and period close | **None** |
| AP payment runs | Emergency single payments by bank portal with manual reconciliation. Not viable above about 20 payments |
| Payroll | Prior-period repeat payment by bank portal, corrected next cycle. Used once in five years |
| Procurement | Verbal and email commitment against a manual log, re-keyed on recovery |
| Reporting and BI | Prior day's extract remains available |

---

## Step 4: what the business leg hands over

This is the boundary. Everything above is the requirement. None of it describes what the
architecture will do, and that is the point.

**Handed to the product owner:** nine processes, an impact scale, impacts, twelve objective rows
across nine processes, and the alternate means. Workbook tabs 2, 3, 4 and 5.

**Still needed from IT before a recovery order exists:** the resource inventory and the map of
which resources each process depends on. Tabs 6 and 7. Without tab 7 none of the above yields a
restore sequence, because nothing connects a two hour deadline to the component that has to come
back first.

**Signed:** assumed for this exercise. The mechanism that binds a signature to specific content,
so that editing a row after sign-off is detectable, is not yet designed.

---

## What running this surfaced

Five things that reading about the method would not have produced.

1. **99.9% is the coherent ask, not a weaker one.** Against a 45 minute recovery it permits
   about one event a month. 99.99% permits about one a year, which makes the availability
   commitment really a promise never to invoke recovery.
2. **RPO cannot vary by process on shared storage.** One synchronous standby protects one
   database. The first draft's per-process RPOs were not purchasable and had to be restated per
   replication boundary.
3. **Zero RPO is directional.** Zero for an availability domain failure, 30 seconds for a
   regional one. A plan stating a flat zero is making a promise the regional leg cannot keep.
4. **Realtime operation re-rated a process.** Partner and EDI integrations moved to Severe
   because continuous exchange has no batch window to absorb an outage.
5. **A technical configuration practice is load bearing on a business commitment.** Preserving
   logical host names is what keeps 30 minutes of margin under order entry's MTD in a regional
   event. The business now owns that fact rather than discovering it during one.
