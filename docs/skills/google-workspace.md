---
description: Manage Google Workspace documents, spreadsheets, presentations, drive files, emails, calendar events, and contacts via CLI.
title: google-workspace
---

# google-workspace

Manage Google Workspace documents, spreadsheets, presentations, drive files, emails, calendar events, and contacts via CLI.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | productivity |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config, api-key] |
| **Roles** | [] |

Manages Google Workspace with Docs, Sheets, Slides, Drive, Gmail, Calendar, and Contacts.

## How you ask

- “Create a Google Doc from this markdown content”
- “Build a presentation in Google Slides from my notes”
- “Send an email via Gmail to the client with the report”
- “Upload this file to our team's shared Drive folder”

## Inputs

- request — The Workspace service, target resource ID or name, and the action to perform
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- gdrive-index (markdown)
- {client.gdrive-archive}/gdrive-index.md

