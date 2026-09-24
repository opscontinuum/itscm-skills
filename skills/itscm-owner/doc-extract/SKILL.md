---
name: doc-extract
description: For whoever reads one continuity document and records what it actually says, working by hand or as one branch of an automated evaluation. Pulls the facts a later assessment needs out of a Business Impact Analysis, a plan, a runbook, a test report, a contract or a training record, each fact carrying the document and the location inside it. Records a missing recovery objective as missing rather than inferring a plausible one, and records whether objectives are keyed to business processes or to infrastructure without correcting either.
---

# Extracting the facts from one continuity document

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **BIA** | Business Impact Analysis |
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **WRT** | Work Recovery Time |
| **ISCP** | Information System Contingency Plan |
| **ITSCP** | IT Service Continuity Plan |
| **BCP** | Business Continuity Plan |
| **DRP** | Disaster Recovery Plan |
| **SLA** | service level agreement |
| **OLA** | operational level agreement |
| **ITSCM** | IT Service Continuity Management |


This runs once per document, on documents the inventory recorded as `provided`. Where a document
was split into extraction units at intake, run it once per unit.

Your input is one document and its inventory entry. Your output is a list of facts, each one
attached to the place it came from, plus an honest list of the things the document was asked for
and did not answer.

You are not assessing anything. The comparison that matters in an [ITSCM](../../../GLOSSARY.md "IT Service Continuity Management") evaluation is between
what the business requires and what the architecture delivers, and it happens two stages from
here. This stage puts both sides on the table exactly as they were written, so that the
comparison is possible. Everything below protects that.

## The rule: never fill a gap

Read this before you read anything else, because it is the rule that gets broken without anyone
noticing.

A missing recovery objective is extracted as missing. Not estimated, not inferred from the
architecture, not carried across from a sibling process, not derived from a service level
agreement, not rounded up from a sentence that nearly says it.

The reason is mechanical. The assessment compares the requirement against the capability. If you
read a four hour failover design and write down a four hour [RTO](../../../GLOSSARY.md "Recovery Time Objective"), the two sides are now equal by
construction, and the comparison will return met for as long as the document exists. The
organization will be told its architecture satisfies its requirements, and the sentence will be
true only because you wrote the requirement from the architecture. The gap that the whole
evaluation exists to find has been closed by the person hired to find it.

### The five ways the fill happens, none of which feel like inventing

Completing a pattern. Nine processes carry an objective, the tenth does not, and the tenth is
similar, so it gets its neighbor's number. Record the tenth as having none.

Reading the design into the requirement. The document says the database replicates every
fifteen minutes. That is a capability. It is not an [RPO](../../../GLOSSARY.md "Recovery Point Objective"). Record it as a capability, under the
architecture, and record the [BIA](../../../GLOSSARY.md "Business Impact Analysis")'s data loss objective as absent if the analysis does not
state one.

Converting. The document says "back by the start of the next business day". Record those words.
If a later stage needs hours, it can convert with the working calendar in front of it, which you
do not have. A conversion recorded as the value has quietly replaced what the business said with
what you assumed about its week.

Reading a general statement as a specific one. "All systems recover within 24 hours" is one fact,
stated once, at the scope of all systems. It is not eleven facts about eleven processes. Record
it once, at the scope it was written at, and record per-process objectives as absent.

Borrowing from another document. The plan says four hours and the analysis says nothing, so the
analysis gets four hours. Extraction is per document, always. A fact from one document never
completes another. Reconciling documents against each other is a later stage's work and it
cannot do that work if you have already made them agree.

### Silence is a value

An extraction that returns fewer facts is often the correct one. A thin, honest extraction from
a thin document produces a finding. A full extraction from a thin document produces a document
that never existed, and nobody downstream can tell the difference.

## Provenance travels with every fact

Every fact carries the document identifier from the inventory and the location inside the
document. Without both, the fact is dropped.

| Document format | The location to record |
|---|---|
| Text document | Section number and heading, plus the paragraph or table |
| Workbook | Tab name, then cell or cell range, then the column header and the row label |
| Paginated or scanned document | Page, then the table and row, or the heading |
| Slide deck | Slide number and the element |
| Wiki or web export | Page title, heading anchor, and the date of the export |

