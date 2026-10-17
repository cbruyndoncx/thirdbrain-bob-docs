---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: culture-craft — ThirdBrain BOB skill
  description: Use this skill to turn culture intent into observable behaviors, rituals, and hiring standards rather than vague value statements.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: culture-craft
catLabel: human-resources
area: people
desc: Designs team culture, defines core values, and creates reinforcing rituals and excellence standards.
summary: Use this skill to turn culture intent into observable behaviors, rituals, and hiring standards rather than vague value statements.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, HR Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- culture-craft (markdown)
- '{scope.knowledge-base.product}/culture-craft-{YYYY-MM-DD}.md'
prompts:
- Define core values for our engineering team
- Design team rituals that reinforce our culture
- Create excellence standards for our product team
- Build a culture document for our growing startup
---
