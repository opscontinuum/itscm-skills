---
name: doc-intake
description: For whoever takes delivery of a continuity documentation set, working by hand or as the first stage of an automated evaluation. Classifies every file by reading it rather than by the title on it, then records each document that should exist as provided, claimed but not provided, confirmed absent, or unreadable. Produces the inventory every later stage cites. Never reports a document it could not read as one that does not exist.
---

# Taking in a continuity documentation set

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **BIA** | Business Impact Analysis |
| **ISCP** | Information System Contingency Plan |
| **ITSCP** | IT Service Continuity Plan |
| **DRP** | Disaster Recovery Plan |
| **BCP** | Business Continuity Plan |
| **COOP** | Continuity of Operations Plan |
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **SLA** | service level agreement |
| **OLA** | operational level agreement |
| **ITSCM** | IT Service Continuity Management |


Somebody has handed over a folder. This stage runs once, before anything is assessed, and it
settles one question: what actually arrived.

Nothing here judges quality. A plan is not good or bad at this stage, it is present or it is
not, and it is one kind of document rather than another. That is the whole job, and it is worth
doing carefully because every later stage cites this inventory and none of them re-opens it. A
runbook classified as a plan gets assessed as a plan, fails criteria it was never written to
meet, and produces a finding about a document that does not exist.

You may be a person reading files, or an agent running one pass over a delivered set. The
method is the same. Nothing below is executed: you read, you decide, you record.

## Classify by reading, never by title

The title on a continuity document is the least reliable thing about it. Titles are chosen once,
by whoever created the file, often from a template name, and they survive years of the content
changing underneath them. A file called a Disaster Recovery Plan is frequently a contingency
plan and occasionally a runbook. A file called a Business Impact Analysis is sometimes an asset
inventory with an impact column bolted on.

So open every file and decide from the content. Record the title separately, because the title
is a fact about the organization even when it is wrong about the document.

### The tells

These are what you see on the page, not definitions. Two or three matching tells settle a
classification. One does not.

| Kind | What you see |
|---|---|
| Information System Contingency Plan | A single named information system as the subject. A system description and a system diagram near the front. Three phases, activation and notification, then recovery, then reconstitution. A damage assessment step. Lettered appendices carrying contact lists, a call tree and vendor details. The vocabulary of a security plan: the system owner, the authorizing official, the categorization of the system |
| IT Service Continuity Plan | A named service as the subject, with a service owner. References to a service catalog, to service level agreements and to operational level agreements. Dependencies listed as services or configuration items rather than as hostnames. Language about restoring service to the business rather than restoring a system |
| Technical runbook | Numbered steps in the imperative. Commands, hostnames, console paths, screenshots. No statement of when to start. No authority to declare anything. No business process anywhere in the document. It assumes somebody has already told you to run it |
| Business Continuity Plan | The organization or a business unit as the subject. People, premises and alternate ways of working. Staff safety, evacuation, relocation, customer communications. Information technology appears as one dependency among several, not as the subject |
| Disaster Recovery Plan | Nothing reliable. There is no standard content behind the title. Classify it by what it contains and record the title separately |
| Business Impact Analysis | One row or one section per business process. An impact scale. Recovery objectives attached to those processes. See the workbook section below, because this one most often arrives as a spreadsheet |
| Test or exercise report | Past tense throughout. A date, a scenario, participants, an outcome, a findings list |
| Post-incident review | A real event with a date and a timeline. Causes. Actions with owners |
| Contract, service level agreement or operational level agreement | Parties, a term, obligations, remedies. Defined terms in initial capitals |
| Training record | Names, dates, a course or a role. Usually a register rather than a document |

### The three pairs that are genuinely hard

**A system plan against a service plan.** Look at the subject line and at what the recovery
objectives hang off. An [ISCP](../../../GLOSSARY.md "Information System Contingency Plan") is about one information system and its objectives sit in a table
keyed to that system. An [ITSCP](../../../GLOSSARY.md "IT Service Continuity Plan") is about a service and reaches toward the business processes
the service carries. A document titled as a service plan whose objectives are all keyed to a
system is a system plan with a service plan's title, and that is what you record. The structures
are deliberately similar, so the subject and the keying are what separate them, not the headings.

**A plan against a runbook.** Ask whether the document tells you when to start. A plan states
activation criteria and names somebody who can declare. A runbook starts when a person tells you
to. Length decides nothing: a sixty page document of flawless procedure with no declaration
authority is a runbook, and a four page document with activation criteria, an authority, a
notification list and a recovery sequence is a plan.

