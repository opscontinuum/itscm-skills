---
name: itscm-coordinator-review
description: For an ITSCM coordinator assessing a whole continuity documentation set rather than one plan. Requests every document it needs, records what did not arrive as evidence in its own right, and reports a capability level from 1 to 5 per dimension against ITIL 4's Service Continuity Management practice. Levels have all-or-nothing entry criteria, so no criterion is ever partially credited or averaged away.
---

# Reviewing a continuity documentation set

You are assessing a **practice**, not a document. The other skills here each read one file.
This one reads everything the organization has, finds what it does not have, and says where
the practice stands.

The output is a capability level per dimension and one sentence naming what blocks the next
level. That sentence is the deliverable. The number is how somebody compares this system to
forty others or to itself a year ago.

## What a level is, and what it is not

Everything else in this repository refuses to produce a score, for a good reason: a weighted
average compresses "which specific fact is missing" into a number that sounds like progress,
and a program at sixty percent tells nobody what to do on Monday.

A capability level here is not that, and the difference is mechanical:

- **Every level has explicit entry criteria, and all of them must be met.** No partial credit.
  Nine criteria out of ten met is the lower level, not ninety percent of the higher one.
- **Nothing is averaged.** Dimensions are not summed, weighted or blended.
- **Every level is reported with the specific criterion blocking the next one**, by name.
- **A criterion is met only on evidence you were shown.** Not on what somebody says is true.

If you find yourself computing anything, you have left the method. Levels are read off a
checklist, not calculated.

## What this assesses against, exactly

Be precise about this, because a number carries more authority than it earns and somebody will
eventually ask where it came from.

**Scope: ITIL 4's Service Continuity Management practice.** One of ITIL 4's management
practices, assessed on its own.

**Scale: the ITIL Maturity Model's practice capability levels**, which PeopleCert publishes
in its free introduction to the model. Their definitions are reproduced verbatim below.

**Criteria: this skill's own.** They are derived from failure modes observed in real continuity
documentation, not from ITIL. This is the part to be careful about, and here is why.

In the real ITIL Maturity Model, capability criteria "are based on the practice success
factors (PSFs)" defined for each practice and "have been mapped to one of the four dimensions
of service management". The PSFs live in the ITIL 4 practice guides, which are available
through PeopleCert+ membership. **This skill does not have the Service Continuity Management
PSFs and does not invent them.** Its criteria are its own, and the dimensions in Part 2 are its
own eight rather than ITIL's four.

So what you are running is an ITIL-aligned capability assessment, not an ITIL Maturity Model
assessment. The level structure and vocabulary are ITIL's so the result is translatable. The
criteria behind each level are this skill's, so the result is reproducible by anyone reading
the same documents.

### Do not confuse this with the two things it resembles

**Capability levels are not maturity levels.** ITIL MM keeps them separate and they have
different definitions. Maturity levels (Initial, Managed, Defined, Quantitative, Optimizing)
describe an organization's whole Service Value System. Capability levels describe one practice.
This assesses one practice, so it reports capability. Using the maturity names here would be
wrong, and it is an easy mistake because the maturity names are the more familiar ones.

**This cannot produce a certification.** In ITIL MM, certification is available only from a
comprehensive assessment covering the Service Value System plus seven or more practices,
performed by a licensed assessor. A capability assessment of a single practice is explicitly
not certifiable even when PeopleCert runs it. If the organization wants a badge, this is not
the route and saying so early costs nothing.

**It also does not measure ITIL adoption.** PeopleCert is explicit that the model "is NOT
designed to assess the extent or success of the implementation of ITIL guidance". Neither is
this. An organization that has never used the word ITIL can score well here.

### Mapping to ITIL's four dimensions

Report this alongside the levels, so the output is usable by anyone who later runs a real
assessment. The four dimensions of service management, and which of Part 2's dimensions feed
each:

| ITIL dimension | Fed by |
|---|---|
| Organizations and people | Training and awareness; Governance, review and change |
| Information and technology | Continuity strategy and design; Scope and inventory |
| Value streams and processes | Business impact analysis; Plans and procedures; Testing and exercises |
| Partners and suppliers | Supplier and dependency continuity |

---

## Part 1: ask for the documents

Ask for all of these by name, in one request. Do not ask for them one at a time as you discover
you need them, because a set requested piecemeal arrives piecemeal and the gaps look like your
oversight rather than theirs.

Say up front that **you expect some of these not to exist, and that saying so is a complete
answer.** Otherwise people produce something rather than admit to nothing, and you end up
assessing a document written the night before.

### The plans

