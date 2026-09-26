---
name: outgoing-document-gate
description: Run on every document before it leaves the team for the organization it describes, including plans, reports, board papers, roadmaps, status pages, summaries, slides and messages that state a finding. Holds any statement about the organization's systems, business or recovery that the organization did not supply and that was not measured on its own systems. That is the first of six tests; the other five keep measurements honest, objectives keyed to processes, gap items from relaxing an objective or claiming a closure they do not deliver, dependency maps reaching shared services, and words from saying more than the evidence does. Reports findings; never rewrites the document.
---

# The outgoing document gate

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **POA&M** | Plan of Action and Milestones |

A team that writes continuity documents for an organization it does not belong to works from two
kinds of material. One is what the organization's people told it, wrote down for it, or let it
measure on the organization's own systems. The other is everything the team brought with it: its
lab, its reference designs, its worked examples, its assumptions about the industry, its
estimates, and the story of its own process. The second kind is useful, and it is how a team
arrives with good questions. Stated as the organization's, it is wrong, and the reader has no way
to tell which sentence is which.

This gate reads a document the way its reader will, and holds every sentence that states the
team's own material as the organization's. That is Test 1. Tests 2 to 6 are the other checks every
document in this method has to pass. It reports. The author fixes, and the gate runs again on the new version.

**Why it exists.** In a rehearsal of this method, 24 statements in documents written for an
organization presented the team's own material as the organization's. The independent audit of
the plan caught 8 of them. Nearly all of the rest sat in the layers written for readers who would
never open the evidence: summaries, status lines, a roadmap, and a board paper whose opening
sentence stated a condition of the team's lab as the condition of the company. Underneath, the
evidence was labeled correctly. The summaries dropped the labels.

## When to run it

On every document before it leaves the team, whoever it is going to: the organization's staff,
its executives or board, its auditors, regulators or suppliers. That includes summaries,
executive summaries, slide decks, status pages, roadmaps, and any email or chat message that
states a finding.

Run it on the document exactly as it will be sent. A document that changes after it passed has not
passed; run the gate again on the new version.

**The team** means the people applying this method who are not the organization: an assessment
team, a consultant, a vendor, or an internal group writing about a part of the organization it does
not run. **The organization** means whoever the document is about.

## What you need

| Input | Why |
|---|---|
| The document, as it will be sent | The gate checks what the reader will read, not a draft of it |
| Its sources | Session records with each speaker's name and role, the document inventory and extracted facts with their locations, measurement registers. A statement is traced to one of these or it is held |
| Who it is for | A board paper and a technical appendix fail in the same way but are read differently. The finding's order follows the reader |

If no sources are provided, say so at the top of the report and hold every statement about the
organization that does not carry its source inline. An untraceable statement is not a supplied one.

If nobody says who the document is for, gate it for the organization's decision makers, the most
exposed readers, and say so in the report.

## Where a statement about the organization may come from

A statement is **about the organization** when it describes the organization's systems, data,
processes, people, roles, business, calendar, obligations, history, current state, risks or
capability, or says what will happen, cannot happen, or has never happened to it.

Only two sources can support one.

| Source | Means | What the document must be able to point to |
|---|---|---|
| SUPPLIED | Said or written by the organization's own people, or read from the organization's own records | Who said it (name and role), or which record and where in it, and when |
| MEASURED THERE | Read from the organization's own running systems, with its consent | The measurement: the command or method, its output, when, and who ran it |

What a person at the organization reports is SUPPLIED, not MEASURED THERE. It may well be true. A
report and a measurement disagreeing is often the finding, so keep them apart.

**SUPPLIED means as supplied.** A paraphrase that changes the meaning, drops a qualifier, or
rates something differently from how the person rated it is the team's words, not theirs. Hold it
under Test 1, class our process.

**Derived from supplied facts is allowed** when the method is shown: a count of the processes they
named, a date computed from their calendar rules, a difference between two of their figures. Say
it was derived and from what. A derived figure that uses anything the team brought, such as an
estimate or a lab timing, is not derived from supplied facts. A derivation that does not say so is
a Test 2 finding.

**Absence is a statement too.** "No backup exists", "it has never been tested", "in no
inventory" and "nobody is named" say something about the organization and need a source. "We
found none", "not located by us" and "unknown to us" say what the team knows, and pass.

