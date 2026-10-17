---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: design-first-dev — ThirdBrain BOB skill
  description: Use this skill when the team needs to decide how much craft to invest and what must be designed before build starts.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: design-first-dev
catLabel: product-management
area: strategy
desc: Creates feature specs, defines all-state UX requirements, prototypes interactions, and sets craft-level standards for design-led development.
summary: Use this skill when the team needs to decide how much craft to invest and what must be designed before build starts.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- design-first-dev (markdown)
- '{scope.knowledge-base.product}/design-first-dev-{YYYY-MM-DD}.md'
prompts:
- Create a feature spec with all-state UX requirements
- Define the design system standards for this feature
- Set craft-level quality standards for our product
- Prototype the interaction design for our settings page
---
