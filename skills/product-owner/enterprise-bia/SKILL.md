---
name: enterprise-bia
description: For an ITSCM owner responsible for more than one program. Lays every program's business impact analysis against the others, finds where they contend for the same resource, DR capacity or people, and produces a ranked recovery priority list plus a board paper naming each unresolved conflict and what resolving it costs. Never defaults a contention to the tightest deadline, because that is a funding decision.
---

# The organization-wide business impact analysis

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ITSCM** | IT Service Continuity Management |
| **DR** | disaster recovery |


Every program in an organization can have a correct, internally consistent BIA, and the
organization can still be unable to recover, because the plans were written as though each
program were alone.

This is the pass that lays them against each other. It is run by whoever owns ITSCM across
programs, and it produces two things: a ranked recovery priority list, and a paper for the
body that can actually decide the conflicts it finds.

## Why nothing smaller finds this

**Contention is invisible inside a program.** Each program's BIA is consistent with itself.
Order entry's two hour deadline is right. Payroll's twenty four hour deadline is right. The
conflict exists only in the fact that both run on the same database, and nothing in either
program's documents says so, because the other program is not in scope for either of them.

So this analysis needs every program's material at once, and it is the only thing in this
repository that does.

## Before you start: what you need from each program

For each program in scope, you need its **process to resource map**: which components each
business process depends on, and its recovery objectives per process. Tab 7 and tab 5 of the
data-collection workbook, or the equivalent sections of a completed BIA.

Programs missing those cannot be included in the analysis. **Say which ones, and say that the
result is therefore partial.** A priority list built from six of eleven programs is a priority
list for six programs, and presenting it as the organization's is worse than not running.

Also collect, for each program: its DR target (which site, region or facility it fails over
to), and the named people in its recovery roles.

## The four kinds of contention

Look for all four. Most reviews find only the first and it is not the most dangerous.

### 1. Deadline contention

Two or more processes, in the same or different programs, depend on one resource and carry
different MTDs or RTOs.

Recovering that resource to serve the tightest deadline gives the looser processes a level of
service nobody funded. Recovering it to the looser deadline means the tighter process misses an
objective its owner signed. Both are real costs and the choice is not technical.

### 2. Data loss contention

The same resource, with different RPOs behind it.

This one is usually the cheapest to resolve, and resolving it toward the tightest is normally
correct, because replication is configured per resource and protecting to the tighter objective
costs money rather than costing another process anything. Say so rather than presenting it as a
symmetrical trade. **Where it is not cheap, say why**, because an expensive RPO resolution is
a real budget line and belongs in the paper.

### 3. Capacity contention

**The one that is almost never on anybody's list.** Two or more programs plan to fail over into
the same DR site, region or capacity pool.

Each plan is individually valid. In a regional event they execute simultaneously, and the
capacity was sized for one of them. Both plans are correct and collectively impossible, and
nothing inside either program can detect that.

Check: for every DR target, what is the sum of what every program expects to run there, against
what is actually provisioned. Ask whether the standby is sized for the largest single program
or for all of them, and what the answer is expected to be when several fail at once.

### 4. People contention

The same named engineer appears in the recovery roles of six programs.

At 3am in a regional event they are in one place. The tier-assignment conversation makes this
point about the whole organization: asked in isolation every owner answers with the highest
tier, and the question only has meaning relative to the other programs competing for the same
people at the same hour.

Check: for each named individual, how many programs list them in a recovery role, and how many
of those would activate together in a single regional event.

## Resolving a contention, and what each resolution costs

Four options. The board picks one per contention. Present them with the cost, not as a
recommendation dressed as a list.

