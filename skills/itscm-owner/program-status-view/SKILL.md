---
name: program-status-view
description: Turn per-system capability assessments into one Markdown status view for a whole program, showing every system against every dimension of service management as red, yellow or green by distance from a declared target level. Colors by what was evidenced rather than what was claimed, shows unassessed systems rather than omitting them, and lists the blocking criterion under every cell that is not green.
---

# The program status view

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **ITIL** | IT Infrastructure Library |

**One acronym, deliberately.** This is the only instrument here whose output goes straight to a
program office or a director, and a page that needs a glossary is a page that gets skimmed and
misread. Write the output the same way.

One page a program manager can take into a room. Every system in the program, every dimension of
service management, colored by how far it sits from where the program said it needs to be. The
levels come from the [ITIL](../../../GLOSSARY.md "IT Infrastructure Library") 4 capability scale,
by way of the per-system assessments that produced them.

**Program here means the funded unit**: a group of systems with a program office and
accountability, not a single application. That is the scope at which continuity gets funded and
traded off, and it is the scope at which this view is worth drawing.

## What you need before you can draw anything

| Input | Where it comes from |
|---|---|
| One capability assessment per system | `itil-scm-evidence-review`, run per system |
| The list of systems in the program | The program office. Not inferred from the assessments you happen to hold |
| **A declared target capability level** | The program office |

### The target is not optional, and asking for it is half the value

Three colors cannot come from five levels without averaging, and averaging is what this whole
method refuses. They come from **distance to a target**, which means somebody has to say what the
target is.

Most programs have never said. Ask, and if the answer is that nobody has decided, **that is the
first finding and it outranks everything the view would have shown.** Write it at the top:

> This program has not declared a target capability level. Every color below is drawn against an
> assumed target of 3, which nobody has agreed to. The first decision this view needs is not on
> this page.

Then draw it against 3 and say so in every heading. An assumed target is usable for one meeting
and is not a baseline.

**Do not accept "level 5" as a target without pushing once.** Level 5 means the practice is
continually improving itself from its own findings, and a program that has never run a test
cannot get there in a planning horizon. A target two levels above current is a plan; four is a
wish, and it makes every cell red, which tells the room nothing.

## The color rule

Distance from target, on the **evidenced** level:

| | |
|---|---|
| **Green** | At or above target |
| **Yellow** | One level below target |
| **Red** | Two or more levels below target |
| **Grey** | Not assessed, or the assessment declined to score that dimension |

Nothing else determines a color. Not the number of criteria met, not how good the documents
looked, not how close the dimension felt.

### Color by evidenced, label with both

Every cell carries two numbers, claimed then evidenced, and takes its color from the second.

A cell reading `4 / 1` colored red is a dimension whose documentation supports level 4 and whose
evidence supports level 1. That is the most common real state and the one a single number hides.
It is also the most useful thing on the page: **the gap between the two numbers is untested
risk**, and a program manager reading a wall of `4 / 1` is looking at a program that has written
a great deal and proven none of it.

Where nothing has been tested, evidenced is 1 across every dimension that depends on proof. Do
not soften that. Put the word **unproven** in the header with the date of the last test that
demonstrated anything, or `NEVER`.

### Grey is not a mild color

An unassessed system is the most dangerous cell on the page, because it is the one nobody is
arguing about. It has no level, no blocking criterion, and no owner looking at it.

**Never omit a system because you have no assessment for it.** A program view that silently
covers eight of eleven systems tells a room the program is in better shape than it is, and the
three missing ones are usually missing for a reason.

## The output

Markdown. One file. A program manager should be able to paste it into a wiki or a slide and have
it render.

### Header

