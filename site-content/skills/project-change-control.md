---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-change-control — ThirdBrain BOB skill
  description: Create or update a project change-control record so changes are logged, assessed, routed, and traceable before implementation.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-change-control
catLabel: project-management
area: project-delivery
desc: Sets up change control, maintains a change log, and routes approvals for scope or baseline impact.
summary: Create or update a project change-control record so changes are logged, assessed, routed, and traceable before implementation.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
- project — The project whose change log is written or updated — an own project id (`project.*` keys), a client-id plus engagement folder (client work), or an internal company project. Omitted when there is no project, in which case the draft goes to the personal inbox.
outputs:
- Client work — inside the engagement's YYYY-MM-name folder (the client.projects glob), named by the project id.
- Internal company project with no own project folder.
- Own project — the project's PMBOK artifacts folder.
- change-log-personal (markdown)
- '{client.projects}/{project-id}/change_log.md'
- '{company.project-management}/change_log.md'
- '{me.inbox}/change_log.md'
- '{project.management}/change_log.md'
prompts:
- Log a change request for expanding the project scope
- Assess the impact of this proposed schedule change
- Set up change control for our new project
- Review and route this change request for approval
---
