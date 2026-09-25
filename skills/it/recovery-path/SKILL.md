---
name: recovery-path
description: For IT staff who must state what a service's recovery path can actually do; walks read-only from the names customers use to the standby's data and produces an evidenced account of which copy answers now, what the switch is and whether it has ever moved, what a move between copies would lose, what a recovery needs that the running system does not, what each machine takes down with it, and the questions only the business can answer.
---

# Walking the recovery path

**Terms used here.** The full list is [`GLOSSARY.md`](../../../GLOSSARY.md).

| | |
|---|---|
| **IT** | information technology |
| **DR** | disaster recovery |
| **DNS** | Domain Name System |
| **UTC** | Coordinated Universal Time |
| **MTD** | Maximum Tolerable Downtime |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |


You are [IT](../../../GLOSSARY.md "information technology"), and you are walking one service's
recovery path from the outside in: from the name a customer types to the data the standby would
serve them. All of it is read-only. You change nothing, including the thing you most want to
test.

The output is evidence, not a verdict. It contains no recovery objective: no
[MTD](../../../GLOSSARY.md "Maximum Tolerable Downtime"),
[RTO](../../../GLOSSARY.md "Recovery Time Objective") or
[RPO](../../../GLOSSARY.md "Recovery Point Objective"), because those belong to the business.
Whether the path is good enough is a comparison between what you measure here and what the
business set, and the product owner makes that comparison. Your job is to make sure what they
compare against is true.

## Why this walk exists

A running system can pass every health check while none of its recovery works. Both copies
answer, the dashboards are green, and the path that would move customers from one copy to the
other has never carried a request.

When this method was first run against real infrastructure, every defect the written skills
missed lay on that path: how many of each component ran, what the standby was and what kept it
in step, and what the switch did. The walk found a public name serving the copy everybody called
the standby. It found a switch nobody had moved in weeks, which checked nothing about the health
of its target and could not reach the other copy at all. It found the
[DR](../../../GLOSSARY.md "disaster recovery") copy better protected than production, and nobody
had asked why.

Walking inward from the customer finds what customers depend on, including the parts nobody
owns. Walking outward from the infrastructure finds only what IT already knows it has.

## What you decide, and what you refuse

**You decide which vantage points to measure from**, and you record, for every network fact,
which one it came from. A name that resolves from your desk may not resolve from a customer's
phone, and a network fact without its vantage point cannot be checked or repeated.

**You decide nothing about which copy is production.** You put it to the business as a
question, in Step 9, with the evidence beside it.

You refuse five things, and you say so in the output rather than silently leaving them out.

| You refuse | Why |
|---|---|
| Any MTD, RTO or RPO value, whether set, suggested or back-filled | They are the business's numbers. An objective set by IT is IT deciding what it is allowed to fail at |
| The words RTO and RPO for anything you measured | What you measure is **restoration time** and **data loss**. The objective and the outcome get different words, so nobody can copy a capability into an objective column |
| Deciding which copy is production | It decides whose data counts and where customers are sent. Those are business consequences |
| Flipping or editing the switch to test it | A flip moves real customers. Done as a test, it is an unapproved failover with nobody watching the data. Exercising the switch belongs to `recovery-drill`, within bounds the owners agree in advance |
| Calling any copy a working DR site without a timed switch in both directions | A copy that has never received customers through the switch is a second copy, not a recovery site. The return trip is required because a move you cannot reverse is a migration, and the return is where diverged data surfaces |

## Before you start

You need three things, and missing any of them is a finding rather than a reason to stop.

1. Read-only access to each copy's platform, or an operator who will run named read-only
   commands and paste back the output. A walk in which every fact is NOT MEASURED, each with the
   command that would settle it, is still a map of what nobody knows.
2. The copies the organization believes exist, and what it calls each one. Record each label
   and where it came from: a person, a document, or a label on the object itself. Throughout
   this skill, "primary" and "standby" mean the roles those labels assign. They are never your
   judgment.
