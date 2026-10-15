---
description: 'Expert B2B cold email copywriter. Cold email has two halves: the infrastructure that gets to the inbox, and the copy that earns the reply. Most people obsess over copy and ignore deliverability.'
title: cold-email
---

# cold-email

Expert B2B cold email copywriter. Cold email has two halves: the infrastructure that gets to the inbox, and the copy that earns the reply. Most people obsess over copy and ignore deliverability.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Sales

Write cold outbound prospecting emails, build sales follow-up sequences, diagnose emails that aren't getting replies, and handle inbound prospect replies.

## How you ask

- “Cold email”
- “Prospecting email”
- “Outbound email”

## Inputs

- lead-records — Lead records — the prospects being worked.
- prospect_context — Who the prospect is, what you sell, the pain you solve, proof points, and the ask
- sequence_length — Number of touches (1-5, default 3)
- profile — Company or client profile for sender identity and value framing.
- offerings — Offerings for matching solutions to prospect pain points.
- email_content — The existing email(s) to audit, plus any available metrics (open rate, reply rate, bounce rate)
- reply_content — The prospect's reply text and any context about the relationship

## Outputs

- Ready-to-send reply text
- audit-report (markdown)
- cold-emails (markdown)
- conversation
- {company.sales.outbound}/{campaign-slug}_cold_email_audit_{YYYY-MM-DD}.md
- {company.sales.outbound}/{campaign-slug}_cold_emails_{YYYY-MM-DD}.md

