---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-schedule — ThirdBrain BOB skill
  description: Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule. Use when user mentions 'projec
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-schedule
catLabel: project-management
area: project-delivery
desc: Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule.
summary: Develop a project schedule with CPM analysis and PERT estimates, delivered as an SVG Gantt chart plus a structured JSON schedule. Use when user mentions 'project schedule,' 'Gantt chart,' 'critical path,' 'PERT estimate,' or 'develop schedule.' This is the scheduling methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- wbs — Work breakdown structure — the deliverable tree (from `project-wbs`)
- request — What to produce
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- profile — Company profile — delivery standards and project context.
- profile_client — Client profile — used instead of the company profile for client engagements.
outputs:
- gantt-chart (svg)
- schedule (markdown)
- schedule-data (json)
- '{project-folder}/activities.json'
- '{project-folder}/gantt.svg'
- '{project-folder}/schedule.md'
prompts:
- Create a project schedule with critical path analysis
- Generate PERT estimates for our project activities
- Build a Gantt chart for our product launch timeline
- Calculate the critical path for our delivery milestones
---
