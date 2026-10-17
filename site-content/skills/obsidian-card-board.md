---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: obsidian-card-board — ThirdBrain BOB skill
  description: Use this skill to set up, troubleshoot, or standardize Card Board workflows inside Obsidian.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: obsidian-card-board
catLabel: obsidian
area: foundational
desc: Creates and manages Obsidian Card Board kanban boards with tagged tasks, lane rules, date-based columns, and movement patterns.
summary: Use this skill to set up, troubleshoot, or standardize Card Board workflows inside Obsidian.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[]'
inputs:
- request — The board to create — its purpose, the task sources it should cover, and whether it is tag, date, or mixed.
- request — The board problem to diagnose — which tasks are missing or misplaced, and on which board.
- request — The scope to standardize — which boards, which tag conventions, and which team consistency problem is being solved.
outputs:
- The documented tag naming convention, any WIP agreement, formalized filter rules, and board rules reported back to the user.
- The new board's model, column definitions, filter rules, and the one verified example task.
- The root cause found, the fix applied or documented, and confirmation the affected task now verifies in the correct lane.
- prefer a permanent directory)
prompts:
- Create a kanban board for my project tasks
- Set up Card Board lanes based on task tags
- Help me configure date-based columns for my sprint board
---
