---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: delivery-confirmation — ThirdBrain BOB skill
  description: Generate proof of delivery documents, document and escalate delivery problems, and produce delivery performance summaries. Activates at the final mile — after g
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: delivery-confirmation
catLabel: operations
area: operations
desc: Records delivery outcomes in the vault, generates proof of delivery documents, and manages customer sign-off.
summary: Generate proof of delivery documents, document and escalate delivery problems, and produce delivery performance summaries. Activates at the final mile — after goods leave the warehouse and before customer sign-off is complete.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- delivery_details — Order number, delivery address, items delivered, recipient name, date/time
- condition_notes — Item condition, packaging state, any exceptions noted at handoff
- 'issue_description — What went wrong: missing items, damage, wrong address, refused delivery, etc.'
- order_reference — Order number or delivery reference for the affected shipment
- period — Reporting period (e.g. 'March 2026', 'Q1 2026', 'last 30 days')
- 'data_source — Source of delivery data: spreadsheet, system export, or manual log'
outputs:
- delivery-report (markdown)
- issue-report (markdown)
- proof-of-delivery (markdown)
- '{client.root}/YYYY-MM-{project}/delivery-issue-{order-id}.md'
- '{client.root}/YYYY-MM-{project}/delivery-receipt-{order-id}.md'
- '{company.operations}/delivery-report-{YYYY-MM}.md'
prompts:
- Confirm delivery
- Delivery receipt
- Proof of delivery
---
