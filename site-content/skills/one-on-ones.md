---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: one-on-ones — ThirdBrain BOB skill
  description: 'Prepare for and facilitate structured 1:1 meetings between managers and direct reports. Produces agenda cards, talking points, and meeting notes with follow-up '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: one-on-ones
catLabel: human-resources
area: people
desc: Prepare and facilitate structured 1:1 meetings with direct reports.
summary: Prepare for and facilitate structured 1:1 meetings between managers and direct reports. Produces agenda cards, talking points, and meeting notes with follow-up commitments.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, HR Manager]'
inputs:
- person — Name, role, and tenure of the direct report
- context — Recent work, concerns, projects, or behaviour to address
- profile — Company profile — values and current priorities for the 1:1.
- prep_card — Existing prep card from the prep route
outputs:
- meeting_notes (markdown)
- prep_card (markdown)
- '{company.meetings}/one_on_ones/{person-slug}_1on1_{YYYY-MM-DD}.md'
prompts:
- Prep for my 1:1 with Sarah tomorrow — she's been struggling with the new project
- Run my one-on-one with David, he's a strong performer and I want to talk about his growth
- I have a check-in with my new hire, what should I ask?
- Help me give feedback to my team lead about missing deadlines
---
