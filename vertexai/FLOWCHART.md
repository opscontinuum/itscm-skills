# The evaluation flow

One root agent and eight subagents. The root holds the sequence, the running result, and the
only knowledge files. Each subagent carries its own method in its instructions, because it
cannot be given a file.

Nothing here runs in parallel. The root delegates in order and carries findings between stages
itself.

```mermaid
flowchart TD
    classDef root fill:#e8eff5,stroke:#2d5f8a,stroke-width:3px,color:#12283a
    classDef sub fill:#efe8f5,stroke:#6b4a8a,stroke-width:2px,color:#2a1a3a
    classDef know fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef io fill:#f2f2f4,stroke:#8791a0,stroke-width:1px,color:#333
    classDef warn fill:#f7dede,stroke:#c62828,stroke-width:2px,color:#411

    subgraph IN["WHAT THE USER BRINGS, in the conversation"]
        direction LR
        D1(["BIA<br/>spreadsheet<br/>or document"]) ~~~ D2(["Contingency<br/>plan"]) ~~~ D3(["DR plan and<br/>runbooks"]) ~~~ D4(["Test and<br/>drill reports"]) ~~~ D5(["Contracts,<br/>training records"])
    end

    subgraph RT["THE ROOT AGENT, holds the sequence and the running result"]
        direction LR
        R(["ITSCM Documentation Review"])
    end

    subgraph KN["KNOWLEDGE FILES, root only. Subagents cannot be given one"]
        direction LR
        K1(["doc-intake"]) ~~~ K2(["doc-extract"]) ~~~ K3(["itil-scm-<br/>evidence-review"]) ~~~ K4(["pi-roadmap"]) ~~~ K5(["GLOSSARY<br/>CONVENTIONS"])
    end

    subgraph ST1["STAGE 1 and 2, what is here and what does it say"]
        direction LR
        S1(["1 Intake<br/>classify by reading"]) --> S2(["2 Extract<br/>facts with provenance"])
    end

    subgraph ST3["STAGE 3, four evaluators, each blind to the others"]
        direction LR
        E1(["3a Organizations<br/>and people"]) ~~~ E2(["3b Information<br/>and technology"]) ~~~ E3(["3c Partners<br/>and suppliers"]) ~~~ E4(["3d Value streams<br/>and processes"])
    end

    subgraph ST4["STAGE 4 and 5, what it means and what to do"]
        direction LR
        S4(["4 Score<br/>criteria to levels"]) --> S5(["5 Roadmap<br/>five horizons"])
    end

    subgraph OUT["WHAT THE MANAGER GETS"]
        direction LR
        O1(["Proven or<br/>unproven"]) ~~~ O2(["A level per<br/>dimension"]) ~~~ O3(["The criterion<br/>blocking each"]) ~~~ O4(["Five horizons on<br/>increment boundaries"])
    end

    NOPE(["Never a certified ITIL Maturity Model assessment.<br/>That needs the licensed practice success factors,<br/>seven or more practices, and a licensed assessor."])

    IN ==> RT
    KN -.-> RT
    RT ==> ST1 ==> ST3 ==> ST4 ==> OUT
    OUT -.-> NOPE

    class R root
    class S1,S2,E1,E2,E3,E4,S4,S5 sub
    class K1,K2,K3,K4,K5 know
    class D1,D2,D3,D4,D5,O1,O2,O3,O4 io
    class NOPE warn
```

## Why it splits where it does

**Four evaluators rather than one**, and not for speed, since nothing here runs in parallel.

One agent holding all four dimensions judges the thin parts in the same context that just judged
the good ones, and a strong dimension carries a weak one. Four subagents each see the facts and
their own criteria, and never see each other's answers.

There is also a practical reason. A subagent's method lives in its instructions field, so one
evaluator would have to hold four dimensions of criteria in a single field. Split four ways, each
holds only its own.

**Scoring and roadmap stay separate and stay last.** Scoring needs all four dimensions before it
can find the lowest. The roadmap is derived from what scoring found rather than from the
documents, which is what stops it becoming a list of documents to write.

## Where it stops rather than guesses

Four refusals, each written into a stage's instructions rather than left to judgment.

| Stage | Refuses to |
|---|---|
| Intake | Believe a title. A file called a Disaster Recovery Plan is often a contingency plan and occasionally a runbook |
| Extract | Fill a gap. A missing recovery objective is extracted as missing, never inferred from the architecture |
| Evaluate | Reward a heading. The question is whether content satisfies the criterion, not whether a section exists |
| Score | Average. A dimension sits at the highest level whose criteria are all met, and nine of ten met is the lower level |

A fifth refusal sits in every agent, including the root: **never author a practice success
factor.** That is where an unlicensed substitute for the ITIL Maturity Model would most
plausibly get invented, and the root is the likeliest place, because it is the agent being asked
for a maturity level.

## The thing the root will get wrong if you let it

There is no state store. The root carries the running result in the conversation, and its
instinct is to summarize each subagent's answer before moving on.

By stage 4 a summarized finding has lost its provenance, and the scorer cannot tell an extracted
fact from an inferred one. The score then reads as analysis and is fiction.

The root's instructions say to pass findings forward intact and to include prior output verbatim
rather than a paraphrase. That is the single most important line in the whole configuration.
