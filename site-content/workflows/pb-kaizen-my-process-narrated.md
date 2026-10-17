---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Kaizen My Process Narrated — BOB Workflow
  description: Kaizen My Process Narrated
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-kaizen-my-process-narrated
youtubeId: ''
published: ''
privacy: unlisted
title: Kaizen My Process Narrated
thumbnail: ''
subtitle: Prioritized, stakeholder-vetted improvement backlog with a visual process map, PDCA + 5S artifacts, an improved SOP, and a re-baseline cadence
inputs:
- label: Process name and a description or link to its current documentation
  icon: 📄
- label: Improvement goal (single, concrete)
  icon: 🎯
- label: Process owner + key participants
  icon: 📋
- label: Any known pain points / recent failures
  icon: 📋
- label: Cadence for the re-baseline (e.g. quarterly)
  icon: 📋
outputs: []
steps:
- label: business-baseline → map the target process as a swimlane; flag bottlenecks and candidate waste
  actor: agent
- label: Confirm the map and set the explicit improvement goal; correct any inaccuracies
  actor: human
- label: process-kaizen (waste-audit) → classify the flags into the 8 Lean wastes, estimate annual cost, write audit-waste findings + a gemba-walk guide
  actor: agent
- label: ask-boardroom → convene a 5-expert panel (role · interests · concerns) to critique the process from diverse lenses; one stakeholder per pass
  actor: agent
- label: prioritization-craft → vet the full idea list (panel critique + waste findings) down to the top 5–10 improvements ranked against the goal
  actor: agent
- label: Select which improvements to implement now vs. backlog
  actor: human
- label: process-kaizen (improvement-kit) → produce the 5S checklist, PDCA (Plan-Do-Check-Act) cycle, and standard-work doc for the process
  actor: agent
- label: playbook-runner → capture the improved process as an SOP / recurring playbook so the gain is standardized
  actor: agent
- label: scheduled-jobs → schedule a re-baseline TaskNote to re-run step 1 next cycle and measure the delta
  actor: agent
trigger: '"Owner or client wants to systematically improve a specific documented process (continuous improvement / Kaizen)"'
timeSavings: 'Typical run: 2-4 hours, multi-session'
compounding: Each run refines templates and context — 7 automated steps improve with accumulated data
frequency: Per trigger event
hook: ''
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: operations
---


