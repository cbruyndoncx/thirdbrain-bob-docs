---
description: USE WHEN user says "task wrapup", "wrap up", "retrospective", "lessons learned", "what did we learn", "process improvement", "how can we do this better", "automate recurring tasks", "create reusable templates", "improve workflow", "session handoff", "handoff to next session", "save session state", "pick up where I left off", "context for next agent", or "hand off context".
title: task-wrapup
---

# task-wrapup

USE WHEN user says "task wrapup", "wrap up", "retrospective", "lessons learned", "what did we learn", "process improvement", "how can we do this better", "automate recurring tasks", "create reusable templates", "improve workflow", "session handoff", "handoff to next session", "save session state", "pick up where I left off", "context for next agent", or "hand off context".

| | |
|---|---|
| **Area** | Foundational |
| **Category** | productivity |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Captures lessons learned at task completion and preserves session context for handoffs.

## How you ask

- “Run a retrospective on this completed project”
- “What worked well and what should we improve?”
- “Capture lessons learned from the client engagement”
- “Create reusable templates from this completed work”
- “Session handoff — save context so the next agent can continue”
- “Hand off this work for me to pick up tomorrow”
- “List my handoffs”
- “Update the migration handoff with today's progress”

## Inputs

- request — What to produce
- request — Mode and context: 'create [description]', 'list', 'update [slug]', or 'view [slug]'
- session-context — Conversation history, open files, recent decisions from the current session

## Outputs

- handoff-document (markdown)
- prefer a permanent directory)
- task-wrapup (markdown)
- {vault.sessions}/

