---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: corpus-integrity — ThirdBrain BOB skill
  description: 'Layer 3 of the readiness family. bob-doctor checks the *environment*, vault-preflight checks the *context*, and this checks the corpus: whether every generated '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: corpus-integrity
catLabel: utilities
area: foundational
desc: Keeps derived vault artefacts consistent with their sources and asserts the source-completeness invariants no generator checks.
summary: 'Layer 3 of the readiness family. bob-doctor checks the *environment*, vault-preflight checks the *context*, and this checks the corpus: whether every generated artefact still agrees with the sources it was generated from, and whether those sources are complete enough to ship.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- report — Also emit a report to {company.qms.corpus-integrity}/reports/
- force — Rebuild all targets regardless of state
- request — User request and source context for source invariants only
- request — User request and source context for record baseline
outputs:
- Current corpus state recorded as the new baseline.
- Input/output hash baseline, rewritten after a rebuild. The rebuilt targets themselves are declared by the skills that own them.
- OPS note written only with --report; a partial --only run refuses to write one.
- accept-result (markdown)
- assert-only-result (markdown)
- build-result (markdown)
- check-result (markdown)
- conversation
- '{company.qms.corpus-integrity}/manifest.json'
- '{company.qms.corpus-integrity}/reports/corpus-integrity-{YYYY-MM-DD}.md'
prompts:
- Corpus check
- Is everything in sync
- Check for drift
---
