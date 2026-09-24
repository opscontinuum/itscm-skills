# How the skills get used

A skill here is a prose instrument. You give it to a model along with a document, and it returns
structured output. That is the whole unit of work, and it is the same unit whether the model is
Grok, a Vertex agent, or a person reading the skill and doing it by hand.

```mermaid
flowchart LR
    classDef skill fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef doc fill:#f2f2f4,stroke:#8791a0,stroke-width:1px,color:#333
    classDef model fill:#e8eff5,stroke:#2d5f8a,stroke-width:3px,color:#12283a
    classDef out fill:#efe8f5,stroke:#6b4a8a,stroke-width:2px,color:#2a1a3a

    SK(["THE SKILL<br/>a prose file"]) --> M(["A MODEL<br/>Grok, a Vertex agent,<br/>or a person"])
    DOC(["THE DOCUMENT<br/>a plan, a spreadsheet,<br/>a test report"]) --> M
    M --> O(["STRUCTURED OUTPUT<br/>a fixed shape the<br/>next stage consumes"])

    class SK skill
    class DOC doc
    class M model
    class O out
```

Nothing in a skill is executed. That is why the same file works in all three places, and it is
why [`../CONVENTIONS.md`](../CONVENTIONS.md) rule 3 exists.

## The five runs, and what goes into each

Five of those units, chained. Each one's output is the next one's input.

Green is the skill you paste in, grey is what you paste alongside it, purple is what comes back.

```mermaid
flowchart TD
    classDef skill fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef doc fill:#f2f2f4,stroke:#8791a0,stroke-width:1px,color:#333
    classDef out fill:#efe8f5,stroke:#6b4a8a,stroke-width:2px,color:#2a1a3a
    classDef warn fill:#f7dede,stroke:#c62828,stroke-width:2px,color:#411

    subgraph R1["RUN 1, once. What is here?"]
        direction LR
        S1(["doc-intake"]) ~~~ I1(["Every file<br/>they sent"]) ~~~ O1(["INVENTORY<br/>provided, claimed,<br/>absent, unreadable"])
    end

    subgraph R2["RUN 2, once per document. What does it say?"]
        direction LR
        S2(["doc-extract"]) ~~~ I2(["ONE document,<br/>plus its line from<br/>the inventory"]) ~~~ O2(["EXTRACTED FACTS<br/>each with the document<br/>and location"])
    end

    subgraph R3["RUN 3, once per dimension. Does it satisfy the criteria?"]
        direction LR
        S3(["itil-scm-<br/>evidence-review"]) ~~~ I3(["All facts, plus<br/>the inventory"]) ~~~ O3(["FINDINGS<br/>met, not met,<br/>not assessable"])
    end

    subgraph R4["RUN 4, once. What level is that?"]
        direction LR
        S4(["itil-scm-<br/>evidence-review<br/>scoring section"]) ~~~ I4(["All findings,<br/>all four dimensions"]) ~~~ O4(["LEVELS<br/>claimed and evidenced,<br/>plus the blocker"])
    end

    subgraph R5["RUN 5, once. What do we do?"]
        direction LR
        S5(["pi-roadmap"]) ~~~ I5(["The levels and<br/>blocking criteria"]) ~~~ O5(["ROADMAP<br/>five horizons on<br/>increment boundaries"])
    end

    NOPE(["Never a certified ITIL Maturity Model assessment.<br/>That needs the licensed practice success factors,<br/>seven or more practices, and a licensed assessor."])

    R1 ==> R2 ==> R3 ==> R4 ==> R5 ==> NOPE

    class S1,S2,S3,S4,S5 skill
    class I1,I2,I3,I4,I5 doc
    class O1,O2,O3,O4,O5 out
    class NOPE warn
```

**Run 2 repeats per document and run 3 repeats per dimension.** That is not parallelism, it is
the same skill run again with different input. A spreadsheet and a Word plan are two runs of
`doc-extract`, not one run that handles both.

**Run 4 uses the same skill file as run 3**, its scoring section. They are separated because
answering criteria and assigning a level are different jobs, and a model doing both in one pass
tends to pick the level first and fit the criteria to it.

## What has to survive between runs

The output of one run is pasted into the next, so everything the later stage needs has to be in
that text. Two things get lost first.

**Provenance.** Every extracted fact carries the document and the location it came from. If a run
2 output is summarized before being pasted into run 3, the facts arrive looking identical to
guesses, and by run 4 nothing can tell them apart. Paste the output whole.

**The four states.** `provided`, `claimed but not provided`, `confirmed absent` and `unreadable`
are not decoration. Run 3 needs them to tell `NOT MET` from `NOT ASSESSABLE`, which have
different remedies: one needs work, the other needs somebody to send a file.

## Where a hosted agent fits

A Vertex agent is one way to run the chain without pasting by hand. It does not change the
instruments, and it adds one constraint worth knowing.

**A rule must be in the agent's instructions, not in a knowledge file.** Knowledge is retrieved
against a query and chunked, so a rule sitting there reaches the model only when something in the
current query resembles it. The moment an agent is about to invent a criterion is exactly the
moment nothing in its query looks like the rule forbidding it.

So the instructions field carries everything load-bearing, derived from the skills, and the
knowledge files carry detail and examples. [`agents/single-agent.md`](agents/single-agent.md) is
that configuration.

The skills stay the source of truth, and the instructions are derived from them. When a skill
changes, the instructions have to be regenerated, and nothing in the agent interface will detect
the drift.

## Where it stops rather than guesses

| Run | Refuses to |
|---|---|
| 1 Intake | Believe a title. A file called a Disaster Recovery Plan is often a contingency plan and occasionally a runbook |
| 2 Extract | Fill a gap. A missing recovery objective is extracted as missing, never inferred from the architecture |
| 3 Evaluate | Reward a heading. The question is whether content satisfies the criterion, not whether a section exists |
| 4 Score | Average. A dimension sits at the highest level whose criteria are all met, and nine of ten met is the lower level |
| Every run | Author a practice success factor. Where a question needs the licensed model, the answer is that it is not assessable against it |
