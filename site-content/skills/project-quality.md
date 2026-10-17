---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-quality — ThirdBrain BOB skill
  description: Generate a quality management plan with metrics, assurance activities, and control tools. Use when user mentions 'quality plan,' 'quality standards,' 'plan qual
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-quality
catLabel: project-management
area: project-delivery
desc: Generate a quality management plan with metrics, assurance activities, and control tools.
summary: Generate a quality management plan with metrics, assurance activities, and control tools. Use when user mentions 'quality plan,' 'quality standards,' 'plan quality management,' 'quality assurance,' or 'quality metrics.' Anchored in PMBOK 8 principle 'Embed Quality into Processes and Deliverables.'
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- request — What to produce
outputs:
- quality-plan (markdown)
- '{project-folder}/quality_plan.md OR {me.inbox}/quality_plan.md'
prompts:
- Generate a quality management plan for our project
- Define quality metrics and assurance activities
- Set up quality standards for our deliverables
- Plan quality control tools and inspection points
---
