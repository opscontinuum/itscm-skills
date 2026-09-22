---
name: iscp-sufficiency
description: Decide whether a contingency plan carries enough data to actually build a continuity program from it, and report exactly what is missing when it does not. Judges by derivability, not maturity: a field is required only when a named downstream artifact provably cannot be produced without it. Distinguishes four ways a field fails, because they need four different remedies.
---

# Can you build a program from this plan

A plan can be complete and useless. Every heading present, every table filled,
an assessor satisfied, and still nothing downstream can be produced from it.

This skill answers a different question from a completeness audit. Not "does the
document have all its parts" but **"can the things a continuity program needs
actually be derived from what is written here, and if not, what exactly is
missing."**

Run `iscp-completeness` first if you have not. It tells you the document is
intact. This tells you whether it is load bearing.

## The rule that makes this defensible

**A field is required here only when a named downstream artifact provably cannot
be produced without it.** Not because a standard demands it. Not because a
mature program would have it.

That distinction is the whole basis of this skill and you must hold it. The
moment you report something as missing because a good program would have it, you
have replaced a fact with an opinion, and the reader is entitled to disagree with
opinions. "You cannot order a recovery sequence without knowing which resources
each process depends on" is a fact about derivation that survives argument.
"Your program is immature" does not.

So every finding in your report carries its own justification, in this shape:

> **You cannot produce** *[the thing]* **because** *[the field]* **is** *[how it
> failed]*.

If you cannot write a finding in that shape, you do not have a finding. Delete
it.

## Write for somebody who does not work in IT

The person who most needs this report is usually the one who has to fund the
work or schedule the workshop, and they are not an engineer. Write accordingly.

- Name the business consequence, not the data structure. "Nobody can say which
  system to restore first when several fail at once" beats "table 3.3 lacks a
  join key."
- Never make the reader look up an identifier. Write "the table listing recovery
  priorities" before, or instead of, "table 3.3".
- One finding, one sentence, then the detail underneath for whoever wants it.
- No score, no percentage, no maturity level. Those exist to spare the writer
  from saying which specific thing is missing.

## The four ways a field fails

A binary present-or-absent verdict is the single most common defect in this kind
of audit, because these four need four different remedies and three of them are
invisible to a presence check.

| State | What you are looking at | What fixes it |
|---|---|---|
| `ABSENT` | The field does not appear anywhere | Somebody writes it |
| `TEMPLATE` | The table is there with the right columns and every cell is blank or placeholder | Somebody runs the workshop that collects the data |
| `MIS-KEYED` | The data is real, filled and good, and it is attached to the wrong unit of analysis | Somebody re-does the analysis against the right unit |
| `UNCOMMITTED` | The data is real, filled, correctly keyed, and nobody with authority agreed to it | Somebody with authority signs it |

### Why `MIS-KEYED` is the one that gets missed

This is the failure a completeness audit structurally cannot see, and in
practice it is common in plans written by good engineers.

Recovery objectives get stated against the thing the author understands. An
infrastructure team states them per service tier: Platinum 15 minutes, Gold
4 hours, Silver 12 hours. Those are real numbers, honestly derived, often
carefully argued. And they cannot answer the only question that matters at the
moment of an outage, which is **whose work stops and for how long.**

NIST asks for recovery objectives per mission or business process for exactly
this reason. A tier is a property of infrastructure. An MTD is a statement about
what a business can survive, and only a business process has one.

When you find this, do not report it as missing. Report it as present and keyed
wrong, say which unit it is keyed to, say which unit it needs, and say that the
remedy is a re-analysis rather than a writing task. The author will otherwise
read "missing" as an accusation they know to be false, and dismiss the rest of
your report with it.

### Why `UNCOMMITTED` is a real state and not a technicality

Numbers that were computed rather than agreed are design targets. They tell you
what the architecture was built to do. They do not tell you what the business
requires, and they cannot be missed, because nobody promised them.

The tells: a number labeled as a target, an objective with the word "expected"
or "design" near it, a value marked provisional pending a first test, a
signature line that is blank, an approval table where every name is a
placeholder.

