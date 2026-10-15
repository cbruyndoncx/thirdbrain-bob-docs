---
description: 'Create items from natural language: `/capture-classify {input}`'
title: capture-classify
---

# capture-classify

Create items from natural language: `/capture-classify {input}`

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Classifies natural language into typed Obsidian `.md` notes with YAML frontmatter, wikilinks, and auto-open via Advanced URI.

## How you ask

- “Log this meeting with Sarah about the Q2 roadmap”
- “Create a task: Follow up with Acme Corp by Friday”
- “Save this idea about improving our onboarding flow”
- “Classify this input and create the right Obsidian notes”

## Inputs

- meeting_template — Entity template used to instantiate a meeting note.
- person_template — Entity template used to instantiate a person note.
- idea_template — Entity template used to instantiate an idea note.
- client_meeting_template — Client-scope meeting-notes template.
- client_project_template — Client-scope project-brief template.
- content — Raw captured text, link, or note to classify and file
- content — Capture containing several distinct items to split and file separately
- content — Capture the classifier could not place confidently
- candidate_types — Entity types under consideration, to present as a choice

## Outputs

- classified-note (markdown)
- classified-notes (markdown)
- draft-note (markdown)
- {me.inbox}/DRAFT_{entity-type}_{title}_{YYYY-MM-DD}.md
- {me.inbox}/{entity-type}_{title}_{YYYY-MM-DD}.md