| Document | Why you need it | If they are unsure what you mean |
|---|---|---|
| Information System Contingency Plan (ISCP) | The system-level recovery plan | The NIST or FedRAMP style plan for one system |
| IT Service Continuity Plan (ITSCP) | The service-level plan | The ITIL style plan covering a service |
| Disaster Recovery Plan | Technical recovery procedure | Often the only thing that exists |
| Business Continuity Plan | The business side | Usually owned outside IT. Ask anyway |
| Continuity of Operations Plan | Organizational continuity | Public sector mostly |
| Crisis communications plan | Who tells whom | Often inside the BCP |

Ask which of these the organization believes it has, and get the file. Titles are unreliable.
A document called a Disaster Recovery Plan is frequently an ISCP, and occasionally a runbook.

### The analysis behind the plans

| Document | Why you need it |
|---|---|
| Business Impact Analysis | The requirement side. Without it every objective in every plan is unsourced |
| Risk assessment covering availability | What the plans are a response to |
| Recovery objectives, however recorded | MTD, RTO, RPO. A spreadsheet counts |
| Service catalog or CI inventory | What is in scope, and what was left out |
| Dependency or service map | Which components each business process needs |

### The evidence the plans work

| Document | Why you need it |
|---|---|
| Test and exercise reports, last three | The only proof a plan does anything |
| Post-incident reviews for real outages | Worth more than any test |
| Training records for recovery roles | Who knows their part |
| Backup and restore verification records | A restore actually performed, with a date |

### The governance around the plans

| Document | Why you need it |
|---|---|
| Approval and signature records | Whether the objectives are commitments or proposals |
| Plan review schedule and last review date | Whether it is current |
| Change records that triggered a plan update | Whether change and continuity are connected |
| Contracts, SLAs and OLAs carrying continuity terms | What was promised externally |
| Supplier continuity attestations | The dependencies you do not control |

### Record what did not arrive

Absence is a finding, and it is often the most important one. For each document, record one of:

| | |
|---|---|
| **Provided** | You have it and can cite it |
| **Exists, not provided** | They say it exists. You have not seen it, so it evidences nothing |
| **Does not exist** | Confirmed absent |
| **Unclear** | Nobody knows whether it exists, which is itself a governance finding |

**Never credit a criterion against a document you were not shown.** "Exists, not provided" is
closer to "does not exist" for assessment purposes than it is to "provided", because an
unproduced document is one nobody could find, and a document nobody can find at review time is
a document nobody will find during an incident.

---

## Part 2: the eight dimensions

Assess each independently. Each gets its own level.

1. **Scope and inventory.** What is covered, what is knowingly excluded, and whether anybody
   has compared the list to reality.
2. **Business impact analysis.** Processes, impacts on a defined scale, and recovery objectives
   keyed to those processes.
3. **Continuity strategy and design.** The architecture chosen to meet the objectives, and
   whether the choice is traced to them.
4. **Plans and procedures.** Documented recovery, at a level of detail somebody who did not
   write it could follow.
5. **Testing and exercises.** Performed, recorded, and acted on.
6. **Training and awareness.** People know their part before the night it matters.
7. **Governance, review and change integration.** Ownership, currency, and whether a change to
   the system reaches the plan.
8. **Supplier and dependency continuity.** The parts of recovery somebody else controls.

---

## Part 3: the levels

Generic meanings first, then the per-dimension criteria.

PeopleCert's definitions of the practice capability levels, verbatim, followed by what each one
means for continuity documentation specifically.

| Level | The practice, verbatim | For a continuity documentation set |
|---|---|---|
| 1 | "not well organised; it is performed as initial/intuitive. It may occasionally or partially achieve its purpose through an incomplete set of activities" | Something exists. It is unowned, unverified, or both |
| 2 | "systematically achieves its purpose through a basic set of activities supported by specialised resources" | Owned, current, and covering the scope it claims |
| 3 | "well defined and achieves its purpose in an organised way, using dedicated resources and relying on inputs from other practices that are integrated into a service management system" | Derived from analysis, consistent across documents, and connected to the practices it depends on |
| 4 | "achieves its purpose in a highly organised way, and its performance is continually measured and assessed in the context of the service management system" | Tested, with results recorded and objectives verified against measured reality |
| 5 | "continually improving organisational capabilities associated with its purpose" | Findings change the practice, evidenced over time |

**Level 1 is the floor, and there is no level 0.** ITIL MM defines capability criteria only from
level 2 upward: level 1 is where a practice sits when it does not yet meet level 2's criteria.
A dimension with nothing at all is level 1 with "nothing exists" stated, not level 0 and not
unrated. The criteria below follow that, starting at 2.

### Entry criteria

A dimension is at the highest level whose criteria are **all** met, and where every lower
level's criteria are also met. Skipping is not possible: an untested plan is not level 4
however good it is.