3. The names the business believes customers use. If nobody can say, that is the first
   question for the business, and you still resolve every name you can find.

### What counts as read-only

| Allowed | Not allowed |
|---|---|
| Listing and describing objects, and reading their status and change history | Any edit, apply, set, patch, scale, restart, delete or rollout on any object, the switch included |
| Name lookups against any resolver | Changing a record, a hosts file or a resolver setting to see what happens |
| A request that reads a page or a health endpoint, a handful of times | A request that writes: adding to a cart, submitting a form, placing an order, signing in as a customer |
| Reading the certificate a server presents | Requesting, renewing or revoking a certificate |
| A count of records, named in advance and run by the operator | Any query that writes or takes a lock, and any load test |

A command run inside a production container is not read-only by default. It executes code in
production. Run one only when the operator agrees the specific command reads and nothing else,
and record in the register that it ran inside the container.

## The evidence standard

This standard binds every IT skill. It is written out in full here because a skill is read on
its own.

### Five labels

Every fact in the output carries exactly one.

| Label | Means |
|---|---|
| MEASURED | Read from a running system by a command shown in the register, with its output |
| ESTIMATE | A number calculated from measured inputs by a stated method. Says what the method leaves out |
| INFERENCE | A conclusion drawn from measured facts that could be wrong. Says what would confirm it |
| UPSTREAM DESIGN | How a product or protocol is documented to behave. Not observed here |
| NOT MEASURED | Not obtained. Says why, and names the one read-only command that would settle it |

A fact with no label is read as MEASURED by whoever picks it up next, which is how a guess
becomes evidence two documents later.

**What a person tells you is NOT MEASURED.** Record it as reported, in their words, with their
name and role: "NOT MEASURED. Reported by the network lead: the switch was last moved in the
spring." It may be true. It is still not a measurement, and the gap between what people report
and what the systems show is often the finding.

Output that an operator ran and pasted back is MEASURED, and the register names the operator as
the person who ran it.

### The register

Every MEASURED fact points to an entry in an evidence register at the end of the document. Each
entry carries:

- a number that includes the document's name, such as `recovery-path E7`, never a bare `E7`.
  Several documents in one engagement each start at E1, and a bare number cited elsewhere
  points at the wrong one
- the time it was run, in [UTC](../../../GLOSSARY.md "Coordinated Universal Time")
- the vantage point, for anything that crossed a network
- who ran it: you, or the named operator
- the exact command, as run
- the relevant output, trimmed to the lines relied on, with the trim stated. If a script
  reshaped or summarized the output, say so and say what it did

### Time

UTC throughout, written as `YYYY-MM-DDTHH:MM:SSZ`. Platforms, logs and annotations print local
offsets. Convert them, and say in the register where you converted.

### Dates, and what went stale

Date every measurement. The system keeps changing while you walk it, and a fact measured an
hour before a deployment may be false an hour after it.

After any change you learn of, list which of your facts it made stale: the evidence number,
what changed, and when. That covers a deployment, a restart, a drill, and a hand edit by
somebody else. Do not silently re-measure over the old value. Both readings are evidence, and a
later document that cites the old one needs to be able to see that it was superseded.

### Secrets and personal data

Describe them. Never reproduce them. Record a secret by its name, its type and where it is
stored, not its value. Record a certificate by the names it covers, its issuer and its expiry,
never its private key. Record customer data by field names and a count. When a response you
probed carries personal data, keep only the line that identifies the copy and say the rest was
discarded.

### When a command cannot be run

Name the one read-only command you would ask the operator to run, and say what you will do with
its output before you ask. Then name the fallbacks in the order you would try them, and what
each can and cannot establish. If none can be run, the fact is NOT MEASURED with the command
beside it. That line is useful on its own: it tells the next person exactly what would settle
the question.

Some platforms hide an object's change history unless it is asked for explicitly. A history that
reads empty because it was never requested is not evidence that nothing changed the object.
Check for the option before you write "no change history".

