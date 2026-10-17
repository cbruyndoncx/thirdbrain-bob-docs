---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: launch-execution — ThirdBrain BOB skill
  description: Writes launch copy and creates go-to-market materials from a completed positioning canvas. Use when user mentions 'product launch,' 'launch copy,' 'go-to-market
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: launch-execution
catLabel: product-management
area: strategy
desc: Writes launch copy and creates go-to-market materials from a completed positioning canvas.
summary: Writes launch copy and creates go-to-market materials from a completed positioning canvas. Use when user mentions 'product launch,' 'launch copy,' 'go-to-market,' 'announcement,' 'feature launch.' For positioning itself, use positioning-craft.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Product Manager]'
inputs:
- product — What is launching
- launch_date — Target launch date
- channels — Channels the launch runs on
- channels — Channels needing copy
- launch_date — Target date, to assess whether readiness is achievable
outputs:
- launch-package (markdown)
- '{company.knowledge-base.product}/launch-execution-{YYYY-MM-DD}.md'
prompts:
- Write launch copy for our new feature release
- Position our product update for the announcement
- Create go-to-market materials for our product launch
- Draft the product announcement for our email list
---
