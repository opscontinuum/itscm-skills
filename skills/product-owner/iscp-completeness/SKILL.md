---
name: iscp-completeness
description: Audit an Information System Contingency Plan against FedRAMP SSP Appendix G ISCP Template v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports every required heading, table, table column and prescribed row as PRESENT AND ANSWERED, PRESENT BUT UNFILLED, or MISSING, and never scores a requirement it could not evaluate. Also asks whether the plan carries a front-of-document fact sheet for whoever meets an incident first, and traces each field the organization wants back to the section that already holds it.
---

# Auditing an ISCP for completeness

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ISCP** | Information System Contingency Plan |
| **DRP** | Disaster Recovery Plan |
| **SSP** | System Security Plan |
| **SLA** | service level agreement |
| **NIST** | National Institute of Standards and Technology |
| **SP** | Special Publication |
| **OMB** | Office of Management and Budget |
| **CSO** | Cloud Service Offering |
| **NOC** | network operations center |
| **OS** | operating system |


You have been given a document that claims to be an Information System
Contingency Plan. Decide what it is missing.

**This skill is self-contained.** Every heading, table title, column header and
prescribed row label below was transcribed from the primary sources named at the
bottom. You do not need the template file, a generator, or a network connection.
Do not fetch anything. Do not work from memory of what a contingency plan
usually contains: work from the lists here.

## The rule

Every requirement starts unmet. Each one ends as exactly one of:

| Verdict | Meaning |
|---|---|
| `ANSWERED` | Present, and carrying content that is not a placeholder |
| `UNFILLED` | Present as a heading or table, and carrying only placeholder text or nothing |
| `MISSING` | Not in the document at all |
| `NOT ASSESSED` | You could not evaluate it, and you say why |

`NOT ASSESSED` is reported, never silently dropped and never counted as a pass.
A checker that omits what it could not evaluate produces a number that reads as
completeness and is not. If the document is a scanned image, a format you cannot
read, or truncated, say so and mark the affected requirements `NOT ASSESSED`
rather than reporting them `MISSING`, which would accuse the author of an
omission that may not exist.

**`UNFILLED` is the verdict that matters most.** A missing section is obvious to
anybody who opens the document. A section that is present, correctly titled, and
contains `Click here to enter text.` looks finished in a table of contents and
fails assessor review. Count these separately and lead your report with them.

## What counts as a placeholder

Text that means the author has not answered. Treat a cell or paragraph as
`UNFILLED` when its content, after trimming whitespace, is only:

```
Click here to enter text.
Choose an item.
{insert}
<Insert CSO Name>
<Enter Number>
```

Also treat as `UNFILLED`: any `<...>` angle-bracket token that reads as an
instruction to the author rather than a value, an empty cell, a cell containing
only `N/A` where the template asks for a fact rather than an applicability
judgment, and any paragraph consisting only of the template's own instructional
text.

**Instructional text should not be there at all.** Every FedRAMP `Instructions:`
box ends with "Delete this and all other instructional text from your final
version of this document." If you find surviving `Instructions:` blocks, report
them as a finding in their own right, separate from the completeness counts.

**NIST's worked examples should not be there either.** NIST SP 800-34 Rev. 1
Appendix B illustrates its BIA tables with a sample organization. If you find
`Pay vendor invoice`, `Web Server 1`, `Optiplex GX280`, or `24 hours to rebuild
or replace`, the author has shipped NIST's illustration as if it were their own
business process. Report it. This is worse than an empty table.

## Part 1: the required headings

Sixty-seven, in the template's own order. Number and text as given. A document
may reword capitalization and may carry its own numbering style; match on the
section number and the substantive words, not on an exact string.

### Front matter
```
Prepared by
Prepared for
Document Revision History
CONTINGENCY PLAN APPROVALS
```

### 1 Introduction and Purpose
```
1 Introduction and Purpose
1.1 Applicable Laws and Regulations
1.2 FedRAMP Requirements and Guidance
1.3 <CSO Name> and Identifier
1.4 Scope
1.5 Assumptions
```

### 2 Concept of Operations
```
2 Concept of Operations
2.1 System Description
2.2 Three Phases
2.3 Data Backup Readiness Information
2.4 Site Readiness Information
2.5 Roles and Responsibilities
```

