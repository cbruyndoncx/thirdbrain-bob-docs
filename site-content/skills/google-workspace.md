---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: google-workspace — ThirdBrain BOB skill
  description: Manage Google Workspace documents, spreadsheets, presentations, drive files, emails, calendar events, and contacts via CLI.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: google-workspace
catLabel: productivity
area: foundational
desc: Manages Google Workspace with Docs, Sheets, Slides, Drive, Gmail, Calendar, and Contacts.
summary: Manage Google Workspace documents, spreadsheets, presentations, drive files, emails, calendar events, and contacts via CLI.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[config, api-key]'
roles: '[]'
inputs:
- request — The Workspace service, target resource ID or name, and the action to perform
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- gdrive-index (markdown)
- '{client.gdrive-archive}/gdrive-index.md'
prompts:
- Create a Google Doc from this markdown content
- Build a presentation in Google Slides from my notes
- Send an email via Gmail to the client with the report
- Upload this file to our team's shared Drive folder
---
