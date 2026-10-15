---
description: Use this skill to create or update Dataview files whose results are serialized into markdown for AI-readable querying.
title: dataview-serializer
---

# dataview-serializer

Use this skill to create or update Dataview files whose results are serialized into markdown for AI-readable querying.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | intermediate |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [config] |
| **Roles** | [] |

Creates Dataview queries that serialize to readable markdown inside Obsidian.

## How you ask

- “Create a Dataview query to list all client meeting notes”
- “Build a serialized markdown table of all skills by category”
- “Query my vault for all notes tagged with #action/follow-up”
- “Generate a Dataview view of all open tasks across projects”

## Inputs

- request — The vault question or view the new Dataview file must answer, including the folder, tags, or frontmatter fields it filters on.
- request — The change to make to the existing query — a new filter, grouping, sort order, or corrected field name.
- existing-query — The existing Dataview file being updated, read back before edits are applied so the update preserves its schema.
- request — The vault question to answer inline, without creating a saved query file.

## Outputs

- Inline query result returned in the response. No file is saved unless the user asks for one.
- Newly created Dataview query file with its serialized markdown result block.
- Updated Dataview query file with the refreshed serialized markdown result block.
- {vault.dataview}/{descriptor}.md

