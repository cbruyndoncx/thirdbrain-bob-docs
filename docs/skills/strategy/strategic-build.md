---
description: Decide whether a proposed build is leverage, neutral, or overhead before the team commits.
title: strategic-build
---

# strategic-build

Decide whether a proposed build is leverage, neutral, or overhead before the team commits.

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Product Manager

Evaluate proposed features or initiatives with LNO classification, strategic review, and pre-mortem analysis.

## How you ask

- “Should we build this feature? Give me a strategic review”
- “Classify this initiative using the LNO framework”
- “Run a pre-mortem on our proposed product direction”
- “Is this real product work or product theater?”

## Inputs

- initiative — Work to classify as strategic or operational
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- initiative — Initiative under review
- evidence — Data supporting or undermining the current direction
- initiative — Initiative to pre-mortem
- horizon — How far ahead to imagine the failure

## Outputs

- build-classification (markdown)
- pre-mortem-analysis (markdown)
- strategic-review (markdown)
- {scope.knowledge-base.product}/strategic-build-classification-{work-item-slug}-{YYYY-MM-DD}.md
- {scope.knowledge-base.product}/strategic-build-pre-mortem-{work-item-slug}-{YYYY-MM-DD}.md
- {scope.knowledge-base.product}/strategic-build-review-{work-item-slug}-{YYYY-MM-DD}.md

