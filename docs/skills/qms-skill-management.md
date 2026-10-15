---
description: 'Consolidated skill-corpus QMS toolkit: one skill, three routes covering spec review, promotion certification, and corpus ops.'
title: qms-skill-management
---

# qms-skill-management

Consolidated skill-corpus QMS toolkit: one skill, three routes covering spec review, promotion certification, and corpus ops.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Runs skill QMS reviews, certification, and corpus operations.

## How you ask

- “Spec-review the `humanize-content` skill”
- “Certify this skill for release promotion”
- “Run a full skill QMS audit”
- “Rerun spec reviews for all governed skills”
- “Remediate the weakest skills”
- “Generate a current-state corpus report”

## Inputs

- skill_path — Skill folder name, passed to batch_spec_review.py as --filter (omit for batch mode)
- batch — If true, review all skills under --skills-dir
- skill_path — Path to the skill directory
- cert_threshold — Minimum spec-review score the gate accepts, default 8.0. Raising it blocks skills the standard bar would approve; lowering it is how a deliberate exception is made visible rather than argued in prose.
- mode — One of integrity-check | scorecard-rerun | spec-review-rerun | remediation | auto-optimize | tessl-review | corpus-report

## Outputs

- Approve-or-block verdict with every failing check named. certify_skill.py has no write path.
- Per-mode report or log; actual artifact path depends on --mode (see Route 3 sub-sections).
- Written by the agent for mode `remediation` — per-skill before/after spec score, delta, KEEP/REVERT result and the fix applied, then the tranche summary.
- Written for mode `auto-optimize` by skillsmith's `run_skill_loop.py` — per-skill eval-loop outcome (kept or reverted) for the skills carrying an eval manifest, and the stop reason.
- spec-review-json (json)
- {company.qms.audits}/optimization-log-{YYYY-MM-DD}.md
- {company.qms.audits}/remediation-log-{YYYY-MM-DD}.md
- {company.qms.spec-reviews-individual}/{skill}-{YYYY-MM-DD}.json

