---
description: Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views. Use when the user mentions 'RACI matrix,' 'RACI chart,' 'responsibility assignment matrix,' 'who is responsible,' or 'roles and responsibilities.' This is the RACI methodology.
title: project-raci
---

# project-raci

Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views. Use when the user mentions 'RACI matrix,' 'RACI chart,' 'responsibility assignment matrix,' 'who is responsible,' or 'roles and responsibilities.' This is the RACI methodology.

- **Area:** Project Delivery
- **Category:** project management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Creates RACI matrices, validates assignments against WBS tasks and team roles, and generates both activity-based and role-based responsibility views.

## How you ask

- “Create a RACI matrix for our project tasks”
- “Validate responsibility assignments against the WBS”
- “Who is responsible for each deliverable on our project?”
- “Generate role-based and activity-based RACI views”

## Inputs

- stakeholder_register — Stakeholder register — who, influence, interest (from `project-stakeholder`)
- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- source (Create RACI Matrix) — WBS tasks and team roles, or project reference
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.

## Outputs

- company-project-raci (markdown)
- raci-matrix (markdown)
- {company.project-management}/project-raci-{{YYYY-MM-DD}}.md
- {project-folder}/raci_matrix.md

