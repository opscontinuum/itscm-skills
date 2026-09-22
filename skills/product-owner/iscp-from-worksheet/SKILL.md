---
name: iscp-from-worksheet
description: Take a filled ISCP data-collection workbook and turn it into a contingency plan, checking first that the data can actually support one. Validates the joins between tabs rather than only the presence of cells, reports what is missing in the four states that need four different remedies, and writes nothing it was not given.
---

# From a filled workbook to a plan

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **BIA** | Business Impact Analysis |
| **ISCP** | Information System Contingency Plan |


Somebody has filled in the data-collection workbook (`worksheets/iscp-data-collection.xlsx`)
and handed it to you. Your job is to check it, say what it cannot support, and write what it
can.

**In that order.** Writing first and checking afterwards produces a plan with confident empty
sections, which is worse than no plan because it looks finished.

## Reading the workbook, whatever form it arrives in

You cannot run anything. The workbook may reach you as an uploaded spreadsheet you can read
directly, as exported CSV, as tables pasted into the conversation, or as a mixture. Work with
whatever arrived.

If something is unreadable, say which tab and ask for it in another form. Do not proceed with
a tab you could not read and do not infer its contents from the others. A tab you could not
read is `NOT ASSESSED`, which is different from empty, and the distinction survives into your
report.

The tabs, and what each one is for:

| Tab | Carries | Feeds |
|---|---|---|
| 1 System | Identity, owner, impact level, availability commitment | ISCP §1 and §2 |
| 2 Processes | The business work the system carries | Everything below |
| 3 Impact scale | What severe, moderate, minimal mean here | Tab 4 |
| 4 Process impact | What an outage costs each process | BIA §3.1.1 |
| 5 Objectives | MTD, RTO, RPO per process | BIA §3.1.1, ISCP §1.4 |
| 6 Resources | The components | BIA §3.2 |
| 7 Process-Resource | Which components each process needs | **Tab 8, and nothing else can replace it** |
| 8 Priorities | Recovery order | BIA §3.3, ISCP §4.1 |
| 9 Contacts | Who to call | Appendix A |
| 10 Vendors | Outside parties | Appendix B |
| 11 Sites and backups | Alternate sites, what protects the data | §2 tables, Appendix C |
| 12 Approvals | Who agreed | Approvals page, and the committed flag on every objective |

## Part 1: validate, before writing anything

### The joins, which matter more than the cells

A workbook can be full and still incoherent. The dropdowns prevent some of that and not all of
it. Check each join and report coverage as a fraction, never as a yes or no.

1. **Every process on tab 2 has at least one impact rating on tab 4.** A process nobody rated
   is a process nobody thought about. Name the ones missing.
2. **Every process on tab 2 has objectives on tab 5.** This is the join that decides whether a
   recovery order exists. Name every process with no row.
3. **Every impact rating on tab 4 uses a category defined on tab 3.** If a category appears
   that tab 3 does not define, the rating means nothing, because the scale it was measured
   against does not exist.
4. **Every process on tab 2 appears on tab 7 at least once.** A process depending on no
   resource is either wrong or the tab was skipped. In practice it means the tab was skipped.
5. **Every resource on tab 6 appears on tab 7 at least once.** A resource no process needs is
   either not in scope, or something depends on it that nobody wrote down.
6. **Every resource on tab 7 appears on tab 8 with a priority.** An unprioritized resource is
   one nobody decided about, and it will be the one somebody argues over mid-incident.

**If tab 7 is empty, stop and say so before anything else.** No recovery order can be derived
without it, tabs 5 and 6 cannot be connected by any other means, and every priority on tab 8
is then an assertion rather than a derivation. This is the single most common way a full
workbook produces an unusable plan.

### The constraint check

For every row on tab 5: **RTO must be shorter than MTD.** Work still has to be done after a
system is technically available before the business is actually running, and that time comes
out of the MTD.

Where RTO is equal to or greater than MTD, one of the two numbers is wrong. Report the row,
report both numbers, and do not choose for them.

### The commitment check

Tab 5's last column says whether each objective is agreed and signed, proposed only, inherited
from a default, or unknown. Cross-check it against tab 12.

Objectives marked agreed where tab 12 has no signature are **not agreed**. Report them as
proposed, say that the workbook claims otherwise, and say who has not signed. This is not
pedantry: an objective nobody signed cannot be missed, because nobody promised it, and a plan
that presents design targets as commitments will be read as making promises it did not make.

