---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Business Owner Operating System — BOB Workflow
  description: Business Owner Operating System
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-business-owner-operating-system
youtubeId: ''
published: ''
privacy: unlisted
title: Business Owner Operating System
thumbnail: ''
subtitle: Current business state diagnosed, binding constraint identified with evidence, top 3 priorities set, one stop-doing item agreed, routed to the right downstream playbook with owner approval, current-state
  and Founder Command Center updated
inputs: []
outputs: []
steps:
- label: vault-preflight → Confirm required company context and data freshness for Owner OS (profile.md, CURRENT-STATE.md, KPI-REGISTRY.md, latest period-close, pipeline freshness, validator). Abort with
    checklist if missing critical context
  actor: agent
- label: owner-priority-system (diagnose-current-state) → Refresh all KPIs, run data-quality gate, compute health-domain scores, identify binding constraint, draft owner brief. Writes to CURRENT-STATE.md
    + briefs/{date}_owner_brief.md
  actor: agent
- label: Review the diagnosis — confirm business state, binding constraint, and top 3 evidence signals. Override if the routing rule misreads the situation; log the override reason in CURRENT-STATE.md
  actor: human
- label: owner-priority-system (route-next-action) → Look up the routing table for (state × constraint) → playbook. Returns the recommendation with three-line rationale. Honors state-based suppressions
    and data-quality short-circuit
  actor: agent
- label: Approve or override the recommended route — "Run the playbook? (y / n / override)". On override, capture the alternative route + reason. On n, capture the deferred-to date
  actor: human
- label: owner-priority-system (set-priorities) → Translate the (now-approved) route into top 3 priorities for the chosen horizon (pass horizon=weekly or horizon=monthly in the run input), plus exactly
    one stop-doing item and decisions-needed table. Writes to CURRENT-STATE.md and brief
  actor: agent
- label: owner-priority-system (write-state) → Write the agreed state, constraint, priorities, decisions, and recommended route to CURRENT-STATE.md frontmatter. Refresh Founder Command Center signals so
    dashboard reflects today's diagnosis
  actor: agent
- label: Schedule next review — set the appropriate `last_*_review` date and tell the owner when the next cadence layer fires. Hand off to the approved downstream playbook IF owner said y at step 5; otherwise
    stop here
  actor: human
trigger: '"run owner os, what should I focus on, or before any cadence review (annual, quarterly, monthly, weekly)"'
timeSavings: 'Typical run: 30–45 minutes'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'Everything feels urgent.

  One thing is actually the constraint.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---


