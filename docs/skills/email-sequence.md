---
description: Create email sequences that nurture relationships, drive action, and move people toward conversion. Covers sequence types, timing, copy guidelines, and automation strategies.
title: email-sequence
---

# email-sequence

Create email sequences that nurture relationships, drive action, and move people toward conversion. Covers sequence types, timing, copy guidelines, and automation strategies.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing funnel |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Creates lifecycle and nurture email campaigns — welcome sequences, onboarding drips, re-engagement flows, and segmentation logic.

## How you ask

- “Create a welcome email sequence for new subscribers”
- “Design a 5-email nurture drip campaign for trial users”
- “Write a re-engagement email sequence for churned customers”
- “Build an onboarding email sequence with optimized timing”

## Inputs

- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set

## Outputs

- email-copy (markdown)
- email-sequence (markdown)
- email-sequence-brief (markdown)
- email-templates (markdown)
- {scope.marketing.email}/email-sequence-brief-{name}.md
- {scope.marketing.email}/email-sequence-{name}.md
- {scope.marketing.email}/email-templates-{category}.md
- {scope.marketing.email}/email-{sequence}-{number}.md

