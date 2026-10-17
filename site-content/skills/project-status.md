---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: project-status — ThirdBrain BOB skill
  description: Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health. Use when the user
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: project-status
catLabel: project-management
area: project-delivery
desc: Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health.
summary: Aggregates milestones, risks, budget, resource signals, and PM artifacts to generate executive project status reports with derived RAG health. Use when the user mentions 'project status report,' 'status update,' 'project health,' 'executive summary,' 'RAG status,' or 'how is the project going.' This is the project status methodology.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- status-report-yyyy-mm-dd (markdown)
- '{project-folder}/status_report_YYYY-MM-DD.md'
prompts:
- Generate a project status report for the executive team
- What's the overall health of our project?
- Create a RAG status update with risks and milestones
- How is the project tracking against our baseline?
---
