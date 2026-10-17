---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: collections-escalation — ThirdBrain BOB skill
  description: Structured collections process for overdue invoices. Generates tiered follow-up sequences, enforces payment terms with formal documentation, and helps resolve i
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: collections-escalation
catLabel: finance
area: finance
desc: Drafts overdue-invoice escalation emails and letters with tiered follow-up sequences, payment-term enforcement, and dispute resolution.
summary: Structured collections process for overdue invoices. Generates tiered follow-up sequences, enforces payment terms with formal documentation, and helps resolve invoice disputes — while preserving client relationships.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- profile — Company or client profile — entity and relationship context.
- invoice-ref — Invoice ID or wikilink to invoice note
- invoice-note — loaded from your vault context
- client-profile — loaded from your vault context
- days-overdue — Days past due date (auto-derived from invoice note if available)
- letter-tone — Severity of the letter — 'reminder' restates the agreed terms cordially, 'demand' states consequences and a payment deadline. Escalate only after a reminder has gone unanswered. (reminder | demand)
- invoice-ref — Invoice ID or wikilink to disputed invoice note
- dispute-details — Client's stated reason for dispute
outputs:
- dispute-response (markdown)
- escalation-sequence (markdown)
- payment-terms-letter (markdown)
- '{client.invoices}/collections_{invoice_id}.md'
- '{client.invoices}/dispute_{invoice_id}_{YYYY-MM-DD}.md'
- '{client.invoices}/payment_letter_{invoice_id}_{YYYY-MM-DD}.md'
prompts:
- Overdue invoices
- Payment terms need enforcing
- Collections process
---