The network facts in this walk can mostly be read with standard tools that exist on any
platform. The rest are the platform's own read-only listing of an object, which you name for the
operator's platform using its list, get or describe verb.

| To establish | A read-only command of this kind |
|---|---|
| Where a name resolves, through a named resolver | `nslookup <name> <resolver>` |
| Which servers are authoritative for a name's zone | `nslookup -type=NS <zone>` |
| What a name returns, with headers, from this vantage point | `curl -sS -D - -o <file> https://<name>/` |
| Whether one target answers for the customer's name | `curl -sS -D - -o /dev/null --resolve <name>:443:<target address> https://<name>/` |
| Which certificate a target presents for the customer's name | `openssl s_client -connect <target address>:443 -servername <name>`, reading subject, issuer and expiry |
| The switch, the instances behind a service, an object's change history, replication status | The platform's own list or describe command for that object, with change history requested |

### Vantage points

A vantage point is where a request starts: which machine, on which network, using which
resolver. Name resolution and reachability both differ by vantage point, so record it for every
network fact.

Use at least two, and make one of them where customers are. For a public service that means
outside the organization's network entirely: a machine on a consumer connection, or a phone off
the office network. For an internal service it is the network the service's users sit on, not
the data center.

| Vantage point | What it shows | What it cannot show |
|---|---|---|
| Where customers are | What customers get: the public answer for each name, the copy they reach, the certificate they see | Anything behind the edge |
| An operator's workstation inside the organization | The internal answer for each name, which often differs from the public one | What customers get. Split name resolution, hosts file entries and local port forwarding all make a workstation misreport it |
| The switch's own position | Whether the switch can reach each of its targets | Anything about customers |
| Inside each copy's platform | Which instances sit behind a service, and what they call | Anything about the path in |

Do not carry a fact from one vantage point to another. A name that resolves only through a hosts
file, or answers only through local port forwarding, is not an entry customers can use, whatever
it does on your screen.

---

## Step 1: the names customers use

Collect every name a customer, partner or dependent system uses to reach the service. Take them
from three places, because each finds names the others miss. Ask the business for the names on
the website, in the app, in emails and in partner contracts. Read the platforms for the host
names in every routing rule and the names on the certificate each entry presents. Read
[DNS](../../../GLOSSARY.md "Domain Name System") for what the organization's zones hold for the
service.

Record where each name came from. A name only the platform knows may be internal and unused. A
name only the business knows may resolve nowhere.

For each name, from each vantage point, record where it resolves and through which resolver.
Then, once per name:

1. Which server is authoritative for it, where that server runs, and who can change the record.
   A name whose authoritative server nobody can identify is a finding, because nobody can move
   that name during an outage.
2. The record's cache lifetime, which is how long resolvers may keep serving the old answer.
   Where the switch is a DNS record, customers move only as fast as their resolvers' caches
   expire, and that time is part of the restoration time.

A name that resolves nowhere you checked is recorded as exactly that, with the vantage points you
checked from. It does not prove customers do not use it. It proves you could not.

When two names each serve a different copy, that is not a problem for you to resolve. It is a
question for the business.

## Step 2: which copy answers now

For each name and each vantage point, establish which copy answered, **without relying on the
application to say so.** Two methods. Use both where you can.

**Follow the address.** Start from the address the name resolved to. Find what owns that address:
a load balancer, a routing layer, an edge service. Find the rule that matches the customer's host
name, and follow it to the service it sends to. Then find the instances behind that service
(pods, tasks, virtual machines) and the machine and site each one runs on. Every hop is a
read-only listing, and every hop goes in the register.

**Read a response marker.** Many services name the instance that served a request, in a response
header or on the page. Send one read-only request, read the marker, and look for that instance
in each copy's instance list. A marker counts only when it names an instance you can find in
exactly one copy. A marker that says "primary", or names a site, is the application's opinion,
set in configuration that may have been copied to both copies unchanged.

Where the two methods disagree, record both and the disagreement. Do not pick one.