Dropping is not a formality. By the time the assessment is written, an extracted fact and an
inferred one are typographically identical. Provenance is the only thing that separates them, it
has to be attached at the moment of reading, and nobody can reattach it afterward. A fact you
are sure of and cannot locate goes in the dropped list, where somebody can go and find it.

Record numbers, dates, names and signatures verbatim. Paraphrase only descriptions, and where
the value is a judgment rather than a number, carry the words you read it from alongside it.

## Extract the shape as well as the content

The content is what a document says. The shape is how it is organized, and downstream it matters
as much.

The shape that matters most is **keying**: what each recovery objective hangs off. Record it as
one of business process, system, server, tier, site, role, or none present. Record it per
objective, not per document, because mixed keying is common and is its own answer: processes in
the analysis, tiers in the plan.

Do not correct it. Record what is there. An objective keyed to infrastructure cannot say whose
work stopped, which is the only question an outage asks, and the assessment needs to know which
kind it found. An extractor who quietly re-keys tier objectives onto the processes that seem to
use them has erased the finding and replaced it with a tidy table.

Four more shape facts to record for every document:

Whether the impact scale is graded with defined thresholds, or a single value per process, or
absent. Whether a process to resource mapping exists, is partial, or is absent. Whether
objectives are stated per process or as one blanket statement over everything. Whether contact
information names people or names roles, and when it was last dated.

## What to pull, by kind of document

The kind comes from the inventory, decided by reading rather than by the title. Where a document
carries two kinds, run the targets for both against the parts that belong to each.

### Business Impact Analysis

| Target | What to record |
|---|---|
| Business processes in scope | The list as written, and the level they are stated at (a department, a process, a transaction) |
| Impact scale | Its categories, its grades, its thresholds, and whether the document defines it or assumes it |
| Impact per process | Which category, which grade, over which time horizon. A scale with no time horizon is recorded as having none |
| MTD per process | Verbatim, with its unit |
| RTO per process | Verbatim, with its unit |
| RPO per process | Verbatim, with its unit |
| Work Recovery Time per process | Where recorded. Most analyses do not carry it, and that is recorded as absent rather than as zero |
| What drives each objective | The stated reason: a regulatory deadline, a contractual penalty, a payroll cutoff, a customer commitment. Verbatim. An objective with no stated driver is recorded as having none |
| Alternate means of working | The manual workaround, its capacity, and how long it can be sustained |
| Process to resource mapping | Which components each process depends on, where present |
| Signatures | Who signed, in what role, on what date, and whether the role can commit the business |
| Currency | Document date, version, review cycle, and who was interviewed to produce it |

