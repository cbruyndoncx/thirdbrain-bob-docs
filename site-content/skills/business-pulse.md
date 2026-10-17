---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: business-pulse — ThirdBrain BOB skill
  description: One prompt, one page. Pull live data from every connected source, synthesize it into a single scannable brief, and surface the single most important thing to ac
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: business-pulse
catLabel: business
area: strategy
desc: Produces a one-page cross-functional business snapshot — cash position (QuickBooks), pipeline movement (HubSpot), this week's commitments (Google Calendar), urgent…
summary: One prompt, one page. Pull live data from every connected source, synthesize it into a single scannable brief, and surface the single most important thing to act on today. Do the work — do not ask the owner to help find the data.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[CEO / Founder, Operations Manager, Finance Manager]'
inputs:
- current-state — Business health state and binding constraint.
- kpi-reports — KPI values refreshed by the weekly KPI Weekly Refresh scheduled-run TaskNote; this is not a direct KPI cron job.
- profile — Company or client profile — entity and relationship context.
- trigger — 'pulse', 'snapshot', 'how are we doing', 'catch me up'
- trigger — 'Monday brief', 'start of week', 'what's coming this week'
- trigger — 'Friday brief', 'end of week', 'wrap up', 'weekly close'
- trigger — 'quarterly review', 'QBR', 'quarter check'
outputs:
- CURRENT-STATE writeback per the cadence-writeback contract — appended/refreshed after saving.
- pulse_note (markdown)
- '{company.management}/CURRENT-STATE.md'
- '{me.inbox}/pulse-QBR-{YYYY-Qn}.md'
- '{me.inbox}/pulse-friday-{YYYY-MM-DD}.md'
- '{me.inbox}/pulse-monday-{YYYY-MM-DD}.md'
- '{me.inbox}/pulse-{YYYY-MM-DD}.md'
prompts:
- How are we doing
- Monday brief
- Friday brief
---
