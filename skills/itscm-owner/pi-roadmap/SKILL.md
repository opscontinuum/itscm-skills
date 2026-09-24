---
name: pi-roadmap
description: Turns a completed capability assessment of an existing continuity documentation set into a roadmap at one, three, six, nine and twelve months, written to be loaded into Program Increment planning. Takes the blocking criterion the assessment named per dimension and schedules the workshop, test or writing that closes it, sequenced by what blocks what rather than by effort.
---

# Turning a capability assessment into a Program Increment roadmap

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ITSCM** | IT Service Continuity Management |
| **ITIL** | IT Infrastructure Library |


This is the last stage of evaluating an [ITSCM](../../../GLOSSARY.md "IT Service Continuity Management") documentation set that already exists. An
earlier stage read the documents the organization actually has, placed each of the four
dimensions of service management on an [ITIL](../../../GLOSSARY.md "IT Infrastructure Library") capability level, and named, per dimension, the
one criterion blocking the next level. The evidence review in `itil-scm-evidence-review`
produces exactly that, and its blocking lines are this skill's input. Your job is to turn those
criteria into scheduled work.

The four dimensions carried through are organizations and people, information and technology,
partners and suppliers, and value streams and processes. Use the names the assessment used, in
the order it used them, so a reader can hold the two documents open side by side.

You are not assessing. Every level and every blocking criterion arrives from the earlier stage
and passes through this skill unchanged. If you catch yourself forming a view about a level,
take it back to whoever produced it. A roadmap built on a level you quietly adjusted traces
back to nothing.

## What you need before you start

| What you need | Why, and what to do without it |
|---|---|
| A capability level per dimension | The starting position. Without it you are writing a wish list. Stop and get the assessment |
| The specific criterion blocking the next level, per dimension | This is the roadmap. Every item exists to close one of these. A dimension whose blocking criterion is stated as a theme rather than a criterion goes back for a rewrite |
| Which documents were provided and which were not | An unprovided document is not evidence, so the work it would have closed is still work |
| The criteria the assessment could not judge, with the document that would settle each | These are gaps in what you were sent, not gaps in the program. They are handled separately, below |
| The claimed level and the evidenced level per dimension | Where the two differ, the difference is proof, and proof is a test |
| The name of a person per document or per dimension | Items need owners. Where there is no name, the item carries `UNOWNED` and that is a finding, not a blank |
| The length of the increment the organization plans in, and the date of the next planning event | The horizons below convert into increments. Converting them after the roadmap is written changes which items are commitments |

## Who reads this, and what that changes

A manager who has to put continuity work into Program Increment planning, next to everything
else competing for the same teams. That reader is not deciding whether continuity matters. They
are deciding what to bring to a planning event where most of what they bring will be cut.

Three consequences run through the whole document. Horizons are expressed in increments as well
as months, because that is the unit the reader plans in. Every item is individually droppable
and says what breaks if it is dropped, because items get cut one at a time. Nothing is sized,
because sizing belongs to the teams who will do it.

## How this differs from the roadmap in `itscm-program-assessment`

Both produce a roadmap. They take different inputs, aim at different targets, and are read by
different people.

| | `itscm-program-assessment` | This skill |
|---|---|---|
| Input | An interview. Answers recorded as established, asserted, unknown or absent | A finished capability assessment of documents that exist, with a level and a blocking criterion per dimension |
| Target | The state where continuity tooling can be installed, tell the truth, and be acted on | The next capability level per dimension, and nothing above it |
| Horizons | One month, three months, one year | One, three, six, nine and twelve months, mapped to increments |
| Reader | A sponsor deciding whether to start | A manager loading work into a planning event |
| When to run it | When nobody knows what the program contains | After the documentation set has been assessed |

Run that one when there is no assessment. Run this one when there is. If both have been run,
keep them as two documents: that roadmap answers whether anything can be observed truthfully,
this one answers what raises the capability of the documentation. An item that appears in both
means one of them has drifted, and the fix is to keep it here and reference it from there.

## Why five horizons, and what each one is for

State the job of a horizon before its items. A reader who does not know what a horizon is for
reads it as a backlog, and a backlog gets sorted by whatever the reader already wanted to do.

| Horizon | Its job | What may go in it |
|---|---|---|
| One month | Close what needs nothing from outside the team | Work already understood: scoped, owned, doable by people who are already here |
| Three months | Commit one increment of continuity work and produce the first evidence | Items that can carry a planning objective and be answered yes or no at the end of the increment |
| Six months | Hold the intent that depends on what the three month work finds | Intent, not commitment. Items whose shape depends on a result that does not exist yet |
| Nine months | Keep the dimensions nobody has started from disappearing | A few outcomes, each tied to a criterion, each with its dependency named |
| Twelve months | Say where this ends, so twelve months is not invented later under pressure | Outcomes only, no task breakdown |

