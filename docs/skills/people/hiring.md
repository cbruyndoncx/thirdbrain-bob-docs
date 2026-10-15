---
description: End-to-end hiring lifecycle for small teams — from "do I even need this hire?" through role definition, sourcing, interviewing, evaluation, and offer.
title: hiring
---

# hiring

End-to-end hiring lifecycle for small teams — from "do I even need this hire?" through role definition, sourcing, interviewing, evaluation, and offer.

- **Area:** People
- **Category:** human resources
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** CEO / Founder, Operations Manager, HR Manager

Plans hiring decisions, writes job posts, designs interview processes, evaluates candidates with scorecards, and makes hire/no-hire recommendations.

## How you ask

- “Should I hire?”
- “Hire”
- “Job post”

## Inputs

- client_company_overview — Client company profile — name, industry, size, offering, key contacts. Read when the request is client-scoped; the route asks the user when absent.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- role — The role to hire for (title or problem statement)
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company profile — stage, mission, and team context for the role.
- icp — ICP — defines who the hire will serve.
- candidates — Candidate names, backgrounds, and interview notes
- hiring_plan — Link to existing hiring plan (for criteria). If absent, criteria are gathered interactively.
- scorecard — Link to candidate scorecard from evaluate route

## Outputs

- The seat itself — a `vacancy` note with `side: employer`, linking the hiring plan. Candidate notes for the seat point at it with `vacancy_ref`.
- decision_brief (markdown)
- hiring_plan (markdown)
- job_post (markdown)
- scorecard (markdown)
- {scope.hr.recruiting}/{role-slug}.md
- {scope.hr}/hiring/{role-slug}_decision_{YYYY-MM-DD}.md
- {scope.hr}/hiring/{role-slug}_hiring_plan_{YYYY-MM-DD}.md
- {scope.hr}/hiring/{role-slug}_job_post_{YYYY-MM-DD}.md
- {scope.hr}/hiring/{role-slug}_scorecard_{YYYY-MM-DD}.md

