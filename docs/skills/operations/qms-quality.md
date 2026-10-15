---
description: 'Quality skill covering the full deliverable QA lifecycle in six routes: configure standards, create rubrics, score outputs, run bounded review loops, and compare outputs against reference templates.'
title: qms-quality
---

# qms-quality

Quality skill covering the full deliverable QA lifecycle in six routes: configure standards, create rubrics, score outputs, run bounded review loops, and compare outputs against reference templates.

- **Area:** Operations
- **Category:** qms
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Quality validation and QA orchestration for any work output.

## How you ask

- “Run a QA self-review on this proposal before I send it”
- “Score this deliverable against the quality rubric”
- “Compare my output against the reference template and show me the gaps”

## Inputs

- scope — Work type the standards govern
- thresholds — Pass, revise, and fail score bands
- business_process — Process the rubric scores
- criteria — Criteria with weights; derived from the process when omitted
- artifact — Deliverable to score
- rubric — Rubric to score it against
- fresh_context — Set true when invoked from a playbook quality gate — scoring context receives rubric, gate conditions, and artifact paths only
- artifact — Deliverable to sanity-check before deeper review
- output_path — Path to the file or inline content to validate
- rubric_hint — Optional rubric name — otherwise resolved from skill-quality-mapping
- output_path — Path to the file to validate
- template_path — Path to the reference template or prior version

## Outputs

- Delta checklist per iteration, gaps closed/remaining, terminal state
- Per-iteration scoring, revision checklists, terminal state (PASS/FAIL/ESCALATED)
- quality-config (markdown)
- quality-rubric (markdown)
- quick-check-verdict (markdown)
- validation-report (markdown)
- {company.qms.qa-reports}/quick-check-{descriptor}.md
- {company.qms.qa-reports}/validation-{descriptor}.md
- {company.qms.qa-reports}/{skill-name}_qa_{YYYY-MM-DD}.md
- {company.qms.rubrics}/{output-type}.md
- {company.qms.standards}

