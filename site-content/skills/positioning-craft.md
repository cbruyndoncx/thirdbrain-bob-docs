---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: positioning-craft — ThirdBrain BOB skill
  description: Use this skill when the team needs a usable positioning artifact, not just abstract messaging advice.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: positioning-craft
catLabel: product-management
area: strategy
desc: Crafts product positioning, defines target customers, chooses market categories, and articulates differentiated value.
summary: Use this skill when the team needs a usable positioning artifact, not just abstract messaging advice.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Marketing, Product Manager]'
inputs:
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- product — What is being positioned
- competitive_alternatives — What customers would use instead
- target_segment — Segment to position for; defaults to the vault ICP
- icp — ICP — target customer the positioning is for.
- profile — Company profile — identity and proof points.
- marketing-context — Prior positioning, narrative, and competitive frame.
- tone-of-voice — Tone of voice — keeps the new positioning on-brand.
- offerings — Offerings catalogue — what is being positioned.
- current_positioning — Positioning statement as it stands today
- what_is_not_landing — Which part is failing, and the evidence for it
- messages — Message variants to test
- audience — Audience to test against; defaults to the vault ICP
outputs:
- positioning-brief (markdown)
- '{scope.profile-root}/positioning-{slug}.md'
prompts:
- Craft our product positioning against the competition
- Define our target customer and market category
- Articulate our differentiated value proposition
- Help me position our new feature in the market
---