A plan whose objectives are all uncommitted can still run a recovery. It cannot
support a conversation about whether the recovery was adequate, because there is
no agreed standard to have been met.

## Part 1: the chain

Everything a continuity program produces hangs off one chain of derivations. Walk
it in order. It breaks at the first missing link and everything after that link
is underivable no matter how good it looks.

```
  the processes          ->  what work does this system carry
        |
  the impact scale       ->  what counts as severe, moderate, minimal
        |
  impact per process     ->  what happens to each one, on that scale
        |
  objectives per process ->  MTD, RTO and RPO for each one
        |
  process -> resource    ->  which components each process depends on
        |
  the resources          ->  what the components are
        |
  recovery priority      ->  the order to bring them back
```

### The link nothing prompts for, and nothing forbids

**Process to resource.** Look at that chain again. NIST SP 800-34 Rev. 1
Appendix B gives a table for processes, a table for impacts, a table for
objectives, a table for resources, and a table for priorities. It gives no
table that says which resources each process depends on.

**Do not read that as a standard declining to require it.** Nothing in NIST
excludes the mapping, and its own third step presupposes one: identifying
recovery priorities for system resources cannot be done without knowing which
processes each resource serves. The priority is derived from the objective, and
this is the derivation. A plan that records it is more conformant, not less.

That mapping is the join. Without it, per-process recovery objectives and a list
of system resources sit on either side of a gap, and no amount of quality in
either one produces a recovery order. You cannot get from "payroll must run
within four hours" to "therefore restore the database before the reporting
server" without knowing that payroll uses the database.

So when you find it absent, the finding is not that the plan omitted something
optional. It is that a required step was performed without its input, which means
the priorities below it were asserted rather than derived.

So check for it explicitly, and expect it to be absent or scattered. It usually
lives, if it lives anywhere, in an architecture document, a dependency diagram,
a service catalog, or in one person's head. Any of those counts if it is written
down and covers every process. None of them counts if it covers only the
resources somebody found interesting.

**When this link is missing, say so first.** It is the single highest-value
finding this skill produces, because it is invisible to every other kind of
audit and it blocks more downstream artifacts than anything else in the chain.

## Part 2: what each downstream artifact needs

This is the derivability table. It is the justification behind every finding, so
cite from it rather than asserting.

| A program needs to produce | It cannot be produced without | Because |
|---|---|---|
| **A recovery order** (what to restore first when several things fail) | objectives per process, process to resource, resources | Order comes from which business work is most urgent, mapped onto what that work runs on |
| **A first-response sheet** (the page a duty operator reads at 2am) | objectives per process, recovery priority | The two decisions in the first minute are how long until this is a different problem, and which failing thing to chase first |
| **An escalation clock** (when to wake somebody) | MTD per process | The MTD is the deadline. Without it, escalation is somebody's judgment about somebody else's tolerance |
| **A judgment on whether the architecture is adequate** | RPO per process, and what the replication actually achieves | An architecture is adequate or not only relative to a stated requirement. With no requirement, it is neither |
| **A test that can pass or fail** | RTO per process | A drill with no target is a rehearsal. It produces a duration and no verdict |
| **An investment case** | impact per process, on a defined scale | Spend is justified against loss avoided. Unquantified impact justifies nothing, in either direction |
| **A tier or criticality assignment across systems** | impact per process, comparable across systems | Assigning tiers without comparable impact data is ranking by advocacy |
| **A commitment to a customer or a regulator** | objectives that are committed, not computed | You cannot promise a number nobody agreed to |
| **A vendor or contract requirement** | objectives per process, resources, process to resource | You buy support for the components that carry urgent work, at the urgency that work requires |

## Part 3: how to run it

1. **Read the whole plan first.** The data you need is often not under the
   heading that asks for it. Objectives hide in architecture documents,
   dependencies hide in runbooks, and a first pass that has not seen the end
   reports false gaps.

2. **Find the processes.** If the plan names no business processes at all, stop
   and say so: the chain has no first link and nothing below it can be assessed.
   This is a short report and an honest one.

