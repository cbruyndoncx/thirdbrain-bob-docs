---
description: One prompt, one page. Pull every customer-facing signal in parallel, cluster into themes, and surface the three actions that protect retention this week. Do the work — do not ask the owner to triage their own inbox.
title: customer-pulse
---

# customer-pulse

One prompt, one page. Pull every customer-facing signal in parallel, cluster into themes, and surface the three actions that protect retention this week. Do the work — do not ask the owner to triage their own inbox.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config] |
| **Roles** | [Operations Manager] |

Aggregates customer signal — Zendesk / Freshdesk tickets, Gmail sentiment, NPS/CSAT from Typeform / Tally, Trustpilot / G2 reviews, Stripe disputes, and vault…

## How you ask

- “How are customers doing”
- “Anything urgent from support”
- “Who's about to churn”

## Inputs

- trigger — 'customer pulse', 'how are customers doing', 'anything urgent from customers'
- client-feedback — Portfolio-wide customer feedback — the primary vault signal source.
- current-state — Business health state — account-health flags and binding constraint.
- trigger — 'weekly customer check', 'Monday customer review', 'this week's customer signal'
- trigger — 'who's about to churn', 'at-risk accounts', 'red flags'
- theme — Theme name from the taxonomy to drill into

## Outputs

- CURRENT-STATE writeback — interim Red Flags entries appended/refreshed after saving.
- pulse_note (markdown)
- {company.management}/CURRENT-STATE.md
- {me.inbox}/customer-pulse-churn-{YYYY-MM-DD}.md
- {me.inbox}/customer-pulse-theme-{name}-{YYYY-MM-DD}.md
- {me.inbox}/customer-pulse-weekly-{YYYY-WW}.md
- {me.inbox}/customer-pulse-{YYYY-MM-DD}.md

