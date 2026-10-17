---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: guarantee-designer — ThirdBrain BOB skill
  description: Remove the buyer's risk. Design guarantees that convert hesitation into commitment.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: guarantee-designer
catLabel: sales
area: sales
desc: Designs risk-reversal guarantees for proposals and offers.
summary: Remove the buyer's risk. Design guarantees that convert hesitation into commitment.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- profile — Company or client profile — entity and relationship context.
- service-context — Service promise, delivery controls, buyer fear, price, proof, and company profile context.
- risk-context — Outcome variability, customer obligations, operational exposure, exclusions, and claim history.
- existing-guarantee — Existing guarantee copy plus conversion, claim, and buyer-objection evidence.
outputs:
- guarantee (markdown)
- guarantee-audit (markdown)
- guarantee-options (markdown)
- optimized-guarantee (markdown)
- '{scope.sales}/guarantee-audit-{date}.md'
- '{scope.sales}/guarantee-options-{service}-{date}.md'
- '{scope.sales}/guarantee-{service}-{date}.md'
prompts:
- Design a guarantee for our 90-day AI transformation service
- Our main objection is 'we tried AI before and it didn't stick' — what guarantee fixes that?
- 'Audit our current guarantee: [paste existing guarantee text]'
- We want premium positioning with no refunds — how do we make that work?
- Give me 3 guarantee options for a $25,000 B2B service
---
