---
name: recovery-drill
description: For IT running a recovery drill on a live system, producing a drill record an auditor can accept as evidence, with the failure chosen as the one most likely to breach an objective, every piece of data the drill could destroy copied or its loss accepted in writing by its owner, and every time taken on one named clock from the customer's side.
---

# Running a recovery drill

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **IT** | information technology |
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |


This is the one [IT](../../../GLOSSARY.md "information technology") skill that changes things on
purpose. Every other IT skill reads, and any that needs something broken to find out sends it
here. A drill breaks something and times the way back, so it is the only IT activity that can
destroy what it is measuring, and the only one that proves recovery works.

Proof is what it is for. Under `itil-scm-evidence-review`, a capability is claimed until a test
demonstrates it, and where nothing has been tested the evidenced level is 1, however good the
documents are. The drill record is the document that changes that reading. So it has to be one
an auditor accepts: every fact labeled, every change listed exactly as run, every time on one
named clock, and nothing destroyed that nobody agreed to lose.

## Why this skill exists

A recovery drill was once run with no procedure behind it. It removed one component at a time
and timed each return. Two of its findings are the core of this skill.

**It destroyed the data it was measuring.** Its instructions told it to remove the cache holding
customers' carts, to measure data loss. Two hundred records became zero, silently. Nothing
logged an error. In that test the records were synthetic. At a real organization they would
have been real customers' data. The loss was provable without causing it: the cache kept its
data in scratch storage that is deleted with the component, and that configuration alone proves
any restart loses everything. The drill held a general authorization to test destructively and
treated it as enough. **It is not.** An authorization to test covers the act. Only the owner of
the data can accept the loss.

**Readiness understated what customers saw.** One component reported ready about 2 seconds after
it was removed, while the storefront returned server errors for about 23 seconds. Another took
the whole store down for about 25 seconds and failed synthetic orders. A drill that reports
component readiness as recovery reports the wrong number, and in the first case it was wrong by
more than ten times. The drill caught it only because it also watched from the customer's side.

It also tested the failure least likely to breach anything. One component on a healthy host
recovers inside almost any time objective. Host loss, failover and restore, where objectives
actually break, were never run.

## What IT owns here, and what it does not