**One month sits inside a single increment**, and that increment is usually already planned and
the teams already loaded. Work that arrives mid increment gets done only if it is small and
already understood. So this horizon holds nothing that needs a decision, a hire, a budget or a
room booked with six business people. Scheduling a workshop with the business is itself the
work, and it does not fit inside a month somebody has already committed.

**Three months is roughly one increment**, and this is where commitment lives. An item here
should survive a planning event: somebody can size it, somebody will own it, and at the end of
the increment somebody can answer yes or no to its done condition. If an item cannot be stated
that way, it belongs at six months, and the honest reason is that its scope is not known yet.

**Six, nine and twelve months are two, three and four increments out.** Write them as intent.
That is accuracy, not softness. The six month item exists because the three month work will
produce a result that changes it, and stating it as a commitment claims knowledge of a result
nobody has. A roadmap that is wrong in a checkable way loses trust in the parts that were right.

**A twelve month item is a placeholder and will be re-planned twice before anybody works on
it.** Write it accordingly: one sentence naming the outcome, the criterion it closes, and what
has to be true before it can be scheduled. No task breakdown, no owner beyond whoever decides,
no done condition more specific than the criterion itself. A twelve month item written as a
detailed task list is worse than an empty line, because the detail is fiction and the next
planner has to spend time deciding whether to trust it.

## Increments, not calendar quarters

The horizons are months because a sponsor reads months. The manager acting on this plans in
increments. Carry both.

State at the top of the roadmap the length of the increment the organization uses and the date
of the next planning event, then give every horizon its offset in increments. An increment is
set by the organization, commonly eight to twelve weeks, so never assume it lines up with a
calendar quarter. Ask for the length before writing rather than after.

Do not place anything inside an increment. No week numbers, no ordering within a sprint, no
dates other than the ones a dependency forces. What happens inside an increment is the team's
to decide at the planning event, and a roadmap that reaches in gets rejected on sight.

## The rule that stops this becoming a document writing backlog

Most of what an assessment finds missing from a continuity documentation set is uncollected
data, not unwritten prose. Nobody has asked the business what an hour of downtime costs. Nobody
has restored anything. Nobody has asked the supplier for evidence. No amount of drafting closes
any of that, and a roadmap full of writing tasks will be delivered in full and move no level.

The test, applied to every gap: could somebody holding all the current documents, given
unlimited time and no new information, write the missing content truthfully? If yes, the item
is a writing task. If no, name what they would have to find out and who holds it, and the item
becomes that instead.

| What the gap actually is | What the item is | What the item must name |
|---|---|---|
| Nobody has asked the business what stopping costs | A workshop | Who must be in the room: the process owners, finance, whoever is accountable for the work. Never IT alone stating a business requirement |
| Recovery objectives are keyed to infrastructure tiers | A workshop that re-derives them per business process | The same room, plus which processes are in scope for the first pass |
| The plan claims a recovery time nobody has attempted | A test | What it measures, against which objective, and who witnesses it |
| A procedure cannot be followed by anyone but its author | A walkthrough performed by somebody who did not write it, recorded | The person who will attempt it, not the document |
| Contact details are old | A collection, run by whoever owns the list | The source of truth for the details, and how it will stay current |
| A supplier continuity claim was accepted on assertion | A request for evidence, or a joint test | The supplier, the contract owner, and what would count as evidence |
| The facts exist and the document does not say them | A writing task | The document, the section, and where the facts come from |

