---
description: Drafts executive memos, board updates, and stakeholder communications using 6-pager and SCQA structures. Use when user mentions 'executive memo,' 'board update,' 'stakeholder email,' 'SCQA,' or '6-pager.'
title: exec-comms
---

# exec-comms

Drafts executive memos, board updates, and stakeholder communications using 6-pager and SCQA structures. Use when user mentions 'executive memo,' 'board update,' 'stakeholder email,' 'SCQA,' or '6-pager.'

- **Area:** People
- **Category:** human resources
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder

Drafts executive memos, board updates, and stakeholder communications using 6-pager and SCQA structures.

## How you ask

- “Draft an executive memo about our Q1 results”
- “Write a board update for our quarterly meeting”
- “Create a stakeholder email using SCQA structure”
- “Draft a 6-pager for our new product initiative”

## Inputs

- decision — The decision to be made or recorded
- options — Options considered, with the trade-off for each
- audience — Who reads it and what they control
- period — Period the update covers
- metrics — KPI values for the period; when omitted, read definitions and source information from the KPI registry ({company.management}/KPI-REGISTRY.md), then use verified readings for the requested period. Request missing readings rather than substituting thresholds or inventing values.
- stakeholders — People or groups to be aligned, and what each currently believes
- position — The position being argued for

## Outputs

- Use a filesystem-safe message slug; if the proposed path exists, choose a non-colliding suffix and preserve the existing file.
- {company.knowledge-base.product}/exec-comms-board-update-{YYYY-MM-DD}-{message-slug}.md
- {company.knowledge-base.product}/exec-comms-decision-memo-{YYYY-MM-DD}-{message-slug}.md
- {company.knowledge-base.product}/exec-comms-stakeholder-brief-{YYYY-MM-DD}-{message-slug}.md

