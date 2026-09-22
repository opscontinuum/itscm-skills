# ITSCM owner

For whoever is accountable for IT service continuity management as a **practice**, across every
program rather than inside one. The ITSCP coordinator, the continuity manager, the person who
answers for the whole thing.

Not the same person as a product owner, who here is the program manager for one group of
applications or infrastructure. Where both exist, the product owner produces a plan and this
role answers for whether the practice those plans belong to is in good order.

| Skill | What it does |
|---|---|
| [`itscm-program-assessment`](itscm-program-assessment/) | Start here. Eight questions about what the organization actually has, then a one month, three month and one year roadmap |
| [`enterprise-bia`](enterprise-bia/) | Lay every program's business impact analysis against the others and find where they contend for the same resource, recovery capacity or people. Produces a ranked priority list and a board paper |
| [`itscm-coordinator-review`](itscm-coordinator-review/) | Assess a whole documentation set rather than one plan, and report a capability level per dimension |

## What only this role can do

**See contention.** Every program's analysis is internally consistent. Two of them sharing a
database with different deadlines is a conflict that exists in neither document, and no program
manager can find it from inside their own program.

**Refuse to resolve it.** Contention is a funding decision. Defaulting it to the tightest
deadline commits money nobody approved and quietly downgrades somebody who will find out during
an incident. This role's job is to put the choice in front of a body that can make it, not to
make it.

**Say the practice is unproven.** A capability level describes how well organized the practice
is, not whether recovery works. Reporting that distinction is this role's, because a program
manager reporting on their own program has every reason not to.