### Five kinds of material that are not from the organization

Everything else is the team's own. It falls into five classes, and knowing them is how you find
them, because each leaks in its own way.

| Class | What it is | How it usually gives itself away |
|---|---|---|
| Our environment | Anything observed in the team's lab, test systems or model, at another client, or in an earlier engagement | Specific names, counts or failures that nobody at the organization gave you; "no copy exists", "nothing is backed up", "one node" |
| Our designs and reference material | The team's own proposed designs, target architectures and plans; reference designs, worked examples and templates; a vendor's documentation of how a product is meant to behave | "as documented", "the design", "the target", "the topology", an unbuilt design written in the present tense, a product's documented behavior stated as the organization's configuration |
| Assumption | Anything assumed, illustrative, typical of an industry, or invented so an example would work, including the team's own picture of the organization before its people confirmed it: a brief, a statement of work, a sales conversation | "typically", "as a retailer", a peak season, calendar, dollar figure or head count nobody at the organization stated; the organization's platforms, regions or systems named before discovery |
| Our process | What the team did or did not do, recorded as a property of the organization; team roles named after the organization's own functions | "nobody is named in any recovery role" when nobody was asked; "the plan was written in a day"; "IT measured", "the architect's target", "the owner's direction" when those are the team's people, which the organization's reader takes to mean its own |
| Estimate stated as fact | A designed, calculated or engineering-judgment figure written as what will, cannot or always happens | "cannot meet", "will take 40 minutes", "no ordering reaches", "is not achievable" about something never built or run |

### How the team's material may appear

The team's material is welcome in an outgoing document in a form that does not state it of the
organization. There are four such forms, and nothing else.

| Form | What it looks like |
|---|---|
| A question to the organization | "Does anything outside the primary region hold a copy of the repository your deployments are rebuilt from?" |
| A check the team will run there | "CHECK THERE: whether the deployment controller's own definitions are kept in the repository." |
| The team's proposal, labeled as the team's | "Our candidate design, not built or tested. Its recovery times are our estimates; a timed drill would confirm or replace them." |
| Method material, in a section that says so | "How we will assess this", "What we measured in our own lab to prepare", written as the team's, never as the organization's |

The label travels with the statement, and **the label's own words say whose material it is**:
"measured in our lab", "our design, not built", "our reference design", "our estimate". A bare
MEASURED, DOCUMENTED or DESIGNED, or a meaning set only in a legend or a document-wide default,
does not travel: lifted into a summary or quoted in a meeting, the organization's reader takes it
as theirs. A heading, table cell, status line, summary bullet or decision request that drops the
label has turned the team's material back into a statement about the organization, and is held.

A question or check must not presuppose the team's material either. "When Phoenix takes over, who
signs off?" states that a Phoenix exists. Ask without the premise, or state the premise as the
team's.

### One tag, split in two

Teams often mark findings with a single word meaning "this applies to them": "transfers",
"relevant", "applies". It carries two meanings, "this is true of the organization" and "this is a
pattern worth checking there", and a reader downstream picks the first. The gate does not accept
the single word. Every such finding becomes one of these:

| Tag | Needs |
|---|---|
| TRUE THERE | A SUPPLIED or MEASURED THERE source |
| CHECK THERE | Wording as a check or a question. Nothing more |

The bare word is held, and so is a definition of it. A qualified use whose own sentence already
words the check ("carries over as a check: whether their suites share storage") is CHECK THERE in
substance and passes; write the tag anyway next time. A finding about the method rather than the
organization states nothing about the organization, and the tag rule does not apply to it.

## The six tests

Read the document in the order its reader will: the summary layer first, then the body. **The
summary layer** is the title, the first paragraph, anything headed as a summary, overview, answer
or "read this first", status lines, decision requests, diagrams, and the table the document
presents as its answer (a status table, a scorecard, a decision table). Other tables are body.
**A finding in the summary layer counts even when the body underneath states the same fact
correctly.** The summary is the part that gets read, and it is where labels get dropped.