| Resolution | What it costs | When it is right |
|---|---|---|
| **Serve the tightest** | Money. Every process sharing the resource now gets premium treatment nobody budgeted for | When the gap is small, or when the tight process is genuinely the organization's priority |
| **Serve the looser** | Risk, carried by the tighter process. Requires that process owner to accept a worse objective than they signed | When the tight objective was aspirational rather than driven by a real mechanism |
| **Decouple** | A project. Separate the resource so the processes stop sharing it | When both objectives are real and the gap is wide enough that neither side should give |
| **Accept and record** | Nothing now, and clarity later | When the organization decides to live with it knowingly. This is a legitimate answer and it is not the same as not deciding |

**"Accept and record" and "unresolved" are different states.** The first is a decision. The
second is an absence of one, and it is what this analysis is mostly going to find.

## The rule this skill exists to enforce

**Never resolve a contention by default.**

The tempting default is that the tightest deadline wins, because it is the safe-sounding answer
and it makes the report look finished. It is a funding decision, it commits money nobody
approved, and made silently it will be discovered during an incident by whoever was quietly
downgraded.

Report unresolved contentions as unresolved, name who has to decide each one, and let the list
be shorter than the organization hoped.

## Part 1: the ranked recovery priority list

The first deliverable. Every shared resource across every program, in the order it is
recovered, with the process that set the order named.

```
ORGANIZATION RECOVERY PRIORITY
Programs in scope: <n> of <total>       Excluded: <which, and why>

 #   Resource                 RTO      Set by                        Contended?
 1   Core banking database    15 min   Payments (Program A)          YES, see C1
 2   Identity provider        15 min   All programs                  no
 3   Order management         2 hr     Order entry (Program B)       no
...
```

The "set by" column is what makes this auditable rather than assertable. A priority with no
process behind it is somebody's opinion about importance and will be argued with forever.

## Part 2: the board paper

The second deliverable, and the one the ITSCM owner actually carries into a room. A board does
not need the analysis. It needs the decisions only it can make.

Structure it as one page per contention:

```
C<n>. <Plain name of the conflict>

WHAT IS SHARED       <resource>, used by <process> (<program>) and <process> (<program>)
THE CONFLICT         <one sentence a non-technical director understands>
AT STAKE             <what each side loses, in business terms, not in minutes>
THE OPTIONS          <the four above, with cost against each>
IF NOTHING IS DECIDED <what happens by default, stated as a consequence rather than a plan>
WHO DECIDES          <the named role or body>
RECOMMENDATION       <yours, marked as a recommendation>
```

Three rules for writing it:

**"If nothing is decided" is not a resolution.** It is what the organization will discover
during an incident. Write it as such: "the database is recovered to whichever deadline the
responding engineer knows about, which is currently unspecified."

**Business terms, not minutes.** A director does not act on "RTO 15 minutes against RTO 4
hours". They act on "we can protect same-day settlement or overnight payroll on this shared
system, and today we have promised both."

**Mark your recommendation as a recommendation.** You are the ITSCM owner, not the decider. A
paper that presents the analyst's preference as the finding removes the decision it was written
to prompt.

## Part 3: what to report when the answer is that you cannot do this yet

The common outcome, and it is a legitimate one.

If most programs have no process to resource map, this analysis cannot run, and the honest
output is one page naming which programs can supply the input and which cannot. That is a more
useful thing to take to a board than a contention list built from the two programs that
happened to be ready.

Say what the missing input is, name the skill that produces it (`bia-workshop`, and the
workbook), and say how long it takes per program. Then the board is deciding whether to fund
the analysis rather than being asked to resolve conflicts nobody has found yet.

## What this does not do

It does not assess any single program's plan. `iscp-completeness`, `iscp-sufficiency` and
`itscm-coordinator-review` do that, one program at a time, and their findings are inputs here
rather than outputs.

It does not rank programs by importance. It ranks **resources** by the recovery deadline of the
processes depending on them. Programs are not comparable to each other; deadlines on a shared
resource are.

It does not decide anything. Every contention it finds ends with a named person or body and an
open question, and a version of this report with no open questions has almost certainly
defaulted something.