If different vantage points reach different copies, that is a finding in its own right. Staff
testing from inside see one copy while customers use another, and every internal check of the
service is checking the wrong one.

## Step 3: the switch

The switch is whatever decides which copy a customer's request reaches. Find it. Do not assume
one exists, and do not assume it is the object somebody named the switch. It may be:

- a DNS record, or a DNS service that rewrites records when a check fails
- a global or site load balancer choosing between backends
- a routing rule on a reverse proxy or an ingress layer
- a service whose backend address was typed in by hand rather than selected
- a network route, or an address announced from one site or the other
- a setting inside client applications or partner systems
- a person who edits one of these during an outage

"There is no switch" is a complete finding. So is "there are two names, one per copy, and
nothing moves customers between them."

Establish each of these, and label every answer.

| Question | What to establish | What counts as evidence |
|---|---|---|
| What it is | The object, the platform it lives on, and the site and machine that platform runs on | A read-only listing of the object |
| What changes it | Every person, role, automation and tool that can write it, and whether any change is automatic | The permissions on the object, and any automation configured to change it |
| When it last changed | The time and the writer of the last change to its target | The object's change history, requested explicitly. For a DNS record, the zone's serial number and its change log where one exists |
| Whether it checks the target's health before sending traffic | What is checked, against which address, how often, how many failures before it acts, and what it does when every target fails | The check's configuration. No configuration means the answer is NO |
| Whether it can reach each target | Address range, route, host name and certificate, for every target, including the one it is not using today | Read-only requests from the switch's position, or NOT MEASURED |
| Whether it has ever been flipped | Every recorded change of target: when, by whom, and why | Change history, drill records, incident records. A flip somebody remembers is NOT MEASURED |

### The health question

This is the one nobody asks. A switch with no health check keeps sending customers to a copy that
is down. A switch whose only check is that a port answers keeps sending them to a copy that
returns an error on every page. Write down exactly what the check proves, in the form "it
confirms that ... and nothing else", and write NO when there is no check.

### Reachability, in four parts

Answer all four for every target, including the copy the switch is not using today.

| Part | The question | How it fails while looking fine |
|---|---|---|
| Address range | Can the switch route to the target's address at all? | The address sits inside another site's private range, reachable only from inside that site |
| Route | Is there a path from the switch to the target, through every firewall between them? | The path exists from an operator's workstation and not from where the switch runs |
| Host name | Does the target answer for the name customers use? | It answers quickly, with a redirect to another name, a different site, or a loop back through the switch |
| Certificate | Does the target present a certificate valid for the customer's name, from an issuer customers' devices trust, and when does it expire? | It presents a certificate for its own name, or one only the organization's own machines trust |

Test what you can with read-only requests sent to the target's address carrying the customer's
name. Record which position you tested from. A target that answers your workstation may not
answer the switch, and a target the switch cannot reach is not a target.

### Where the switch lives

Where the switch lives matters as much as what it does. A switch hosted in one of the sites it
switches between is lost with that site, and so is the ability to move customers away from it.
Carry it into Step 8.

### Flipped, and timed both ways

A switch that has never been flipped is a design, not a capability.

**Only a timed switch in both directions makes a copy a working DR site.** That means customers
were moved to the standby and back, each move timed from the decision to the moment customers
were served by the target copy as seen from outside, in an approved drill or a real incident.
This skill never produces that timing. It reads the record, from `recovery-drill` or from an
incident review, and cites it. Where no such record exists, the output says "no copy is a working
DR site on this evidence", in those words.

## Step 4: compare each pair of copies

Do this for every pair: a primary and its standby, or two copies whose relation nobody can
state.

### How each copy is deployed

Establish whether the standby is deployed **from the same source, by the same controller** as
the primary. Record, for each copy, the source (repository, path, revision) and the controller
that applies it. Where the platform records which tool last wrote each object, read it. Hand
tools in that record mean a copy maintained by hand.

