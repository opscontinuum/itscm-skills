# IT

**Two skills exist. The rest of this side is still missing, and that is still the finding.**

This side states what the architecture can actually deliver: the achievable recovery time, the
data loss the replication actually permits, the inventory of components, and which components
each business process depends on. That last one usually exists only in an engineer's head, and
writing it down is the single most useful thing this side contributes.

It does not set the recovery objectives. A maximum tolerable downtime set by IT is IT deciding
what it is allowed to fail at, and a requirement copied from a capability means the plan can
never report the architecture as inadequate.

## What exists

| Skill | What it does |
|---|---|
| [`recovery-path`](recovery-path/) | Walk read-only from the names customers use to the standby's data: which copy answers now, what the switch does and whether it has ever moved, what a move between copies would lose, and what a recovery needs that the running system does not |
| [`recovery-drill`](recovery-drill/) | Drill the failure most likely to breach an objective, within bounds the owners agreed in advance, timed on one clock and measured from the customer's side. Refuses to destroy data that has no copy and no written acceptance of its loss |

Neither was on the list below. The first run of this method against real infrastructure found
that every defect the written skills missed lay in the recovery path, and that the only step
allowed to change anything had no skill. These two were written first for that reason.

## What belongs here and has not been written

| Missing | What it would do |
|---|---|
| Infrastructure interview | What the platform can deliver, and under what conditions |
| Application interview | Application-level recovery behavior and its dependencies |
| Governance interview | Ownership, review cadence, and change integration |
| Continuity interview | The continuity questions that sit outside the business impact analysis |
| DR runbook authoring | Operational writing discipline for recovery procedures |
| Portfolio and dependency scope | Building the register across systems, which `enterprise-bia` assumes exists |

Until these exist, a start-to-finish walkthrough stops after the product owner for everything IT
contributes except the recovery path and the drill. The rest still has to be improvised.

## Why this is a separate folder rather than merged upward

The business states the requirement. This side states the capability. The gap between them is
either a funded project or an accepted risk, and it is the reason the whole exercise is worth
doing.

Run both as one conversation and the gap stops being visible, which is how a recovery objective
ends up being whatever the architecture already does.
