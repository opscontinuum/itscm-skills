# itscm-skills

A continuity program you can run by hand.

These are instruction documents for working out what happens when a system stops, how long the
business can stand it, and what to recover first. They need no software. A word processor, a
spreadsheet and the right people in a room will do.

## Find your way in

Three people have to do different things here, and doing somebody else's part is the most
common way this goes wrong.

### You own a business process

Somebody has asked you how long your work can be down. You are the only person who can answer
that, and this section is short because your part is short.

You will be asked what stops when the system stops, what it costs by the hour, and at what
point the consequences change shape. Answer in your own words. If you find yourself describing
servers, you have drifted into somebody else's job.

Three things to hold on to:

You set the maximum tolerable downtime. Not IT, not the vendor, not whoever wrote the last
plan. If the only people in the room are technical, stop the session. A recovery target set by
IT is IT deciding what it is allowed to fail at.

Answer for the worst week, not an average one. Continuity is bought for period close, the
payroll run and the day the bank file cuts. It is almost always specified against a quiet
Tuesday.

Your numbers are a proposal until you sign them. An objective nobody signed cannot be missed,
because nobody promised it.

Read [`bia-workshop`](skills/bia-workshop/) if you want to know what the session will ask
before you walk into it.

### You own a system and have to produce a plan

You are running this. The order matters, because each step feeds the next and doing them out of
order is how plans end up describing infrastructure instead of the business.

1. Find out what already exists.
   [`itscm-program-assessment`](skills/itscm-program-assessment/) asks eight questions about
   your organization and produces a one month, three month and one year roadmap. Start here
   even when you are sure the answer is "nothing", because that produces a three item roadmap
   rather than a forty item one.
2. If a plan already exists, test it twice.
   [`iscp-completeness`](skills/iscp-completeness/) asks whether the document is intact against
   the standard that governs it. [`iscp-sufficiency`](skills/iscp-sufficiency/) asks whether
   anything can be built from what it contains. A plan can pass either and fail the other.
3. Collect the data.
   [`worksheets/iscp-data-collection.xlsx`](worksheets/) has a tab for each thing a plan needs.
   Fill it in the order the tabs are numbered.
4. Run the session that produces the numbers.
   [`bia-workshop`](skills/bia-workshop/) is half a day with the business, and it is where the
   recovery objectives come from.
5. Write the plan.
   [`iscp-from-worksheet`](skills/iscp-from-worksheet/) takes the filled workbook and produces
   the document, refusing to write any section the data does not support.

One warning, because it is the thing most likely to sink you. Tab 7 of the workbook records
which components each business process depends on. Every standard template leaves it out, so
almost everybody skips it, and without it there is no route from "payroll matters most" to
"restore the database first". A plan missing that tab can look finished and still not say what
to fix first.

### You run the infrastructure

Your part is to say what the system can actually do, and to keep that separate from what the
business needs it to do.

You own the recovery time that is technically achievable, the data loss the replication
actually permits, the inventory of components, and which components each process depends on.
That last one usually only exists in your head, and writing it down is the single most useful
thing you can contribute.

You do not set the maximum tolerable downtime. If you are the only person available when that
question comes up, say so and stop rather than filling it in. A requirement copied from a
capability destroys the only comparison worth having, because the plan can then never tell
anyone the architecture is inadequate.

When the business asks for something the architecture cannot deliver, the answer is a tracked,
owned, dated gap item, which NIST calls a Plan of Action and Milestone. It is not a quietly
relaxed target. Writing the achievable number into the requirement makes the gap invisible and
guarantees nobody funds closing it.

[`iscp-sufficiency`](skills/iscp-sufficiency/) is the one to read if you have inherited a plan
and want to know whether it can actually drive anything.

## The skills

| Skill | What it does |
|---|---|
| [`itscm-program-assessment`](skills/itscm-program-assessment/) | Interview an organization to find out what its continuity program actually contains, then produce a one month, three month and one year roadmap. Assumes none of the opscontinuum tooling is installed. |
| [`bia-workshop`](skills/bia-workshop/) | Facilitate the Business Impact Analysis that becomes ISCP Appendix L, in the order NIST states it. Keeps recovery objectives keyed to business processes rather than to systems or tiers. |
| [`iscp-completeness`](skills/iscp-completeness/) | Audit a plan against FedRAMP SSP Appendix G v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports what is missing, what is present but unfilled, and what is present and answered. Also asks whether the plan carries a fact sheet for whoever meets an incident first. |
| [`iscp-sufficiency`](skills/iscp-sufficiency/) | Decide whether a plan carries enough data to build a program from it. A field is required only when a named downstream artifact provably cannot be produced without it. |
| [`iscp-from-worksheet`](skills/iscp-from-worksheet/) | Turn a filled data-collection workbook into a plan, after checking the data can support one. Validates the joins between tabs rather than the presence of cells. |