A copy maintained by hand drifts. List where the copies differ today, field by field. A summary
such as "minor configuration drift" hides exactly the field that matters. Where the primary is
deployed from a source and the standby is not, record the INFERENCE that the next change to the
source reaches the primary and not the standby, and say what would confirm it.

### How each copy is provisioned

Compare them property by property.

| Property | What to compare |
|---|---|
| Instances | How many of each component run in each copy |
| Machines | Which machines those instances run on, and whether several instances share one |
| Capacity | Processor, memory and storage, and any quota that caps how far each copy could grow |
| Data persistence | For each data store: what survives a process restart, and what survives the instance being replaced |
| Data protection | For each data store: what copies it, how often, and where the copy lives |
| Versions | What each copy runs, by exact build identifier rather than by tag. A tag can point at different builds in each copy |
| Supporting services | What each copy calls: identity, telemetry, payment or other partners, and whether each copy calls its own or a shared one |
| Entry | The name each copy answers to, its certificate, and the certificate's issuer |

**Flag every property where the standby is weaker or stronger than the primary.** Both go to
the business as questions, and neither is yours to explain away.

A weaker standby may not carry the primary's load, or may lose data the primary would have kept.
Ask whether that is accepted, and say what it would cost on the day.

A stronger standby needs the same question, and it is the one that gets skipped. Sometimes the
better protected copy is the one customers actually use, and the labels are wrong. Sometimes
somebody improved the standby and never the primary. Sometimes it is intended. You do not know
which, and a guess written into the report will be read as the answer. Do not file a stronger
standby under drift. Drift says how it happened. The business needs to know what it means: the
copy with more protection may not be the copy their customers depend on.

## Step 5: data between the copies

Cover every place the service keeps state a customer would notice losing: databases, caches that
hold sessions or shopping carts, queues, uploaded files. A store nobody lists is a store nobody
copies.

For each store, establish whether its data is copied between the copies, by what mechanism, in
which direction, and whether a write waits for the copy.

**If it is copied, measure the lag.** Read the replication status at both ends as close to the
same moment as you can, and record the lag with its time and vantage point. One reading is one
reading. Lag moves with load, and the reading that matters is the worst one during the business's
busiest hour, so say when yours was taken. Then say how the lag is watched continuously, or that
nothing watches it. A lag nobody watches is checked for the first time during a failover, which
is the moment it is too late to fix.

**If it is not copied, state the data loss of a move, in both directions.** Everything written
in the copy being left since the copies diverged is absent from the copy being entered. Count it
where a read-only count can be taken in both copies in the same minute. State the return
direction as well, because moving back loses whatever customers wrote in the standby while they
were there.

The word is "data loss". It is never RPO. The business compares your data loss with its objective.
You do not.

## Step 6: what is needed to recover but not to run

A running system does not use most of what it would take to rebuild it. Its instances already
hold their images, their secrets and their certificates. Its servers already resolved their names
and authenticated. Nothing reads the source repository until something has to be rebuilt. None
of these can fail a health check, so the first time anybody learns one is missing is during a
recovery.

For each item, answer two questions: **where does it live, and does it survive the loss of the
primary?**

**A recovery source that lives inside the thing that failed is not a recovery source.**

