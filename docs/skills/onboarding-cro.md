---
description: Design and optimize post-signup onboarding flows to drive user activation and retention.
title: onboarding-cro
---

# onboarding-cro

Design and optimize post-signup onboarding flows to drive user activation and retention.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing funnel |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config] |
| **Roles** | [Head of Marketing, Product Manager] |

Deep-dive into post-signup onboarding — designs activation flows, creates checklists, analyzes drop-off points, and recommends engagement triggers.

## How you ask

- “Design an onboarding flow for our SaaS product”
- “Create an activation checklist for new users”
- “Analyze drop-off points in our first-run experience”
- “Reduce time-to-value in our user onboarding”

## Inputs

- request — The product and onboarding flow to audit, plus where the user believes activation is being lost.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- activation-event — The activation event already in use, if one is defined. Absent, the audit defines a candidate and labels it as proposed rather than measured.
- funnel-data — Step-by-step funnel export from the product analytics tool. Absent, every drop-off in the audit is marked as assumed rather than measured.
- request — The product, its first-run context, and the target user the redesigned flow is for.
- activation-event — The event the flow is designed to reach. Required here — a flow with no activation target cannot be judged good or bad.
- onboarding-audit — Audit from the `audit` route, read back so the redesign starts from the measured biggest drop instead of a blank page.
- request — Which screens, checklist items, or messages need rewriting, and the tone or product voice to hold to.
- onboarding-flow — Flow design from the `flow-design` route, read back so the copy is written against the real step order rather than a guessed one.
- request — The stall problem — how long users go inactive, at which step, and which channels are available to reach them.
- activation-event — The activation event, used to separate a stalled user from one who already got value and simply left.
- funnel-data — Inactivity and incomplete-setup cohorts exported from product analytics, used to size each stall pattern.

## Outputs

- Activation goal, first-run approach with its trade-off, step-by-step flow, checklist items, empty states, email sequence, and the metrics plan.
- Stall patterns with their detection rule, the email and in-app re-entry point for each, and the escalation path for high-value accounts.
- Step map with drop-off per step, the activation event used, and each finding as impact plus recommendation plus priority.
- Welcome screen, checklist items, empty states, tooltips, email sequence, and milestone celebration copy, ready to paste into the product.
- {scope.marketing}/experiments/onboarding-audit-{product}.md
- {scope.marketing}/experiments/onboarding-copy-{product}.md
- {scope.marketing}/experiments/onboarding-cro-{YYYY-MM-DD}.md
- {scope.marketing}/experiments/onboarding-flow-{product}.md