`itscm-program-assessment` is the entry point for an organization. `bia-workshop` is the entry
point for a session with the business.

The three document skills answer different questions about the same file and should not be
collapsed into one. Whether the document is intact, whether a program can be derived from it,
and what the organization has in people and cadence are three findings with three different
remedies.

## The workbook

[`worksheets/iscp-data-collection.xlsx`](worksheets/) collects everything a plan needs across
thirteen tabs, ordered so each one feeds the next. Regenerate it with
`worksheets/build_workbook.py`; that script runs here, never at the reader.

The dropdowns are fed by the tabs already filled in. Processes entered on tab 2 and resources
on tab 6 become the only permitted values wherever they are referenced later, so an objective
cannot be recorded against a process nobody named and a dependency cannot point at a component
that does not exist. The spreadsheet enforces that, rather than a reviewer noticing three
months later.

Tab 7 records which resources each process depends on. No standard template prompts for it and
none forbids it, and NIST's third BIA step, identifying recovery priorities for system
resources, cannot be performed without it. The mapping is a prerequisite of a required step
rather than an addition to the method.

## The keying rule

A recovery objective belongs to a business process. Not to a system, a server or a tier.

Systems are what processes depend on. A system tier, where one exists, is derived from process
requirements by a stated mapping, and never replaces them.

This is the failure a completeness audit cannot see. A plan whose objectives hang off
infrastructure tiers looks finished: every heading present, every table filled, real numbers
carefully argued. It just cannot answer the question an outage asks, which is whose work has
stopped and for how long. A tier is a property of infrastructure. Only a business process has a
maximum tolerable downtime.

Competent people break this rule constantly, because an infrastructure team naturally states
objectives against what it owns, and because tooling that builds a register of systems invites
hanging the numbers on the system row.

## Everything here runs with no interpreter

No skill in this repository executes anything. The reader may be a web based agent with no
filesystem and no interpreter, working from a document somebody pasted into a chat window.
Every skill has to be useful under exactly those conditions.

Some questions do need a machine to answer. A skill here asks the operator to run one command
and paste the result back, under four rules: name the exact command, keep it read only, say
what you will do with the output first, and still work when the answer is "I cannot run that".

That last rule is the one that matters. What somebody tells you is not what you measured, and
the report says which it was.

## This does not replace the plugin path

Anything picoagent does is a plugin. That architecture is unchanged.

The two paths carry the same method to different places. A plugin runs inside the tooling,
reads real systems and writes into a generated document. These skills are what an organization
uses when it cannot run any of that. Where both exist for one job, the plugin is authoritative
about mechanics and the skill is authoritative about judgment. Neither is a degraded copy.

## Every requirement starts unmet

A requirement gets a verdict or it gets `NOT ASSESSED`, and `NOT ASSESSED` is reported rather
than counted as a pass. A checker that quietly omits what it could not evaluate produces a
number that reads as completeness and is not.

The assessment skill uses four states instead: `Established`, `Asserted`, `Unknown` and
`Absent`. Those are four different facts with four different remedies, not four points on a
scale, and nothing here averages them into a percentage. A program described as sixty percent
mature tells nobody what to do on Monday.

## Provenance

Reference data in `iscp-completeness` was transcribed from:

- FedRAMP SSP Appendix G: Information System Contingency Plan (ISCP) Template, version 5.0,
  dated 12/06/2024. Downloaded 2026-09-02 from
  `https://www.fedramp.gov/resources/templates/SSP-Appendix-G-Information-System-Contingency-Plan-(ISCP)-Template.docx`,
  HTTP 200, 153865 bytes, md5 `298f6b1392ee21b1cded5164c2523b86`.
- NIST SP 800-34 Rev. 1, Appendix B, "Sample Business Impact Analysis (BIA) and BIA Template",
  pages B-1 to B-4, May 2010 (errata 2010-11-11).

Both are public documents published by their issuing bodies.
