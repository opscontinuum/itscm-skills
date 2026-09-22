# itscm-skills

Skills for IT service continuity work: auditing contingency plans against the
templates and standards that govern them, and assessing where a continuity
program actually stands.

A skill here is a self-contained instruction document. It carries the reference
data it needs inside itself, because the model that runs it will not have the
generator source, the template file, or a network connection to fetch either.

## Skills

| Skill | What it does |
|---|---|
| [`itscm-program-assessment`](skills/itscm-program-assessment/) | Interview an organization to find out what its continuity program actually contains, then produce a one month, three month and one year roadmap. Assumes none of the opscontinuum tooling is installed in the environment being assessed. |
| [`iscp-completeness`](skills/iscp-completeness/) | Audit an Information System Contingency Plan against FedRAMP SSP Appendix G ISCP Template v5.0 and NIST SP 800-34 Rev. 1 Appendix B. Reports what is missing, what is present but unfilled, and what is present and answered. |

`itscm-program-assessment` is the entry point. It calls `iscp-completeness` when
the organization has a plan to audit, and works without it when they do not.

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
