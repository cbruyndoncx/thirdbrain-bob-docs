---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: create-client — ThirdBrain BOB skill
  description: Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders. Use when the u
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: create-client
catLabel: sales
area: sales
desc: Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders.
summary: Creates standardized client workspace folders in Obsidian with profile, deals, invoices, leads, meetings, sales, archive, and project subfolders. Use when the user says 'onboard a new client,' 'start a project engagement,' 'initialize a client workspace,' or 'set up the folders.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- client_id — Kebab-case client identifier, used as the folder name
- client_name — Legal or trading name
- location — Primary location or jurisdiction
- industry — Sector the client operates in
- client_id — Existing client the project belongs to
- project_name — Project name; the folder is prefixed YYYY-MM automatically
- client_id — Existing client workspace to extend
- folders — Subfolders to add to the workspace
outputs:
- Project folder copied from the project template, declared by its brief — `project_brief_template.md` from the standard template, `project_brief.md` from the website template — beside the research (`{~project.research}/`), analysis (`{~project.analysis}/`) and `deliverables/` folders.
- client-profile (markdown)
- extended-structure (markdown)
- '{client.profile}'
- '{client.root}/{YYYY-MM}-{project-name}/project_brief*.md'
prompts:
- Create a new client workspace for Acme Corp
- Set up client folders for Acme Industries in Dubai
- 'Onboard new client: TechStart Inc, SaaS, Berlin'
---