**One finding per distinct statement.** A statement that fails more than one test is one finding,
filed under the first test it fails and naming the others. The same statement repeated is one
finding with every other place listed under "also at"; list each repeat in the summary layer
separately, because each is read on its own. A premise that runs through the whole document, such
as a platform or region the organization never named, is one finding where it is first stated,
with "also at" pointing to where it is relied on.

Tests 3, 4 and 5 apply only where the document contains objectives, gap items or a dependency
map. Where it does not, write "not applicable" and the reason. Never skip one silently.

### Test 1: provenance

For each statement about the organization: is it SUPPLIED or MEASURED THERE, and can you point to
where? If it is neither, name which of the five classes it came from and hold it.

Look hardest at statements of the organization's **current state** ("today there is no..."), its
**history** ("has never been tested"), its **risk** ("if the region is lost there is no recovery"),
and what **cannot** happen. These are the sentences a reader carries out of the room, and they are
the ones most often built from the team's lab or the team's design.

### Test 2: kind of fact

Nothing is presented as measured unless it was measured on the organization's systems. A reported
fact stays reported, an estimate stays an estimate, and a vendor's documented behavior stays
documented behavior. Watch the plain present tense: "the replica lags ten minutes" states a
measurement, and needs one.

### Test 3: keying

A tier number on a system reads to the organization as its priority, so it needs the supplied
mapping from process objectives too, even in a document with no objectives of its own.

