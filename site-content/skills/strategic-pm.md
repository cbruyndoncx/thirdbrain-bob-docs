---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: strategic-pm — ThirdBrain BOB skill
  description: Reframe tactical work into a strategic brief with a real bet, a named trade-off, an outcome, and a time horizon.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: strategic-pm
catLabel: product-management
area: strategy
desc: Creates strategic framing briefs in Obsidian that tie initiatives to outcomes, trade-offs, and now-next-later horizons.
summary: Reframe tactical work into a strategic brief with a real bet, a named trade-off, an outcome, and a time horizon.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- strategic-pm (markdown)
- '{scope.knowledge-base.product}/strategic-pm-{YYYY-MM-DD}.md'
prompts:
- Help me be more strategic about our roadmap priorities
- Create a strategic framing brief for this initiative
- Tie our feature work to business outcomes
- Map our initiatives to now-next-later horizons
---