#### 1. Scope and inventory

| Level | All of these must be true |
|---|---|
| 2 | A list of systems or services in scope exists, has a named owner, and carries a date |
| 3 | The list states what is deliberately excluded and why; scope is consistent across every plan provided |
| 4 | The list has been compared to what is actually running, and the comparison is recorded with its date and its discrepancies |
| 5 | That comparison is repeated on a schedule, and discrepancies from the last one were closed or accepted in writing |

#### 2. Business impact analysis

| Level | All of these must be true |
|---|---|
| 2 | Recovery objectives exist in writing for the systems in scope |
| 3 | Objectives are keyed to **mission or business processes**, not to systems or tiers; an impact scale with graded values exists; each objective names what drives it; RTO is shorter than MTD everywhere |
| 4 | Objectives are signed by somebody with authority to commit the business, and the processes are mapped to the resources they depend on |
| 5 | The analysis is re-run on a defined trigger as well as a calendar, and a re-run has demonstrably changed an objective |

**Level 3 is where most organizations stop, and the keying criterion is why.** Objectives
stated per infrastructure tier are level 2 no matter how carefully derived, because they cannot
answer whose work stopped. This is the single most common cap on the whole assessment.

#### 3. Continuity strategy and design

| Level | All of these must be true |
|---|---|
| 2 | A recovery approach is documented for each system in scope |
| 3 | The approach is traceable to the objectives in dimension 2; where it cannot meet them, the shortfall is documented as a tracked gap rather than a relaxed objective |
| 4 | The achievable recovery time and data loss are **measured**, not estimated, and compared to the objectives |
| 5 | Measured shortfalls drive design change, with at least one change evidenced |

#### 4. Plans and procedures

| Level | All of these must be true |
|---|---|
| 2 | A recovery plan exists, has a named owner, and has been reviewed within its stated cycle |
| 3 | Procedures are specific enough to follow without the author; activation criteria and authority are stated; contact information is current; the plan is consistent with the objectives in dimension 2 |
| 4 | The plan has been followed end to end in a test or a real incident, and the record says where it was wrong |
| 5 | Plans are corrected from those records, with version history showing it |

#### 5. Testing and exercises

| Level | All of these must be true |
|---|---|
| 2 | A test has been performed and recorded, with a date |
| 3 | Tests follow a documented scope and pass criteria; a schedule exists; test type is stated |
| 4 | Tests **measure** recovery time and data loss against the objectives, and findings are recorded with owners |
| 5 | Findings are closed, closure is evidenced, and the test scope has widened over time |

**A test that found nothing is a finding about the test.** Note it rather than crediting it.

#### 6. Training and awareness

| Level | All of these must be true |
|---|---|
| 2 | Recovery roles are named and the people in them know they hold the role |
| 3 | Role-specific training exists with a defined syllabus and a cadence |
| 4 | Training completion is recorded per person, and new joiners are trained within a stated period |
| 5 | Training content is updated from test and incident findings |

#### 7. Governance, review and change integration

| Level | All of these must be true |
|---|---|
| 2 | Every plan has a named owner and a review date |
| 3 | A review cadence is defined and was met; approvals are signed; plans are version controlled |
| 4 | Changes to a system **reach the plan**: at least one change record is traceable to a plan update |
| 5 | Continuity review is a gate in the change process rather than a periodic catch-up, and evidence shows it stopping or altering a change |

**Dimension 7 level 4 is the one almost nothing passes.** Ask for a specific recent
architecture change and follow it to the plan. If the plan does not mention it, the plan is
describing a system that no longer exists, whatever its review date says.

#### 8. Supplier and dependency continuity

| Level | All of these must be true |
|---|---|
| 2 | Suppliers and external dependencies material to recovery are listed |
| 3 | Continuity obligations are stated in contracts, SLAs or OLAs, and the list covers every dependency in the plans |
| 4 | Supplier continuity claims are **evidenced**, by attestation, audit or joint test, not accepted on assertion |
| 5 | Suppliers are included in exercises, and a finding against one has been acted on |

---

## Part 4: the report

