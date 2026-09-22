---
name: bia-workshop
description: Facilitate the Business Impact Analysis that becomes ISCP Appendix L, following NIST SP 800-34 Rev. 1 Appendix B in the order NIST states it. Keeps recovery objectives keyed to mission and business processes rather than to systems or tiers, which is the failure that makes an otherwise complete plan unable to say what to recover first.
---

# Running the Business Impact Analysis

This is a facilitation procedure, not an audit. You are in a room with people, getting numbers
out of them that they will later be held to.

Half a day, if the processes are already named. Longer if they are not.

## Why the structure is not yours to choose

FedRAMP's ISCP template carries one sentence at Appendix L: "Insert the Business Impact
Analysis here. Please see NIST SP 800-34, Revision 1 for more information on how to conduct a
Business Impact Analysis."

So the structure is not FedRAMP's. It comes from **NIST SP 800-34 Rev. 1, Appendix B, "Sample
Business Impact Analysis (BIA) and BIA Template"**, and its headings and table columns are
reproduced verbatim. Tell the room this. It is what stops the session inventing a format that
an assessor will not recognize, and it settles the first argument before it starts.

| NIST section | Table columns, verbatim |
|---|---|
| 1 Overview | none |
| 2 System Description | none |
| 3.1 Determine Process and System Criticality | Mission/Business Process · Description |
| 3.1.1 Identify Outage Impacts and Estimated Downtime | Impact category · Severe · Moderate · Minimal |
| 3.1.1 (second) | Mission/Business Process · *one column per chosen category* · Impact |
| 3.1.1 (third) | Mission/Business Process · MTD · RTO · RPO |
| 3.2 Identify Resource Requirements | System Resource/Component · Platform/OS/Version (as applicable) · Description |
| 3.3 Identify Recovery Priorities for System Resources | Priority · System Resource/Component · Recovery Time Objective |

## The rule that this whole skill exists to protect

**The unit of analysis is the mission or business process. Not the system, not the server, not
the tier.**

Systems are what processes depend on. A system tier, where one exists, is *derived* from
process requirements by a stated mapping, and is never a substitute for them.

This gets violated constantly, and almost always by competent people, because an
infrastructure team naturally states recovery objectives against the thing it owns. "The
database is Tier 1, so four hours" is a true statement about infrastructure. It cannot answer
the only question an outage asks, which is whose work has stopped and for how long.

**Watch for these three and stop the session when you see one:**

- A row in the process table that a non-engineer would not recognize. `prd-app-04` has no
  business meaning until somebody says what work runs on it.
- Recovery objectives arriving already filled in, from a tiering exercise or a vendor default.
  Those are the architecture's numbers and you are here for the business's.
- Anybody describing an existing system-tier table as "basically the BIA". It is not. See the
  two-table section below for exactly what it is missing.

## The order, which is load bearing

NIST states the BIA in three steps: determine mission and business processes and recovery
criticality; identify resource requirements; identify recovery priorities for system
resources. **Run the workshop in that order.**

The order is the control. Resources cannot be prioritized before you know which business
processes they serve, and running it backwards, starting from the infrastructure inventory,
is precisely how a plan ends up keyed to systems.

---

## Step 1: the processes

**Work with the people who own the work, not with the people who own the servers.**

Ask what *business* processes stop if this system stops. One row per process, with a
description a non-engineer would recognize.

If the only people available are from IT, stop and say so rather than proceeding. An MTD set
by IT is IT telling itself what it is allowed to fail at.

NIST's own example, "Pay vendor invoice", is an illustration. Do not borrow it.

**Record:** Mission/Business Process · Description · the owner's name.

A process with no named owner is recorded as `UNOWNED`, which is a finding rather than a
blank. Somebody has to answer for the number you are about to write next to it.

## Step 2: the impact scale, then the impacts

NIST: "Impact categories and values should be created in order to characterize levels of
severity to the organization."

NIST shows **Cost** as *an example of an impact category*, with sample dollar figures. **Those
figures are a sample, not a default.** A scale copied from the standard describes the
standard's illustration, and every rating recorded against it afterwards means nothing.

Ask the organization for its own categories. A menu to start from, not to impose: cost, harm
to individuals, ability to perform the mission, reputation, regulatory exposure. Use the ones
this organization already argues about in other contexts, because those are the ones people
can actually rate against.

Then their own Severe, Moderate and Minimal values for each.

**Only then**, per process, the impact under each category. The table is as wide as the
categories the organization chose; the column count is an output of this step, not a fixed
format.

For the overall rating per process, take the worst single category rather than an average. A
business does not average a missed payroll.

## Step 3: MTD, then RTO, then RPO, in that order

Ask in that order. The order is the second anti-mis-keying control: MTD is elicited first and
is a business number, RTO is then derived to satisfy it, RPO last.

Use NIST's definitions verbatim, because paraphrase is where the meaning slips:

- **Maximum Tolerable Downtime (MTD)**: "the total amount of time leaders/managers are willing
  to accept for a mission/business process outage or disruption." A business number.
- **Recovery Time Objective (RTO)**: "the maximum amount of time that a system resource can
  remain unavailable before there is an unacceptable impact on other system resources,
  supported mission/business processes, and the MTD."
- **Recovery Point Objective (RPO)**: "the point in time, prior to a disruption or system
  outage, to which mission/business process data must be recovered (given the most recent
  backup copy of the data) after an outage."

### The constraint to enforce in the room

"Because the RTO must ensure that the MTD is not exceeded, the RTO must normally be shorter
than the MTD" (NIST SP 800-34 Rev. 1, §3.2.1, p. 16).

Work still has to happen after a system is technically available and before the business is
actually running: re-submitting what was in flight, replaying interfaces, reconciling.

