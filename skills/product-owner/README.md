# Product owner

For the program manager accountable for a group of applications or infrastructure, who has to
produce and defend a continuity plan for it.

| Skill | What it does |
|---|---|
| [`iscp-completeness`](iscp-completeness/) | Is an existing plan intact against the standard that governs it |
| [`iscp-sufficiency`](iscp-sufficiency/) | Can a program actually be derived from what that plan contains. A plan can pass one of these and fail the other |
| [`iscp-from-worksheet`](iscp-from-worksheet/) | Turn a filled data-collection workbook into the plan, refusing to write any section the data does not support |

**Each of these reads one program's artifact.** Anything that reads across programs, or assesses
the practice rather than a document, is in [`../itscm-owner/`](../itscm-owner/).

## Where to start

If a plan exists, audit it twice before touching it: `iscp-completeness` for whether the
document is intact, `iscp-sufficiency` for whether anything can be built from what it says. Those
answer different questions and a plan can pass one and fail the other.

If no plan exists, the order is the business impact analysis first
([`../business/bia-workshop/`](../business/bia-workshop/)), then the workbook, then
`iscp-from-worksheet`. Writing the plan before the analysis produces a document that describes
the architecture rather than what the business needs.
