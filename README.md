# itscm-skills

Skills for IT service continuity work: auditing contingency plans against the
templates and standards that govern them, and assessing where a continuity
program actually stands.

A skill here is a self-contained instruction document. It carries the reference
data it needs inside itself, because the model that runs it will not have the
generator source, the template file, or a network connection to fetch either.

## Everything here runs with no interpreter

**No skill in this repository executes anything.** No Python, no shell, no
script, no binary. The reader may be a web-based agent with no filesystem and no
interpreter, working from a document somebody pasted into a chat window. Every
skill must be useful under exactly those conditions, and a skill that needs to
run something to do its job does not belong here.

This is a stronger rule than self-containment, and it is the line between this
repository and the plugin path below.

### When a skill needs something it cannot work out

Some questions genuinely need a machine to answer: what is actually running,
what a cluster reports, what a replication lag currently is. A skill here asks
the operator to run one command and paste the result back. Four rules:

1. **Name the exact command.** Not "check your cluster." The literal text to run.
2. **It must be read-only.** Nothing here asks anybody to change a system.
3. **Say what you will do with the output**, before they run it.
4. **The skill must still work when the answer is "I cannot run that."** Degrade
   to asking a person, and record what they tell you as reported rather than
   measured.

That fourth rule is the one that matters. A fact somebody told you is not a fact
you measured, and the report says which it was. A skill that stalls because
nobody could run a command has made the tooling mandatory through the back door.

## This does not replace the plugin path

Anything picoagent does is a plugin. That is the architecture and this repository
does not change it.

The two paths carry the same doctrine to different places. A plugin runs inside
the tooling, reads real systems, and writes into a generated document. A skill
here is what an organization uses when it cannot run any of that: the same
method, performed by people, against a document they already have. Where both
exist for one job, the plugin is authoritative about the mechanics and the skill
is authoritative about the judgment, and neither is a degraded copy of the
other.

## Skills

| Skill | What it does |
|---|---|
| [`itscm-program-assessment`](skills/itscm-program-assessment/) | Interview an organization to find out what its continuity program actually contains, then produce a one month, three month and one year roadmap. Assumes none of the opscontinuum tooling is installed in the environment being assessed. |
| [`iscp-from-worksheet`](skills/iscp-from-worksheet/) | Take a filled data-collection workbook and turn it into a plan, after checking that the data can support one. Validates the joins between tabs rather than the presence of cells, and writes nothing it was not given. |
| [`iscp-sufficiency`](skills/iscp-sufficiency/) | Decide whether a plan carries enough data to actually build a program from it. Judges by derivability: a field is required only when a named downstream artifact provably cannot be produced without it. Distinguishes absent, blank template, keyed to the wrong unit, and agreed by nobody, because those need four different remedies. |
| [`iscp-completeness`](skills/iscp-completeness/) | Audit an Information System Contingency Plan against FedRAMP SSP Appendix G ISCP Template v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports what is missing, what is present but unfilled, and what is present and answered. Also asks whether the plan carries a fact sheet for whoever meets an incident first, and traces each field back to the section that already holds it. |

`itscm-program-assessment` is the entry point. It calls `iscp-completeness` when
the organization has a plan to audit, and works without it when they do not.

The three document skills answer three different questions about the same file
and should not be collapsed. `iscp-completeness` asks whether the document is
intact against the authority that governs it. `iscp-sufficiency` asks whether a
program can be derived from its content. `itscm-program-assessment` asks what the
organization has, which is a question about people and cadence rather than about
any document. A plan can pass any one of these and fail the others.

## The workbook

[`worksheets/iscp-data-collection.xlsx`](worksheets/) collects everything a plan needs, across
thirteen tabs, in the order each one feeds the next. `worksheets/build_workbook.py` regenerates
it; the build tool runs here, never at the reader.

Two things in it are doing real work.

**The dropdowns are fed by the tabs the reader already filled.** Processes entered on tab 2 and
resources on tab 6 become the only permitted values on the tabs that reference them. An
objective cannot be recorded against a process nobody named, and a dependency cannot point at a
component that does not exist. Referential integrity, enforced by the spreadsheet rather than by
a reviewer noticing later.

**Tab 7 exists because no standard template asks for it.** It records which resources each
process depends on. Without that link, per-process recovery objectives and a resource inventory
sit on either side of a gap, and no recovery order can be derived from either one: there is no
way to get from "payroll matters most" to "therefore restore the database first". It is the most
common reason a complete-looking plan cannot answer what to fix first, and the workbook puts it
on its own tab with a warning rather than leaving it to be inferred.

Fill it, then hand it to `iscp-from-worksheet`.

## The rule these skills follow

Every requirement starts unmet. A requirement gets a verdict or it gets
`NOT ASSESSED`, and `NOT ASSESSED` is reported rather than counted as a pass.
A checker that silently omits what it could not evaluate produces a score that
reads as completeness and is not.

The same rule shapes the assessment skill, where the states are `Established`,
`Asserted`, `Unknown` and `Absent`. Those are four different facts with four
different remedies, not four points on a scale, and neither skill averages them
into a number. A program described as "sixty percent mature" tells nobody what
to do on Monday.

## Provenance

The reference data in `iscp-completeness` was transcribed from:

- **FedRAMP SSP Appendix G: Information System Contingency Plan (ISCP) Template,
  version 5.0, dated 12/06/2024.** Downloaded 2026-09-02 from
  `https://www.fedramp.gov/resources/templates/SSP-Appendix-G-Information-System-Contingency-Plan-(ISCP)-Template.docx`,
  HTTP 200, 153865 bytes, md5 `298f6b1392ee21b1cded5164c2523b86`.
- **NIST SP 800-34 Rev. 1, Appendix B**, "Sample Business Impact Analysis (BIA)
  and BIA Template", pages B-1 to B-4, May 2010 (errata 2010-11-11).

Both are public documents published by their issuing bodies.
