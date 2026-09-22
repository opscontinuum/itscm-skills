# Business

**Terms used here.** The full list is [`GLOSSARY.md`](../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |


For the people whose work stops when the system stops. Process owners, finance, whoever is
accountable for the work itself rather than for the machinery under it.

**This side states the requirement.** How long the work can be down, what an outage costs, and
how much data loss is survivable. Nobody else can answer those, and a recovery objective set by
IT is IT deciding what it is allowed to fail at.

| Skill | What it does |
|---|---|
| [`bia-workshop`](bia-workshop/) | Facilitate the Business Impact Analysis. Half a day. Produces the processes, the impact scale, the impacts, and MTD, RTO and RPO per process |

A worked example of this leg run end to end is in
[`examples/ebs-exadata-business-leg.md`](../../examples/ebs-exadata-business-leg.md).
