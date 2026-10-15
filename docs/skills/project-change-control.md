---
description: Create or update a project change-control record so changes are logged, assessed, routed, and traceable before implementation.
title: project-change-control
---

# project-change-control

Create or update a project change-control record so changes are logged, assessed, routed, and traceable before implementation.

| | |
|---|---|
| **Area** | Project Delivery |
| **Category** | project management |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Sets up change control, maintains a change log, and routes approvals for scope or baseline impact.

## How you ask

- “Log a change request for expanding the project scope”
- “Assess the impact of this proposed schedule change”
- “Set up change control for our new project”
- “Review and route this change request for approval”

## Inputs

- request — What to produce
- project — The project whose change log is written or updated — an own project id (`project.*` keys), a client-id plus engagement folder (client work), or an internal company project. Omitted when there is no project, in which case the draft goes to the personal inbox.

## Outputs

- Client work — inside the engagement's YYYY-MM-name folder (the client.projects glob), named by the project id.
- Internal company project with no own project folder.
- Own project — the project's PMBOK artifacts folder.
- change-log-personal (markdown)
- {client.projects}/{project-id}/change_log.md
- {company.project-management}/change_log.md
- {me.inbox}/change_log.md
- {project.management}/change_log.md

