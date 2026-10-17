---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-wbs — ThirdBrain BOB skill
  description: Create a deliverable-oriented WBS that is concrete enough to estimate, assign, validate, and hand downstream to scheduling or risk work.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-wbs
catLabel: project-management
area: project-delivery
desc: Generates a deliverable-oriented Work Breakdown Structure with work-package dictionary fields, effort rollups, and optional canvas output.
summary: Create a deliverable-oriented WBS that is concrete enough to estimate, assign, validate, and hand downstream to scheduling or risk work.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- project_charter — Approved charter — scope, objectives, constraints (from `project-charter`)
- request — What to produce
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.
outputs:
- project-wbs (markdown)
- wbs-canvas (canvas)
- '{project-folder}/wbs.canvas'
- '{project-folder}/wbs.md'
prompts:
- Create a Work Breakdown Structure for our website redesign
- Decompose the project scope into deliverable-based packages
- Build a WBS with effort rollups for estimation
- Validate our WBS against the 100% rule
---
