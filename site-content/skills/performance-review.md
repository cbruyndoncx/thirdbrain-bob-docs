---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: performance-review — ThirdBrain BOB skill
  description: Prepare structured performance reviews, development plans, and 90-day probation check-ins for SME teams — without an HR system or complex process.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: performance-review
catLabel: human-resources
area: people
desc: Structures performance review conversations as vault markdown drafts, creates review templates, and prepares 90-day check-in agendas.
summary: Prepare structured performance reviews, development plans, and 90-day probation check-ins for SME teams — without an HR system or complex process.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[HR Manager]'
inputs:
- role — The team member's role and tenure
- context — Recent work, projects, or specific incidents to cover
- profile — Company profile — values and stage for review framing.
- role — Current role and target growth area
- gaps — Skills or behaviours to develop
- role — The new hire's role and start date
outputs:
- development-plan (markdown)
- probation-check (markdown)
- review-template (markdown)
- '{company.hr}/dev-plan_{name}_{YYYY-MM-DD}.md'
- '{company.hr}/probation_{name}_{YYYY-MM-DD}.md'
- '{company.hr}/review_{name}_{YYYY-MM-DD}.md'
prompts:
- Performance review
- Development plan
- Probation check-in
---
