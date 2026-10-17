---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: influence-craft — ThirdBrain BOB skill
  description: Navigates organizational politics — maps power dynamics, builds coalitions, and develops influence strategies without formal authority. Use when user mentions '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: influence-craft
catLabel: human-resources
area: people
desc: Navigates organizational politics — maps power dynamics, builds coalitions, and develops influence strategies without formal authority.
summary: Navigates organizational politics — maps power dynamics, builds coalitions, and develops influence strategies without formal authority. Use when user mentions 'buy-in,' 'company politics,' 'managing up,' 'building coalitions,' or 'influence without authority.' For formal stakeholder registers, see project-stakeholder. For feedback and relationship management, see stakeholder-craft. This is the influence methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- influence-craft (markdown)
- '{scope.knowledge-base.product}/influence-craft-{YYYY-MM-DD}.md'
prompts:
- Map the power dynamics in my organization
- How do I build buy-in for my proposal without authority?
- Identify the key stakeholders I need to influence
- Develop an influence strategy for this cross-functional project
---