```
PROGRAM CONTINUITY STATUS
Program: <name>              Systems in scope: <n>        Assessed: <n>
Target capability level: <n>  <declared by whom, or ASSUMED, NOT AGREED>
Drawn: <date>                From assessments dated: <range>

PROVEN OR UNPROVEN
  <one word>.  Last test that demonstrated anything: <date, or NEVER>

Colors are distance from the target level, on what was evidenced rather than
what the documentation claims. Each cell reads claimed / evidenced.
```

### The matrix

Rows are systems, columns are the four dimensions of service management. Draw it as a
Mermaid flowchart with one band per system,
each band running left to right, so it renders anywhere Markdown does.

```
flowchart TD
    classDef green fill:#e4f2e9,stroke:#1b7f3b,stroke-width:2px,color:#123
    classDef yellow fill:#fdf3d6,stroke:#b58600,stroke-width:2px,color:#321
    classDef red fill:#f7dede,stroke:#c62828,stroke-width:2px,color:#411
    classDef grey fill:#eceef0,stroke:#8791a0,stroke-width:2px,color:#444

    subgraph SYS1["<system name>"]
        direction LR
        A1(["People<br/>4 / 1"]) ~~~ A2(["Info and tech<br/>3 / 3"]) ~~~ A3(["Suppliers<br/>2 / 2"]) ~~~ A4(["Value streams<br/>4 / 1"])
    end

    subgraph SYS2["<system name>"]
        direction LR
        B1(["People<br/>not assessed"]) ~~~ B2(["Info and tech<br/>3 / 1"]) ~~~ B3(["Suppliers<br/>1 / 1"]) ~~~ B4(["Value streams<br/>2 / 2"])
    end

    class A2,A3 green
    class A1,A4,B2,B3 red
    class B4 yellow
    class B1 grey
```

One band per system, in the program's own order rather than sorted by score. A view sorted worst
first reads as a ranking of teams, and the argument that follows is about the sort rather than
about the gaps.

### Under the matrix, the part people act on

```
WHERE THE GAPS ARE

<system> · <dimension>            evidenced <n>, target <n>
  Blocking criterion: <verbatim from the assessment>
  What would close it: <workshop | test | writing>, and who has to be in the room
  ...

NOT ASSESSED
  <system> · <dimension>     <why: not provided, unreadable, declined to score>
  What to send: <the document that would settle it>

WHAT THE PROGRAM HAS NOT DECIDED
  <the target level, if assumed>
  <any contention between systems that no one has resolved>
```

The blocking criterion is quoted verbatim from the assessment, never paraphrased. A paraphrase
loses the thing that makes it actionable, which is that it names one specific missing fact.

## What this view must not do

**Do not roll the program up to a single level.** Somebody will ask for one. The answer is the
lowest evidenced level across every system and dimension, stated as that, with which cell set it.
A program is not two and a half levels mature, and a mean across eleven systems hides the one
that will fail.

**Do not average across systems or dimensions.** Four yellows are not one green.

**Do not color by claimed.** It is the flattering number and it is the one the program already
believes. Coloring by it produces a page that agrees with the room and changes nothing.

**Do not omit a system, a dimension, or an unassessed cell.** Completeness is the only reason
this page is more useful than the individual assessments.

**Do not invent a target.** An assumed target is labeled in the header and in every heading, or
it becomes a baseline by the third time somebody sees the page.

## Spell out every acronym in what you produce

This page is read by somebody who was not in the room: a director, a program office, an auditor.
Write the first use of every acronym in full, with the short form in brackets after it, and use
the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of the
skill needs them; they are expanded in the output because a reader of the page was never given a
glossary and cannot ask for one.

## What this skill does not do

It does not assess anything. Every level on the page comes from an assessment run per system, and
this skill draws what those found. If a level here disagrees with the assessment it came from,
the assessment is right and this page has a transcription error.

It does not produce the roadmap. The blocking criteria it surfaces are the input to that.

It does not resolve contention between systems. Where two systems in the program contend for the
same resource, recovery capacity or people, that is a separate analysis and a funding decision,
and this page notes that it exists rather than settling it.
