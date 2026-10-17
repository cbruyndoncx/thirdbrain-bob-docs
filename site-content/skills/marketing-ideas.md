---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: marketing-ideas — ThirdBrain BOB skill
  description: Help users find the right marketing strategies from 139 proven approaches, matched to their stage, budget, and goals.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: marketing-ideas
catLabel: marketing-strategy
area: marketing
desc: Creates marketing plans and recommends channel-specific tactics for SaaS products from a library of 139 proven strategies.
summary: Help users find the right marketing strategies from 139 proven approaches, matched to their stage, budget, and goals.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
outputs:
- marketing-ideas (markdown)
- marketing-ideas-company (markdown)
- '{client.marketing}/strategy/marketing-ideas-{focus}.md'
- '{company.marketing}/strategy/marketing-ideas-{focus}.md'
prompts:
- Give me marketing ideas for our B2B SaaS product
- What marketing channels should we prioritize with a $10K budget?
- Recommend tactics to promote our new consulting service
- Create a marketing plan for our product launch
---