Section 2.5 must carry all eight role headings, plus two more:
```
Contingency Planning Director (CPD)
Contingency Planning Coordinator (CPC)
Outage and Damage Assessment Lead (ODAL)
Hardware Recovery Team (HRT)
Software Recovery Team (SRT)
Telecommunications Team (TC)
Procurement and Logistics Coordinator (PLC)
Security Coordinator (SC)
Plan Distribution and Availability
Line of Succession/Alternates Roles
```
The eight role headings and their duty lists are boilerplate the template
supplies as **final** text, not as instruction. A plan that has deleted them has
deleted a requirement, not a comment.

### 3 Activation and Notification
```
3 Activation and Notification
3.1 Activation Criteria and Procedure
3.2 Notification Instructions
3.3 Outage Assessment
```

### 4 Recovery
```
4 Recovery
4.1 Sequence of Recovery Operations
4.2 Recovery Procedures
4.3 Recovery Escalation Notices/Awareness
```

**Check 4.2 for a cross-reference.** ISCP section 4.2 says keystroke-level
procedures may live in an appendix, and that "if specific procedures are
provided in an appendix, a reference to that appendix must be included in this
section." If 4.2 defers to an appendix without naming it, that is a finding.

### 5 Reconstitution
```
5 Reconstitution
5.1 Data Validation Testing
5.2 Functional Validation Testing
5.3 Recovery Declaration
5.4 User Notification
5.5 Cleanup
5.6 Returning Backup Media
5.7 Backing-Up Restored Systems
5.8 Event Documentation
```

### 6 Contingency Plan Testing
```
6 Contingency Plan Testing
```
Section 6 asserts that operational tests are performed **annually** and that a
Contingency Plan Test Report is documented after each annual test. If the plan
states a different cadence, report it as a deviation rather than silently
accepting it.

### Appendices
```
Appendix A Key Personnel and Team Member Contact List
Appendix B Vendor Contact List
Appendix C Alternate Storage, Processing and Provisions
    Section 1: Alternate Storage Site Information
    Section 2: Alternate Processing Site Information
    Section 3: Alternate Telecommunications Provisions
Appendix D Alternate Processing Procedures
Appendix E System Validation Test Plan
Appendix F Contingency Plan Test Report
Appendix G Diagrams
Appendix H Hardware and Software Inventory
Appendix I System Interconnections with Other Services
Appendix J Test and Maintenance Schedule
Appendix K Associated Plans and Procedures
Appendix L Business Impact Analysis
```

## Part 2: the required tables and their columns

Eighteen tables. For each, check that the table exists, that its column headers
match, and that it has at least one data row that is not a placeholder.

| Table | Required columns |
|---|---|
| Table 1.3 `<CSO Name>` and Title | Unique Identifier · Cloud Service Offering Name · Information System Abbreviation |
| Table 1.4 Plans Outside of ISCP Scope | Plan Name · Mission/Purpose |
| Table 2.1 Backup Types | Backup Type · Description |
| Table 2.2 Backup System Components | System/Component · Description |
| Table 2.3 Back-Up Storage Location | label/value, see prescribed rows below |
| Table 2.4 Alternative Site Types | Type of Site · Description |
| Table 2.5 Primary and Alternative Site Locations | Designation · Site Name · Site Type · Address |
| Table 3.1 Personnel Authorized to Activate the ISCP | Name · Title and ISCP Role · Contact Information |
| Table 5.1 Cleanup Roles and Responsibilities | Role · Cleanup Responsibilities |
| Table 5.2 Event Documentation Responsibility | Role Name · Documentation Responsibility |
| Table A.1 Key Personnel and Team Member Contact List | Role · Name and Home Address · Email · Phone |
| Table B.1 Vendor Contact List | Vendor · Product or Service License #, Contract #, Account #, or SLA · Phone |
| Table C.1 Alternate Storage Site Information | label/value, see prescribed rows below |
| Table C.2 Alternate Processing Site Information | label/value, see prescribed rows below |
| Table C.3 Alternate Telecommunications Provisions | label/value, see prescribed rows below |
| Table E.1 System Validation Test Plan | Procedure · Expected Results · Actual Results · Successful? · Performed by |
| Table F.1 Contingency Plan Test Report | label/value, see prescribed rows below |
| Table K.1 Associated Plans and Procedures | System Name · Plan Name |

## Part 3: tables whose ROWS are the requirement

For these, the row labels are prescribed by the template. A missing row is a
missing requirement even when the table is present.

**Table 2.1 Backup Types.** Four rows, and they are boilerplate the template
supplies as final text, so they must be present with their descriptions:
`Full Backup` · `Differential Backup` · `Incremental Backup` · `Mirror Backup`