A [WRT](../../../GLOSSARY.md "Work Recovery Time") of zero and an absent one are different facts. So are an [MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime") that equals an RTO
because the business said so and one that equals it because somebody copied a column.

### Plans

Covers an [ISCP](../../../GLOSSARY.md "Information System Contingency Plan"), an [ITSCP](../../../GLOSSARY.md "IT Service Continuity Plan"), a [DRP](../../../GLOSSARY.md "Disaster Recovery Plan") and a [BCP](../../../GLOSSARY.md "Business Continuity Plan"). The targets are the same; what differs is the subject.

| Target | What to record |
|---|---|
| Activation criteria | What conditions start the plan. Record whether they are thresholds or left to judgment |
| Declaration authority | Who declares, by role and by name, and the deputy. Record all three or record which are missing |
| Notification | Who is told, through which channel, in what order, within what time |
| Recovery sequence | The order of restoration and what each step waits on. Record whether the order is stated or merely implied by the order of the sections |
| Roles and responsibilities | The teams, their membership, and whether membership is by person or by role |
| Contact currency | The date on the contact list, the number of entries, and whether entries are people or roles |
| Recovery objectives as the plan states them | Verbatim, with their keying, and separately from anything the analysis says |
| Alternate site or alternate processing | The arrangement, its location, and whether it is contracted, reserved or assumed |
| External dependencies | What the plan says it needs from somebody else |
| Reconstitution and return | How the service comes back to its normal home. This is the section most often absent |
| Governance | Owner, approver, approval date, version, last review, review cycle |

### Runbooks

| Target | What to record |
|---|---|
| Procedures | Each named procedure, and what it claims to accomplish |
| Sequence | The order, and whether it is stated or implied |
| Prerequisites | Access, credentials, tools and state assumed before step one |
| Decision points | Each branch, its condition, and what happens down each side |
| Verification | How the operator knows a step worked. A procedure with no verification is recorded as having none |
| Duration | Time expected per step, and whether it is measured or estimated |
| Rollback | What happens when a step fails, where stated |
| Followability | See below |

Followability is the target the others exist to support, and it is recorded as evidence rather
than as an opinion. The question is whether somebody who did not write the runbook could follow
it. Do not answer yes or no. List what the document leaves to the reader: a hostname with no
indication of where it lives, a phrase like "the usual process", a console named but not located,
a script path with no repository, an unexplained acronym, a credential referred to but not
sourced. Record the count and three or four examples with their locations. A later stage decides
what that count means.

### Test and exercise reports

| Target | What to record |
|---|---|
| Scope | Which systems, which processes, which phase of the plan. And what was stated as out of scope |
| Type | Walkthrough, tabletop, simulation, parallel, full interruption. As the report names it, not as you would classify it |
| When | Date and duration |
| Participants | By role, and whether the people who hold the recovery roles were among them |
| Objective in force | The objective the test was run against, as the report states it |
| Result | The recovery time and data loss actually achieved |
| How the result was arrived at | Measured, observed, or asserted. These are three different things and reports blur them |
| Findings | Each one, with its owner and its due date where present |
| Closure | Whether each finding was closed, by what evidence, on what date |

Record the objective and the result as two separate facts, always. Never extract the report's own
verdict as the fact. A report that says "RTO met" has compressed a measurement and a requirement
into one word, and the assessment needs both numbers. Where the report gives only the verdict,
record the verdict as the fact, note that no measurement was published, and record the
measurement as absent.

A test that recorded no findings is recorded as having recorded none. That is a fact about the
test, not a fact about the plan.

### Contracts, service level agreements and operational level agreements

| Target | What to record |
|---|---|
| Parties and term | Who is bound, and until when |
| Continuity obligations | Availability, recovery time, data protection, notification, alternate provision. Verbatim, with the clause reference |
| Evidenced or asserted | See below |
| Remedies | And whether the remedy restores service or compensates for its loss |
| The supplier's own dependencies | Where the document states them |
| Relationship owner | Who holds it internally |

Evidenced against asserted is the distinction the assessment needs and the one contracts hide. An
obligation is asserted when the document contains a clause and nothing stands behind it. It is
evidenced when something does: an attestation with a date, an audit report, a joint test record,
or a right to audit that was actually exercised. Record which, and record the evidence's own
location. A clause promising four hour recovery with nothing behind it is a sentence, and a
sentence is what will be available during the incident.

An [SLA](../../../GLOSSARY.md "service level agreement") binds the organization to somebody outside it. An [OLA](../../../GLOSSARY.md "operational level agreement") binds one internal team to
another and carries no external force. Record which you are reading.

### Training records

| Target | What to record |
|---|---|
| Who holds which recovery role | Person, role, and the date the assignment was recorded |
| Last trained | Per person, with the date and the content |
| Kind of training | Role specific, or general awareness. These are not interchangeable |
| New joiners | Whether anyone joined a role since the last training round, and whether they were covered |
| Role list against the plan's role list | Record both lists as they stand. Do not reconcile them |

## Record what the document conspicuously lacks

This is a second kind of output and it is distinct from a document that was never provided.

A plan with no declaration authority and a plan that nobody handed over are both gaps, and only
one of them is evidence about a document in your hands. The first is a defect in a document that
exists, was approved and is presumably in use. The second is an absence. They belong in different
lists, and collapsing them loses the more damning of the two.

Record a lack only where the kind of document would normally carry the target. A runbook has no
declaration authority and that is not a lack, because a runbook is not the place for one. A plan
without one is a lack, and it is the most serious one a plan can have.

Three grades:

| Grade | What you saw |
|---|---|
| `ABSENT` | No section, no heading, no mention anywhere |
| `PRESENT BUT EMPTY` | A heading with nothing under it, or placeholder text from the template, or "TBD" |
| `PRESENT BUT UNREADABLE` | A table that did not survive a conversion, an image of a diagram, a linked page you cannot open |

`PRESENT BUT EMPTY` is the grade a table of contents hides and an auditor finds. Record what the
document contains instead of the answer, verbatim, because "TBD" and "see Appendix D" and a
template's sample text are three different findings.

## When only part of the document is readable

Record which parts you read and which you could not.

Facts from the readable parts are facts. The unreadable parts produce no facts and, this is the
part that gets it wrong, they produce no absences either. You cannot say a document lacks
something you could not read. Any target that the unreadable part might have answered is graded
`PRESENT BUT UNREADABLE`, never `ABSENT`.

## Do not reconcile and do not resolve

A document that contradicts itself is extracted as two facts with two locations. An analysis
whose summary says four hours and whose table says eight hours has given you two facts, and the
contradiction is one of the more useful things you will find. Resolving it here hides it.

The same applies to anything that looks like an error: an RPO longer than an MTD, a plan dated
after its own review date, a process appearing twice with different objectives. Record it as
written. Add a note that says what you noticed. Never edit the value.

## The facts

This is the output. Field names and status words are fixed vocabulary, because the next stage
matches on them.

```
EXTRACTED FACTS
Document id: <id from the inventory>        Part: <extraction unit, or WHOLE>
Kind: <as classified at intake>             File: <filename as delivered>
Extracted: <date>                           Extracted by: <name or agent>
Read: <ALL / PART, and which parts were not readable>

FACTS                                                                 <n>
  target      <the extraction target this answers>
  subject     <the process, system, party or person the value belongs to>
  value       <verbatim for a number, date, name or signature>
  keyed to    <business process / system / server / tier / site / role / NOT KEYED>
  scope       <the scope the value was written at: one process, all systems, the service>
  basis       <MEASURED / OBSERVED / ASSERTED / STATED AS A REQUIREMENT>
  where       <section and heading, or tab and cell, or page, table and row>
  quoted      <the words the value was read from, where the value is a judgment>
  ...one block per fact

TARGETS NOT ANSWERED                                                  <n>
  <target>   <subject>   <ABSENT / PRESENT BUT EMPTY / PRESENT BUT UNREADABLE>
             <where it would have been>   <what is there instead, verbatim>
  ...

CONSPICUOUSLY LACKING                                                 <n>
  <what a document of this kind normally carries>   <grade>   <where>
  ...
  Distinct from a document that was never provided. This document exists.

SHAPE
  Objectives keyed to     <business process / system / server / tier / mixed / none present>
  Objective scope         <per process / one blanket statement / none>
  Impact scale            <graded with thresholds / graded without thresholds / single value / absent>
  Process to resource     <present / partial / absent>
  Contacts                <people / roles / mixed / absent>   dated <date or NONE>
  Currency                <document date>  <last review>  <review cycle>

CONTRADICTIONS WITHIN THIS DOCUMENT                                   <n>
  <fact A and where>   against   <fact B and where>
  ...
  Recorded, not resolved.

DROPPED FOR NO PROVENANCE                                             <n>
  <what the document appeared to say>   <why no location could be recorded>
  ...

IMPLICATIONS, NOT FACTS                                               <n>
  <what the document implies but does not state>   <where>
  ...
  Nothing in this block may be cited as evidence. It is here so the next stage
  knows what a reader would probably assume, not so it can be counted.

NOTHING WAS INFERRED
  Every value in FACTS was read from the location beside it. No objective,
  date, owner or result was estimated, converted, completed from a pattern,
  or carried in from another document.
```

The last block is a statement you sign, not a heading you leave in place. If it is not true,
find the fact that makes it untrue and move that fact into `IMPLICATIONS, NOT FACTS` or into
`TARGETS NOT ANSWERED`.

## Spell out every acronym in what you produce

The output this skill produces is read by somebody who was not in the room: a director, a
business owner, an auditor, somebody's replacement. Write the first use of every acronym in
full, with the short form in brackets after it, and use the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of
the skill needs them; they are expanded in the output because a reader of the report was never
given a glossary and cannot ask for one.

An acronym nobody expands is a reader quietly deciding the document was not written for them.

## What this skill does not do

It does not decide what arrived or what is missing from the set. That is `doc-intake`, and its
inventory is this stage's input.

It does not compare documents against each other. An analysis that disagrees with a plan is two
extractions, and the disagreement is found where both are in view.

It does not judge whether a fact is good enough. A four hour recovery objective is extracted as
four hours whether it is ambitious, unfunded or trivially met.

It does not grade, level or score anything, and it produces no number that could be averaged
with another.
