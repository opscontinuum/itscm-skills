---
name: itscm-program-assessment
description: Interview an organization to determine the current state of its IT service continuity management program, then produce a one month, three month and one year roadmap to the point where the opscontinuum tooling can be installed, tell the truth, and be acted on. Assumes none of that tooling is present in the environment being assessed.
---

# Assessing an ITSCM program, and routing it to a roadmap

You are in front of people who run an IT service continuity program, or who
have been told they have one. Find out what is actually there, then say what
the next month, quarter and year should contain.

**Assume none of our tooling is installed.** No `ci-observe`, no `iscp-author`,
no `itscm-onboarding`, no plug-in, no collector. Every question below is
answerable by a person in the room or by a read-only command they run
themselves on their own laptop. If you find yourself wanting to run our
software to answer a question, the question is wrong for this skill.

## What this produces, and what it refuses to produce

It produces a **state**, then three roadmaps.

It does not produce a score, a percentage, a maturity level between one and
five, or a red-amber-green tile. Those compress the one thing that matters,
which is *which specific fact is missing*, into a number that sounds like
progress. A program at "60 percent" tells nobody what to do on Monday.

It does not produce a target the organization did not agree to. The roadmaps
below are scoped to one question only: **what has to be true before our tooling
can be installed, tell the truth, and be acted on.** That is a narrower goal
than "a mature continuity program", and saying so honestly is what stops this
becoming a consulting pitch with a tool attached.

## The rule about unknowns

Every answer is one of:

| | |
|---|---|
| **Established** | Somebody stated it and can point at where it is written |
| **Asserted** | Somebody stated it and cannot point at anything |
| **Unknown** | Nobody in the room knows |
| **Absent** | It was looked for and is not there |

`Asserted` and `Unknown` are not weaker versions of `Established`, they are
different facts with different remedies. `Asserted` needs evidence. `Unknown`
needs somebody to go and look. `Absent` needs work. Never average them, never
place them on a scale, and never let `Unknown` render as a middling value:
almost everything in a young program is `Unknown`, and a chart that shows that
as "halfway" is describing nothing.

Record who said each thing. A continuity fact with no name attached decays
without anybody noticing.

## Part 1: the eight questions that decide everything else

Ask these first, in this order. The order is deliberate: each one makes the
next one answerable or pointless.

### 1. Who owns continuity for this system, by name?

Not a team, not a role in an org chart. A person who would be woken.

If the answer is a team name, ask who on that team. If the answer is "we all
do", record `Absent` and stop treating later answers as reliable: a program
with no named owner has no one whose job it is to notice any of the gaps you
are about to find.

Follow up: **who is their deputy, and has that deputy ever acted?**

### 2. Is there a written continuity plan, and which authority does it follow?

Get the file. Read the first page.

The distinction matters and people conflate it constantly:

- An **ISCP** is an Information System Contingency Plan, a system-level artifact
  under NIST SP 800-34 Rev. 1 and FedRAMP SSP Appendix G.
- An **ITSCP** is an IT Service Continuity Plan, a service-level artifact under
  ITIL. An ITSCP may *align to* the ISCP structure without being one.
- A **BCP**, **COOP** or **DRP** is none of the above. FedRAMP's own Table 1.4
  lists BCP, COOP, Occupant Emergency Plan and crisis communications as "Plans
  Outside of ISCP Scope", and neither FedRAMP nor NIST publishes a DRP template.

If they hand you a document titled "Disaster Recovery Plan", that is not a
finding against them, it is a vocabulary difference to resolve before anything
else. Ask what it is *for*: a system, or a facility, or the business.

If a plan exists, run the `iscp-completeness` skill against it before going
further. Its output is a large part of Part 2.

### 3. Is there a configuration item inventory, and what is it for?

Three sub-questions, and the third is the one that matters:

