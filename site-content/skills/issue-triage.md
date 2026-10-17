---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: issue-triage — ThirdBrain BOB skill
  description: Classify incoming customer issues by severity, assign SLA response timelines, determine the right owner, and produce a structured issue record — without requiri
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: issue-triage
catLabel: operations
area: operations
desc: Triages incoming customer issues by assigning severity, setting SLA timelines, and routing first-line handling.
summary: Classify incoming customer issues by severity, assign SLA response timelines, determine the right owner, and produce a structured issue record — without requiring a ticketing system.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- issue_description — Customer's description of the problem or complaint
- client — Client or account name
- profile — Company or client profile — sector and operating context.
- issue_description — Full description of the reported issue
- severity — Pre-classified severity (Critical/Major/Minor/Low), or leave blank to classify first
- issues — List of issues — one per line or as a numbered list
outputs:
- Ranked table of all issues with severity, SLA, and routing
- Severity level, SLA target, assigned owner, and routing rationale
- issue-note (markdown)
- user-specified output path for triage classification
- user-specified output path for triage table
- '{client.issues}/ISS-{YYYY-MM-DD}-{slug}.md'
prompts:
- Customer issue
- New complaint
- Service failure
---
