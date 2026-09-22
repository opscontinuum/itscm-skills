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

Report states, not scales. Where a number is genuinely useful, it is read off all-or-nothing
criteria rather than calculated, and it ships with the specific criterion blocking the next
level. Nine criteria of ten met is the lower level, not ninety percent of the higher one.

## 5. Recovery objectives are keyed to business processes

Not to systems, servers or tiers. Systems are what processes depend on; a tier is derived from
process requirements by a stated mapping and never replaces them.

*Cost of breaking it:* a plan whose objectives hang off infrastructure tiers looks finished and
cannot answer whose work stopped, which is the only question an outage asks.

## 6. The objective and the outcome get different words

An RPO is what the business will accept losing. Data loss is what a mechanism would actually
cost on the day. They are compared, never equated. The same holds for a claimed capability level
against an evidenced one, and for what a person reported against what was measured.
