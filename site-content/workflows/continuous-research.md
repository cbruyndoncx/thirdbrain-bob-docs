---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Continuous Research — The market moved
  description: Run recurring research cycles against configurable domain configs. Each cycle discovers new entries, scores them through a weighted quality gate, compares again
  socialImage: https://img.youtube.com/vi/CdGlqzS3AFk/maxresdefault.jpg
skillName: continuous-research
youtubeId: CdGlqzS3AFk
published: '2026-03-27'
privacy: public
title: The market moved.
thumbnail: https://img.youtube.com/vi/CdGlqzS3AFk/maxresdefault.jpg
subtitle: Recurring Intelligence Cycles
inputs:
- label: domain-config.md
  icon: ⚙️
- label: previous_kb_latest.md
  icon: 📊
- label: scoring_calibration.md
  icon: 🎯
outputs:
- label: kb_2026-03-23.md
  icon: 📗
- label: changelog.md
  icon: 📋
- label: inbox_briefing.md
  icon: 📬
- label: report.pdf
  icon: 📕
steps:
- label: Load domain config + previous KB
  actor: agent
- label: nlm-skill → deep research (50-70 sources)
  actor: agent
- label: Import & query NotebookLM notebook
  actor: agent
- label: Map entries → score with calibrated rubric
  actor: agent
- label: Delta detection vs previous cycle
  actor: agent
- label: Review findings, adjust weights
  actor: human
- label: Write KB + changelog + briefing
  actor: agent
trigger: '"Run a research cycle on procurement-ai"'
timeSavings: 8 hours manual research → 15 minutes automated
compounding: Each cycle builds on previous — trends emerge over time
frequency: Weekly per domain (cron scheduled)
hook: 'The market moved.

  You found out three months later.'
outcome: Recurring research cycles — scored, filtered, compared — so you never fall behind.
benefits:
- 32× faster
- Change detection between cycles
- Weighted scoring surfaces what matters
cta: Set up continuous intelligence in 15 minutes
difficulty: advanced
primaryRoles:
- Head of Marketing
- Product Manager
pricingTier: starter
category: research
filterGroup: research
area: research
---

Run recurring research cycles against configurable domain configs. Each cycle discovers new entries, scores them through a weighted quality gate, compares against the previous knowledge base, and writes an updated KB with a change delta.

The market moved.

Recurring research cycles — scored, filtered, compared — so you never fall behind.
