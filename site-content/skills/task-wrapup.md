---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: task-wrapup — ThirdBrain BOB skill
  description: USE WHEN user says "task wrapup", "wrap up", "retrospective", "lessons learned", "what did we learn", "process improvement", "how can we do this better", "autom
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: task-wrapup
catLabel: productivity
area: foundational
desc: Captures lessons learned at task completion and preserves session context for handoffs.
summary: USE WHEN user says "task wrapup", "wrap up", "retrospective", "lessons learned", "what did we learn", "process improvement", "how can we do this better", "automate recurring tasks", "create reusable templates", "improve workflow", "session handoff", "handoff to next session", "save session state", "pick up where I left off", "context for next agent", or "hand off context".
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
- 'request — Mode and context: ''create [description]'', ''list'', ''update [slug]'', or ''view [slug]'''
- session-context — Conversation history, open files, recent decisions from the current session
outputs:
- handoff-document (markdown)
- prefer a permanent directory)
- task-wrapup (markdown)
- '{vault.sessions}/'
prompts:
- Run a retrospective on this completed project
- What worked well and what should we improve?
- Capture lessons learned from the client engagement
- Create reusable templates from this completed work
- Session handoff — save context so the next agent can continue
- Hand off this work for me to pick up tomorrow
- List my handoffs
- Update the migration handoff with today's progress
---
