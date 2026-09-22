# IT

**Nothing here yet. That is the finding, not an oversight.**

This side states what the architecture can actually deliver: the achievable recovery time, the
data loss the replication actually permits, the inventory of components, and which components
each business process depends on. That last one usually exists only in an engineer's head, and
writing it down is the single most useful thing this side contributes.

It does not set the recovery objectives. A maximum tolerable downtime set by IT is IT deciding
what it is allowed to fail at, and a requirement copied from a capability means the plan can
never report the architecture as inadequate.

## What belongs here and has not been written

| Missing | What it would do |
|---|---|
| Infrastructure interview | What the platform can deliver, and under what conditions |
| Application interview | Application-level recovery behavior and its dependencies |
| Governance interview | Ownership, review cadence, and change integration |
| Continuity interview | The continuity questions that sit outside the business impact analysis |
| DR runbook authoring | Operational writing discipline for recovery procedures |
| Portfolio and dependency scope | Building the register across systems, which `enterprise-bia` assumes exists |

Until these exist, a start-to-finish walkthrough stops after the product owner.

## Why this is a separate folder rather than merged upward

The business states the requirement. This side states the capability. The gap between them is
either a funded project or an accepted risk, and it is the reason the whole exercise is worth
doing.

Run both as one conversation and the gap stops being visible, which is how a recovery objective
ends up being whatever the architecture already does.