Where the gap is an unasked business question, the item is the workshop that produces a
[BIA](../../../GLOSSARY.md "Business Impact Analysis"), and the roadmap names the room. Where the gap is an unverified claim, the item is the
test, and the item says what it measures: elapsed time against the
[RTO](../../../GLOSSARY.md "Recovery Time Objective"), data loss against the [RPO](../../../GLOSSARY.md "Recovery Point Objective"), and whether the business could work again inside
the [MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime"). Those are comparisons, and the item is not done until the comparison is written
down.

Writing tasks are a minority in a healthy roadmap. If most of your items are writing, go back
through them with the test above.

## Criteria nobody could assess, and levels nobody could read

The assessment separates a criterion that failed from a criterion it could not judge because the
document never arrived. Keep the separation, because the remedies are not alike. A failed
criterion needs work. An unjudged one needs somebody to send a file.

Unjudged criteria do not enter the horizons. Chasing a document does not need an increment, and
putting errands into a planning event teaches everybody that the roadmap is a list of chores.
Collect them in a section of their own, with the document, the person who holds it, and the date
it was asked for. If the answer comes back that the document does not exist, the criterion
becomes a real gap and enters the roadmap at the next re-planning, as a workshop, a test or a
writing task like any other.

Where the assessment declined to score a dimension at all because too much of its evidence was
missing, schedule nothing for that dimension and say so. Name what is missing instead. A roadmap
that plans toward a level nobody could read is planning against a guess, and the guess will be
quoted back as a commitment.

Where the evidenced level sits below the claimed level, the difference is proof and the item is
always a test, never an edit. Put it at three months, because a test needs a window, people and
somebody to witness it. Write its done condition as the record the test produces, not as the
test having happened.

## Sequencing by what blocks what

Order every horizon by blocking, never by effort. An easy item that blocks nothing waits behind
a hard item that blocks four. Ordering by effort feels productive and puts the item that decides
whether the year works at the end of the year.

Every item names what it unblocks by naming the later item. Give every item an identifier made
of its horizon and its position, `M01-1`, `M03-2`, `M06-1`, so the reference is unambiguous
after somebody reorders a horizon. Blocking across horizons is normal, and it is usually the
reason an item sits where it does: the six month item is at six months because `M03-2` has to
happen first, not because six months felt right.

Three checks, run after the roadmap is drafted:

An item that unblocks nothing and closes no criterion does not belong in the roadmap. Move it to
the register of known and unscheduled work.

If two items unblock each other, they are one item described twice, or one of them is scoped
wrongly. Split them until the dependency runs one way.

If an item unblocks something in an earlier horizon, one of the two is in the wrong horizon. Fix
the horizon, not the reference.

## What each item carries

| Field | What goes in it | What makes it wrong |
|---|---|---|
| What | One sentence, one outcome | Two outcomes joined by "and". Split it |
| Type | Workshop, test or writing, from the rule above | A type chosen to make the item sound cheaper than it is |
| Who | A named person, or `UNOWNED` in capitals | A team name or a role. Both are `UNOWNED` with extra words |
| Closes | The dimension and the criterion the assessment named, in the assessment's words | "Improves governance." The criterion has words already, so use them |
| Unblocks | The identifiers of later items that cannot start until this is done, or the word `nothing` | A blank, which reads as nobody having checked |
| Done when | Something observable, checkable by a person who was not involved | "Completed", "reviewed", "in progress" |

Observable means somebody outside the work can confirm it without asking the owner whether it is
finished.

> Done when: the recovery objectives for all eleven in scope processes are signed by the process
> owner named against each one, and the signed copies sit in the plan repository.

Not: *"the analysis is complete."*

Keep `UNOWNED` visible in capitals rather than filling it with the nearest team. An unowned item
that reaches a planning event either gets an owner or gets rejected, and both outcomes are more
useful than an item assigned to a group that never agreed to it.

## Two things that must be marked distinctly

Two kinds of item look like ordinary work, plan like ordinary work, and stall a roadmap without
anybody noticing.

`NO PERSON YET` marks an item that needs a person who is not in the organization. The item keeps
an owner, and that owner is whoever can decide to hire or borrow, never `UNOWNED`. The hiring or
borrowing decision is its own item in an earlier horizon, and it unblocks this one. Without that
earlier item the roadmap holds work that nobody can start and nobody is visibly failing to
start.

`AWAITING FUNDING` marks an item that depends on a funding decision somebody else makes. Name
the decision, the person who makes it, and the date it is expected. If the date is not known,
write `UNKNOWN` and treat every item this one unblocks as unschedulable, which usually means
moving those items out a horizon and saying why in the document.

Both markers appear on the item and again in a list of their own near the end of the roadmap.
The manager reading this has to raise them as dependencies at the planning event, and hunting
for them through five horizons is how they get missed.

Neither marker is a reason to leave an item out. An unfunded item that closes a blocking
criterion is often the most useful line in the document, because it turns "continuity is behind"
into a decision with somebody's name on it.

## An empty horizon is stated, not padded

Write "Nothing scheduled" and the reason. Two reasons are honest. The criteria that could be
closed in this horizon are already closed by earlier items. Or the work that would go here
depends on a result that does not exist yet, which is named. Both tell the reader something.

Do not pull a twelve month item forward to fill a nine month gap. A horizon filled to look busy
costs the reader confidence in the horizons that were not filled, and the twelve month item
arrives at nine months with none of the preconditions it needed.

## Length discipline, and the assessment that found thirty gaps

A roadmap longer than the organization can hold gets filed, and the assessment behind it gets
remembered as an expensive way to be told bad news.

An item enters the roadmap on one of two grounds only. It closes a blocking criterion the
assessment named, or it unblocks an item that does. Nothing else gets scheduled, however
obviously worth doing it is.

Plan one level per dimension. The criteria above the next level are not in this roadmap.
Scheduling two levels ahead commits work against criteria whose blocking criterion is not known
yet, because it depends on how the first level closed. When a dimension reaches its next level,
run the assessment again and write a new roadmap.

Four dimensions moving one level each is usually eight to fourteen items across all five
horizons, and no more than three or four inside the one month horizon. If a single dimension
needs six items to gain one level, look again. That is usually one piece of work, a workshop
series or a test program, decomposed too early, and a work breakdown belongs to the team that
will do it.

Everything that did not get in goes into a register of known and unscheduled gaps, with the
criterion it would close and the reason it is not scheduled: capacity, a dependency, or a
deliberate decision to accept it. The register is what makes a short roadmap honest. A thirty
gap assessment followed by a ten item roadmap with no register reads as though twenty gaps were
forgotten, and the first reader to notice will doubt the assessment rather than credit the
discipline.

## The output shape

```
CONTINUITY ROADMAP FOR PROGRAM INCREMENT PLANNING
Organization / service: <name>      Prepared: <date>      Prepared by: <name>

INPUT
  Assessment: <which review this came from>       Dated: <date>
  Increment length: <weeks>                       Next planning event: <date>
  Horizons convert as: 1 month = inside the current increment, 3 months = next
  increment, 6 / 9 / 12 months = 2 / 3 / 4 increments out.

STARTING POSITION, CARRIED FROM THE ASSESSMENT
                                  claimed   evidenced
  Organizations and people          <n>        <n>     Blocked by: <criterion, verbatim>
  Information and technology        <n>        <n>     Blocked by: <criterion, verbatim>
  Partners and suppliers            <n>        <n>     Blocked by: <criterion, verbatim>
  Value streams and processes       <n>        <n>     Blocked by: <criterion, verbatim>
  <dimension>   NOT SCORED   <what was missing>     (omit if every dimension was scored)

ONE MONTH  (inside the current increment)
  Job: <one sentence>
  M01-1  <what, one sentence>
         Type:       workshop | test | writing
         Who:        <name> | UNOWNED
         Closes:     <dimension> / <criterion>
         Unblocks:   M03-2, M06-1 | nothing
         Done when:  <observable>
         Marked:     NO PERSON YET | AWAITING FUNDING    (omit this line if neither)
  M01-2  ...

THREE MONTHS  (next increment)
  Job: <one sentence>
  M03-1  ...

SIX MONTHS  (two increments out, stated as intent)
  Job: <one sentence>
  M06-1  ...

NINE MONTHS  (three increments out, stated as intent)
  Job: <one sentence>
  Nothing scheduled. <why>

TWELVE MONTHS  (four increments out, a placeholder that will be re-planned twice)
  Job: <one sentence>
  M12-1  <the outcome, one sentence>
         Closes:      <dimension> / <criterion>
         Depends on:  <what has to be true before this can be scheduled>
         Decided by:  <name>

BLOCKED ON SOMEBODY ELSE
  <item id>   NO PERSON YET     <the role, who decides the hire, which item unblocks it>
  <item id>   AWAITING FUNDING  <the decision, who makes it, date expected | UNKNOWN>

KNOWN AND NOT SCHEDULED
  <gap>   <the criterion it would close>   <why it is not scheduled>

EVIDENCE NOT YET PROVIDED   (a file, not an increment. Not scheduled work)
  <criterion>   <the document that would settle it>   <who holds it>   <asked on>

WHAT THIS ROADMAP DOES NOT MOVE
  <dimension>   Level <n>   <one sentence on why nothing here raises it>
```

## Spell out every acronym in what you produce

The report this skill produces is read by somebody who was not in the room: a director, a
business owner, an auditor, somebody's replacement. Write the first use of every acronym in
full, with the short form in brackets after it, and use the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of
the skill needs them; they are expanded in the output because a reader of the report was never
given a glossary and cannot ask for one.

An acronym nobody expands is a reader quietly deciding the document was not written for them.

## What this skill does not do

It does not assess anything. Levels and blocking criteria are carried, not derived. If a level
looks wrong, raise it with whoever produced it and wait.

It does not produce a score, a percentage, a completion figure or a burn-up. The levels it
carries were read off all-or-nothing criteria and they stay that way. An item half done closes
nothing, and a roadmap reporting itself as sixty percent delivered has hidden which criterion is
still open.

It does not size or estimate the work. Estimation belongs to the teams at the planning event. A
roadmap that arrives pre-sized by somebody outside the team is either rejected or believed, and
both cost more than leaving the column out.

It does not plan inside an increment, and it does not decide which increment an item lands in.
It says what has to come before what, and the planning event does the rest.

It does not replace the interview-based roadmap in `itscm-program-assessment`, which targets a
different state and answers a different question.
