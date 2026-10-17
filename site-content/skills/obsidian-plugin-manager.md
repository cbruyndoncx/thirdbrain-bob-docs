---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: obsidian-plugin-manager — ThirdBrain BOB skill
  description: Document Obsidian plugin configuration so AI agents understand available vault capabilities.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: obsidian-plugin-manager
catLabel: obsidian
area: foundational
desc: Lists and documents Obsidian plugins and generates the vault plugin index (`{vault.plugins-note}`).
summary: Document Obsidian plugin configuration so AI agents understand available vault capabilities.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
outputs:
- obsidian-plugin-manager (markdown)
- obsidian-plugins (markdown)
- prefer a permanent directory)
- '{vault.plugins-note}'
prompts:
- List all installed plugins in my vault
- Regenerate the plugin inventory document
- What plugins are enabled in my vault?
---
