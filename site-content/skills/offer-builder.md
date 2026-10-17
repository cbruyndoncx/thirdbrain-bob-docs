---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: offer-builder — ThirdBrain BOB skill
  description: Design Grand Slam Offers that make saying yes easy and saying no feel irrational. Based on Alex Hormozi's *$100M Offers* framework.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: offer-builder
catLabel: sales
area: sales
desc: Builds irresistible Grand Slam Offers using Hormozi's value equation framework — dream outcome, perceived likelihood, time delay, and effort reduction.
summary: Design Grand Slam Offers that make saying yes easy and saying no feel irrational. Based on Alex Hormozi's *$100M Offers* framework.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- profile — Company or client profile — entity and relationship context.
- offer-context — Target buyer, desired outcome, current service or product, price, proof, delivery model, and known objections.
- existing-offer — Existing offer copy, proposal, or structured offer document to assess.
- risk-context — Promise, buyer fear, delivery dependencies, controllable conditions, and refund or performance boundaries.
- naming-context — Target buyer, result, timeframe, objection eliminator, and preferred brand register.
outputs:
- guarantee-menu (markdown)
- offer-audit (markdown)
- offer-document (markdown)
- offer-names (markdown)
- '{scope.sales}/guarantee-options-{service}.md'
- '{scope.sales}/offer-audit-{client}-{YYYY-MM-DD}.md'
- '{scope.sales}/offer-names-{service}.md'
- '{scope.sales}/offer-{service}-{YYYY-MM-DD}.md'
prompts:
- Build a Grand Slam Offer for our AI operations transformation service
- Audit our current BOB offer using the value equation
- Design a guarantee for our 90-day AI implementation package
- Generate 10 offer name options for our enterprise AI service
- 'What''s wrong with our current offer? Here it is: [paste offer]'
---
