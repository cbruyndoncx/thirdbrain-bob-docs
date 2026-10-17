---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: notion-workflows — ThirdBrain BOB skill
  description: 'Four connected Notion workflows. They run on either of two backends: the Notion MCP server when it is connected, otherwise the `notion` CLI skill. See Setup → B'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: notion-workflows
catLabel: productivity
area: foundational
desc: Runs Notion-powered workflows for knowledge capture, meeting intelligence, research documentation, and spec-to-implementation.
summary: 'Four connected Notion workflows. They run on either of two backends: the Notion MCP server when it is connected, otherwise the `notion` CLI skill. See Setup → Backend for how to choose and how the two map.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[mcp]'
roles: '[]'
inputs:
- content — Raw note, link, or idea to file
- database — Target Notion database; inferred from content type when omitted
- transcript — Meeting notes or transcript to structure
- attendees — Participants, for attribution of actions
- topic — Research subject
- sources — URLs or documents to ground the research in
- feature — Feature or change the spec describes
- context — Background, constraints, and prior decisions
- page_id — Notion page to check against the route's output contract
outputs:
- implementation-plan (markdown)
- meeting-prep (markdown)
- prefer a permanent directory)
- quality-report (markdown)
- research-doc (markdown)
- wiki-entry (markdown)
prompts:
- Turn this conversation into a Notion wiki entry
- Prep for my meeting using context from Notion pages
- Convert this spec into implementation tasks in Notion
- Research across our Notion workspace for related content
---