| Item | Why a running system hides its absence | What to establish |
|---|---|---|
| The source repository a deployment controller rebuilds from | Nothing reads it while everything runs | Where it is hosted, and who and what can read it |
| The deployment controller, and its own configuration | It is only needed to create things, not to keep them running | Where the controller would be installed from, and whether the definitions telling it what to deploy are themselves in the repository |
| Container image registries | Running instances already hold their images | Where each image is pulled from, whether it is pinned to an exact build, and whether the registry lives at the primary |
| Secrets, and the vault or key that unseals them | Running instances already hold their secrets | Where each secret is kept, what unseals the store, and where that key lives |
| Bootstrap credentials | They are used once, at build time | The first credential a rebuild needs: to the repository, the registry, the cloud account or the hypervisor. Where it is kept, and who can reach it |
| Directory services and DNS | Running servers have already resolved and authenticated | Which directory and which name servers a rebuilt server must reach before it can join or resolve anything, and where they run |
| Certificate authorities and issued certificates | Running entries already hold issued certificates | For each certificate, the authority that issues it, where that authority's signing key lives, and whether issuing a new one depends on the entry that is down |
| License servers and license terms | Running software already checked its license at start | Whether the terms allow the standby to run production, where the license server lives, and whether the license is tied to a specific machine |
| Per-site configuration | Nobody notices an address that points at a working site | Whether each copy carries its own values for addresses, connection strings and callbacks, so recovered workloads stop pointing at the failed site, and whether those values are declared in the source |
| Backups, their catalog, and their encryption keys | A backup is only read during a restore | Where the backup, its catalog and its key each live. A backup on the disk it protects fails with that disk |
| Infrastructure definitions, and their state | They are only used to build | Where the definitions that build hosts and networks live, and where their state is kept |
| The recovery procedure, and access to run it | Nobody opens it until the night it matters | Where the runbook is stored, and whether the people who would run it can reach the systems when the primary is gone, including any gateway they sign in through |
| The monitoring that shows recovery worked | It is watching the primary, which is fine until the primary is gone | Where it runs. Monitoring that lives at the primary means recovering blind |

An item survives only if everything needed to use it also survives. A repository hosted
elsewhere, readable only with a credential stored at the primary, does not survive. Follow each
item until you reach something that lives outside the primary, or something that does not.

A location can be a person. "In one engineer's password manager" and "in the head of the person
who built it" are locations, and they go in the table as written.

Answer "survives loss of the primary" with Yes, No or NOT MEASURED. "Probably" is NOT MEASURED.

## Step 7: when recovery is a rebuild

Many recoveries do not fail over state. They rebuild it. A DR orchestration step installs a
deployment controller at the standby site, the controller pulls declared state from a
repository, and it creates whatever the repository describes. GitOps, where a controller applies whatever a
repository declares, is the common form.

**In a rebuild, anything running that is not declared in the source does not come back.** The gap
between what is declared and what is running is a count of what a recovery would silently lose.

Measure it in three parts, and list every item behind each count.

| Part | What it holds | What a rebuild does with it |
|---|---|---|
| Running, and not declared | Every object in scope that no source declares: a permission applied by hand, a setting patched in place, a job somebody added | Loses it |
| Running, and different from declared | Every field the source does not pin. If the source does not set how many instances run, the controller never corrected the running count, because the field was never its business | Replaces today's value with the default |
| Declared, and not running | Anything somebody stopped deliberately, or that is broken | Brings it back |

**Do not take these counts from the controller's own status.** A controller reports drift only in
what it manages. An object it never knew about does not show up as drift. It does not show up at
all. Count from a read-only listing of everything running in scope, compared with the source
rendered at the revision the controller tracks.

Check the controller's own configuration. The definitions that tell a controller what to deploy
must themselves be in the repository. A freshly installed controller with no application
definitions deploys nothing, and reports itself healthy while doing it.

Declared state carries no data. A rebuild brings every data store back empty unless the recovery
includes a restore from a copy that survived. Name each store and what would fill it.

A copy maintained by hand has no source at all. Rebuilding it means rebuilding from memory.

Report each count beside its full list. A count on its own stands in for knowing which things
are missing, and the list is what somebody fixes.

## Step 8: shared fate

For each machine, each site, and each shared service on the path, record what its loss takes
down with it. Include the machine the switch runs on, the authoritative name servers, the
repository host, the identity service, shared storage, and the links between sites.

Record two kinds of loss separately, because they fail on different days. What stops running is
visible at once. What stops being recoverable is invisible until a recovery is attempted. The
loss of a repository host stops nothing running and makes a rebuild impossible, and that row
matters more than it looks.

Look for three patterns in particular:

