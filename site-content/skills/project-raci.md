---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-raci — ThirdBrain BOB skill
  description: Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views. Use when t
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-raci
catLabel: project-management
area: project-delivery
desc: Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views.
summary: Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views. Use when the user mentions 'RACI matrix,' 'RACI chart,' 'responsibility assignment matrix,' 'who is responsible,' or 'roles and responsibilities.' This is the RACI methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- stakeholder_register — Stakeholder register — who, influence, interest (from `project-stakeholder`)
- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- source (Create RACI Matrix) — WBS tasks and team roles, or project reference
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.
outputs:
- company-project-raci (markdown)
- raci-matrix (markdown)
- '{company.project-management}/project-raci-{{YYYY-MM-DD}}.md'
- '{project-folder}/raci_matrix.md'
prompts:
- Create a RACI matrix for our project tasks
- Validate responsibility assignments against the WBS
- Who is responsible for each deliverable on our project?
- Generate role-based and activity-based RACI views
---
