---
description: Diagnose why problems happened and define what needs to change so they stop happening.
title: root-cause-analysis
---

# root-cause-analysis

Diagnose why problems happened and define what needs to change so they stop happening.

- **Area:** Operations
- **Category:** operations
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Diagnoses root causes of customer issues, service failures, and recurring problems using a 5-Whys framework, fishbone diagrams, and pattern matching.

## How you ask

- “Why something went wrong”
- “Recurring issues”
- “Systemic vs one-off”

## Inputs

- problem-statement — Brief description of the issue: what happened, who was affected, when
- problem-statement — Description of the current issue
- issue-records — Reference to vault issue records, support logs, or incident history if available
- root-cause — Root cause identified from five-whys or pattern-check output
- systemic-flag — Whether the issue was classified as systemic

## Outputs

- corrective-action-plan (markdown)
- five-whys-analysis (markdown)
- pattern-assessment (markdown)
- {company.qms.root}/rca-{YYYY-MM-DD}-corrective-action.md
- {company.qms.root}/rca-{YYYY-MM-DD}-pattern-check.md
- {company.qms.root}/rca-{YYYY-MM-DD}.md

