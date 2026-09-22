---
name: iscp-completeness
description: Audit an Information System Contingency Plan against FedRAMP SSP Appendix G ISCP Template v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports every required heading, table, table column and prescribed row as PRESENT AND ANSWERED, PRESENT BUT UNFILLED, or MISSING, and never scores a requirement it could not evaluate.
---

# Auditing an ISCP for completeness

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
5. **Count, and show the denominator.** Never emit a finding count alone.
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
```

Lead with `UNFILLED`. It is the category a table of contents hides and an
assessor finds.

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
