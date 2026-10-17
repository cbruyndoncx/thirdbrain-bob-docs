---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-receipt — ThirdBrain BOB skill
  description: Generate a virtual invoice that compares what completed work would have cost through a traditional agency or freelancer versus what it actually cost with AI ass
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-receipt
catLabel: utilities
area: foundational
desc: Generate a PNG virtual invoice that compares what completed work would have cost through an agency against the actual AI cost — line-item breakdown, hours saved, money…
summary: Generate a virtual invoice that compares what completed work would have cost through a traditional agency or freelancer versus what it actually cost with AI assistance.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under the client root (`client.root`) — a string with one reserved value, not a closed set
outputs:
- ai-receipt (markdown)
- ai-receipt-client (markdown)
- ai-receipt-client-png (png)
- ai-receipt-png (png)
- '{client.ai-receipts}/receipt_{YYYY-MM-DD}_{slug}.md'
- '{client.ai-receipts}/receipt_{YYYY-MM-DD}_{slug}.png'
- '{company.ai-receipts}/receipt_{YYYY-MM-DD}_{slug}.md'
- '{company.ai-receipts}/receipt_{YYYY-MM-DD}_{slug}.png'
prompts:
- Print a receipt for this session
- How much would this work have cost at an agency?
- Generate a virtual invoice comparing AI cost vs agency cost
- Show me the ROI of this AI-assisted work session
---
