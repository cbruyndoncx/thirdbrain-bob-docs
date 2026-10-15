---
description: 'Target Audience: Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.'
title: delay-analysis-tool
---

# delay-analysis-tool

Target Audience: Project schedulers, claims consultants, project directors, and PMC firms performing delay analysis on FIDIC construction projects in UAE/GCC.

| | |
|---|---|
| **Area** | Operations |
| **Category** | engineering |
| **Level** | expert |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [mcp, api-key] |
| **Roles** | [Operations Manager] |

Perform Time Impact Analysis using Critical Path Method to quantify delay events, insert schedule fragnets, and produce contemporaneous delay assessments for FIDIC EOT…

## How you ask

- “Analyze the delay impact of 3 weeks late site access on our critical path”
- “Perform a TIA for the variation order that pushed foundation work back”
- “Compare our as-planned vs as-built schedule for the arbitration claim”
- “We have concurrent delays from both the Employer and our subcontractor — assess entitlement”

## Inputs

- delay-event — Delay event description, dates, affected activities
- schedule-data — Current approved schedule, critical path, activity durations
- as-planned — Original baseline schedule
- as-built — Actual completion dates and sequence
- delay-events — Multiple delay events with dates, causes, and responsible parties

## Outputs

- concurrent-report (markdown)
- delay-report (markdown)
- tia-report (markdown)
- {project-folder}/concurrent_delay_assessment.md
- {project-folder}/delay_analysis_{date}.md
- {project-folder}/tia_report_{date}.md

## Seen in these workflows

- [Delay Analysis Tool](../workflows/delay-analysis-tool.md)

