# itscm-skills

**Terms used here.** The full list is [`GLOSSARY.md`](GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ISCP** | Information System Contingency Plan |
| **ITSCM** | IT Service Continuity Management |
| **SSP** | System Security Plan |
| **NIST** | National Institute of Standards and Technology |
| **SP** | Special Publication |
| **ITIL** | IT Infrastructure Library |
| **DR** | disaster recovery |


A continuity program you can run by hand.

These are instruction documents for working out what happens when a system stops, how long the
business can stand it, and what to recover first. They need no software. A word processor, a
spreadsheet and the right people in a room will do.

## The whole process, and how much of it exists

Business sets the requirement, the product owner assembles it, IT states what can actually be
delivered. Color is completeness: green is done, red is nothing exists yet.

```mermaid
flowchart TD
    classDef full fill:#1b7f3b,stroke:#0d4d22,color:#ffffff,font-weight:bold
    classDef half fill:#f2b705,stroke:#a87e00,color:#1a1a1a,font-weight:bold
    classDef some fill:#e8710a,stroke:#9c4a00,color:#ffffff
    classDef none fill:#c62828,stroke:#7f1d1d,color:#ffffff,font-weight:bold

    subgraph BUS["1 . BUSINESS  ·  states the requirement"]
        direction TB
        B1[Name the business processes]
        B2[Define the impact scale<br/>severe / moderate / minimal]
        B3[Rate impact per process]
        B4[Set MTD, RTO and RPO<br/>per process]
        B5[Record alternate ways of working]
        B6[Sign the objectives]
        B1 --> B2 --> B3 --> B4 --> B5 --> B6
    end

    subgraph PO["2 . PRODUCT OWNER  ·  assembles the program"]
        direction TB
        P1[Assess what exists today]
        P2[Audit a plan for structure]
        P3[Audit a plan for derivability]
        P4[Collect into the workbook]
        P5[Build the resource inventory]
        P6[Map each process to its resources]
        P7[Derive the recovery priority order]
        P8[Write the plan]
        P9[Onboard a PROGRAM<br/>not a single system]
        P10[Find contention across programs]
        P11[Review capability against ITIL]
        P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8
        P8 --> P9 --> P10 --> P11
    end

    subgraph IT["3 . IT  ·  states the capability"]
        direction TB
        I1[Infrastructure interview]
        I2[Application interview]
        I3[Governance interview]
        I4[Continuity interview]
        I5[State the achievable RTO and RPO]
        I6[Author the DR runbooks]
        I7[Capture the freeze windows]
        I8[Run the drill and record it]
        I9[Measure replication lag<br/>against the signed RPO]
        I1 --> I2 --> I3 --> I4 --> I5 --> I6 --> I7 --> I8 --> I9
    end

    subgraph APP["4 . THE PRODUCT  ·  what it must hold"]
        direction TB
        X1[Reconciliation across<br/>four truth claims]
        X2[Approval control<br/>two principals]
        X3[Execution and audit record]
        X4[Domain model for<br/>programs and objectives]
        X5[Storage for program content<br/>versioned and signed]
        X6[Onboarding surface]
        X7[Sign-off surface<br/>routed to the right signer]
        X8[Capability picture<br/>claimed vs evidenced]
        X9[Failover and DR actions]
        X10[MTD countdown and hold-down]
        X1 --> X2 --> X3
        X4 --> X5 --> X6 --> X7 --> X8
        X9 --> X10
    end

    B6 -.->|"the signed requirement"| P4
    I5 -.->|"the real capability"| P6
    P6 -.->|"what IT must deliver"| I6
    P9 -.->|"needs all of section 4"| X4
    I9 -.->|"breach raises an incident"| X10

    class B1,B2,B3,B4,B5 full
    class B6 half
    class P1,P2,P3,P4,P7,P8,P10,P11 full
    class P5,P6 half
    class P9 none
    class I8 some
    class I1,I2,I3,I4,I5,I6,I7,I9 none
    class X1,X2,X3 full
    class X6 some
    class X4,X5,X7,X8,X9,X10 none

    click B1 href "skills/business/bia-workshop/" "bia-workshop, step 1: name the processes"
    click B2 href "skills/business/bia-workshop/" "bia-workshop, step 2: build the impact scale"
    click B3 href "skills/business/bia-workshop/" "bia-workshop, step 2: rate each process"
    click B4 href "skills/business/bia-workshop/" "bia-workshop, step 3: MTD then RTO then RPO"
    click B5 href "skills/business/bia-workshop/" "bia-workshop, step 3: alternate means"
    click B6 href "skills/business/bia-workshop/" "bia-workshop: get it signed in the room"
    click P1 href "skills/product-owner/itscm-program-assessment/" "itscm-program-assessment"
    click P2 href "skills/product-owner/iscp-completeness/" "iscp-completeness"
    click P3 href "skills/product-owner/iscp-sufficiency/" "iscp-sufficiency"
    click P4 href "worksheets/" "the data-collection workbook"
    click P5 href "worksheets/" "workbook tab 6"
    click P6 href "worksheets/" "workbook tab 7, the join"
    click P7 href "skills/business/bia-workshop/" "bia-workshop, step 4: derive priorities"
    click P8 href "skills/product-owner/iscp-from-worksheet/" "iscp-from-worksheet"
    click P10 href "skills/product-owner/enterprise-bia/" "enterprise-bia"
    click P11 href "skills/product-owner/itscm-coordinator-review/" "itscm-coordinator-review"
```

### Reading it

| | |
|---|---|
| **Green** | Exists and is usable today |
| **Amber** | The method exists, the mechanism that enforces it does not |
| **Orange** | A fragment exists, mostly as an example rather than a procedure |
| **Red** | Nothing exists |

**A box you can click is a box that exists.** Every green and amber node links to the skill or
worksheet that performs it. The red ones link nowhere, because there is nothing to open.

**Section 1 is done.** A business impact session can be run today, start to finish.

**Section 2 works apart from two things.** The resource inventory and the process-to-resource
map are amber because the workbook has tabs for them and nothing walks anybody through filling
them, and both need input from section 3. Onboarding a program rather than a single system is
red everywhere it appears.

**Section 3 is the wall.** Every interview that produces IT's half of the comparison is
unported, so the walkthrough stops after the product owner. This is the shortest path to an
end-to-end process and it is four skills.

**Section 4 is three green boxes and seven red ones.** What exists is reconciliation, the
approval control and the execution record, and all three are real. What does not exist is
anywhere to put a program, an objective, a signature, or a countdown.

The two dotted lines into section 3 are the point of the whole arrangement. The business states
what it needs, IT states what it can do, and the gap between them is either a funded project or
an accepted risk. Collapse the two legs into one conversation and that gap stops being visible.

## Find your way in

Three people have to do different things here, and doing somebody else's part is the most
common way this goes wrong.

### You own a business process

Somebody has asked you how long your work can be down. You are the only person who can answer
that, and this section is short because your part is short.

You will be asked what stops when the system stops, what it costs by the hour, and at what
point the consequences change shape. Answer in your own words. If you find yourself describing
servers, you have drifted into somebody else's job.

Three things to hold on to:

You set the maximum tolerable downtime. Not IT, not the vendor, not whoever wrote the last
plan. If the only people in the room are technical, stop the session. A recovery target set by
IT is IT deciding what it is allowed to fail at.

Answer for the worst week, not an average one. Continuity is bought for period close, the
payroll run and the day the bank file cuts. It is almost always specified against a quiet
Tuesday.

Your numbers are a proposal until you sign them. An objective nobody signed cannot be missed,
because nobody promised it.

Read [`bia-workshop`](skills/business/bia-workshop/) if you want to know what the session will ask
before you walk into it.

### You own a system and have to produce a plan

You are running this. The order matters, because each step feeds the next and doing them out of
order is how plans end up describing infrastructure instead of the business.

1. Find out what already exists.
   [`itscm-program-assessment`](skills/product-owner/itscm-program-assessment/) asks eight questions about
   your organization and produces a one month, three month and one year roadmap. Start here
   even when you are sure the answer is "nothing", because that produces a three item roadmap
   rather than a forty item one.
2. If a plan already exists, test it twice.
   [`iscp-completeness`](skills/product-owner/iscp-completeness/) asks whether the document is intact against
   the standard that governs it. [`iscp-sufficiency`](skills/product-owner/iscp-sufficiency/) asks whether
   anything can be built from what it contains. A plan can pass either and fail the other.
3. Collect the data.
   [`worksheets/iscp-data-collection.xlsx`](worksheets/) has a tab for each thing a plan needs.
   Fill it in the order the tabs are numbered.
4. Run the session that produces the numbers.
   [`bia-workshop`](skills/business/bia-workshop/) is half a day with the business, and it is where the
   recovery objectives come from.
5. Write the plan.
   [`iscp-from-worksheet`](skills/product-owner/iscp-from-worksheet/) takes the filled workbook and produces
   the document, refusing to write any section the data does not support.

One warning, because it is the thing most likely to sink you. Tab 7 of the workbook records
which components each business process depends on. Every standard template leaves it out, so
almost everybody skips it, and without it there is no route from "payroll matters most" to
"restore the database first". A plan missing that tab can look finished and still not say what
to fix first.

### You coordinate continuity across more than one system

You are not producing a plan. You are answering whether the practice is in good order, usually
for somebody who will not read a plan.

[`itscm-coordinator-review`](skills/product-owner/itscm-coordinator-review/) is yours. It asks for the whole
documentation set in one request, records what did not arrive as evidence in its own right, and
reports a capability level from 1 to 5 across eight dimensions, using the [ITIL](GLOSSARY.md "IT Infrastructure Library") Maturity Model's
practice capability scale applied to ITIL 4's Service Continuity Management practice. The scale
and vocabulary are ITIL's so the result translates; the criteria are the skill's own, derived
from failure modes seen in real documentation, because the practice success factors that real
ITIL criteria come from sit behind a PeopleCert membership. The skill says so in its own words
rather than letting a number imply a badge it cannot issue.

Two things about it worth knowing before you run it. It treats "it exists, we just cannot find
it" as closer to absent than to present, because a document nobody can produce at review time
is a document nobody will produce during an incident. And the overall level is the lowest
dimension rather than an average, because a well designed and widely trained recovery
capability that has never been tested is an unproven one, and averaging hides exactly that.

### You own ITSCM across more than one program

Your problem is not any one plan. It is that every plan can be right on its own and the
organization still cannot recover, because each was written as though its program were alone.

[`enterprise-bia`](skills/product-owner/enterprise-bia/) lays them against each other. It finds four kinds of
contention, and most reviews only look for the first: two processes sharing a resource with
different deadlines, the same with different recovery point objectives, two programs planning to
fail over into the same [DR](GLOSSARY.md "disaster recovery") capacity that was sized for one of them, and the same named engineer
appearing in six recovery rosters that would all activate in the same regional event.

It produces a ranked recovery priority list and a board paper, because the conflicts it finds
are funding decisions and you are not the one who gets to make them. It will not resolve a
contention by defaulting to the tightest deadline, which is the tempting answer that makes a
report look finished while quietly committing money nobody approved.

### You run the infrastructure

> **There is no skill for your part yet.** This section tells you what you own and what to
> refuse. It does not walk you through a session. The infrastructure and application interviews
> have not been written yet, so a start-to-finish walkthrough currently stops after the
> product owner.

Your part is to say what the system can actually do, and to keep that separate from what the
business needs it to do.

You own the recovery time that is technically achievable, the data loss the replication
actually permits, the inventory of components, and which components each process depends on.
That last one usually only exists in your head, and writing it down is the single most useful
thing you can contribute.

You do not set the maximum tolerable downtime. If you are the only person available when that
question comes up, say so and stop rather than filling it in. A requirement copied from a
capability destroys the only comparison worth having, because the plan can then never tell
anyone the architecture is inadequate.

When the business asks for something the architecture cannot deliver, the answer is a tracked,
owned, dated gap item, which NIST calls a Plan of Action and Milestone. It is not a quietly
relaxed target. Writing the achievable number into the requirement makes the gap invisible and
guarantees nobody funds closing it.

[`iscp-sufficiency`](skills/product-owner/iscp-sufficiency/) is the one to read if you have inherited a plan
and want to know whether it can actually drive anything.

## The skills

They are grouped by who runs them, because running someone else's part is the main way this
goes wrong.

```
skills/
├── business/        states the requirement    1 skill
├── product-owner/   assembles the program     6 skills
└── it/              states the capability     empty, and that is the finding
```

[`skills/it/`](skills/it/) holds a README and no skills. The folder exists so the gap is
structural rather than a footnote: six pieces belong there and none is written, which is why a
walkthrough stops after the product owner.

| Skill | What it does |
|---|---|
| [`itscm-program-assessment`](skills/product-owner/itscm-program-assessment/) | Interview an organization to find out what its continuity program actually contains, then produce a one month, three month and one year roadmap. Assumes no continuity tooling is installed. |
| [`enterprise-bia`](skills/product-owner/enterprise-bia/) | Lay every program's BIA against the others, find where they contend for the same resource, DR capacity or people, and produce a ranked recovery priority list plus a board paper. Never defaults a contention to the tightest deadline. |
| [`bia-workshop`](skills/business/bia-workshop/) | Facilitate the Business Impact Analysis that becomes ISCP Appendix L, in the order NIST states it. Keeps recovery objectives keyed to business processes rather than to systems or tiers. |
| [`itscm-coordinator-review`](skills/product-owner/itscm-coordinator-review/) | Assess a whole continuity documentation set rather than one plan. Requests every document it needs, records what did not arrive, and reports a capability level per dimension against ITIL 4 Service Continuity Management. |
| [`iscp-completeness`](skills/product-owner/iscp-completeness/) | Audit a plan against FedRAMP SSP Appendix G v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports what is missing, what is present but unfilled, and what is present and answered. Also asks whether the plan carries a fact sheet for whoever meets an incident first. |
| [`iscp-sufficiency`](skills/product-owner/iscp-sufficiency/) | Decide whether a plan carries enough data to build a program from it. A field is required only when a named downstream artifact provably cannot be produced without it. |
| [`iscp-from-worksheet`](skills/product-owner/iscp-from-worksheet/) | Turn a filled data-collection workbook into a plan, after checking the data can support one. Validates the joins between tabs rather than the presence of cells. |

`itscm-program-assessment` is the entry point for an organization. `bia-workshop` is the entry
point for a session with the business.

The three document skills answer different questions about the same file and should not be
collapsed into one. Whether the document is intact, whether a program can be derived from it,
and what the organization has in people and cadence are three findings with three different
remedies.

## What is not here yet

A start-to-finish walkthrough works for the business and the product owner and then stops.
These are the pieces still to be written, listed in [`skills/it/`](skills/it/):

| Missing | What it would do |
|---|---|
| Infrastructure and application interviews | The IT leg. What the architecture can actually deliver, and the dependency map |
| Governance and continuity interviews | Ownership, cadence, and the continuity questions that sit outside the BIA |
| `dr-runbook-authoring` | Operational writing discipline for recovery procedures. Nothing here covers it |
| Portfolio and dependency scope | Building the register across systems. `enterprise-bia` assumes it exists |

They are routed into two entry points rather than one, deliberately. The business leg and the
IT leg collect different halves of one comparison, and a single entry point that ran all of
them would put IT in the room when the recovery objectives are set.

## A worked example

[`examples/ebs-exadata-business-leg.md`](examples/ebs-exadata-business-leg.md) is the business
leg run end to end against a real architecture: Oracle E-Business Suite on Exadata across two
regions, with the product owner asking for realtime operation, 99.9% availability and a
recovery point objective of zero or near zero. The architecture it needs is reproduced inside it, so it stands alone.

It is here because it shows what a finished business leg actually contains, and because running
it surfaced things the method alone does not. The most useful: **an [RPO](GLOSSARY.md "Recovery Point Objective") cannot vary by process
when the processes share a database.** One synchronous standby protects one database, so a
first pass setting zero for revenue and five minutes for procurement was asking for something
not purchasable. RPO is stated per replication boundary.

Also worth the read: 99.9% turns out to be the more rigorous ask rather than the weaker one,
because against a 45 minute recovery it permits about one event a month, where 99.99% permits
about one a year and is really a promise never to invoke recovery at all.

## The workbook

[`worksheets/iscp-data-collection.xlsx`](worksheets/) collects everything a plan needs across
thirteen tabs, ordered so each one feeds the next. Regenerate it with
`worksheets/build_workbook.py`; that script runs here, never at the reader.

The dropdowns are fed by the tabs already filled in. Processes entered on tab 2 and resources
on tab 6 become the only permitted values wherever they are referenced later, so an objective
cannot be recorded against a process nobody named and a dependency cannot point at a component
that does not exist. The spreadsheet enforces that, rather than a reviewer noticing three
months later.

Tab 7 records which resources each process depends on. No standard template prompts for it and
none forbids it, and NIST's third [BIA](GLOSSARY.md "Business Impact Analysis") step, identifying recovery priorities for system
resources, cannot be performed without it. The mapping is a prerequisite of a required step
rather than an addition to the method.

## The keying rule

A recovery objective belongs to a business process. Not to a system, a server or a tier.

Systems are what processes depend on. A system tier, where one exists, is derived from process
requirements by a stated mapping, and never replaces them.

This is the failure a completeness audit cannot see. A plan whose objectives hang off
infrastructure tiers looks finished: every heading present, every table filled, real numbers
carefully argued. It just cannot answer the question an outage asks, which is whose work has
stopped and for how long. A tier is a property of infrastructure. Only a business process has a
maximum tolerable downtime.

Competent people break this rule constantly, because an infrastructure team naturally states
objectives against what it owns, and because tooling that builds a register of systems invites
hanging the numbers on the system row.

## Everything here runs with no interpreter

No skill in this repository executes anything. The reader may be a web based agent with no
filesystem and no interpreter, working from a document somebody pasted into a chat window.
Every skill has to be useful under exactly those conditions.

Some questions do need a machine to answer. A skill here asks the operator to run one command
and paste the result back, under four rules: name the exact command, keep it read only, say
what you will do with the output first, and still work when the answer is "I cannot run that".

That last rule is the one that matters. What somebody tells you is not what you measured, and
the report says which it was.

## The manual path is one of two

The same method can be carried by tooling: a collector reading the running systems, a generator
writing into the document, a plug-in per source. These skills are what an organization uses when
it cannot run any of that, which is most organizations most of the time.

Where both exist for one job, the tooling is authoritative about mechanics and the skill is
authoritative about judgment. Neither is a degraded copy of the other.

## Every requirement starts unmet

A requirement gets a verdict or it gets `NOT ASSESSED`, and `NOT ASSESSED` is reported rather
than counted as a pass. A checker that quietly omits what it could not evaluate produces a
number that reads as completeness and is not.

The assessment skill uses four states instead: `Established`, `Asserted`, `Unknown` and
`Absent`. Those are four different facts with four different remedies, not four points on a
scale, and nothing here averages them into a percentage. A program described as sixty percent
mature tells nobody what to do on Monday.

### The one place a number is allowed

`itscm-coordinator-review` reports a capability level from 1 to 5, and that is not a
contradiction of the rule above, because a level here is read off a checklist rather than
calculated.

Each level has explicit entry criteria and all of them must be met. Nine criteria out of ten is
the lower level, not ninety percent of the higher one. Nothing is weighted, summed or blended,
and every level is reported alongside the specific criterion blocking the next one. The number
exists so a coordinator can compare forty systems or show movement across two years, which a
gap list genuinely cannot do. The sentence naming the blocker is still the part anybody acts
on.

## Conventions

[`CONVENTIONS.md`](CONVENTIONS.md) holds the binding rules for anything written here, each with
the cost of having broken it once. The two that shape every page: every acronym is expanded on
first use and linked with hover text, and this repository cites nothing outside itself.

## Acronyms are defined where they are used

Every acronym is expanded the first time a document uses it, and each document carries a short
table of just the terms it uses. [`GLOSSARY.md`](GLOSSARY.md) holds all of them in one place.

The per-document tables are not redundancy for its own sake. A skill is read on its own, often
by a model with no filesystem working from a pasted document, and a reader who has to leave the
page to find out what [MTD](GLOSSARY.md "Maximum Tolerable Downtime") stands for has been sent somewhere they may not be able to go. The
same reasoning governs citations below.

## This repository cites nothing outside itself

Every path in these documents resolves inside this repository, and every fact a reader needs is
written here.

The rule exists because it was broken once. The worked example cited an architecture by file
path, those files lived in a different repository, and anyone following them found nothing.
Rather than linking out, the architecture the example depends on is now reproduced inside it.

Duplication is the deliberate choice. A skill that sends its reader somewhere else has assumed
the reader can get there, and the reader is frequently a model with no filesystem working from a
document somebody pasted into a chat window. Anything worth citing is worth restating.

## Provenance

Reference data in `iscp-completeness` was transcribed from:

- FedRAMP [SSP](GLOSSARY.md "System Security Plan") Appendix G: Information System Contingency Plan ([ISCP](GLOSSARY.md "Information System Contingency Plan")) Template, version 5.0,
  dated 12/06/2024. Downloaded 2026-09-02 from
  `https://www.fedramp.gov/resources/templates/SSP-Appendix-G-Information-System-Contingency-Plan-(ISCP)-Template.docx`,
  HTTP 200, 153865 bytes, md5 `298f6b1392ee21b1cded5164c2523b86`.
- NIST SP 800-34 Rev. 1, Appendix B, "Sample Business Impact Analysis (BIA) and BIA Template",
  pages B-1 to B-4, May 2010 (errata 2010-11-11).

Both are public documents published by their issuing bodies.