3. **Walk the chain in order.** For each link: `ABSENT`, `TEMPLATE`,
   `MIS-KEYED`, `UNCOMMITTED`, or present and usable. Do not skip ahead. A link
   that follows a break is not assessed, it is unreachable, and reporting it as
   a separate failure inflates the problem.

4. **Test the joins, not just the presence.** For each adjacent pair, ask whether
   they share a key. The specific checks:
   - Do the processes named in the objectives table match the processes named in
     the process table, by name, with none dropped?
   - Is every process covered, or only the interesting ones?
   - Does every resource trace back to at least one process?
   - Does the priority order cover every resource, or only the ones somebody
     thought of?
   A join that covers half the rows is `PARTIAL` and you say which half.

5. **Check the constraint NIST states.** "Because the RTO must ensure that the
   MTD is not exceeded, the RTO must normally be shorter than the MTD"
   (NIST SP 800-34 Rev. 1, §3.2.1). Where an RTO equals or exceeds its MTD, one
   of the two numbers is wrong, and that is a finding regardless of everything
   else being present. NIST's own remedy when the architecture genuinely cannot
   meet the business number is a Plan of Action and Milestone documenting the
   situation, not a quietly relaxed RTO.

6. **Say what can be built today.** Lead with this. A report that only lists
   gaps reads as a failure notice, and most plans can produce something.

## Part 4: the report

```
CAN A PROGRAM BE BUILT FROM THIS PLAN
Document: <name>

WHAT YOU CAN BUILD TODAY
  <artifact>   using <the parts of the plan that support it>
  ...

WHAT YOU CANNOT BUILD, AND WHY
  <artifact>
    You cannot produce this because <field> is <state>.
    <one plain sentence on the business consequence>
    Where it would have to come from: <section, or "nowhere in this document">
    What fixes it: <write it | run the workshop | re-do the analysis | get it signed>
  ...

THE CHAIN
  processes              <state>
  impact scale           <state>
  impact per process     <state>
  objectives per process <state>
  process -> resource    <state>
  resources              <state>
  recovery priority      <state>
  First break at: <link>.  Everything below it is unreachable rather than absent.

CONSTRAINT VIOLATIONS
  <process>: RTO <x> is not shorter than MTD <y>
  ...
```

Then, and only when the gaps are the kind that data collection closes, the
agenda below.

## Part 5: when the answer is a workshop, not an edit

The most common outcome of this audit is that the plan is well written and the
analysis behind it was never done. `TEMPLATE` and `MIS-KEYED` both mean this.

When that is the finding, an edit list is the wrong deliverable and will be
ignored, because no amount of writing produces impact data nobody collected. The
right deliverable is the agenda for the session that collects it, and who has to
be in the room.

Produce it in this shape:

> **Session:** recovery objectives for *[system]*
> **Who must be there:** the person accountable for each named process, somebody
> who can commit the business to a number, and somebody who knows what the
> architecture can actually do. All three. Two of the three produces numbers
> that are either unachievable or unagreed.
> **What comes out:** the specific rows this audit found empty, named.
> **What does not come out:** anything the architecture team can decide alone.

Two rules to state in the agenda, both from the BIA method:

- **Recovery objectives are the business's numbers, not the architecture's.** Do
  not compute an MTD from what the system can currently do. The system is then
  judged against the number, which is the entire point of having one.
- **Do not carry a standard's sample figures into a real plan.** NIST prints
  example impact values to illustrate the shape of the table. A plan that ships
  them has recorded an illustration as a decision.

## What this skill does not do

It does not grade maturity, score the plan, or rank it against other plans.

It does not require anything a downstream artifact does not need. If you find
yourself about to report a gap and you cannot name the artifact it blocks, that
is not a gap, it is a preference.

It does not assess whether the plan is complete against FedRAMP or NIST. That is
`iscp-completeness`, it answers a different question, and a plan can pass either
one of these and fail the other. A document with every heading filled can be
underivable, and a document missing half its appendices can carry a complete
chain.

It does not assess the organization, only the document. What the organization
has in people, cadence and ownership is `itscm-program-assessment`.
