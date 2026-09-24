# The evaluation flow

Five stages, worked through in order inside **one agent and one context**. Nothing is delegated,
so nothing is serialized into prose and read back, so provenance survives to the stage that
needs it.

Blue is the agent, green is a knowledge file, purple is a stage it works through, grey is what
goes in and comes out.

```mermaid
flowchart TD
    classDef agent fill:#e8eff5,stroke:#2d5f8a,stroke-width:3px,color:#12283a
    classDef know fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef stage fill:#efe8f5,stroke:#6b4a8a,stroke-width:2px,color:#2a1a3a
    classDef io fill:#f2f2f4,stroke:#8791a0,stroke-width:1px,color:#333
    classDef warn fill:#f7dede,stroke:#c62828,stroke-width:2px,color:#411

    subgraph IN["WHAT THE USER BRINGS, in the conversation"]
        direction LR
        D1(["BIA<br/>spreadsheet<br/>or document"]) ~~~ D2(["Contingency<br/>plan"]) ~~~ D3(["DR plan and<br/>runbooks"]) ~~~ D4(["Test and<br/>drill reports"]) ~~~ D5(["Contracts,<br/>training records"])
    end

    subgraph AG["ONE AGENT, one context, no delegation"]
        direction LR
        A(["ITSCM Documentation Review"])
    end

    subgraph KN["KNOWLEDGE FILES, the method it follows"]
        direction LR
        K1(["doc-intake"]) ~~~ K2(["doc-extract"]) ~~~ K3(["itil-scm-<br/>evidence-review"]) ~~~ K4(["pi-roadmap"]) ~~~ K5(["GLOSSARY<br/>CONVENTIONS"])
    end

    subgraph P1["STAGES 1 and 2, what is here and what does it say"]
        direction LR
        S1(["1 Intake<br/>classify by reading,<br/>never by title"]) --> S2(["2 Extract<br/>facts with provenance,<br/>fill no gaps"])
    end

    subgraph P3["STAGE 3, four dimensions, one at a time, each written out before the next"]
        direction LR
        E1(["3a Organizations<br/>and people"]) --> E2(["3b Information<br/>and technology"]) --> E3(["3c Partners<br/>and suppliers"]) --> E4(["3d Value streams<br/>and processes"])
    end

    subgraph P4["STAGES 4 and 5, what it means and what to do"]
        direction LR
        S4(["4 Score<br/>criteria to levels,<br/>never averaged"]) --> S5(["5 Roadmap<br/>five horizons on<br/>increment boundaries"])
    end

    subgraph OUT["WHAT THE MANAGER GETS"]
        direction LR
        O1(["Proven or<br/>unproven"]) ~~~ O2(["A level per<br/>dimension"]) ~~~ O3(["The criterion<br/>blocking each"]) ~~~ O4(["Five horizons"])
    end

    NOPE(["Never a certified ITIL Maturity Model assessment.<br/>That needs the licensed practice success factors,<br/>seven or more practices, and a licensed assessor."])

    IN ==> AG
    KN -.-> AG
    AG ==> P1 ==> P3 ==> P4 ==> OUT
    OUT -.-> NOPE

    class A agent
    class K1,K2,K3,K4,K5 know
    class S1,S2,E1,E2,E3,E4,S4,S5 stage
    class D1,D2,D3,D4,D5,O1,O2,O3,O4 io
    class NOPE warn
```

## Where it stops rather than guesses

Five refusals, written into the instructions rather than left to judgment.

| Stage | Refuses to |
|---|---|
| Intake | Believe a title. A file called a Disaster Recovery Plan is often a contingency plan and occasionally a runbook |
| Extract | Fill a gap. A missing recovery objective is extracted as missing, never inferred from the architecture |
| Evaluate | Reward a heading. The question is whether content satisfies the criterion, not whether a section exists |
| Score | Average. A dimension sits at the highest level whose criteria are all met, and nine of ten met is the lower level |
| Every stage | Author a practice success factor. Where a question needs the licensed model, the answer is that it is not assessable against it |

## Why stage 3 runs one dimension at a time

The four dimensions are separate questions about the same documents, and the common failure is a
well documented set carrying a thin dimension upward: the same context that just found the plan
excellent is the context judging the supplier evidence.

Finishing and writing out one dimension's findings before starting the next is what prevents it.
The findings stay in one context rather than being handed anywhere, so the protection costs no
fidelity.

## The alternative, and what it costs

An earlier version of this design split the work across a root agent and eight subagents, one
per stage and one per dimension. `agents/00-root.md` through `agents/05-roadmap.md` still carry
that configuration.

**It loses information at every handoff**, and the losses are structural rather than incidental:

```mermaid
flowchart LR
    classDef ok fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef bad fill:#f7dede,stroke:#c62828,stroke-width:2px,color:#411

    R1(["Root holds<br/>the facts"]) --> L1(["Encodes to prose"]) --> L2(["Subagent reads"]) --> L3(["Works from<br/>what it was told"]) --> L4(["Encodes back"]) --> R2(["Root reads,<br/>summarizes"])

    class R1,R2 ok
    class L1,L2,L3,L4 bad
```

There is no state object, so the running result is serialized into natural language and read back
at every hop. Provenance is a structural fact, a document and a location per item, and it is
exactly the kind that does not survive repeated round trips.

A subagent cannot hold knowledge files either, so it never sees the source documents or the skill
it is applying. And the root decides what to forward without knowing what the subagent needs,
because the criteria live in the subagent's instructions, which the root never reads. That puts a
filter operated by the wrong party at the point where dropping one fact changes a verdict.

**What the split buys** is that four evaluators cannot see each other's answers, which prevents
the halo effect structurally rather than behaviorally. That is real and it is small next to the
loss above.

**When to revisit:** watch the single agent flatter its weakest dimension, then run the same
document set through both and compare that one dimension. If the split scores it lower, it has
earned its cost. If the scores match, it has not.
