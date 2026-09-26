# Conventions

Binding rules for anything written into this repository. They exist because each was broken
once, and the cost of each is recorded so a later reader can judge whether the rule still earns
its place.

## 1. Every acronym is expanded on first use

Three layers, and they solve three different problems.

**In the document.** Each document carries a table of the terms it uses, under its title, and
the first appearance of each term in prose links to [`GLOSSARY.md`](GLOSSARY.md) with the
expansion as hover text: `[MTD](GLOSSARY.md "Maximum Tolerable Downtime")`. A Markdown link
title renders as a tooltip, so one mechanism gives both the link and the hover.

**In the glossary.** [`GLOSSARY.md`](GLOSSARY.md) holds every term used anywhere here.

**In the output.** Every skill that produces a report tells whoever runs it to write each
acronym out in full on first use, short form in brackets. This is the layer that matters most
and the one easiest to forget: the skill document is read by somebody working on continuity,
and the report is read by a director, an auditor, or somebody's replacement, who was never
given a glossary and cannot ask for one.

*Cost of breaking it:* WRT appeared seven times in a worked example and "Work Recovery Time"
appeared nowhere in the repository.

### What not to link

Do not link inside tables, headings or code. Do not link a term that is part of a citation
string: `NIST SP 800-34 Rev. 1` reads as one reference and breaking it into two links makes it
harder to read, not easier. Link first use in prose, once per document.

## 2. This repository cites nothing outside itself

Every path resolves inside this repository. Every fact a reader needs is written here. No
outbound URLs, no other repository named, no cross-repository paths.

Duplicate rather than link. A skill that sends its reader elsewhere has assumed the reader can
get there, and the reader is frequently a model with no filesystem working from a document
somebody pasted into a chat window.

*Cost of breaking it:* a worked example cited an architecture by file path, those files lived in
a different repository, and anyone following them found nothing.

## 3. No skill executes anything

No interpreter, no shell, no script. Where a machine genuinely has to answer, the skill names
one read-only command for the operator to run and paste back, says what will be done with the
output first, and still works when the answer is that they cannot run it. What a person reports
is recorded as reported, never as measured.

## 4. Nothing is averaged into a score

**Scope: what a skill reports about somebody else's program.** That is where the damage is done,
and the rule is absolute there.

Report states, not scales. Where a number is genuinely useful, it is read off all-or-nothing
criteria rather than calculated, and it ships with the specific criterion blocking the next
level. Nine criteria of ten met is the lower level, not ninety percent of the higher one.

The pathology is a number that **substitutes** for knowing which specific thing is missing. A
program described as sixty percent mature tells nobody what to do on Monday, and the person who
wrote the sixty percent has been spared naming the gap.

### What the rule does not govern

Our own build status is not an assessment of anybody's program, and reporting how much of this
repository exists is not the thing the rule was written against. A proportion is acceptable
there under one condition: **it appears beside the full itemization rather than in place of it.**
The completeness diagram in the README qualifies, because every node and its state is visible in
the same view, so the figure adds orientation without hiding anything.

A figure quoted away from that itemization has lost the condition that made it acceptable. If
you find yourself writing a percentage with nothing beside it, you are back inside the rule.

## 5. Recovery objectives are keyed to business processes

Not to systems, servers or tiers. Systems are what processes depend on; a tier is derived from
process requirements by a stated mapping and never replaces them.

*Cost of breaking it:* a plan whose objectives hang off infrastructure tiers looks finished and
cannot answer whose work stopped, which is the only question an outage asks.

## 6. The objective and the outcome get different words

An RPO is what the business will accept losing. Data loss is what a mechanism would actually
cost on the day. They are compared, never equated. The same holds for a claimed capability level
against an evidenced one, and for what a person reported against what was measured.

## 7. Nothing is stated of an organization that the organization did not supply

A statement about an organization's systems, business or recovery rests on something its own
people said or wrote, or on a measurement of its own systems. Everything a team brings with it,
its lab, its reference designs, its worked examples, its assumptions, its estimates and the story
of its own process, appears only as a question, as a check to run there, or as a proposal labeled
as the team's. A one-word tag meaning "this applies to them" is split into TRUE THERE, which needs
a source, and CHECK THERE, which needs only to be worded as a check.

[`outgoing-document-gate`](skills/itscm-owner/outgoing-document-gate/SKILL.md) enforces this on
every document before it leaves the team, and every skill whose output goes to the organization
ends by sending its output there.

*Cost of breaking it:* in a rehearsal of this method, 24 statements in documents written for an
organization presented the team's own material as the organization's. The audit of the plan
caught 8. The first of the rest was the opening sentence of a board paper, which stated a
condition of the team's lab as the condition of the company.