- an entry that shares a machine with the copy it serves, so the name and the copy fall together
- the switch living in one of the sites it switches between
- a recovery source on the same machine or disk as what it protects

Where you cannot tell what shares a machine, as with a virtual machine whose host you cannot see
or a managed service whose zones you cannot see, record NOT MEASURED and name who could answer.

## Step 9: the questions for the business

Every conflict between what things are called and what they do, and every property you flagged,
goes to the business as a question. IT does not answer it, propose an answer, or recommend one.
A recommendation from IT on which copy is production reads as the answer, and the business stops
thinking about it.

Ask each of these where the walk raised it.

1. Which names do customers use? Give the evidence of which copy each name serves.
2. Which copy is production? Give what each label says and where the switch points.
3. Is the standby meant to be a standby, or a second copy in its own right?
4. For each property where the standby is weaker or stronger than the primary: is that intended,
   and what does it mean for the customers of each copy?
5. For each data store that is not copied between the copies: a move loses the data stated in
   Step 5, in each direction. Is that acceptable? This asks the business to compare an outcome
   with its own objective. It does not ask anyone to set an objective here.
6. For a standby that is not a working DR site on this evidence: is it acceptable as the place
   recovery would go?

Each question carries the evidence numbers it rests on and the role it is put to. A question
nobody has answered stays in the output as unanswered. It is never closed by default.

---

## The report

```
RECOVERY PATH
Service:  <the name the business uses for it>
Walked:   <start> to <end>, Coordinated Universal Time (UTC)
By:       <name, role>                   Changed during the walk: nothing
Copies:   <each copy, where it runs, what it is called, and the source of that label>

This document states no Maximum Tolerable Downtime (MTD), Recovery Time Objective (RTO) or
Recovery Point Objective (RPO). It states restoration time and data loss where they were
measured. It does not decide which copy is production, it did not flip or edit the switch,
and it calls no copy a working disaster recovery (DR) site without a timed switch in both
directions.

THE ANSWERS FIRST
  1  <one sentence>                                        <label>   <evidence numbers>
  ...
  Working DR site:  <copy, with the drill or incident that timed a switch both ways>
                    or NO COPY IS A WORKING DR SITE ON THIS EVIDENCE

VANTAGE POINTS
  V1  <machine, network, resolver>                         <inside or outside the organization>
  ...

ENTRY NAMES
  Name  Source of name  From  Resolves to  Authoritative server, where it runs  Cache lifetime
        Label  Evidence

WHICH COPY ANSWERS NOW
  Name  From  Copy that answered  Address chain  Response marker  At (UTC)  Label  Evidence

THE SWITCH
  What it is               <object, platform, site and machine>   or NO SWITCH
  What changes it          <every person, role, automation and tool that can write it>
  Last changed             <time, writer>   or NOT MEASURED, and why
  Checks target health     "it confirms that ... and nothing else"   or NO
  When every target fails  <what it does>
  Ever flipped             <each recorded flip: time, direction, by whom>   or NO RECORD OF A FLIP
  Timed both ways          <drill or incident, date, time each way>   or NEVER

  Target  Address range  Route  Answers for the name  Certificate for the name  Tested from
          Label  Evidence

COPIES COMPARED                                           (one block per pair)
  <copy A> and <copy B>
  Deployed from            <A: source, revision, controller>   <B: same, or BY HAND>
  Property   <copy A>   <copy B>   B against A: weaker / equal / stronger   Evidence
  Differences today        <field by field>
  Flagged                  <each weaker or stronger property>   Question B<n>

DATA BETWEEN THE COPIES
  Store  Copied?  Mechanism and direction  Lag, at UTC, from where  Watched continuously?
         Label  Evidence
  Data loss of a move, where not copied
    <A> to <B>   <what is lost, counted where possible, at UTC>
    <B> to <A>   <what is lost on the return>

NEEDED TO RECOVER, NOT TO RUN
  Item  What it is here  Where it lives  Survives loss of the primary?  Depends on
        Without it, recovery does what  Label  Evidence

WHEN RECOVERY IS A REBUILD          (if recovery never rebuilds, say so and why)
  Declared source                    <repository, path, revision the controller tracks>
  Controller's own definitions       DECLARED or NOT DECLARED
  Running, not declared              <n>   <every item>           lost on rebuild
  Running, differs from declared     <n>   <every item and field>
  Declared, not running              <n>   <every item>
  Data a rebuild brings back empty   <every store, and what would fill it>

SHARED FATE
  If this is lost   Stops running   Stops being recoverable   Evidence

QUESTIONS FOR THE BUSINESS
  B1  <question>                       Put to: <role>   Rests on: <evidence numbers>
  ...

NOT MEASURED
  Fact   Why   The one read-only command to ask for   Fallbacks, in order

STALE
  <evidence number>   <what changed>   <when, UTC>

EVIDENCE REGISTER
  recovery-path E1   <time, UTC>   From: <vantage point>   Run by: <you, or the named operator>
  <exact command>
  <relevant output, with any trim or reshaping stated>
```