**If the answers violate that, say so and ask which number is wrong.** Do not fix it yourself.
The room decides which of the two was wrong, because both are their numbers.

### When the architecture cannot meet the number

This is the moment the session is really for, and the honest outcome is the one NIST states:
"when it is not feasible to immediately meet the RTO and the MTD is inflexible, a Plan of
Action and Milestone should be initiated to document the situation and plan for its
mitigation."

A tracked, owned, dated gap item. **Not a quietly relaxed RTO.** The requirement is not edited
down to what the architecture already does, because that comparison is the entire reason the
number exists.

### Three things to capture alongside every number

- **Granularity.** Values are "expected to be specific time frames, identified in hourly
  increments (i.e., 8 hours, 36 hours, 97 hours, etc.)". This rules out "as soon as possible",
  "best effort" and "next business day".
- **Provenance.** What each number comes from: a mandate, a contract, a workload, a
  performance measure. A number with no source is a number nobody can defend when it is
  challenged, and it will be challenged the first time it costs money.
- **Alternate means of processing.** The secondary processing or manual work-around. **"If
  none exist, so state."** A recorded "none" is a complete answer. A blank is not.

### Processes whose tolerance changes with the calendar

Some processes are near-harmless to interrupt for eleven months and severe for three days:
period close, a payment run, a payroll disbursement. Give them **two rows** with the condition
named, rather than one averaged number that is too loose in the window and needlessly tight
outside it.

## Step 4: resources, the dependency map, and priorities

**Resources.** "A system resource can be software, data files, servers, or other hardware and
should be identified individually or as a logical group." Grouping is allowed and usually
clearer: "application tier nodes" beats eleven hostnames. The test is whether you would
recover them together.

If an inventory already exists, from infrastructure-as-code, a CMDB or a discovery tool, it
can populate the identity columns: resource, platform, version, region. **It cannot populate
the judgment columns.** Recovery priority and recovery time are left empty on purpose for a
human to fill, and an inventory that arrives with them pre-filled has had somebody's guess
inserted where a decision belongs.

### The dependency map, which NIST's third step presupposes

Before priorities, record **which resources each process depends on**, and whether the process
is unusable or merely degraded without each one.

NIST gives a table for processes, one for impacts, one for objectives, one for resources and
one for priorities, and no table joining resources back to processes. **That is an absence of a
prompt, not a prohibition.** Nothing in the method excludes the mapping, and the method in fact
depends on it: NIST's own third step is to identify recovery priorities for system resources,
and that step cannot be performed at all without knowing which processes each resource serves.
The priority in §3.3 is derived from the objective in §3.1.1, and the mapping is the derivation.

So collecting it is not an extension of the method. It is an unstated prerequisite of a step
the method requires, and a session that skips it has no route from "payroll must run within
four hours" to "therefore restore the database before the reporting server."

This is the step most sessions skip, and skipping it is the most common reason a finished plan
cannot say what to fix first. Add the table. Nobody will object to a BIA that shows its
working, and an assessor reading §3.3 will find the derivation behind it rather than an
assertion.

### Priorities

Now derive them. Each resource inherits the tightest RTO of any process that depends on it as
essential. Name which process set each one, so the order can be audited later instead of
trusted.

**Do not fill a priority order the business has not agreed.** Recovery order is a decision
with consequences for whoever waits longest, and it is theirs to make.

Close with alternate strategies: backup or spare equipment, and vendor support contracts.

---

## The two tables with different keys

This is the structural point that explains the most common failure, and NIST does not state it
outright.

There are **two recovery-time tables in the BIA and they are keyed to different things:**

| | Keyed to | Carries |
|---|---|---|
| §3.1.1, third table | Mission/Business Process | MTD · RTO · RPO |
| §3.3 | System Resource/Component | Priority · Recovery Time Objective |

The resource-level RTO in §3.3 is a **consequence** of the process-level RTO in §3.1.1,
produced in NIST's third step by way of the dependency map.

**A plan that has only the §3.3-shaped table has kept the output and skipped the analysis.**
It looks finished. It has a tidy list of components with recovery times against them. And it
cannot tell you why any of those numbers is what it is, cannot survive a challenge to one of
them, and cannot be updated when the business changes, because the reasoning that produced it
was never recorded.

If you are handed such a table and asked to treat it as the BIA, say plainly what it is
missing: the processes, the impacts, and the derivation.

## What not to do

1. **Do not compute an MTD, RTO or RPO from the architecture.** They are the business's
   numbers; the architecture is then judged against them.
2. **Do not carry a standard's sample figures into a real plan.**
3. **Do not fill a priority order the business has not agreed.**

## Getting it written down

Every number from this session needs a home, and a signature.

[`worksheets/iscp-data-collection.xlsx`](../../../worksheets/) has a tab per step of this
workshop: processes on tab 2, the impact scale on 3, impacts on 4, objectives on 5, resources
on 6, the dependency map on 7, priorities on 8, and the signatures on 12. Its dropdowns enforce
the keying rule mechanically, since an objective can only be recorded against a process
somebody named.

Then hand it to `iscp-from-worksheet`.

**Unsigned objectives are proposals.** Tab 12 is what converts them into commitments, and an
objective nobody signed cannot be missed, because nobody promised it. Get the signatures in
the room while the reasoning is fresh. Chasing them afterwards takes months and usually fails.

## Checking your own output

- Every process has an owner, an impact rating and an objective.
- Every objective has a source and satisfies RTO shorter than MTD.
- Every process appears in the dependency map.
- Every resource with a priority has the process that set it named.
- Every "none" was written deliberately rather than left blank.
- The tightest RTO here matches the RTO stated in ISCP section 1.4 Scope. They are the same
  number and they drift apart silently.