### The four states

Every gap is exactly one of these, and reporting all of them as "missing" sends the reader
down the wrong path three times in four.

| State | What you are looking at | What fixes it |
|---|---|---|
| `ABSENT` | The tab or column is empty | Somebody writes it |
| `TEMPLATE` | Structure present, every cell blank or placeholder | Run the session that collects it |
| `MIS-KEYED` | Real data attached to the wrong unit of analysis | Re-do the analysis against the right unit |
| `UNCOMMITTED` | Real, correct, and nobody with authority signed it | Get the signature |

`MIS-KEYED` survives into a workbook mainly as objectives entered against infrastructure
rather than a process: a row on tab 5 whose process column carries a server name, a tier, an
environment, or a component from tab 6. The dropdown makes this harder and does not make it
impossible, because somebody may have added the infrastructure to tab 2 to get past the
validation. When you see a tab 2 entry that is not business work, say so. It is the most
consequential thing you can catch, because everything downstream looks correct.

## Part 2: what to write, and what to refuse to write

Write only sections the workbook supports. For each section of the plan:

- **Supported.** Write it from the workbook's data.
- **Partly supported.** Write what is there, and mark the gap inline in the plan itself, not
  only in your report. A gap visible only in a covering note is a gap that disappears the
  first time the plan is forwarded.
- **Unsupported.** Write the heading, and under it one sentence naming what is needed and
  which tab it comes from. Never an empty section, never invented content, never a
  placeholder that reads like prose.

**Every sentence you write traces to a cell.** If you cannot point at the cell, do not write
the sentence. The temptation is strongest in the narrative sections, where a plausible
paragraph about recovery philosophy costs nothing to produce and quietly becomes something
the organization believes it decided.

What you derive rather than copy, and how:

| Plan element | Derived from | How |
|---|---|---|
| Recovery priority order | Tabs 5, 6, 7 | Each resource inherits the tightest RTO of any process that lists it as essential on tab 7 |
| Which process set each priority | Tabs 5, 7 | Name it, so the order can be audited rather than trusted |
| Recovery sequence | Tab 8 plus technical dependency | Priority says what may not be sacrificed; technical dependency orders within a priority group |
| Scope RTO | Tab 5 | The tightest RTO across all processes |
| Overall impact rating | Tab 4 | Usually the worst single category, not an average. If the workbook averaged, say so |

**Do not compute an objective from an architecture.** If tab 5 is empty and tab 11 shows
synchronous replication, you know the system's capability and you still do not know the
business's requirement. Writing the capability into the requirement destroys the only
comparison that makes the document worth having.

## Part 3: the report, before the plan

```
WORKBOOK REVIEW
System: <from tab 1>          Collected: <date from tab 1>

CAN THIS WORKBOOK PRODUCE A PLAN?
  <one sentence: yes, yes with named gaps, or no and why>

JOINS
  processes with an impact rating      <n> of <total>
  processes with objectives            <n> of <total>
  processes mapped to resources        <n> of <total>
  resources mapped to a process        <n> of <total>
  resources with a priority            <n> of <total>
  <name every process or resource on the short side of each fraction>

CONSTRAINT VIOLATIONS
  <process>: RTO <x> is not shorter than MTD <y>

COMMITMENT
  objectives agreed and signed         <n> of <total>
  claimed agreed but unsigned on tab 12: <list>

GAPS
  <tab / column>   <state>   <what fixes it>

NOT ASSESSED
  <tab>   <why you could not read it>
```

Lead with the question at the top, answered in one sentence. Everything under it is the
evidence for that answer.

## When the honest answer is that it is too early

A workbook with tab 2 filled and tabs 4, 5 and 7 empty is not a failed submission. It is an
organization that has identified its business processes and has not yet held the session that
values them, which is a normal and common place to be.

Say that, rather than producing a long gap list that reads as a failure notice. What they need
next is a session with the process owners, somebody who can commit the business to a number,
and somebody who knows what the architecture can actually do. All three in the room: any two
of them produce numbers that are either unachievable or unagreed.

The tabs that session fills are 3, 4, 5 and 7. Say that too, because it makes the ask concrete
and about half a day long instead of open-ended.