```
ITSCM CAPABILITY REVIEW
Organization / service: <name>            Reviewed: <date>          Reviewer: <name>

ASSESSED AGAINST
  Scope:    ITIL 4 Service Continuity Management practice
  Scale:    ITIL Maturity Model practice capability levels 1 to 5
  Criteria: this skill's own, derived from observed failure modes, NOT from the
            practice success factors in the licensed ITIL 4 practice guide
  Not a certified assessment. ITIL MM certification requires a comprehensive
  assessment of the Service Value System plus seven or more practices.

DOCUMENTS
  Provided              <n>   <list>
  Exists, not provided  <n>   <list>        (evidences nothing)
  Does not exist        <n>   <list>
  Unclear               <n>   <list>

LEVELS
  1 Scope and inventory                    <level>
  2 Business impact analysis               <level>
  3 Continuity strategy and design         <level>
  4 Plans and procedures                   <level>
  5 Testing and exercises                  <level>
  6 Training and awareness                 <level>
  7 Governance, review and change          <level>
  8 Supplier and dependency continuity     <level>

  Overall claimed:   <lowest claimed level>
  Overall evidenced: <lowest evidenced level>
  Constrained by: <which dimension, and the one criterion it fails>

PROVEN OR UNPROVEN
  <one word>.  Last test that demonstrated anything: <date, or NEVER>
  <if unproven: one sentence naming what the documentation claims and nothing confirms>

WHAT BLOCKS THE NEXT LEVEL
  <dimension>   <the specific criterion>   <what would satisfy it>
  ...

EVIDENCE NOT SEEN
  <criterion>   <the document that would have settled it>
```

### Claimed against evidenced

A level on its own does not say whether recovery works, and somebody reading a 3 will assume it
does. Report each dimension twice:

| | |
|---|---|
| **Claimed** | The level the documentation supports |
| **Evidenced** | The level a test, drill or real incident has demonstrated |

**Where nothing has been tested, evidenced is 1** on every dimension that depends on proof,
however good the documents are. That is not an ITIL demotion and you should not present it as
one: ITIL's level 1 means "not well organised; performed as initial/intuitive", which is about
disorder, and a well documented untested program is not disorderly. ITIL puts proof at level 4,
where "performance is continually measured and assessed", so on their scale an untested
practice caps at 3. The evidenced reading is a separate statement the scale cannot carry.

Dimensions where claimed and evidenced can differ: continuity strategy and design, plans and
procedures, testing and exercises, training, supplier continuity, and scope and inventory.

Dimensions where they do not: business impact analysis and the governance of it. A signed
recovery objective is a requirement the business committed to, not a claim about capability, so
a test neither confirms nor refutes it.

**Say "unproven" in words, above the levels, with the date of the last test that demonstrated
anything.** A reader who has to work it out from a number will not.

### Why overall is the lowest and not an average

An organization is not two and a half levels mature. For continuity specifically, the weakest
dimension is the one that decides the outcome: a perfectly designed, well documented, widely
trained recovery capability that has never been tested is an unproven capability, and averaging
it up to a comfortable middle is the exact thing this repository refuses to do everywhere else.

Report the lowest, and name which dimension set it. The per-dimension levels are right there
for anybody who wants to see the strong ones.

### Writing the blocking sentence

One per dimension, and this is what people act on. It names a criterion, not a theme.

> Business impact analysis is at 2. Objectives exist for all eleven systems and are keyed to
> infrastructure tiers rather than to business processes, so nothing can say whose work stops.
> Level 3 needs the objectives re-derived per process, which is the workshop in `bia-workshop`.

Not: *"the BIA needs strengthening."*

## What this skill does not do

It does not assess the plans' technical content, which is `iscp-completeness` for structure
and `iscp-sufficiency` for whether anything can be derived from them. Run those on the
individual documents and bring their findings in as evidence here.

It does not assess the organization's people and cadence from interview, which is
`itscm-program-assessment`. That one asks people. This one reads documents. Where they
disagree, the documents are what an auditor will see and the interview is what is actually
happening, and the gap between them is worth reporting on its own.

It does not issue a certification or a badge, for the reasons in the scope section above.

It does not benchmark against other organizations. ITIL MM offers benchmarking because
PeopleCert holds assessment data across its clients. This skill holds none, and inventing a
comparison would be the most damaging thing a number like this could do.

## Sources

- **Introduction to the ITIL Maturity Model**, PeopleCert, June 2025. Retrieved 2026-09-22 from
  `https://www.peoplecert.org/-/media/folders-reorganized/pdfs/itil-maturity-model/services-page/introduction-to-the-itil-mm.pdf`.
  Supports: the practice capability level definitions quoted verbatim in Part 3; that capability
  criteria "are defined for each capability level, from level 2 to level 5", "are based on the
  practice success factors (PSFs)" and "have been mapped to one of the four dimensions of
  service management"; the separation of practice capability levels from Service Value System
  maturity levels; that certification is available only from a comprehensive assessment
  covering the SVS and seven or more practices; and that the model "is NOT designed to assess
  the extent or success of the implementation of ITIL guidance".
- ITIL 4 practice guides, including Service Continuity Management and its practice success
  factors, are available through PeopleCert+ membership. **Not consulted.** The criteria in this
  skill are not derived from them and do not reproduce them.
