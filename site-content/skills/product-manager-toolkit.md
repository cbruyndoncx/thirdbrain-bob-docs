---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: product-manager-toolkit — ThirdBrain BOB skill
  description: Use this skill to choose the right PM workflow, run it with the minimum required inputs, and return a concrete artifact rather than generic PM advice.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: product-manager-toolkit
catLabel: product-management
area: strategy
desc: Full PM workflow toolkit — PRD templates, customer interview analysis, product roadmaps, and discovery frameworks.
summary: Use this skill to choose the right PM workflow, run it with the minimum required inputs, and return a concrete artifact rather than generic PM advice.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager]'
inputs:
- transcript — Interview transcript or call notes — needed only for customer discovery
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- product-manager-toolkit (markdown)
- '{scope.knowledge-base.product}/product-manager-toolkit-{YYYY-MM-DD}.md'
prompts:
- Prioritize these features using RICE scoring
- Generate a PRD template for our new feature
- Analyze these customer interview transcripts for patterns
- Build a product roadmap from our discovery findings
---
