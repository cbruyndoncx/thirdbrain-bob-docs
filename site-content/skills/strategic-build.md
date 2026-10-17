---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: strategic-build — ThirdBrain BOB skill
  description: Decide whether a proposed build is leverage, neutral, or overhead before the team commits.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: strategic-build
catLabel: product-management
area: strategy
desc: Evaluate proposed features or initiatives with LNO classification, strategic review, and pre-mortem analysis.
summary: Decide whether a proposed build is leverage, neutral, or overhead before the team commits.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- initiative — Work to classify as strategic or operational
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- initiative — Initiative under review
- evidence — Data supporting or undermining the current direction
- initiative — Initiative to pre-mortem
- horizon — How far ahead to imagine the failure
outputs:
- build-classification (markdown)
- pre-mortem-analysis (markdown)
- strategic-review (markdown)
- '{scope.knowledge-base.product}/strategic-build-classification-{work-item-slug}-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/strategic-build-pre-mortem-{work-item-slug}-{YYYY-MM-DD}.md'
- '{scope.knowledge-base.product}/strategic-build-review-{work-item-slug}-{YYYY-MM-DD}.md'
prompts:
- Should we build this feature? Give me a strategic review
- Classify this initiative using the LNO framework
- Run a pre-mortem on our proposed product direction
- Is this real product work or product theater?
---