- Where does it live? (A CMDB, a spreadsheet, a Terraform state, nobody's head)
- Who maintains it, and when did they last touch it?
- **Has anyone ever compared it to what is actually running?**

The third question usually produces a pause. Record the pause. An inventory
nobody has reconciled is a document about the past, and the gap between it and
reality is the thing our tooling exists to measure. If they say "yes, it is
accurate", ask how they know, and record the answer as `Asserted` unless they
can name the comparison.

### 4. What can be read, today, with credentials that already exist?

This is the product's installability question and it is answerable without
installing anything. For each, ask whether a read-only credential exists **now**:

| Source | The question | What it would give us |
|---|---|---|
| Cluster | Can somebody run `kubectl get deploy -A` against production today? | What is running |
| Telemetry | Is there an APM or tracing system, and does it carry an environment label per service? | What is observed |
| GitOps | Is there a repository whose contents are applied to the cluster by a controller? | What is intended |
| Controller | Is Argo CD, Flux or similar installed, and does it own what is running? | What is applied |
| CMDB | Is there a ServiceNow or equivalent with CI records? | What is recorded |

**The telemetry sub-question is the one people get wrong.** "Do you have APM?"
almost always gets a yes. The question that matters is whether each reported
service carries an environment or site label. Without it, telemetry cannot be
attributed to a cluster, and the comparison between observed and running cannot
be made at all. Ask to see one service's tags.

### 5. What are the recovery objectives, and where did they come from?

MTD, RTO and RPO. For each, ask the number and then ask **who set it and against
what analysis.**

An RTO that came from a Business Impact Analysis is a requirement. An RTO that
came from a vendor's default, a contract nobody reread, or a number somebody
liked is a wish. Both are common. Record which.

If the answer is "we do not have them", that is `Absent` and it lands in the
three month roadmap, not the one month one. Deriving real recovery objectives
takes a workshop with people who know what the business loses per hour, and
that cannot be rushed into a month.

### 6. What backs this system up, and has a restore ever been performed?

Two questions, and the second is the real one.

- What mechanism? (Snapshots, volume backups, database dumps, object replication,
  a managed DR service)
- **When was the last restore, and who watched it?**

"We take backups" and "we have restored from backup" are separated by the entire
risk. Also ask: **is the backup inside the blast radius?** A snapshot on the same
storage as the thing it protects survives a file deletion and does not survive
the storage.

### 7. Who may change production, and can one person do it alone?

Ask for a specific recent change and walk through who approved it.

- Is there an approval step at all?
- Can the person who requested a change also approve it?
- Is the approval recorded somewhere that survives the person leaving?
- **Is the identity of the approver verified, or asserted by a form field?**

The last one is the one that decides whether a two-person control is real. An
approval workflow where anybody can type any name is a ceremony, and it is worth
knowing that before recommending one.

### 8. When was the plan last tested, and what happened?

Not "do you test". When, what kind, and what did it find.

- A tabletop, a functional test, or a full failover?
- Were the findings written down?
- **Was anything changed as a result?**

A program that tests and changes nothing is running a rehearsal, not a test. A
program that has never tested has a plan whose truth is unknown, which is a
different and more honest position.

## Part 2: what to look at, not just ask about

Ask for these artifacts. Their absence is itself an answer.

| Artifact | What its absence means |
|---|---|
| The plan document | Everything downstream is `Unknown` |
| The last test report | Testing is `Asserted` at best |
| The CI inventory export | Reconciliation cannot even be attempted |
| One service's APM tags | Observed-versus-running cannot be joined |
| The approval record for one recent production change | The control is `Asserted` |
| The last restore's evidence | Recovery is `Asserted` |

If a plan exists, run `iscp-completeness` on it and fold its `UNFILLED` count
into your findings. That skill's distinction between missing and present-but-
unfilled maps directly onto the roadmap: missing sections are work, unfilled
sections are usually a single interview.

## Part 3: positioning

Write one paragraph, not a rating. It should name:

- the owner, or the absence of one
- whether a plan exists and against which authority
- which of the five readable sources actually exist today
- whether recovery objectives came from analysis or from somewhere else
- whether a restore has ever been performed
- whether the approval control is verified or asserted

Then one sentence on the single largest gap. Not a list. The one thing that, if
it stays as it is, makes everything else cosmetic.

## Part 4: the three roadmaps

Each horizon has a different job. State the job before the items, because a
reader who does not know what a horizon is for will read it as a backlog.

### One month: make it installable and truthful

**The job: our tooling can be pointed at this environment and will report
something true, even if that something is "almost nothing is known".**

This horizon contains only preconditions. It deliberately does not contain plan
writing, BIA work or drills, because none of those gate installation.

Typical contents, ordered by what blocks what:

1. **Name the owner.** One line, one person, written down. Everything else in
   every horizon is unowned until this is done, and it costs a conversation.
2. **Create a read-only credential per environment to be watched.** Cluster-wide
   read, no write verbs. This is the single technical prerequisite. Nothing in
   our tooling needs write access to observe.
3. **Establish where declarations will live.** A file, a repository path, a
   volume. It does not need contents yet, only a decided location and somebody
   who may write to it.
4. **Get one service's telemetry emitting an environment label.** One service,
   not all of them. It proves the path and it makes the label question concrete
   for everybody else.
5. **Collect the artifacts from Part 2 into one place**, including the ones that
   do not exist, recorded as not existing.

**What this month buys:** a reading. Not a good reading. A true one, with its
own gaps named, which is the only honest starting point and is worth more than
a confident inventory nobody has checked.

**What it deliberately does not buy:** any improvement in actual continuity.
Nothing here makes a recovery faster. Say so plainly, because a sponsor who
expects month one to reduce risk will be disappointed by a correct outcome.

### Three months: make it useful and gated

**The job: the readings mean something, and anything acted on is controlled.**

1. **A declared inventory exists**, even a partial one, so reconciliation has two
   sides. Start with the systems the owner would be woken for, not with
   everything.
2. **Environment labels across the services that matter**, so observed and
   running can be joined per environment. Until this is done, a multi-cluster
   comparison invents findings in both directions and is worse than none.
3. **Recovery objectives derived from an analysis**, not inherited from a
   default. This is the BIA, and it belongs here rather than in month one
   because it needs a room with people who know the business impact, which takes
   scheduling rather than effort.
4. **A named group per approval role**, and an authenticating proxy in front of
   anything that acts. Both halves. A roster without verified identity turns
   "anybody may approve" into "anybody may approve by typing one of six names",
   and verified identity without a roster still lets a developer approve as
   security.
5. **One restore performed and witnessed**, on the least important system that
   still has real data. The point is to learn what breaks, and learning it on
   something that matters is the expensive way.
6. **Fill the `UNFILLED` sections** the completeness audit found. Most are one
   interview each.

**What this quarter buys:** findings somebody can act on, and a control that
means something when they do.

### One year: make the program defensible

**The job: an assessor, an auditor or a bad night can be met with evidence
rather than assertion.**

1. **The plan is current and complete** against its authority, re-audited after
   every material change rather than annually by calendar.
2. **The plan has been tested, and the test changed something.** A test that
   finds nothing is a test that was too easy or was not really run.
3. **Recovery objectives drive recovery priorities**, and the sequence in the
   plan matches what the BIA says matters. These drift apart silently and
   nothing detects it but a re-read.
4. **Reconciliation runs continuously and its gaps are worked**, rather than
   being generated and admired. A finding list nobody closes trains everybody to
   scroll past it.
5. **Every system in scope is covered**, and coverage is stated as a numerator
   over a denominator taken from the union of all sources, never from one
   store. A denominator from a single CMDB silently excludes whatever that CMDB
   missed, which is exactly the drift the exercise exists to surface.
6. **Drills are scheduled and the schedule survives a busy quarter.** This is an
   organizational fact, not a technical one, and it is the one most likely to
   quietly lapse.

**What the year buys:** the ability to answer "can you recover this, and how do
you know" with a document, a test report and a reading, rather than with a
person's confidence.

## Part 5: writing the roadmap

Each item, in every horizon, carries:

- **What** in one sentence
- **Who**, a named person, or `UNOWNED` in capitals
- **What it unblocks**, naming the later item by number
- **How you will know it is done**, stated as something observable

Order within a horizon by what blocks what, never by effort. An easy item that
blocks nothing can wait behind a hard item that blocks four.

**If a horizon has no items, say so and explain why**, rather than padding it.
A program that already has a named owner, read credentials and a location for
declarations has an empty month one, and that is a finding worth stating rather
than hiding behind invented tasks.

**Mark every item that depends on our tooling being installed.** There should be
very few, and they should all be in the three month horizon or later. If month
one contains an item that requires our software, the assessment has drifted into
a deployment plan and should be rewritten.

## What to do when the answer to everything is "no"

This is the common case and it is not a disaster. A program with no plan, no
inventory and no named owner is at the beginning, and the correct month one is
three items long: name an owner, create a read credential, decide where
declarations live.

Do not produce a forty item roadmap for such a program. A roadmap longer than
the organization can hold is a document that gets filed, and the assessment that
produced it gets remembered as an expensive way to be told bad news.

## What this skill is not

It is not an audit against a control framework. It does not grade against
NIST SP 800-53 CP controls, FedRAMP baselines, CNSSI 1253 or any DoD
instruction. Those are separate assessments with their own evidence rules, and
conflating them with this produces a document that satisfies neither.

It is not a gap analysis against a product roadmap. The three horizons target
the state where our tooling is useful, which is a means. The organization's own
continuity goals are the end, and where the two diverge, say so rather than
quietly optimizing for ours.
