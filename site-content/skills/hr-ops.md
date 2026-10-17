---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: hr-ops — ThirdBrain BOB skill
  description: Build HR operational assets — job descriptions and onboarding or training curricula.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: hr-ops
catLabel: human-resources
area: people
desc: Drafts HR operational assets as vault markdown — job descriptions and training or onboarding curriculum outlines.
summary: Build HR operational assets — job descriptions and onboarding or training curricula.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[HR Manager]'
inputs:
- role — Role the job description covers
- seniority — Level, which sets scope and requirement language
- profile — Company profile — stage and team context for the JD.
- topic — Training subject
- audience — Who is being trained, which sets depth and examples
- profile — Company profile — context for the training curriculum.
outputs:
- job-description (markdown)
- training-module (markdown)
- '{company.hr}/jd_{role-title}.md'
- '{company.hr}/training_{module-name}.md'
prompts:
- Create a job description for a marketing manager role
- Build a training module outline for new employee onboarding
- Draft an HR onboarding checklist for remote workers
- Write a job description for a customer success lead
---
