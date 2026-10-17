---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: stakeholder-craft — ThirdBrain BOB skill
  description: Create practical stakeholder plans for ongoing alignment, structured feedback, or recovery after trust has slipped.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: stakeholder-craft
catLabel: product-management
area: strategy
desc: Plans stakeholder relationships with cadence plans, SBI feedback briefs, and recovery plans for cross-functional trust.
summary: Create practical stakeholder plans for ongoing alignment, structured feedback, or recovery after trust has slipped.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager]'
inputs:
- stakeholder — Person or group being managed
- current_state — Where the relationship stands today
- recipient — Who receives the feedback
- situation — What happened, in observable terms rather than judgment
- stakeholder — Relationship needing repair
- what_went_wrong — The rupture, stated plainly
outputs:
- feedback-brief (markdown)
- recovery-plan (markdown)
- source-client (markdown)
- stakeholder-map (markdown)
- '{client.knowledge-base.product}/stakeholder-craft-{YYYY-MM-DD}.md'
- '{company.knowledge-base.product}/stakeholder-craft-{YYYY-MM-DD}.md'
prompts:
- Create a stakeholder map for this cross-functional project
- Prepare SBI feedback for my manager about a team issue
- Build a cadence plan for my stakeholder communications
- Help me navigate a difficult conversation with my VP
---
