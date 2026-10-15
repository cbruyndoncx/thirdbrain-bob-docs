---
description: Establish project context with PMBOK 7 tailoring decisions, delivery approach selection, and principle prioritization. Use when user mentions 'start a new project,' 'project setup,' 'project context,' 'tailoring,' or 'delivery approach.' This is the recommended entry point for new projects — offers to chain into project-charter when done.
title: project-context
---

# project-context

Establish project context with PMBOK 7 tailoring decisions, delivery approach selection, and principle prioritization. Use when user mentions 'start a new project,' 'project setup,' 'project context,' 'tailoring,' or 'delivery approach.' This is the recommended entry point for new projects — offers to chain into project-charter when done.

- **Area:** Project Delivery
- **Category:** project management
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Product Manager

Establish project context with PMBOK 7 tailoring decisions, delivery approach selection, and principle prioritization.

## How you ask

- “Start a new project with PMBOK 7 tailoring decisions”
- “Select the right delivery approach for our project”
- “Establish project context and prioritize principles”
- “Set up project context for an agile software delivery”

## Inputs

- request — The project characteristics the caller can state now — name, budget range, duration, team size, industry, requirement clarity — and any governance constraint that should override the scoring heuristics.
- project-brief — Project note or written brief read to extract the characteristics instead of asking the caller to restate what is already documented.
- existing-context — The `project_context.md` in force today — its scores and tailoring decisions are the baseline the revision is measured against, and its unchanged sections are preserved.
- request — What changed since the context was written — budget move, scope growth, team change, new regulatory constraint — and which decisions the caller believes it invalidates.
- project-brief — Updated project note or brief carrying the new characteristics the revised scores are derived from.
- existing-context — The `project_context.md` under review — checked section by section against the completion criteria and for tailoring depths that contradict the stated profile or delivery approach.
- request — Narrows the check to specific sections or decisions. Absent, the whole document is checked.

## Outputs

- Per-section verdict against the completion criteria, the inconsistencies found between profile, delivery approach and tailoring depths, and the list of decisions that need a rescore via the `refresh` route.
- Project profile with size, complexity and uncertainty scores, the selected delivery approach and its scored factors, the tailoring matrix across the PM skills, priority principles with project-specific application notes, and the elevated performance domains.
- Revised context in which every changed score, approach decision and tailoring depth states what moved it, and downstream skills whose depth changed are named so their artifacts can be re-cut.
- {project-folder}/project_context.md OR {me.inbox}/project_context.md

