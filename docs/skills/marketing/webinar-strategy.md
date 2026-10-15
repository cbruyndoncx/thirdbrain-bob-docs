---
description: Plan, promote, and execute webinars that acquire customers by embedding product value into educational content delivered to borrowed audiences.
title: webinar-strategy
---

# webinar-strategy

Plan, promote, and execute webinars that acquire customers by embedding product value into educational content delivered to borrowed audiences.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Plans and executes webinar-based customer acquisition strategies.

## How you ask

- “Plan a webinar series for our product launch”
- “Create a guest speaker outreach template for our webinar”
- “Design a webinar promotion campaign with email sequences”
- “Build a webinar outline for our AI automation workshop”

## Inputs

- topic — Webinar topic or buyer pain point to address
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- icp — loaded from your vault context
- marketing-context — loaded from your vault context

## Outputs

- webinar-strategy (markdown)
- {scope.marketing}/webinars/webinar-strategy-{YYYY-MM-DD}.md