Lead with the answers, one sentence each, so a reader who stops after the first screen still
knows which copy customers reach, whether the switch works, and whether anything is a working DR
site. The questions for the business come before the register, because they are what somebody
acts on.

Hand the report to the product owner, who sets it beside the business's objectives. The
needed-to-recover table asks the same question as the "Survives loss of the primary site?"
column on tab 11 of [`worksheets/iscp-data-collection.xlsx`](../../../worksheets/), for things
that are not backups. The workbook has no tab for them, so the table travels in this report.

## Spell out every acronym in what you produce

The report this skill produces is read by somebody who was not in the room: a director, a
business owner, an auditor, somebody's replacement. Write the first use of every acronym in
full, with the short form in brackets after it, and use the short form thereafter.

> Maximum Tolerable Downtime (MTD) is four hours for payroll.

This applies to the output, not to this document. Terms are defined here because a reader of
the skill needs them; they are expanded in the output because a reader of the report was never
given a glossary and cannot ask for one.

An acronym nobody expands is a reader quietly deciding the document was not written for them.

## Checking your own output

- Every fact carries one of the five labels, and every MEASURED fact has a register entry.
- Every evidence number carries the document's name.
- Every time is in UTC.
- Every network fact names its vantage point, and at least one vantage point is where customers
  are.
- No MTD, RTO or RPO value appears anywhere, and the words RTO and RPO appear only in the
  statement that this document sets none.
- Nothing says which copy is production.
- No copy is called a working DR site without a cited, timed switch in both directions.
- The switch's health question is answered, even when the answer is NO.
- Every target of the switch has all four reachability parts answered or marked NOT MEASURED.
- Every property where the standby is weaker or stronger than the primary appears as a question
  to the business.
- Every data store has either a measured lag or a stated data loss for a move, in both
  directions.
- Every item needed to recover has a location and a survives answer, and each was followed
  through whatever it needs until that reached something outside the primary or something lost
  with it.
- Every count in the rebuild section sits beside its full list.
- No secret value, private key or personal data appears anywhere, the register included.
- Every change you learned of has its stale facts listed.

## What this skill does not do

It does not exercise anything. Flipping the switch, restoring a copy and timing a move in both
directions belong to `recovery-drill` in this folder, which changes things only within bounds
the system owner and the affected process owners agree in advance. This skill reads the record
of a drill and cites it, and the drill reads this skill's output before scoping a failover.

It does not set or judge objectives. The business sets them in `bia-workshop`. The product owner
compares them with what this walk measured, and a shortfall becomes a tracked gap rather than a
relaxed objective.

It does not inventory everything the service runs, or map every dependency to the work it
supports. It covers the path between the customer and each copy's data, and what a move or a
rebuild between copies needs. The rest of IT's side is listed in this folder's README, and most
of it is not written yet.

It does not decide which copy is production, which name customers use, or whether any gap is
acceptable. It asks.
