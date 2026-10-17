---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ship-decisions — ThirdBrain BOB skill
  description: Binary go/no-go shipping decisions using reversibility analysis (one-way vs two-way doors) and technical debt trade-offs. Use when user asks 'should we ship thi
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ship-decisions
catLabel: product-management
area: strategy
desc: Binary go/no-go shipping decisions using reversibility analysis (one-way vs two-way doors) and technical debt trade-offs.
summary: Binary go/no-go shipping decisions using reversibility analysis (one-way vs two-way doors) and technical debt trade-offs. Use when user asks 'should we ship this now,' 'ready to ship,' 'one-way door,' 'two-way door,' or 'tech debt vs shipping.' For defining craft levels and deciding what to polish vs defer, see quality-speed. This is the ship decision methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- decision — The call to be made
- deadline — When the decision stops being useful
- reversibility — How costly the decision is to undo — reversible, costly-to-reverse, or irreversible. Raises the evidence bar and the required sign-off as it worsens. (reversible | costly-to-reverse | irreversible)
- artifact — Thing being assessed for readiness to ship
outputs:
- hold-decision (markdown)
- readiness-brief (markdown)
- ship-decision (markdown)
- '{company.knowledge-base.product}/ship-decisions-{YYYY-MM-DD}.md'
prompts:
- Should we ship this feature or iterate more?
- Is this a one-way door or two-way door decision?
- Balance the technical debt against shipping speed
- 'Help me decide: ready to ship or needs more work?'
---