**A plan against a Business Continuity Plan.** Ask whether information technology is the subject
or a dependency. If the document discusses where staff will sit and how orders get taken on
paper, it is a [BCP](../../../GLOSSARY.md "Business Continuity Plan") whatever its title says, and the recovery of a database appears in it as
one line somebody else owns.

### When a document is two things

This is common and it must not be flattened. A plan with a forty page runbook appendix is a plan
and a runbook. A workbook holding both the impact analysis and the contact list is an analysis
and a contact register.

Record a primary classification and a second kind, and record which parts of the document belong
to which. The next stage extracts different facts from each part, and if the second kind is lost
here the runbook appendix is never read as a procedure.

### Record the basis, always

Every classification carries the two or three tells that decided it. A classification with no
basis is an opinion, and nobody downstream can check it or overturn it. Two words are enough:
"three phases, damage assessment, system diagram".

## Titles, and what to do with the mismatch

Record the title as delivered and the classification from the content, in separate fields, and
never reconcile them. Where they differ, that difference is a finding in its own right and it
belongs in the inventory rather than in a later stage.

The reason is operational, not clerical. The organization believes it holds a disaster recovery
plan. What it holds is a runbook. On the night, somebody will search for the title, find the
file, open it, and discover that nothing in it says whether they are allowed to start.

## The four states

Every document that should exist ends in exactly one of four states. This is the load bearing
part of the inventory, because later stages decide what is evidenced from these words alone.

| State | Meaning |
|---|---|
| `provided` | You have it, you read it, and you can cite a location inside it |
| `claimed but not provided` | Somebody says it exists. You have not seen it |
| `confirmed absent` | A named person who would know states that it does not exist |
| `unreadable` | You have the file and could not read it: a scan, a format you cannot open, a corrupted or password protected file, a link to a system you have no access to |

### How to decide which

You have the bytes and you read them, so it is `provided`. You have the bytes and could not read
them, so it is `unreadable`. You do not have the bytes and somebody named says it exists, so it
is `claimed but not provided`. You do not have the bytes and a named person who would know says
it does not exist, so it is `confirmed absent`.

Absence requires a confirmer, by name. Where nobody will say either way, you have no
confirmation, so the entry is `claimed but not provided` with the claimant field reading that
nobody would confirm. That nobody could answer is worth a line in the inventory notes, because
it says something about ownership that no document will say.

### Claimed but not provided sits closer to absent than to present

State this in the inventory rather than leaving it to be inferred. A document nobody can produce
at review time is a document nobody will produce during an incident. It evidences nothing. No
later stage may credit a criterion against it, cite it, or count it toward coverage. The claim
is recorded because the gap between what an organization believes it has and what it can hand
over is itself worth reporting, not because the document counts.

### Unreadable is not absent, and reporting it as absent is a fabrication

A scanned plan is a plan. A workbook you cannot open holds whatever it holds. The state of its
contents is unknown, and unknown is not empty.

Carry `unreadable` all the way through to the output as its own category. Record what stopped
you and what would fix it: a text layer, a password, an export to a readable format, access to
the wiki. Those are usually cheap to resolve and a set can often be moved out of `unreadable`
in a day, which is not true of anything else in this inventory.

## Ask for the whole set in one request

Ask for everything below at once, by name. Do not ask for documents one at a time as you
discover you need them. A set requested piecemeal arrives piecemeal, takes weeks, and the gaps
start to look like your oversight rather than theirs.

Say up front, in the request itself, that **you expect some of these not to exist, and that
saying so is a complete answer.** Without that sentence people produce something rather than
admit to nothing, and you spend the assessment reading a document written the night before that
describes nothing anybody does.

Three more things to put in the request. Ask for the file rather than a description of it. Ask
for the version somebody would actually open during an incident, not the version in the
document management system, and record if they differ. Ask who holds each one, because the
answer to that question is frequently the finding.

### The plans

| Ask for | If they are unsure what you mean |
|---|---|
| Information System Contingency Plan | The system level recovery plan, often in the security plan's appendices |
| IT Service Continuity Plan | The service level plan, written around a service rather than a server |
| Disaster Recovery Plan | Often the only thing that exists. Ask for it by that name because that is the name they will recognize |
| Business Continuity Plan | The business side. Usually owned outside information technology. Ask anyway |
| Continuity of Operations Plan | Organizational continuity, mostly public sector |
| Crisis communications plan | Who tells whom, and who speaks to customers |
| Runbooks referenced by any of the above | The procedures the plan assumes exist |

