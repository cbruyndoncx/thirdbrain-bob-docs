---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: strategic-storytelling — ThirdBrain BOB skill
  description: Turn product or initiative context into a persuasive story with a defined audience action.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: strategic-storytelling
catLabel: product-management
area: strategy
desc: Creates product pitches, memo narratives, and leadership storylines using a five-act structure, proof points, and audience-specific calls to action.
summary: Turn product or initiative context into a persuasive story with a defined audience action.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Product Manager]'
inputs:
- product — What is being pitched
- audience — Who hears it and what they care about
- change — The change the organization must get behind
- resistance — Where pushback is expected and why
- thesis — The argument the deck must land
- evidence — Supporting data points
outputs:
- source-client (markdown)
- strategic-narrative (markdown)
- '{client.knowledge-base.product}/strategic-storytelling-{YYYY-MM-DD}.md'
- '{company.knowledge-base.product}/strategic-storytelling-{YYYY-MM-DD}.md'
prompts:
- Create a product pitch using a five-act narrative structure
- Build a strategic story for our board presentation
- Write a talk track that frames our features around stakes
- Draft a memo narrative for our new product initiative
---
