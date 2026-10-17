---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: strategy-frameworks — ThirdBrain BOB skill
  description: 'Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks. Use when user mentions ''product '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: strategy-frameworks
catLabel: product-management
area: strategy
desc: Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks.
summary: Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks. Use when user mentions 'product strategy,' 'where to play,' 'beachhead market,' 'competitive positioning,' 'crossing the chasm,' 'strategic roadmap.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Product Manager]'
inputs:
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- strategy-frameworks (markdown)
- '{scope.knowledge-base.product}/strategy-frameworks-{YYYY-MM-DD}.md'
prompts:
- Create a product strategy using where-to-play/how-to-win
- Select our beachhead market for crossing the chasm
- Build a strategic canvas for competitive positioning
- Define our product strategy and strategic roadmap
---
