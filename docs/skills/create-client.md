---
description: Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders. Use when the user says 'onboard a new client,' 'start a project engagement,' 'initialize a client workspace,' or 'set up the folders.'
title: create-client
---

# create-client

Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders. Use when the user says 'onboard a new client,' 'start a project engagement,' 'initialize a client workspace,' or 'set up the folders.'

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [install] |
| **Roles** | [] |

Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders.

## How you ask

- “Create a new client workspace for Acme Corp”
- “Set up client folders for Acme Industries in Dubai”
- “Onboard new client: TechStart Inc, SaaS, Berlin”

## Inputs

- client_id — Kebab-case client identifier, used as the folder name
- client_name — Legal or trading name
- location — Primary location or jurisdiction
- industry — Sector the client operates in
- client_id — Existing client the project belongs to
- project_name — Project name; the folder is prefixed YYYY-MM automatically
- client_id — Existing client workspace to extend
- folders — Subfolders to add to the workspace

## Outputs

- Project folder copied from the project template, declared by its brief — `project_brief_template.md` from the standard template, `project_brief.md` from the website template — beside the research (`{~project.research}/`), analysis (`{~project.analysis}/`) and `deliverables/` folders.
- client-profile (markdown)
- extended-structure (markdown)
- {client.profile}
- {client.root}/{YYYY-MM}-{project-name}/project_brief*.md

## Seen in these workflows

- [New client.](../workflows/create-client.md)

