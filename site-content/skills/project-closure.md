---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-closure — ThirdBrain BOB skill
  description: Create a closure report that records final delivery status, performance, lessons learned, remaining handoffs, and formal sign-off.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-closure
catLabel: project-management
area: project-delivery
desc: Generates a project closure report with deliverable acceptance, lessons learned, performance summary, outstanding handoffs, and sign-off.
summary: Create a closure report that records final delivery status, performance, lessons learned, remaining handoffs, and formal sign-off.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- project_charter — Approved charter — scope, objectives, constraints (from `project-charter`)
- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- schedule — Schedule — activities, durations, dependencies (from `project-schedule`)
- risk_register — Risk register — risks, scores, responses (from `project-risk`)
- request — What to produce
- profile — Company or client profile — delivery standards and project context.
outputs:
- project-closure (markdown)
- project-closure-personal (markdown)
- '{me.inbox}/project_closure.md'
- '{project-folder}/project_closure.md'
prompts:
- Generate a project closure report with lessons learned
- Create a deliverable acceptance and sign-off document
- Wrap up the project with a performance summary
- Document outstanding handoffs and post-mortem findings
---
