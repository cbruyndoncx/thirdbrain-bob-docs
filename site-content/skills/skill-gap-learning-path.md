---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skill-gap-learning-path — ThirdBrain BOB skill
  description: Use this skill for honest career-development planning, not to manufacture qualifications or make a candidate appear qualified for an unsuitable role. It classif
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skill-gap-learning-path
catLabel: human-resources
area: people
desc: Compare a job or target role with the candidate's evidence, identify evidenced strengths and unproven or missing capabilities, then create a prioritized learning path…
summary: Use this skill for honest career-development planning, not to manufacture qualifications or make a candidate appear qualified for an unsuitable role. It classifies each requirement of one role against the candidate's documented evidence, explains where study can and cannot close a gap, and builds a prioritised learning path with one capstone project.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[context-pack]'
roles: '[]'
inputs:
- job-note — One vacancy note to analyse; give this or role-brief.
- role-brief — A pasted job description or target-role brief, used when there is no vacancy note.
- candidate-profile — Approved candidate profile and the evidence it links to.
- candidate-constraints — Weekly hours, budget, deadline, preferred learning format and target role level, when known.
outputs:
- Case note with the evidence matrix, gap analysis, learning path and sources-checked date; written only when the user asks to build a case.
- '{me.job-search.skill-gap-cases}/{case-name}.md'
prompts:
- Compare Integration Architect - Ravago with my profile and build a learning path
- I want to pivot into cloud data engineering — here is a job description, what am I missing?
- Build a skill-gap case for this role; I have 6 hours a week and no budget for paid courses
---
