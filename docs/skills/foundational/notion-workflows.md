---
description: 'Four connected Notion workflows. They run on either of two backends: the Notion MCP server when it is connected, otherwise the `notion` CLI skill. See Setup → Backend for how to choose and how the two map.'
title: notion-workflows
---

# notion-workflows

Four connected Notion workflows. They run on either of two backends: the Notion MCP server when it is connected, otherwise the `notion` CLI skill. See Setup → Backend for how to choose and how the two map.

- **Area:** Foundational
- **Category:** productivity
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** mcp
- **Roles:** 

Runs Notion-powered workflows for knowledge capture, meeting intelligence, research documentation, and spec-to-implementation.

## How you ask

- “Turn this conversation into a Notion wiki entry”
- “Prep for my meeting using context from Notion pages”
- “Convert this spec into implementation tasks in Notion”
- “Research across our Notion workspace for related content”

## Inputs

- content — Raw note, link, or idea to file
- database — Target Notion database; inferred from content type when omitted
- transcript — Meeting notes or transcript to structure
- attendees — Participants, for attribution of actions
- topic — Research subject
- sources — URLs or documents to ground the research in
- feature — Feature or change the spec describes
- context — Background, constraints, and prior decisions
- page_id — Notion page to check against the route's output contract

## Outputs

- implementation-plan (markdown)
- meeting-prep (markdown)
- prefer a permanent directory)
- quality-report (markdown)
- research-doc (markdown)
- wiki-entry (markdown)