**Table 2.2 Backup System Components.** Five rows:
`Software Used` · `Hardware Used` · `Frequency` · `Backup Type` · `Retention Period`

**Table 2.3 Back-Up Storage Location.** Three rows:
`Site Name` · `Street Address` · `City, State, Zip Code`

**Table 2.4 Alternative Site Types.** Four rows, also final boilerplate:
`Cold Sites` · `Warm Sites` · `Hot Sites` · `Mirrored Sites`

**Table C.1 Alternate Storage Site Information.** Ten rows:
```
Address of alternate storage site
Distance from primary facility
Is the alternate storage facility owned by the organization or is a third-party storage provider?
Points of contact at alternate storage location
Delivery schedule and procedures for packaging media for delivery to alternate storage facility
Procedures for retrieving media from the alternate storage facility
Names and contact information for those persons authorized to retrieve media
Potential accessibility problems to the alternate storage site in the event of a widespread disruption or disaster
Mitigation steps to access alternate storage site in the event of a widespread disruption or disaster
Types of data located at alternate storage site, including databases, application software, operating systems, and other critical information system software
```

**Table C.2 Alternate Processing Site Information.** Eight rows:
```
Address
Distance from primary facility
Alternate processing site is owned by the organization or is a third-party site provider
Point of Contact
Procedures for accessing and using the alternate processing site, and access security features of alternate processing site
Names and contact information for those persons authorized to go to alternate processing site
Type of Site (from Table 2-4 Alternative Site Types)
Mitigation steps to access alternate processing site in the event of a widespread disruption or disaster
```

**Table C.3 Alternate Telecommunications Provisions.** Four rows:
```
Name and contact information of alternate telecommunications vendors by priority
Agreements currently in place with alternate communications vendors
Contracted capacity of alternate telecommunications
Names and contact information of individuals authorized to implement or use alternate telecommunications
```

**Table F.1 Contingency Plan Test Report.** Fourteen rows:
```
Name of Test
System Name
Date of Test
Team Test Lead and Point of Contact
Location Where Conducted
Participants
Components
Assumptions
Objectives
Methodology
Activities and Results (Action, Expected Results, Actual Results)
Post Test Action Items
Lessons Learned and Analysis of Test
Recommended Changes to Contingency Plan Based on Test Outcomes
```

## Part 4: Appendix L, the Business Impact Analysis

Appendix L is a single FedRAMP instruction: "Insert the Business Impact Analysis
here. Please see NIST SP 800-34, Revision 1 for more information on how to
conduct a Business Impact Analysis." So its structure comes from NIST, not from
FedRAMP, and it is audited against NIST SP 800-34 Rev. 1 Appendix B.

Required headings:
```
1 Overview
1.1 Purpose
2 System Description
3 BIA Data Collection
3.1 Determine Process and System Criticality
3.1.1 Identify Outage Impacts and Estimated Downtime
3.2 Identify Resource Requirements
3.3 Identify Recovery Priorities for System Resources
```

Six tables, by the columns they must carry. NIST's templates are untitled, so
match on the column set:

| Under | Required columns |
|---|---|
| 3.1 | Mission/Business Process · Description |
| 3.1.1 | Impact category · Severe · Moderate · Minimal |
| 3.1.1 | Mission/Business Process · Impact |
| 3.1.1 | Mission/Business Process · MTD · RTO · RPO |
| 3.2 | System Resource/Component · Platform/OS/Version (as applicable) · Description |
| 3.3 | Priority · System Resource/Component · Recovery Time Objective |

**The MTD/RTO/RPO table is the one to check hardest.** It is the row an assessor
reads first and the one most often shipped with an empty `Recovery Time
Objective` column. An RTO column of blanks is `UNFILLED`, and it is a more
serious finding than a missing appendix, because the table's presence implies
the analysis was done.

**A BIA that is absent entirely is a single `MISSING` finding at the top of your
report, not eight.** Say the appendix is absent, then list its eight headings
and six tables as consequences of that one fact. Reporting fourteen separate
misses for one missing appendix inflates the count and buries everything else.

## Part 5: what the plan should NOT contain

Report each as its own finding:

- **A Disaster Recovery Plan.** FedRAMP asks a cloud service provider for
  exactly one contingency-planning document, the ISCP, and publishes no DRP
  template. NIST SP 800-34 Rev. 1 §2.2 defines a DRP as a plan *type* and also
  publishes no template. A section titled "Disaster Recovery Plan" with a
  structure of its own invention will fail assessor review.
