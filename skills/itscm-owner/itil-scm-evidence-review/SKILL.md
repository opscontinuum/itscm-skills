---
name: itil-scm-evidence-review
description: Score a continuity documentation set that already exists against the ITIL 4 Service Continuity Management practice, using capability levels 1 to 5 across the four dimensions of service management. Criteria are evidence questions answerable from a document somebody handed over. It does not reproduce the licensed practice success factors and does not invent any, so it is an ITIL-aligned evidence review rather than an ITIL Maturity Model assessment, and every output says so.
---

# Scoring documentation that already exists

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ITSCM** | IT Service Continuity Management |
| **ITIL** | IT Infrastructure Library |
| **MM** | Maturity Model |
| **PSF** | practice success factor |
| **SLA** | service level agreement |
| **OLA** | operational level agreement |
| **DR** | disaster recovery |

Somebody has handed over a folder. This says where what is in it stands, and what specifically
holds it back.

You are scoring **documents**, not observing a practice. That is a real limit and it is the
reason this instrument is shaped the way it is.

## What this is, exactly

Be precise about it, because a capability level carries more authority than it earns and
somebody will eventually ask where it came from.

| | |
|---|---|
| **Scope** | The [ITIL](../../../GLOSSARY.md "IT Infrastructure Library") 4 Service Continuity Management practice, whose purpose is to ensure that the availability and performance of a service is maintained at a sufficient level in the event of a disaster |
| **Scale** | Practice capability levels 1 to 5, as published in the introduction to the ITIL Maturity Model |
| **Organized by** | The four dimensions of service management: organizations and people, information and technology, partners and suppliers, value streams and processes |
| **Criteria** | **This instrument's own.** Evidence questions, each mapped to a dimension and a level |

### The part to be careful about

In the real ITIL [MM](../../../GLOSSARY.md "Maturity Model"), capability criteria derive from
the **[practice success factors](../../../GLOSSARY.md "practice success factor")** defined in
the ITIL 4 practice guides, and are mapped to one of the four dimensions. Those guides are
behind a PeopleCert subscription.

**This instrument does not have the Service Continuity Management practice success factors, and
it does not invent them.** Do not write a [PSF](../../../GLOSSARY.md "practice success factor").
Do not infer one. Do not present a criterion below as though it descended from one. If you find
yourself about to author something that looks like a practice success factor, stop: the correct
output is a finding that this criterion could not be assessed against the licensed model, not a
substitute for it.

What the criteria are instead: evidence questions, answerable by pointing at a document. That
is a genuine difference in kind. A practice success factor is a statement about how a practice
behaves, which documents cannot settle. An evidence question is answerable by reading, which is
what you have been given.

### What this cannot produce

A certified assessment. ITIL MM certification comes only from a comprehensive engagement
covering the Service Value System plus seven or more practices, performed by a licensed
assessor, and a single practice capability assessment is not certifiable even when PeopleCert
runs it.

It also does not measure ITIL adoption. PeopleCert is explicit that the model is not designed
to assess the extent or success of the implementation of ITIL guidance. Neither is this. An
organization that has never used the word ITIL can score well here.

**Put all of that in the report header**, not in a footnote. A reader who takes this for a
certified assessment has been misled by its shape, and the shape is yours.

## The levels

Verbatim, then what each means for a documentation set.

| Level | The practice, verbatim | For a folder of documents |
|---|---|---|
| 1 | "not well organised; it is performed as initial/intuitive. It may occasionally or partially achieve its purpose through an incomplete set of activities" | Something exists. It is unowned, uncurrent, or unverifiable |
| 2 | "systematically achieves its purpose through a basic set of activities supported by specialised resources" | Owned, current, and covering the scope it claims |
| 3 | "well defined and achieves its purpose in an organised way, using dedicated resources and relying on inputs from other practices that are integrated into a service management system" | Derived from analysis, internally consistent, and connected to the practices it depends on |
| 4 | "achieves its purpose in a highly organised way, and its performance is continually measured and assessed" | Evidenced by measurement rather than assertion |
| 5 | "continually improving organisational capabilities associated with its purpose" | Findings change the documents, and the history shows it |

**Level 1 is the floor and there is no level 0.** Criteria run from 2 upward; level 1 is where a
dimension sits when it has not met level 2. A dimension with nothing at all is level 1 with
"nothing exists" stated, never unrated.

