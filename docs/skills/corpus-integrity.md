---
description: 'Layer 3 of the readiness family. bob-doctor checks the *environment*, vault-preflight checks the *context*, and this checks the corpus: whether every generated artefact still agrees with the sources it was generated from, and whether those sources are complete enough to ship.'
title: corpus-integrity
---

# corpus-integrity

Layer 3 of the readiness family. bob-doctor checks the *environment*, vault-preflight checks the *context*, and this checks the corpus: whether every generated artefact still agrees with the sources it was generated from, and whether those sources are complete enough to ship.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Keeps derived vault artefacts consistent with their sources and asserts the source-completeness invariants no generator checks.

## How you ask

- “Corpus check”
- “Is everything in sync”
- “Check for drift”

## Inputs

- report — Also emit a report to {company.qms.corpus-integrity}/reports/
- force — Rebuild all targets regardless of state
- request — User request and source context for source invariants only
- request — User request and source context for record baseline

## Outputs

- Current corpus state recorded as the new baseline.
- Input/output hash baseline, rewritten after a rebuild. The rebuilt targets themselves are declared by the skills that own them.
- OPS note written only with --report; a partial --only run refuses to write one.
- accept-result (markdown)
- assert-only-result (markdown)
- build-result (markdown)
- check-result (markdown)
- conversation
- {company.qms.corpus-integrity}/manifest.json
- {company.qms.corpus-integrity}/reports/corpus-integrity-{YYYY-MM-DD}.md