### The analysis behind the plans

| Ask for | Why you need it |
|---|---|
| Business Impact Analysis | The requirement side. Without it every objective in every plan is unsourced |
| Recovery objectives however recorded | A spreadsheet counts. A wiki page counts. A slide counts |
| Risk assessment covering availability | What the plans are a response to |
| Service catalog or configuration item inventory | What is in scope, and what was left out |
| Dependency or service map | Which components each business process needs |
| The impact scale or rating definitions | Frequently a separate page, and without it the impact ratings mean nothing |

### The evidence the plans work

| Ask for | Why you need it |
|---|---|
| Test and exercise reports, the last three | The only proof a plan does anything |
| Post-incident reviews for real outages | Worth more than any test |
| Backup and restore verification records | A restore actually performed, with a date |
| Replication or data loss compliance records | Whether the data loss objective has been held continuously or only asserted |
| Training records for recovery roles | Who knows their part |

### The governance around the plans

| Ask for | Why you need it |
|---|---|
| Approval and signature records | Whether the objectives are commitments or proposals |
| Plan review schedule and last review date | Whether it is current |
| Change records that triggered a plan update | Whether change and continuity are connected |
| Contracts, service level agreements and operational level agreements carrying continuity terms | What was promised, and to whom |
| Supplier continuity attestations | The dependencies nobody in the room controls |

An [SLA](../../../GLOSSARY.md "service level agreement") between the organization and its customers and an [OLA](../../../GLOSSARY.md "operational level agreement") between two internal teams
are different documents with different force, and both get asked for. A [COOP](../../../GLOSSARY.md "Continuity of Operations Plan") and a [DRP](../../../GLOSSARY.md "Disaster Recovery Plan") are
also different documents, and an organization holding one often believes it holds the other.

## The spreadsheet Business Impact Analysis

The [BIA](../../../GLOSSARY.md "Business Impact Analysis") is the document the assessment leans on hardest, and it is the one that arrives as a
workbook more often than as prose. That makes it the hardest thing in the set to classify,
because a workbook has tabs rather than headings and a tab structure carries no title. The usual
title test has nothing to work on.

### Tells that a workbook is an impact analysis

