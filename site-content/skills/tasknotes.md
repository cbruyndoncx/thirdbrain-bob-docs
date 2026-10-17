---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: tasknotes — ThirdBrain BOB skill
  description: CRUD operations on tasks via TaskNotes plugin HTTP API (localhost, port from plugin settings — see below).
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: tasknotes
catLabel: obsidian
area: foundational
desc: Drives the TaskNotes Obsidian plugin via its local HTTP API (127.0.0.1, port from plugin settings) to create, update, complete, and list tasks.
summary: CRUD operations on tasks via TaskNotes plugin HTTP API (localhost, port from plugin settings — see below).
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- title — Task title
- priority — Priority for the created task — low, normal, or high. Omit to let the TaskNotes plugin apply its configured default. (high | low | none | normal)
- due — Due date
- projects — Projects the task belongs to
- task — Task to update
- fields — Field values to change
- task — Task to delete
- confirmed — Explicit owner confirmation — deletion is never inferred
outputs:
- created-task (markdown)
- deleted-task (markdown)
- updated-task (markdown)
- '{output.tasks}/'
prompts:
- 'Create a new task: Review client proposal by Friday'
- Mark the website redesign task as completed
- List all open tasks with high priority
- Update the status of the marketing audit task
---
