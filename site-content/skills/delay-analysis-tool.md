---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: delay-analysis-tool — ThirdBrain BOB skill
  description: 'Target Audience: Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: delay-analysis-tool
catLabel: engineering
area: operations
desc: Perform Time Impact Analysis using Critical Path Method to quantify delay events, insert schedule fragnets, and produce contemporaneous delay assessments for FIDIC EOT…
summary: 'Target Audience: Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.'
difficulty: expert
inputType: conversation
outputType: document
requires: '[mcp, api-key]'
roles: '[Operations Manager]'
inputs:
- delay-event — Delay event description, dates, affected activities
- schedule-data — Current approved schedule, critical path, activity durations
- as-planned — Original baseline schedule
- as-built — Actual completion dates and sequence
- delay-events — Multiple delay events with dates, causes, and responsible parties
outputs:
- concurrent-report (markdown)
- delay-report (markdown)
- tia-report (markdown)
- '{project-folder}/concurrent_delay_assessment.md'
- '{project-folder}/delay_analysis_{date}.md'
- '{project-folder}/tia_report_{date}.md'
prompts:
- Analyze the delay impact of 3 weeks late site access on our critical path
- Perform a TIA for the variation order that pushed foundation work back
- Compare our as-planned vs as-built schedule for the arbitration claim
- We have concurrent delays from both the Employer and our subcontractor — assess entitlement
---
