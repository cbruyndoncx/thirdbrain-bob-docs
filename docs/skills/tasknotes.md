---
description: CRUD operations on tasks via TaskNotes plugin HTTP API (localhost, port from plugin settings — see below).
title: tasknotes
---

# tasknotes

CRUD operations on tasks via TaskNotes plugin HTTP API (localhost, port from plugin settings — see below).

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [install] |
| **Roles** | [] |

Drives the TaskNotes Obsidian plugin via its local HTTP API (127.0.0.1, port from plugin settings) to create, update, complete, and list tasks.

## How you ask

- “Create a new task: Review client proposal by Friday”
- “Mark the website redesign task as completed”
- “List all open tasks with high priority”
- “Update the status of the marketing audit task”

## Inputs

- title — Task title
- priority — Priority for the created task — low, normal, or high. Omit to let the TaskNotes plugin apply its configured default. (high | low | none | normal)
- due — Due date
- projects — Projects the task belongs to
- task — Task to update
- fields — Field values to change
- task — Task to delete
- confirmed — Explicit owner confirmation — deletion is never inferred

## Outputs

- created-task (markdown)
- deleted-task (markdown)
- updated-task (markdown)
- {output.tasks}/

