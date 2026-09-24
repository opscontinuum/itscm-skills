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

## Evaluating documentation that already exists

A second path, for when somebody hands over a folder rather than asking you to build one. These
four run in order, each consuming the one before it.

| Skill | What it does |
|---|---|
| [`doc-intake`](doc-intake/) | Establish what actually arrived. Classifies by reading rather than by title, and separates provided from claimed, absent and unreadable |
| [`doc-extract`](doc-extract/) | Pull the facts out of one document, with provenance, filling no gaps and recording whether objectives are keyed to processes or to infrastructure |
| [`itil-scm-evidence-review`](itil-scm-evidence-review/) | Score the set against the ITIL 4 Service Continuity Management practice, capability levels 1 to 5 across the four dimensions of service management |
| [`pi-roadmap`](pi-roadmap/) | Turn the blocking criteria into one, three, six, nine and twelve month horizons, sized for Program Increment planning |

`itscm-coordinator-review` and `itil-scm-evidence-review` overlap deliberately and are not
duplicates. The first is run by a person working through a documentation set and asks for the
documents as part of its own method. The second is the scoring instrument for the pipeline
above: it takes already-extracted facts, and it is shaped to be split across agents that cannot
see each other's answers.

Neither reproduces the practice success factors from the licensed ITIL 4 practice guides, and
neither invents any. Both say so in their own output.

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
