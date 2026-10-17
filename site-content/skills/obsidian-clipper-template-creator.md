---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: obsidian-clipper-template-creator — ThirdBrain BOB skill
  description: Create, repair, and standardize templates for the Obsidian Web Clipper.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: obsidian-clipper-template-creator
catLabel: obsidian
area: foundational
desc: Creates importable templates for the Obsidian Web Clipper.
summary: Create, repair, and standardize templates for the Obsidian Web Clipper.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- url — Example page URL the template must parse
- url — Example page URL
- entity_type — Vault entity type the clipped note must validate against
- template — Existing clipper template that is mis-parsing
- url — Page it fails on, for reproduction
outputs:
- clipper-template (json)
- prefer a permanent directory)
- repaired-template (json)
prompts:
- Create a web clipper template for saving articles
- Build a clipping template with custom frontmatter fields
- Fix my web clipper template — the CSS selectors aren't matching
---