One row per business process in the main table, with the process named in business terms
(invoice posting, order entry, payroll run) rather than in system terms. Column headers carrying
[MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime"), [RTO](../../../GLOSSARY.md "Recovery Time Objective") and [RPO](../../../GLOSSARY.md "Recovery Point Objective"), or the phrases maximum tolerable, recovery time and recovery point
written out. A separate tab or legend defining an impact scale, often with grades and money
thresholds. Data validation dropdowns feeding the impact columns, usually backed by a lookup tab
nobody has opened in years. Conditional formatting coloring impact severity. A frozen header
row, an instructions tab, and a revision log tab.

Tab names are the strongest single signal. Processes, Impacts, Objectives, Dependencies,
Contacts, Scale, Assumptions, Sign-off. Record every tab name in the inventory verbatim, whether
or not you understand it.

### What it is not, and how to tell

A risk register has columns for likelihood and impact, a scoring grid, a treatment and a risk
owner, and it has no recovery objectives. An asset inventory has one row per server or
application and no business process anywhere. A capacity or cost model has money and no
downtime. A configuration export has one row per configuration item and a column of identifiers.

The case that matters most is the unfilled template. Complete structure, complete formatting,
complete dropdown lists, and every data row empty or carrying the template's own examples
(Process A, 4 hours, High). That workbook is `provided` and it is a template, not an analysis.
Classify it as a template, say so in the basis field, and let the later stage extract zero facts
from it rather than extracting the examples as though they were the organization's.

### What to record for every workbook

Every tab name in order. Which tabs carry real data, which are empty, which are instructions,
lookups or revision logs. The row count of each data table. Whether hidden tabs, hidden columns
or filtered rows exist, because a filtered view hides rows from a reader and from an agent
equally. Whether formulas reference another workbook, since a formula pointing at a file you
were not given has just told you a document should exist.

Each data tab is a separate extraction unit and is listed as one in the inventory. The tabs of
one workbook are not one document, and treating them as one is how the dependency tab goes
unread.

A scanned or image-only analysis, whether workbook or document, is `unreadable`. It is never
`confirmed absent`.

## Reconcile against what should exist

You now have two lists: the documents you asked for, and the documents the delivered documents
themselves name. Both feed the inventory.

The second list is the one people forget and it is the stronger evidence. A plan that cites a
business impact analysis has told you in writing that one should exist. A test report that names
a plan version has told you which version should exist. A procedure that says "follow the
failover runbook" has named a document. Record each reference, what named it, and the state of
the thing named.

A document referenced in writing by a document you hold, and produced by nobody, is the
strongest form of `claimed but not provided`. The claim is not somebody's recollection in a
meeting. It is in the organization's own approved document.

## What this stage must refuse to do

| Refuse to | Because |
|---|---|
| Believe a title | It is the least reliable fact about the file, and everything downstream inherits the error |
| Classify from a filename or a table of contents | A table of contents describes the template the document started from |
| Record `unreadable` as `confirmed absent` | One is a gap in the documentation, the other is a gap in your access, and only one of them is the organization's problem |
| Credit, cite or count anything not provided | A document nobody can produce at review time evidences nothing |
| Merge several files into one entry | Each file gets an entry, even where three of them are drafts of the same plan. Which draft is current is a finding |
| Assess anything | Completeness, quality and sufficiency are later stages. Intake says what arrived |
| Fill a field you do not know | An unknown owner is recorded as unknown, never as the person who sent the email |

## The inventory

This is the output. Field names and state words are fixed vocabulary, because the next stage
matches on them.

```
DOCUMENT INVENTORY
Set: <organization, service or program>      Received: <date>      Recorded by: <name>
Requested: <date the full set was asked for>      Requested from: <name and role>

PROVIDED                                                              <n>
  id            <short stable identifier, cited by every later stage>
  file          <filename as delivered>
  title         <the title on the document>
  classified    <kind, decided from the content>
  basis         <the two or three tells that decided it>
  second kind   <other kind of content it also carries, and which part, or NONE>
  covers        <the system, service, process set or organization it is about>
  keyed to      <what its recovery objectives hang off, or NONE PRESENT>
  dated         <date on the document, or NONE>
  version       <version on the document, or NONE>
  owner         <named owner on the document, or NONE>
  approved      <signature or approval, with role and date, or NONE>
  format        <docx, xlsx, pdf text, pdf scan, wiki export, slide deck, email body>
  parts         <sections, tabs or appendices that each become an extraction unit>
  notes         <anything a later stage needs and no field above carries>
  ...one block per document

CLAIMED BUT NOT PROVIDED                                              <n>
  <kind>   claimed by <name and role>   asked <date>   <reason given, or NONE>
  ...
  These evidence nothing. No later stage may cite one.

CONFIRMED ABSENT                                                      <n>
  <kind>   confirmed by <name and role>   <date>
  ...

UNREADABLE                                                            <n>
  <file>   <format>   <what stopped you>   <what would make it readable>
  ...
  Not absent. Contents unknown until read.

TITLE AGAINST CONTENT
  <file>   titled <title>   is <classification>
  ...

REFERENCED BUT NOT IN THE SET
  <document that refers to it>   names   <document named>   <state of the named document>
  ...

WORKBOOKS
  <file>   tabs: <every tab name in order>
           data: <tabs carrying data>   empty: <tabs with none>
           hidden: <hidden tabs, columns or active filters, or NONE>
           external: <workbooks referenced by formula, or NONE>
  ...

EXTRACTION UNITS
  <id>   <kind>   <part, where the document splits into more than one>
  ...

NOTES ON THE SET
  <one line per observation about the set as a whole: drafts of the same plan,
   nobody able to confirm existence, a version in use differing from the version
   under control>
```

Order the provided blocks so the analysis comes before the plans and the plans before the
procedures. The later stages read requirements before they read responses, and an inventory
ordered that way is one fewer thing for them to sort.

## Spell out every acronym in what you produce

The inventory this skill produces is read by somebody who was not in the room: a director, a
business owner, an auditor, somebody's replacement. Write the first use of every acronym in
full, with the short form in brackets after it, and use the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of
the skill needs them; they are expanded in the output because a reader of the report was never
given a glossary and cannot ask for one.

An acronym nobody expands is a reader quietly deciding the document was not written for them.

## What this skill does not do

It does not read a document for content. Pulling the facts out of each provided document is
`doc-extract`, one run per extraction unit listed above.

It does not judge whether a plan is complete, sufficient or current. Those come later and they
depend on this inventory being right.

It does not chase the documents that did not arrive. That is a conversation with whoever owns
them, and the inventory is what you take into it: a list of names, dates and states rather than
an impression that things are missing.

It does not assign any [ITSCM](../../../GLOSSARY.md "IT Service Continuity Management") level, grade or score. Nothing in this repository averages
findings into a number, and this stage produces no findings at all, only states.
