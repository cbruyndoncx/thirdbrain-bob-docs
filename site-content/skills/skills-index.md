---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skills-index — ThirdBrain BOB skill
  description: Generate a consolidated markdown document that embeds all skill documentation using Obsidian's `![[]]` syntax.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skills-index
catLabel: utilities
area: foundational
desc: Generates a consolidated index of all skills with embeds.
summary: Generate a consolidated markdown document that embeds all skill documentation using Obsidian's `![[]]` syntax.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
outputs:
- skills-index (markdown)
- '{vault.dataview}/skills_index.md'
prompts:
- Generate a consolidated index of all skills
- Create a skills overview page with embedded files
- Rebuild the skills index document
---
