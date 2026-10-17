---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: invoice-description — ThirdBrain BOB skill
  description: Transform completed work into clear, professional invoice line items that clients understand and approve without questions.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: invoice-description
catLabel: finance
area: finance
desc: Converts completed work items into invoice line-item descriptions for QuickBooks or Xero.
summary: Transform completed work into clear, professional invoice line items that clients understand and approve without questions.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- client-profile — Client profile — billing entity context.
- source (Raw work items) — Task list, time log, or work summary
- offerings — loaded from your vault context
- profile — loaded from your vault context
- source (Review route) — Existing draft line items to review
- source (Summary route) — Work items and period for billing summary
outputs:
- invoice (markdown)
- revised-invoice (markdown)
- '{client.invoices}/invoice-{client-id}-{YYYY-MM-DD}.md'
prompts:
- Convert these task items into invoice line descriptions
- Write professional invoice descriptions for this week's work
- Turn my time log into client-ready billing summaries
---