- **A Business Continuity Plan, Continuity of Operations Plan, Occupant
  Emergency Plan, or crisis communications plan.** Table 1.4 lists these as
  "Plans Outside of ISCP Scope". They are named in Table 1.4 and not reproduced.
- **A System Security Plan.** The ISCP is Appendix G *of* the SSP. It does not
  contain one.
- **Surviving instructional text**, per the placeholder section above.
- **NIST's worked examples**, per the placeholder section above.

## Part 6: the fact sheet, which you ask about rather than score

A plan can pass every check in Parts 1 through 5 and still be unopenable by the
person who meets it first. The usual first reader is not the system owner. It is
a watch function: a virtual NOC, a duty operator, an on-call who covers many
systems and wrote none of them. That reader needs about eight facts in the first
minute, and every one of those facts is already somewhere in the plan you just
audited. What is missing is a page at the front that carries them.

Call it the **fact sheet**.

### It is not a requirement, and you must not report it as one

FedRAMP SSP Appendix G does not ask for one. NIST SP 800-34 Rev. 1 does not ask
for one. **A plan with no fact sheet is not deficient**, and a verdict of
`MISSING` against it would be you inventing a requirement and then failing a
document for not meeting it. That is the one thing this skill exists to not do.

So the fact sheet never enters the verdict set, never enters the denominator,
and never appears in the `MISSING` list. It gets its own section of the report,
written as an observation and a set of questions.

What licenses the observation is that neither authority prescribes a layout.
NIST 800-34 gives content guidance and a sample format. FedRAMP gives a template
whose required content an assessor checks for presence. Neither forbids a page
in front. Adding one removes no required section and fails no check.

### Step 1: say whether the plan already has one

Look ahead of section 1 for a quick-reference page, summary card, at-a-glance
table, or equivalent, whatever it is called. Report one of:

- **Present.** Say what it carries, then go to step 3 and check its fields
  against their sources, because a fact sheet that disagrees with the body is
  worse than none: it is the page the reader will trust fastest.
- **Absent.** Say so as an observation, not a defect, and go to step 2.

### Step 2: ask, because the layout is the business's to decide

Do not propose a page. What belongs on it depends on who reads it, what else
they hold, and what they are permitted to do, and those differ per organization.
Ask, and ask the person who owns the plan:

1. **Who reads this first at two in the morning, and do they know this system?**
   A team that owns one system needs a different page from a watch function
   covering two hundred.
2. **What are they allowed to do?** Declare and activate, or detect and
   escalate? This is the question that changes the page most. A detect-only
   reader needs the escalation target and the criteria for meeting it, and does
   not need the recovery sequence at all.
3. **What do they already have in front of them?** If their console already
   carries the system owner and the support contract, repeating those on the
   fact sheet creates a second copy that will drift.
4. **What decision do they have to make in the first sixty seconds?** Usually
   one of: is this the thing I escalate, how long until this becomes a different
   problem, or which of several failing things do I chase first.
5. **How many plans does this reader hold?** If it is many, the fact sheets
   should be identical in shape across all of them, and that shape is a decision
   made once for the organization rather than once per plan.
6. **What is the review cadence for this page specifically?** This is the
   question people skip and it is the one that decides whether the page is an
   asset. Contact lists and dependency order churn faster than an annual plan
   review. A fact sheet refreshed annually puts the stalest data where it is
   trusted most.

### Step 3: for every field they name, find its source in the plan

This is the part that pays for the exercise. For each field the organization
wants, locate where that fact already lives in the document you just audited:

| Field a reader typically asks for | Where the plan already carries it |
|---|---|
| System name, boundary, owner | 1 Introduction and Purpose, 2 Concept of Operations |
| What order to recover things in | Appendix L BIA, table 3.3, Priority · System Resource/Component · Recovery Time Objective |
| How long before this is a different problem | Appendix L BIA, table 3.1.1, MTD · RTO · RPO |
| When this counts as an incident | 3.1 Activation Criteria |
| Who declares it | 3 Activation and Notification |
| Who to escalate to | 4.3 Recovery Escalation Notices/Awareness |
| Whether there is somewhere else to run | Table 2.4 Alternate Site Types, Table 2.5 Primary and Alternative Site Locations |
| Who to call | Appendix A Key Personnel and Team Member Contact List |
| Which vendor and under what contract | Appendix B Vendor Contact List |

Then report each field as one of:

- **Derivable.** Name the section it comes from. That field is settled.
- **Derivable but `UNFILLED`.** The plan has the right heading and no content
  there. The fact sheet cannot be built until that section is answered, which
  makes it a reason to fix the `UNFILLED` rather than a separate problem.
- **Not in the plan.** This is a real finding and the audit above could not have
  produced it. Every heading can be present and answered while a fact the first
  reader needs is nowhere in the document, because no heading asked for it. Say
  which field, say that the plan does not carry it, and let the owner decide
  whether the field is wrong or the plan is.

### The rule for the page itself

**No field on a fact sheet may be typed. Every one is copied from a named
section of the plan.** A hand-authored fact sheet is a second copy of facts that
already exist in section 2, section 3, Appendix A and Appendix L, and second
copies diverge. Within a year the front page says four hours and Appendix L says
twelve, and the reader trusts the page they were pointed at.

If the organization cannot commit to deriving it, say plainly that a fact sheet
refreshed by hand at a different cadence from the plan will eventually be wrong
in the direction of looking right, and that no fact sheet is better than one
nobody re-derives.

## How to run the audit

1. **Read the whole document first.** Do not audit section by section as you
   read: a plan may answer a requirement somewhere other than where the template
   puts it, and a first pass that has not seen the end will report false misses.
2. **Establish what you are reading.** If it is the blank FedRAMP template
   rather than a filled plan, say so immediately: every requirement will be
   `UNFILLED` and that is the correct answer, not a failure.
3. **Walk Part 1, then Part 2, then Part 3, then Part 4.** Give every requirement
   a verdict.
4. **Then Part 5**, which is a different kind of finding and goes in its own
   section.
5. **Then Part 6**, which is not a finding at all. It is an observation and a
   set of questions, it stays out of the verdict set and out of the denominator,
   and its one genuine finding is a field the first reader needs that the plan
   does not carry anywhere.
6. **Count, and show the denominator.** Never emit a finding count alone.
   "23 of 67 headings answered" is a reading somebody can act on. "23 findings"
   is not.

## The report

```
ISCP COMPLETENESS AUDIT
Document: <path or name>          Audited against: FedRAMP SSP Appendix G v5.0
Assessed: <n> of <total> requirements        Not assessed: <n>, reasons below

UNFILLED: present and carrying only placeholder text        <n>
  <requirement>  <what it contains instead>
  ...

MISSING: not in the document                                 <n>
  <requirement>
  ...

SHOULD NOT BE PRESENT                                        <n>
  <finding>  <where>
  ...

NOT ASSESSED                                                 <n>
  <requirement>  <why you could not evaluate it>
  ...

ANSWERED                                                     <n> of <total>

FACT SHEET (not a FedRAMP or NIST requirement, not counted above)
  Present / absent ahead of section 1:  <which>
  Fields requested by the owner:        <n>
    derivable from      <field>  <-  <section that carries it>
    blocked by UNFILLED <field>  <-  <section, which is empty>
    not in the plan     <field>  <-  no section carries this
  Questions outstanding: <the ones in Part 6 nobody answered>
```

Lead with `UNFILLED`. It is the category a table of contents hides and an
assessor finds.

The fact sheet block sits below the count and outside it. Nothing in it is a
deficiency against FedRAMP or NIST, with one exception worth stating out loud:
a field the first reader needs that no section of the plan carries is a real
gap, and it is one the heading-by-heading audit above structurally cannot find,
because the heading was present and answered.

Do not compute a percentage or a grade. A contingency plan is not complete
because 90 percent of its headings carry text; it is complete when a person who
has to recover the system at three in the morning can follow it. Report what is
there and what is not, and let a human judge.

## Sources

Transcribed from the primary sources, not from memory:

- **FedRAMP SSP Appendix G: Information System Contingency Plan (ISCP) Template,
  version 5.0, dated 12/06/2024**, whose own revision history describes v5.0 as
  "Updated to align with OMB Memo M-24-15 and remove PMO references". Retrieved
  2026-09-02 from `fedramp.gov`, 153865 bytes,
  md5 `298f6b1392ee21b1cded5164c2523b86`.
- **NIST SP 800-34 Rev. 1, Appendix B**, "Sample Business Impact Analysis (BIA)
  and BIA Template", pages B-1 to B-4, May 2010 (errata 2010-11-11).

If you are auditing against a newer template than v5.0, say so in your report
and mark any requirement you cannot confirm against the version in hand as
`NOT ASSESSED`. Auditing a v6 plan against a v5 list and reporting the
differences as omissions would be this skill producing the exact failure it
exists to catch.
