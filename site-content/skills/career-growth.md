---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: career-growth — ThirdBrain BOB skill
  description: Help a PM decide what promotion target to pursue, identify the evidence gap, and turn that gap into a concrete development plan.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: career-growth
catLabel: human-resources
area: people
desc: Plans PM career advancement, identifies skill gaps, and structures promotion cases with gap analysis.
summary: Help a PM decide what promotion target to pursue, identify the evidence gap, and turn that gap into a concrete development plan.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- career-growth (markdown)
- '{scope.knowledge-base.product}/career-growth-{YYYY-MM-DD}.md'
prompts:
- Help me build a promotion case for senior PM
- Identify my skill gaps for transitioning to management
- Plan my career growth path from IC to director level
- Should I go into management or stay as an IC?
---