## Three verdicts per criterion, and the third is the one that gets dropped

| | |
|---|---|
| `MET` | You can point at the document and the location that satisfies it |
| `NOT MET` | You read what should satisfy it and it does not |
| `NOT ASSESSABLE` | The document that would settle it was not provided, was unreadable, or does not exist |

**`NOT ASSESSABLE` is never scored as `NOT MET`.** They have different remedies: one needs
work, the other needs somebody to send you a file. Report the count separately and name the
document that would settle each one.

**A dimension with more than two criteria `NOT ASSESSABLE` at a level is not scored at that
level.** Report it as unscored, with what is missing. A level assigned on a third of the
evidence is a number you invented.

## The criteria

Each criterion names the document that would satisfy it. Where none exists, that is the finding.

### Organizations and people

| Level | Criterion | Satisfied by |
|---|---|---|
| 2 | Every plan names an owner, and the recovery roles name people rather than teams | The plan's front matter, a roster |
| 2 | The people named know they hold the role | A roster with a confirmation date, training records |
| 3 | Roles carry documented responsibilities and a line of succession for unreachability | A roles document, a call tree |
| 3 | Role-specific training exists, with a syllabus and a stated cadence | A training plan |
| 4 | Training completion is recorded per person, and new joiners are trained within a stated period | Training records with dates |
| 4 | A test record shows the named people performing their own roles | A drill report naming participants |
| 5 | Training content has been changed by a test or incident finding | Version history plus the finding it answers |

### Information and technology

