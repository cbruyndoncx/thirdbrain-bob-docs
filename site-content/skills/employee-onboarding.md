---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: employee-onboarding — ThirdBrain BOB skill
  description: Create practical onboarding materials that get a new hire productive fast — without requiring an HR system or enterprise process.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: employee-onboarding
catLabel: human-resources
area: people
desc: Creates employee onboarding checklists, first-week schedules, tool setup guides, role clarity documents, and 30/60/90 day plans as markdown files.
summary: Create practical onboarding materials that get a new hire productive fast — without requiring an HR system or enterprise process.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[HR Manager]'
inputs:
- role — Job title and brief description of the role
- start_date — Employee start date (YYYY-MM-DD)
- team_context — Team size, direct manager name, key colleagues
- profile — Company profile — mission and stage for onboarding framing.
- tone-of-voice — Tone of voice — onboarding doc register matches brand.
- priorities — Top 3 outcomes the hire needs to own within 90 days
- team_context — Team context, manager expectations, company stage
- role — Job title (determines which tools are relevant)
- tools — List of tools the team uses (e.g. Slack, Notion, GitHub, HubSpot)
outputs:
- first_week_plan (markdown)
- ninety_day_plan (markdown)
- tool_setup_guide (markdown)
- '{client.hr}/onboarding/{role}-90day-plan-{YYYY-MM-DD}.md'
- '{client.hr}/onboarding/{role}-first-week-{YYYY-MM-DD}.md'
- '{client.hr}/onboarding/{role}-tool-setup.md'
prompts:
- New hire onboarding
- First-week plan
- Tool setup
---
