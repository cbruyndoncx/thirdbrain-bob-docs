---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: team-status-generator — ThirdBrain BOB skill
  description: Generate team status updates and standup summaries by pulling data from project management tools or analyzing meeting transcripts.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: team-status-generator
catLabel: productivity
area: foundational
desc: Generate team status updates and standup summaries from project management tools (Linear, Jira, Asana) or meeting transcripts.
summary: Generate team status updates and standup summaries by pulling data from project management tools or analyzing meeting transcripts.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Product Manager, Operations Manager]'
inputs:
- 'source (Team Status Generator) — Where team state comes from: tasknotes, tasks-plugin, card-board, linear, jira, asana, transcript, slack, or agent-logs'
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set
outputs:
- sprint-report (markdown)
- standup-summary (markdown)
- status (markdown)
- '{company.meetings}/{YYYY-MM-DD}_standup-summary.md'
- '{company.reports}/sprint-{sprint-id}-report.md'
- '{company.reports}/status-{YYYY-MM-DD}.md'
prompts:
- Generate a standup summary from our Linear board
- What did the team accomplish this sprint?
- Create a team status update from our Jira tickets
- Compile a progress report from this week's PM data
---
