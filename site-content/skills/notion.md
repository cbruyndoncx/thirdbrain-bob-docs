---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: notion — ThirdBrain BOB skill
  description: 'Single-file CLI covering the core Notion API (version `2026-03-11`, data-source model): pages, databases, data sources, blocks, todos, query, search, users, com'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: notion
catLabel: productivity
area: foundational
desc: Manages Notion workspace via CLI for pages, databases, todos, blocks, and search.
summary: 'Single-file CLI covering the core Notion API (version `2026-03-11`, data-source model): pages, databases, data sources, blocks, todos, query, search, users, comments, page properties, and markdown read/create. Runs from a locally cached copy fetched from GitHub (see Setup). Surfaces not yet wired in (file uploads, webhooks, views, markdown update) are catalogued with method + path in [references/unsupported_endpoints.md](references/unsupported_endpoints.md).'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[]'
inputs:
- query — What to find in Notion
- database — Restrict the search to one database
- target — Page or database row to create or update
- properties — Field values to write
- target — Page or row to archive or delete
- confirmed — Explicit owner confirmation — destructive routes never infer consent
outputs:
- notion-data (markdown)
- notion-deletion (markdown)
- notion-update (markdown)
- prefer a permanent directory)
prompts:
- Create a new Notion page for our project kickoff
- Search Notion for all pages related to product roadmap
- Update the status of our Q1 goals in Notion
- Query our Notion database for overdue tasks
---
