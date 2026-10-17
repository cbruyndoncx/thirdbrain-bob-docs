---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Skill Upgrade Cycle — BOB Workflow
  description: Skill Upgrade Cycle
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-skill-upgrade-cycle
youtubeId: ''
published: ''
privacy: unlisted
title: Skill Upgrade Cycle
thumbnail: ''
subtitle: One skill is upgraded with current behavior evidence, validation, and a recorded QMS gate result
inputs:
- label: Skill name and path
  icon: 👤
- label: Reproduced defect or requested improvement
  icon: 📋
- label: Local test command or fixture route
  icon: 🧪
- label: Any owner decision required before behavior or external publication changes
  icon: 📋
outputs: []
steps:
- label: vault-preflight → confirm the skill path, local instructions, current QMS mapping, and available test fixtures
  actor: agent
- label: skillsmith → inspect the current SKILL.md, scripts, references, and existing functional tests
  actor: agent
- label: qms-skill-management → compare the skill against its live CLI/docs and QMS registration
  actor: agent
- label: Apply the smallest scoped patch and run the skill's local test route
  actor: human
- label: vault-validator → validate modified vault notes and generated metadata
  actor: agent
- label: qms-quality → run the QMS gate, save the evidence note, and record follow-up work
  actor: agent
trigger: '"A governed skill needs inspection, patching, verification, and QMS evidence"'
timeSavings: 'Typical run: 45-90 minutes, 1 session'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per trigger event
hook: It worked last quarter. Nobody has checked since.
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: foundational
---