Every recovery objective ([MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime"), [RTO](../../../GLOSSARY.md "Recovery Time Objective"), [RPO](../../../GLOSSARY.md "Recovery Point Objective")) is keyed to a business process, never to a system,
server or tier. A tier may appear as something derived from process objectives by a stated
mapping, and never in place of them.

### Test 4: tracked gaps

Where the document carries gap items, a [POA&M](../../../GLOSSARY.md "Plan of Action and Milestones") or anything like one:

- No item changes an objective's number. An objective the design cannot meet stays as the business
  set it, and the shortfall is the item.
- An item marked closed is closed only by what its evidence delivers today. A design that is not
  built closes nothing today. It may close the item later, and it may say so, but only in the mark
  itself ("closes when built and drilled"), and never in a summary row that drops the condition.
- Each closure test would fail if the objective were still unmet. A test that passes whether or
  not the objective is met closes nothing.
- Residual risk is assigned to someone the organization said can hold that level of risk.
- An item about a dependency, such as a shared service, names the objective it serves. Its
  closure test may prove the dependency is fixed, and the item says which objective still owes a
  timed test.
- An option offered to the organization's decision makers to change their own objective is theirs
  to take, and may appear, with what it gives up. The team never recommends it.

### Test 5: the dependency map

Where the document maps processes, systems, tiers or recovery steps to what they depend on, the map reaches the shared services a
recovery needs as well as the applications: directory and authentication, name resolution,
certificates, the source repository a rebuild pulls from, the image registry, and secrets and
keys. A map that stops at the applications calls a tier recoverable when it is not.

### Test 6: words

- Objective and outcome get different words: an RPO is what the business accepts losing; data loss
  is what a mechanism would cost. An RTO is what the business requires; restoration time is what a
  drill or a walk measured. A claimed level and an evidenced level are compared, never equated, and
  neither is a single drill's restoration time or data loss a general statement of the
  organization's capability.
- Readiness time is not restoration time. A component reporting ready is not a customer recovered,
  and the gap between the two, where it was measured, travels with the figure rather than being
  rounded away.
- The one-word "applies to them" tag is split, as above.
- "Cannot", "will", "always" and "never" are attached only to what was supplied or measured, never
  to an estimate or a design. Said of the organization, that is Test 1, estimate stated as fact;
  this test catches it when said of the team's own design.
- An assurance about the document itself, such as "nothing here rests on our lab" or "no
  laboratory fact on any page", is checked like any other statement. A false one tells the reader
  to trust everything else, so it is a finding, usually in the summary layer.
- Every acronym is written out in full at its first use, short form in brackets. A terms table
  placed before the first use counts. Citation handles such as a document code are not acronyms.

## What you report

```
OUTGOING DOCUMENT GATE
Document       <title, version, date>
For            <who will read it>
Sources given  <each source, or NONE>
Rehearsal     <no | yes, and the first line says so | yes, and the first line does not say so>
Result         HOLD | RELEASE
Findings       <n>, of which <n> in the summary layer

FINDINGS, in the order the reader meets them
  G1  <where: section and line, or table and cell>
      "<the words, quoted exactly and briefly>"
      Test <n>, <name>          Class <one of the five, for Test 1>
      Why: <what it states of the organization, and where it actually came from>
      Also fails: <other tests, or none>        Also at: <other places, or none>
      Fix: <see the fixes below>
  G2  ...

TESTS
  1 Provenance      <n>
  2 Kind of fact    <n>
  3 Keying          <n, or not applicable and why>
  4 Tracked gaps    <n, or not applicable and why>
  5 Dependency map  <n, or not applicable and why>
  6 Words           <n>

GATED BY  <name and role, or the tool and the person who ran it>   ON  <date>
VERSION   <the version or date of the document gated>
```

| Test | Fixes to offer |
|---|---|
| 1 Provenance | Cite the source; ask it as a question; make it a check; label it as ours in its own words; remove |
| 2 Kind of fact | Relabel it as what it is: reported, estimated, documented behavior, measured in our lab |
| 3 Keying | Key it to the business process; state the supplied mapping from process to tier; remove the tier |
| 4 Tracked gaps | Put the objective back as supplied; withdraw the closure or state its condition in the mark; reword the closure test so it fails while the objective is unmet; give the risk to someone who can hold it |
| 5 Dependency map | Add the missing shared service, or mark it NOT MEASURED with who could answer |
| 6 Words | Use the outcome word; split the tag; drop the absolute; write the acronym out |

**RELEASE only with no findings.** There is no partial release and no release with conditions. A
document with one open finding is held, and it says NOT RELEASED on its first line until the gate
passes it.

Give the fix, not a rewrite. The author knows which source exists, which question to ask, and
whether the statement should go at all.

## What you must not do

- **Rewrite the document.** Report, and let the author fix it. A gate that edits what it gates has
  nobody checking the edit.
- **Release a document because the evidence underneath is labeled correctly.** The reader does not
  read the evidence.
- **Accept "everyone knows this about them", "it is typical", or "we will confirm it later" as a
  source.** Each of those is a question to ask them.
- **Treat silence as supply.** A draft the organization did not object to has not supplied
  anything in it.
- **Pass a statement because it is probably true.** Probably true and not supplied is held. It
  becomes a question, and that question is usually worth asking.
- **Count your way to a verdict.** Findings are listed, not scored. Nine clean pages do not
  outweigh a held first sentence.

## In a rehearsal

When a team rehearses this method with people it plays itself, the statements of role-players who
**stand for the organization's own people** count as SUPPLIED inside the rehearsal. Roles that
stand for the team, even when named after one of the organization's functions (IT, an architect, a
product owner writing the plan), are the team, and what they write is the team's. A persona
identified by a letter and a role is enough to cite. In a session record, what the facilitator
writes about the session itself (who attended, what was asked) is the record; anything the
facilitator adds about the organization is the team's.

Every rehearsal document says it is one on its first line. The report records whether it does,
and a missing line is a finding under Test 1, because without it every role-played statement
reads as real.

The gate then tests what matters in a rehearsal: whether the team's lab, its designs and reference
material, its own process or its estimates got into the documents written as the organization's.
Judge each document as if it were about to be sent. That is what rehearsing the gate is for, even
though a rehearsal document is never sent.

Nothing a role-player supplied is true of any real organization. A rehearsal document, or a figure
or example from one, never leaves the rehearsal.

## Spell out every acronym in what you produce

The gate's own report is read by the document's author and, often, by whoever decides whether the
document goes. Write out every acronym in full at its first use, with the short form in
brackets. Do the same for the organization's own abbreviations: quoted from the document, they
still need expanding once.

## What this skill does not do

It does not judge whether a supplied fact is true. The organization is the authority on what it
told you, and whether its systems agree is what measurement is for. A conflict between the two is
a finding for the organization, not a reason for the team to edit.

It does not replace the plan audits. `iscp-completeness` and `iscp-sufficiency` in the
product-owner folder check whether a plan is complete and whether it could support a continuity
program; this gate checks whether what a document states is the organization's to state.

It does not decide whether a document should be sent. It says whether the document, as written,
states anything of the organization that the organization did not supply.
