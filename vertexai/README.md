# Running the evaluation as a Vertex AI agent

A layout for evaluating continuity documentation that already exists. Somebody hands over a
Business Impact Analysis, a contingency plan, a disaster recovery plan, test reports, whatever
they have, and this produces where that documentation stands against the ITIL 4 Service
Continuity Management practice, plus a roadmap sized for Program Increment planning.

The reader is a manager or an engineer who inherited a folder and needs to know what is in it.

## What the agent interface gives you, and what this design assumes

This is built for an interface with one root agent and a set of subagents. **The two do not
carry the same fields, and the difference drives the whole design.**

| Field | Root | Subagent |
|---|---|---|
| Name | yes | yes |
| Description | yes | yes. The root reads it to decide when to delegate, so it is functional rather than decorative |
| Instructions | yes | yes. For a subagent this is the only place its method can live |
| Model | yes | yes |
| Connectors | yes | yes. **Web search only**, deliberately |
| Knowledge, as files | yes | **no** |
| Personalization, starter prompts | yes | **no** |

**No code, no tools, no state object.** State is whatever the conversation carries.

### The consequence: subagent instructions carry their own method

Only the root can hold knowledge files, so only the root can be handed a skill. A subagent's
instructions have to be self-contained, which means the relevant part of a skill is written into
that field rather than referenced from it.

That creates a maintenance coupling worth naming up front: **a subagent's instructions are
derived from a skill, and when the skill changes they have to be regenerated.** Nothing in the
interface will detect the drift. The file for each agent in `agents/` records which skill and
which section it came from, so a later reader can tell what to re-derive.

It also puts a ceiling on how much method one subagent can hold, which is the practical argument
for splitting evaluation four ways below.

`agents/` holds one file per agent with the exact text to paste into each field:

| File | Agent |
|---|---|
| `agents/00-root.md` | The root, the only one with knowledge files and starter prompts |
| `agents/01-intake.md` | What arrived, and what did not |
| `agents/02-extract.md` | The facts, with provenance |
| `agents/03a-evaluate-org-people.md` | Organizations and people |
| `agents/03b-evaluate-info-tech.md` | Information and technology |
| `agents/03c-evaluate-partners.md` | Partners and suppliers |
| `agents/03d-evaluate-value-streams.md` | Value streams and processes |
| `agents/04-score.md` | Criteria into capability levels |
| `agents/05-roadmap.md` | Five horizons |

## The mechanism: skills are knowledge files

The judgment lives in the skills in [`../skills/`](../skills/). Each one is attached to the
agent that runs it as a knowledge file.

That is the whole integration, and it is why the skills stay executable free per
[`../CONVENTIONS.md`](../CONVENTIONS.md) rule 3. A skill written to be read is a skill that can
be a knowledge file. Had they been written as scripts, this interface could not run them at all.

The same property means the instruments still work by hand for an organization that will never
deploy any of this.

## Why web search is the only connector

Two reasons, and the second matters more.

The instruments need no data source. They read documents the user brings and criteria they carry
in knowledge. A datastore connector would add a place for the agent to find something that looks
like an answer and is not.

And web search has exactly one legitimate use here: confirming the current edition of a standard
before citing it. Every agent's instructions say that, and say what it must never be used for:
looking up what a criterion should be, finding an organization's documents, or filling a gap in
what the user provided. A gap is a finding.

## Topology

```
Root: ITSCM Documentation Review
├── 1 Intake            what arrived, and what did not
├── 2 Extract           the facts, with provenance
├── 3a Evaluate: organizations and people
├── 3b Evaluate: information and technology
├── 3c Evaluate: partners and suppliers
├── 3d Evaluate: value streams and processes
├── 4 Score             criteria into capability levels
└── 5 Roadmap           five horizons for Program Increment planning
```

Eight subagents. The root holds the sequence and the running state.

### Why evaluation is four subagents rather than one

Two reasons, and neither is speed, since nothing here runs in parallel.

**Isolation.** One agent holding all four dimensions judges the thin parts in the same context
that just judged the good parts, and a strong dimension carries a weak one. Four subagents each
see the facts and their own criteria, and never see each other's answers.

**Room.** Since a subagent's method lives in its instructions, one evaluator would have to hold
all four dimensions of criteria in a single field. Split four ways, each holds only its own.

**If eight subagents is too many to configure**, collapse 3a through 3d into one evaluator and
expect the weakest dimension to score about a level higher than it should. Do not collapse
stages 4 or 5 into anything.

### What the root has to do that the interface will not do for it

With no state object, the root carries the running result in the conversation and passes the
relevant part into each delegation. Its instructions have to be explicit about that, because the
default behavior of a root agent is to summarize a subagent's answer rather than carry it
forward intact.

The specific risk: by stage 4 a summarized finding has lost its provenance, and a scorer cannot
tell an extracted fact from an inferred one. The root's instructions repeat the provenance rule
for that reason.

## The honesty constraint, which shapes the criteria

The ITIL Maturity Model derives its capability criteria from practice success factors defined in
the ITIL 4 practice guides, which are behind a PeopleCert subscription.

**No agent here has those, and none invents one.** Where a criterion would need the licensed
model, the agent returns that it is not assessable against it and names what it would have
needed. That rule is in every agent's instructions, not only the evaluators, because the root is
where an unlicensed substitute would most plausibly get authored.

What the design uses instead is public: the practice purpose, the four dimensions of service
management, and capability levels 1 to 5. Criteria are evidence questions this project wrote,
each mapped to a dimension and a level, and every output says so.

So this is an ITIL-aligned evidence review, not an ITIL Maturity Model assessment, and it cannot
be presented as one.

## Getting documents into it

Knowledge files are configured when the agent is built and only the root has them, so they hold
the **instruments**: the skills, the glossary. They are stable across every run, and the root is
the only agent that can consult them directly.

The documents under evaluation arrive with the user, in the conversation. If the interface
allows attaching files to a conversation, that is the better path and the instructions handle
it. If it does not, the user pastes content, and intake records the format limitation as part of
the inventory rather than ignoring it.

**A document the agent could not read is `unreadable`, never `absent`.** That distinction
survives into the report, because one needs a better copy and the other is a finding against the
organization.