| Level | Criterion | Satisfied by |
|---|---|---|
| 2 | Recovery objectives exist in writing for the systems in scope | The [BIA](../../../GLOSSARY.md "Business Impact Analysis"), the plan, or a spreadsheet |
| 2 | A recovery approach is documented for each system in scope | An architecture or strategy document |
| 3 | Objectives are keyed to mission or business processes, not to systems, servers or tiers | The BIA's objectives table |
| 3 | [RTO](../../../GLOSSARY.md "Recovery Time Objective") is shorter than [MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime") on every row, and each objective names what drives it | The same table |
| 3 | The recovery approach traces to those objectives, and any shortfall is a tracked gap rather than a relaxed objective | Strategy document, a gap or risk register |
| 4 | Achievable recovery time is measured rather than estimated, and compared to the objective | A drill report with timings |
| 4 | Data loss is measured **continuously** against the [RPO](../../../GLOSSARY.md "Recovery Point Objective"), not only at test time | Replication lag records, an availability report |
| 5 | A measured shortfall has driven a design change | Change record plus the measurement that prompted it |

**The keying criterion at level 3 is the one that caps most assessments.** Objectives stated per
infrastructure tier are real numbers, often carefully derived, and they cannot answer whose work
stopped. Report it as present and keyed wrong, never as missing, and say the remedy is a
re-analysis rather than a writing task. An author who reads "missing" about a table they can see
will dismiss the rest of the report with it.

### Partners and suppliers

| Level | Criterion | Satisfied by |
|---|---|---|
| 2 | Suppliers and external dependencies material to recovery are listed | A vendor appendix, a contact roster |
| 3 | Continuity obligations appear in contracts, [SLAs](../../../GLOSSARY.md "service level agreement") or [OLAs](../../../GLOSSARY.md "operational level agreement"), covering every dependency the plans name | The contracts, cross-checked against the plan |
| 4 | Supplier continuity claims are evidenced by attestation, audit or joint test, not accepted on assertion | An attestation, an audit report |
| 5 | A supplier has been included in an exercise, and a finding against one was acted on | A drill report, a change record |

### Value streams and processes

| Level | Criterion | Satisfied by |
|---|---|---|
| 2 | A plan exists covering activation, recovery and reconstitution, and was reviewed within its own stated cycle | The plan, its revision history |
| 3 | A BIA exists with named business processes and impacts rated on a defined scale | The BIA |
| 3 | Activation criteria and declaration authority are stated, and procedures are followable by somebody who did not write them | The plan's activation and recovery sections |
| 3 | Which resources each business process depends on is recorded somewhere | A dependency map, an architecture document, the BIA |
| 3 | The plan's objectives match the BIA's, and contact information is current | Both documents, cross-checked |
| 4 | The plan has been followed end to end in a test or a real incident, with the result recorded against the objective | A drill report, a post-incident review |
| 4 | A change to a system reached the plan, traceably | A change record and the plan revision answering it |
| 5 | Plans are corrected from test and incident findings, with version history showing it | Revision history plus the findings |

**The level 4 change-integration criterion is the one almost nothing passes.** Take a specific
recent architecture change and follow it into the plan. If the plan does not mention it, the
plan describes a system that no longer exists, whatever its review date says.

## Scoring

A dimension sits at the **highest level whose criteria are all met**, and where every lower
level's criteria are also met. Skipping is impossible: an untested documentation set is not
level 4 however good it reads.

**Nothing is averaged, weighted or blended.** Nine criteria of ten met is the lower level, not
ninety percent of the higher one. If you find yourself computing anything, you have left the
method: levels are read off a checklist.

### Overall is the lowest dimension

Not a mean. An organization is not two and a half levels mature, and for continuity the weakest
dimension decides the outcome: a well documented, widely trained recovery capability that has
never been measured is an unproven one, and averaging it up to a comfortable middle is the thing
this instrument exists to refuse.

Report the lowest, name which dimension set it, and show the per-dimension levels beside it so
the strong ones are visible.

### Claimed against evidenced

A level says how well organized the documentation is. It does not say whether recovery works.
Report each dimension twice:

| | |
|---|---|
| **Claimed** | What the documentation supports |
| **Evidenced** | What a test, drill or real incident has demonstrated |

**Where nothing has been tested, evidenced is 1** on every dimension that depends on proof. Say
the word **unproven** in the report header, with the date of the last test that demonstrated
anything, because a reader who has to infer that from a number will not.

Organizations and people, information and technology, partners and suppliers, and value streams
and processes can all differ between the two readings. Nothing is exempt here, because a
documentation set is exactly the thing that can look complete and be untested.

## The report

```
ITSCM DOCUMENTATION EVIDENCE REVIEW
Organization / service: <name>        Reviewed: <date>        Reviewer: <name>

WHAT THIS IS
  Scope:    ITIL 4 Service Continuity Management practice
  Scale:    ITIL Maturity Model practice capability levels 1 to 5
  Criteria: this instrument's own evidence questions, mapped to the four
            dimensions of service management. NOT derived from the practice
            success factors in the licensed ITIL 4 practice guide, which were
            not available and were not reconstructed.
  This is not a certified assessment and cannot be presented as one.

PROVEN OR UNPROVEN
  <one word>.   Last test that demonstrated anything: <date, or NEVER>

LEVELS                                  claimed    evidenced
  Organizations and people                 <n>        <n>
  Information and technology               <n>        <n>
  Partners and suppliers                   <n>        <n>
  Value streams and processes              <n>        <n>

  Overall claimed   <lowest>       Overall evidenced  <lowest>
  Constrained by:   <dimension>, on <the one criterion it fails>

WHAT BLOCKS THE NEXT LEVEL
  <dimension>   <the criterion, verbatim>   <what document would satisfy it>
  ...

NOT ASSESSABLE                                        <n>
  <criterion>   <the document that was not provided, unreadable, or absent>

DOCUMENTS
  provided <n>   claimed but not provided <n>   absent <n>   unreadable <n>
```

Lead with proven or unproven. Everything under it is the evidence for that word.

### Writing the blocking line

One per dimension, and this is the part anybody acts on. It names a criterion, not a theme.

> Information and technology is at 2. Objectives exist for all eleven systems and are keyed to
> service tiers rather than to business processes, so nothing in the set can say whose work
> stops. Level 3 needs the objectives re-derived per process, which is a workshop with the
> business rather than an edit.

Not: *"the analysis needs strengthening."*

## Spell out every acronym in what you produce

The report is read by somebody who was not in the room: a director, an auditor, somebody's
replacement. Write the first use of every acronym in full, with the short form in brackets
after it, and use the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of the
skill needs them; they are expanded in the output because a reader of the report was never given
a glossary and cannot ask for one.

An acronym nobody expands is a reader quietly deciding the document was not written for them.

## What this does not do

It does not assess an individual plan's structure or derivability. Those are separate
instruments, they read one document each, and their findings are inputs here rather than
outputs.

It does not interview anybody. It reads what it was given, which is why a dimension can be
`NOT ASSESSABLE` rather than failed, and why the report separates the two.

It does not produce the roadmap. The blocking criteria it names are the input to that.