IT states outcomes: restoration time and data loss, measured. It does not set, suggest or
quote a recovery objective. The [MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime"),
[RTO](../../../GLOSSARY.md "Recovery Time Objective") and
[RPO](../../../GLOSSARY.md "Recovery Point Objective") belong to the process owners, who set them
per business process in the [BIA](../../../GLOSSARY.md "Business Impact Analysis").

The objective and the outcome get different words, so that they can be compared rather than
equated. Write "restoration time" and "data loss" for what the drill measured. Never write RTO or
RPO for it. Never put an objective's value in the record beside a timing either: a number IT
writes next to its own measurement reads as the requirement by the time it reaches a plan.

The record may name which process's objective a scenario threatens, by process and by the
document and row that hold it. It does not repeat the value. The comparison belongs to the
product owner, who sets the drill record against the objectives.

Which copy is production is not IT's to decide either. A failover drill needs to know which way
is "over" and which is "back". If the business has not said, the drill cannot be scoped, and
that is the finding.

## The evidence standard

This binds every IT skill. It is repeated here in full because a skill is read on its own.

Every fact in the record carries exactly one label.

| Label | Means | Must carry |
|---|---|---|
| MEASURED | A command ran and its output is in the register | The register entry |
| ESTIMATE | Arithmetic on measured values | The method |
| INFERENCE | A conclusion drawn from measured facts | The reasoning |
| UPSTREAM DESIGN | How the software's publisher built it, not observed here | Which published behavior is relied on |
| NOT MEASURED | Nobody looked, or nothing could | What would settle it |

Every MEASURED fact points at a register entry that gives the exact command and the relevant
output. Number the entries with a prefix taken from the record's own name, such as `DRILL-R7`,
never a bare `R7`. Other documents' registers also start at 1, and a bare number cited in a
later document points at all of them. Trim output to the lines relied on and say it was trimmed.
If a script reshaped the output, say what it did.

Every time is Coordinated Universal Time, with its date. Every measurement carries when it was
taken. A count without a time is a count of an unknown moment, and the drill is about to change
it. After any change, list the facts it made stale (step 7 says how).

Describe secrets and personal data. Never reproduce them. Write that one session identifier was
reused for every probe request, not the identifier. Write that 200 customer records were
counted, not what they contain. The record will be read by more people than were allowed to see
the data.

Where a command cannot be run, name the one read-only command to ask the operator for, and say
first what you will do with its output. Then give the fallbacks, in order: the platform's event
history, the monitoring system's history, the component's own log. If none of them answers, the
fact is NOT MEASURED.

A person's statement with no output behind it is not MEASURED. Record it as NOT MEASURED with
who said what: `NOT MEASURED (reported by the storage owner: a nightly copy exists)`.

Refuse any MTD, RTO or RPO value, and the words RTO and RPO for anything the drill measured.

---

## Step 1: choose the scenario

**The first drill most organizations need is the one they least want to run.**

Component loss usually passes. Platforms are built to replace a failed part, so removing one on
a healthy host proves the platform does what it was built for. That is why it gets run first,
and why it so often gets run only. The failures that breach objectives are host or site loss,
failover and failback, and restore from backup. **A drill program that only ever tests component
loss is producing reassurance, not evidence.**

| Failure class | What it answers | How it usually goes |
|---|---|---|
| Component loss | Does the platform replace one failed part, and what do customers see meanwhile | Passes. That is why it gets run |
| Data store loss | What data survives replacement of the thing holding it | Often provable from configuration without running it |
| Host loss | Does anything survive the machine it runs on | Where single points of failure show. Rarely drilled |
| Site loss | Does anything survive the building, region or provider | Rarely drilled. Usually assumed from a diagram |
| Failover and failback | Can customers be moved to the standby and back, with their data | Often built, rarely timed, almost never timed back |
| Restore from backup | Does the copy restore, how old is it, how long does it take | Backups are taken. Restores are not |
| Rebuild from declared state | Does the declared state, applied to empty infrastructure, produce what was running | What was never declared is lost, and nobody has counted it |

### Choose from objectives against capability

The input is the product owner's comparison of objectives against capability: for each process,
what the business requires set against what IT has shown. Read it for the failure class most
likely to breach an objective, and test that one before the one most likely to pass.

| Ask of each failure class | It moves up the list when |
|---|---|
| What does the capability statement say about it? | NOT MEASURED, or an ESTIMATE nobody has checked |
| What does it remove? | A single point of failure: one host, one copy, one switch, one store |
| Whose work depends on what it removes? | The process with the tightest objective |

Record the choice, and why each other class was not chosen first. "Host loss not drilled: needs
spare hardware, booked for the 14th" is an answer. "Not chosen" is not.

If no comparison exists yet, the drill can still run, but it cannot be chosen against objectives,
and the record says so. Prefer the failure class the capability statement leaves NOT MEASURED. A
drill scheduled before the objectives exist tends to test whatever is convenient.

### When the failure that matters would take production down

Host loss on a system that runs on one host is an outage. The outage is usually provable from
configuration without causing it. What configuration cannot tell you is how long the way back
takes. Rehearse it on equivalent spare infrastructure, time it, and name in the record every
difference between the spare and production that could change the time.

If the organization will not run the failure most likely to breach, in any form, record that.
The objective it threatens stays unproven by decision, and the decision has an owner.

## Step 2: declare the bounds

Write the bounds before anything changes. Get them agreed by the system owner and by every
process owner whose objective the scenario threatens. Bounds changed during a drill are bounds
nobody checked.

| Bound | What it states |
|---|---|
| Scope | Every environment, component and copy the drill may act on, by name |
| Out of scope | Every copy that must not be touched, by name: the standby, the backups, replicas, other environments on the same hosts |
| Production | Which copy is production, as the business decided it, and who decided |
| Mutating verbs | The only commands that change anything, written out. Nothing else changes state |
| Preconditions | What must be true before each mutating step: the target is the one you mean, everything is healthy, customers have recovered from the previous step |
| Window | Start and end, in Coordinated Universal Time, checked against every freeze window |
| Stop rule | The conditions that end the drill, who may call a stop, and what state a stop returns to |
| Participants | Each person and the role they hold. An auditor looks for named people performing their own roles |

If the organization raises change records, the drill needs one. Put its reference in the record.

### Copies outside scope

A copy outside scope gets no command of any kind. If the drill needs to read it, add it to the
scope before the drill starts.

Check which copy each entry actually serves before you probe through it. An entry that routes
to a copy outside scope turns the probe into a touch on that copy. It happens: a public name has
served the standby while everybody believed it served production.

### Freeze windows

Do not run a drill inside a freeze window. The business sets freeze windows around the periods
when a failure costs most: a period close, a sale, a payroll run. A drill is a failure on
purpose.

IT does not set them. Ask the process owners whether the drill window falls inside one, and
record the answer with who gave it. If none has been set, record that too. It is not permission.
Nothing enforcing a window is not the same as no window existing.

### The stop rule

Decide it before the drill, not during it. Under pressure, a stop rule gets renegotiated by
whoever most wants to finish.

A stop rule has three parts. The first is the conditions: a step that has not recovered within
the agreed time limit, customer impact beyond what the bounds allow, any change to data that
step 3 does not cover, anything observed outside the scope. The second is who may call a stop.
Name them. Anybody on that list can call one, nobody overrules it during the drill, and resuming
needs the drill lead and the process owner both agreeing, recorded with the time. The third is
what a stop returns to: the state named in the bounds, by a back-out path checked before the
drill started.

A rule that says "stop" without saying what to return to, and how, is half a rule. A failover
stopped halfway is two copies in an unknown state.

The process owner agrees the time limit. It bounds the drill. It is not the objective, and the
record states it as a limit rather than a target.

## Step 3: protect the data before anything is destroyed

Before any destructive step on a component that holds data, one of two things must be true. A
copy has been taken off that component and shown to restore. Or every process owner whose RPO
covers that data has accepted that specific loss in writing. If neither is true, that step does
not run.

**A general authorization to test destructively is not acceptance.** It covers the act.
Acceptance covers a consequence, and only the person who set the RPO for the data can accept a
breach of it. The drill that prompted this skill had the first and treated it as the second.

### Find every component that holds data

Take the list from the inventory and the protection posture where they exist, then check it. A
component described as stateless may still write to local disk: a queue, a session store, an
upload directory. For each one, record what it holds, the count before, and which processes
depend on it.

### First ask whether configuration already proves the outcome

A drill exists to measure what cannot be known without running it. If the storage is deleted
with the component, the loss on any restart is already proven: the configuration is MEASURED and
the consequence is INFERENCE. Record it that way and do not trigger the loss. Destroying the
data to watch it go adds nothing to the evidence and costs the data.

### Then protect it or get the loss accepted

| | What it takes | What does not count |
|---|---|---|
| A copy that restores | A copy taken off the component, outside whatever the step will destroy, restored somewhere other than the original, with the record count and a sample of record identities checked against the original at the same moment | A copy on the same disk or host. A copy never restored. A count of files rather than records |
| Written acceptance | From every process owner whose RPO covers the data. Names the component, the data, the loss expected and the window. Dated | A general authorization to test. Acceptance from IT, the drill sponsor or anyone who does not own the objective. A verbal yes |

Take the copy as close to the step as you can. Records written between the copy and the step
are the loss the copy cannot cover. Count them.

Data with no owner can only be copied. Nobody can accept a loss against an objective nobody
owns. One owner who declines is a refusal, whatever the others say.

If the step loses data you copied, restoring the copy is part of the back-out. Time it. You
have just run a restore drill as well, and it goes in the record.

The copy is itself data. Keep it under the same controls as the original, describe it in the
record rather than reproducing it, and delete or keep it as the owner says.

## Step 4: decide the probe

The probe is yours to decide, and one rule governs it: **it does not write the data the drill
measures.** A probe that adds records to a store while you count that store's losses has
corrupted both numbers.

Within that rule, the probe has to see what customers see.

Go through the entry customers use. Record the name, the path, and where the probe ran from.
A probe from inside the network skips the load balancer, the name lookup and the certificate,
and any of those can be the thing that fails.

Exercise the function that depends on the component. A probe of the home page reports nothing
while payment is down, because the home page does not call payment. If exercising the path must
write to the store being measured, mark those writes as synthetic, count them apart, and take
the data loss over the records that existed before the step. If the synthetic writes cannot be
told apart, use existing traffic and logs for that path instead.

Sample faster than the effect you want to see, and record the interval. The start and end of an
outage are known only to within one interval, so they are an ESTIMATE with the spacing stated.

Use a second source: the logs of the component in front, and traffic that already flows. Where
nobody tried the path during the window, the result is NOT MEASURED. It is not "no impact".

Define "recovered" before the drill as a stated number of consecutive successes. The first
success after a failure is sometimes a fluke.

## Step 5: use one clock

Take every timestamp from one authoritative clock, and name which: the control plane's clock,
the database server's clock, whichever clock the platform itself stamps its events with. Never
mix a workstation clock with a server clock.

Workstation clocks drift, and time synchronization steps them. A duration computed across a
step is wrong in a way nothing flags. In the drill that prompted this skill, the workstation's
wall clock stepped backward several times, and its steady clock ran about five percent fast.

If a recorder has to run on a second clock, measure that clock's offset and rate against the
reference at the start and at the end, record both readings in the register, and convert every
local reading. Never subtract a reading on one clock from a reading on another.

State the reference clock's resolution. If it stamps whole seconds, two stamps two seconds apart
bound a duration between one and three seconds, and the record says so.

## Step 6: run it

Take a baseline first: the health of every component, the count in every data store, the
versions actually running (identifiers, not floating names), and what the probe sees. Use the
same commands you will use afterward.

Then make one change at a time. The next step runs only when the previous one has recovered on
the customer's side, not only on the component's.

Record every mutating command exactly as run: the text, the time on the reference clock, who ran
it, and what it returned. Check each precondition immediately before the command it guards, and
put the check in the register too. Disclose every read that fell outside the literal wording of
the bounds, including harmless ones.

Count data by identity, not only by number. New writes after the step can refill a count and
hide the loss. Read the after count before new writes can arrive, or compare which records
exist.

Report every run. If a step ran three times, give three durations, not their mean. The slowest
is the one a real event will meet.

Record what noticed the failure: which alert fired, and when, relative to the failure. A loss
nothing noticed is a finding of its own. In the drill that prompted this skill, the records
vanished and nothing logged an error. A returning customer would simply have found an empty
cart.

Record near misses. A replacement that failed one of the three consecutive health checks that
would have killed it is one. On a worse day it is killed, and recovery starts over.

### Readiness is not recovery

Every step has two numbers, and they are not the same number.

| | Starts | Ends |
|---|---|---|
| Readiness time | The failure | The component reports ready |
| Restoration time | The failure | The customer's sustained success, through the entry customers use |

Report restoration time as the result, with readiness time beside it and the gap between them.
Never report readiness time alone, and never call it restoration time.

The gap has causes, and they sit outside the component. Callers that were refused while it was
down wait longer between retries, and their next try can come long after it is ready.
Connection pools hold dead connections. Caches keep the failure. A load balancer's health check
lags. None of them shows in the component's own status.

A component that comes back ready and empty has not recovered. Report its data loss beside its
restoration time.

Refuse component readiness as recovery: a pod reporting ready, a health check passing, a
database accepting connections. Each is a fact about the component. Recovery is a fact about
the customer.

### Failover is two drills

**Failover is not demonstrated until it has been timed in both directions.** A switch to the
standby that nobody has switched back is a one-way door. The organization is now running on the
copy it built to use for a few hours, and nobody has walked the way home.

Time each direction as its own drill: the decision to switch, the switch, the customers'
sustained success on the other copy, and the data the destination lacks that the source held.
While customers are on the standby, count what they write there. After failback, count how much
of it came home. What did not is data loss, and it belongs to the failback, where nobody thinks
to look.

Record, from its configuration, what the switch checks about a target before sending customers
to it. A switch that checks nothing sends customers to a dead standby as readily as to a live
one. Record whether the switch can reach each copy at all, and when it last moved.

Both copies and the switch are in scope for a failover drill, by name. Which copy is production
comes from the business. Until both directions are timed, the record does not call the standby
a working one.

### Restore from backup

Restore to somewhere other than the original, unless the original is already lost and that
loss was accepted. Time from the decision to restore to the customers' sustained success on the
restored data. The data loss is what the restored copy lacks against the baseline, by count and
by identity, and the age of the newest copy that restored. A backup that has never been
restored has not been shown to be one.

### Rebuild from declared state

Some recovery is a rebuild. An orchestration step installs a deployment controller, the
controller pulls declared state from a repository, and the environment assembles itself. Time
each stage: infrastructure, platform, controller, first complete sync, customers' sustained
success. Then do two things a timing alone misses.

Before the drill, take the inventory of what is running and set it against what is declared.
Anything running but undeclared is what the rebuild will lose: a replica count changed by hand,
a permission granted by hand, an endpoint edited by hand, a secret created by hand, and all of
the data. Count it now, so that afterward is a comparison and not a discovery.

After the drill, check that the rebuilt environment matches what was declared, and set it
against the inventory from before.

| List | What it means |
|---|---|
| Declared, came back | The rebuild did its job |
| Declared, did not come back | The rebuild is broken, or depends on something it does not install |
| Running before, not declared | What the recovery lost. Count it. Nobody else will |
| Came back different | A floating version reference resolved to something newer. A hand-tuned setting reverted to its default |

A controller that reports itself in sync has reported readiness. The customer check still
applies.

Record what the rebuild needed and did not install: access to the repository, credentials,
sources for images or packages, secrets kept outside the repository. Each has to be available
on the day the rebuild is real.

## Step 7: afterward

Return to the state the bounds named, and check it with the baseline commands.

Then list every earlier measurement the drill made stale. A drill changes the system it
measured. Counts, component names, restart counts, versions, which copy serves which entry: any
fact recorded before the drill, in this record or in any other document, may no longer be true.
For each one, give the document, its register entry, the fact as recorded with its time, the
state now, and the step that changed it. Without the list, later documents cite the before and
the after side by side and nobody notices that they disagree.

Say what the drill demonstrates and what it does not, by failure class. A component drill
demonstrates component loss under the conditions it ran in, and nothing about host loss. A
reader who takes it as a test of the plan has been misled by its title, and the title is yours.

List what made the drill kinder than a real event: caches already warm, the host healthy, staff
on hand and expecting it, a quiet hour. Every drill is a best case. The record says how good a
case it was.

If every step passed, say so, and say which failure class was not tested. A drill that found
nothing is a finding about the drill.

Send the record to the product owner, who sets it against the objectives. The record carries
the facts for that comparison and no verdict on it.

---

## The drill record

```
RECOVERY DRILL RECORD   <record name>                  Register prefix: <PREFIX>
System or program: <name>
Drill window:      <date> <start> to <end>, Coordinated Universal Time
Reference clock:   <which clock>, resolution <n s>. Every time here is on it unless marked
Drill lead:        <name>
Participants:      <name, role>; <name, role>; ...
Procedure used:    <runbook name and version, or NONE>. Where it was wrong: <step, what>
Change record:     <reference, or NONE>

This record sets no objective. Every figure in it is an outcome: restoration time
or data loss. The comparison with objectives belongs to the product owner.

DEMONSTRATES
  <failure class>, under <conditions>
DOES NOT DEMONSTRATE
  <every failure class not exercised>

SCENARIO
  Chosen:       <failure class, and exactly what was made to fail>
  Threatens:    <process>, objective in <document>, <row>. Value not repeated
  Capability before this drill: <what the capability statement said, with its label>
  Chosen against objectives: YES, from <comparison document, date>
                          or NO, because <reason>
  Not chosen first:
    <failure class>   <why not, and when it will be run>
    ...

BOUNDS                                        agreed by <names>, <date and time>
  In scope:          <environments, components and copies, by name>
  Out of scope:      <every copy, standby, backup and environment not to be touched>
  Production copy:   <which>, decided by <business owner>, or NOT DECIDED
  Mutating verbs:    <each command that changes anything, written out>. Nothing else
  Preconditions:     <what is checked immediately before each mutating step>
  Freeze windows:    <none in the drill window>, per <name>, <date>
  Stop rule:         <each condition>
  Time limit:        <duration> per step, agreed by <process owner>. A limit, not an objective
  Who may call stop: <names>. Resuming needs <drill lead> and <process owner>, recorded
  On stop:           return to <state> by <back-out path>, checked <date and time>

PRE-DRILL DATA CHECK                           one entry per component that holds data
  <component>   holds <what data>   <n> records at <time>   <ref>
    RPO covering it owned by: <process owner or owners>, or UNOWNED
    Configuration proves the outcome: YES, <ref>. Step not run
                                   or NO
    Protected by:  COPY at <where, off the component>, restored to <where> at <time>,
                   <n> of <n> records, <n> identities sampled, <ref>.
                   Records written between copy and step: <n>
               or  ACCEPTANCE in writing from <each owner>, <date>, accepting <which loss>
                   of <which data> during <window>, <ref>
               or  NEITHER. Step <n> NOT RUN

PROBE
  Ran from:        <vantage point>
  Entry:           <the name and path customers use>, serving <which copy>, <ref>
  Exercises:       <the function that depends on the component>
  Writes:          NOTHING, or synthetic records marked <how>, counted apart
  Interval:        <n s>
  Recovered means: <n> consecutive successes
  Second source:   <logs, existing traffic>

STEPS                                          every run listed, none averaged
  Step <n>  <what was made to fail>                                   <label>  <ref>
    Failed at          <time>
    Ready at           <time>            readiness time <t>
    Customers failing  <time> to <time>, <n> consecutive successes from <time>
    Restoration time   <t, or a range where clock resolution or probe spacing limits it>

WHAT CUSTOMERS SAW, AS DISTINCT FROM READINESS
  Step <n>  ready after <t>, customers back after <t>, gap <t>
            Saw: <errors, failed actions, with counts>
  Step <n>  nobody used <function> in the window: NOT MEASURED, not "no impact"
  Noticed by:  <alert or log, and when>, or NOTHING
  Near misses: <what, when>

DATA LOSS
  <component>  before <n> at <time>  after <n> at <time>  by count and by identity
               <label>  <ref>

DECLARED AGAINST WHAT CAME BACK                rebuild or restore only
  Declared, came back:           <n>, <ref>
  Declared, did not come back:   <list>
  Running before, not declared:  <list>. What this recovery lost
  Came back different:           <item>: <identifier before> to <identifier after>

CHANGES MADE                                   every mutating command, exactly as run
  <ref>  <time>  <who>  <command>  <what it returned>
  Reads outside the literal wording of the bounds: <list>, or NONE

STALE AFTER THIS DRILL
  <document>  <register entry>  <fact as recorded, with its time>  <state now>  <step>

KINDER THAN A REAL EVENT
  <warm caches, healthy host, staff expecting it, quiet hour, ...>

FOR THE PRODUCT OWNER
  <the facts to set against the objectives. No objective value repeated, no verdict>

REGISTER
  <PREFIX>-R1  <date and time>  <exact command>
               <relevant output, trimmed. Secrets and personal data described, not shown>
  ...
```

Lead with what the drill demonstrates and what it does not. A reader who stops after the header
should still know which failures remain unproven.

## What this skill refuses

| Refuse | Why |
|---|---|
| Destroying data with no copy and no written acceptance | A general authorization to test destructively covers the act, not the loss. Only the owner whose RPO covers the data can accept losing it |
| Running inside a freeze window | The business set the window because a failure then costs more than at any other time. A drill is a failure on purpose |
| Touching copies outside scope | A standby or backup the drill damages is the one the next real event needs |
| Reporting pod or component readiness as recovery | It was wrong by more than ten times in the case that prompted this skill |
| Any MTD, RTO or RPO value | They belong to the business. A value IT writes beside its own timing becomes the requirement by proximity |
| The words RTO and RPO for what was measured | Objective and outcome get different words, so they are compared rather than equated |
| Deciding which copy is production | A business decision. A failover drill scoped on IT's guess tests the wrong direction |
| Calling a standby working without a timed switch in both directions | A switch nobody has reversed is a one-way door |
| A guess where a measurement is missing | NOT MEASURED is a complete answer. A guess is a number somebody will later quote |
| Changing the bounds during the drill | Bounds changed under pressure are bounds nobody checked |

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

It does not set, compare or relax a recovery objective. The business sets them, the product
owner compares, and a shortfall becomes a tracked gap item rather than a relaxed objective.

It does not walk the recovery path from the customer's entry to the standby's data. That is
`recovery-path`. Read its output before scoping a failover drill, or the drill is scoped from a
diagram.

It does not measure data loss continuously. A drill measures replication lag once, on the day.
Whether data loss stays inside what the business accepts between drills is a monitoring
question, and a program that only learns its lag during a failover learns it too late.

It does not write the runbook. It records where the runbook it followed was wrong, which is the
evidence a rewrite starts from.

## Checking your own output

- The scenario was chosen against objectives, or the record says why it could not be.
- Every other failure class has a reason it was not first.
- The bounds were agreed by named people before the first change.
- Every component holding data has a copy that restored, written acceptance from each owner
  whose RPO covers it, a proof from configuration, or a step that did not run.
- Every time is on the named reference clock, in Coordinated Universal Time.
- Every step has a restoration time measured on the customer's side, with readiness beside it.
- Every mutating command appears exactly as run.
- Every MEASURED fact has a register entry carrying the record's prefix.
- No MTD, RTO or RPO value appears. RTO and RPO appear only as names of objectives the business
  owns.
- The stale list exists and names documents other than this one where they cite changed facts.
- No secret and no personal data is reproduced.
