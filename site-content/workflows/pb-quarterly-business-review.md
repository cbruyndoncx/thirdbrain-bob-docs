---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Quarterly Business Review — Quarter ended
  description: Quarter ended.
  socialImage: https://img.youtube.com/vi/7R2CXx50BBQ/maxresdefault.jpg
skillName: pb-quarterly-business-review
youtubeId: 7R2CXx50BBQ
published: '2026-03-31'
privacy: public
title: Quarter ended.
thumbnail: https://img.youtube.com/vi/7R2CXx50BBQ/maxresdefault.jpg
subtitle: QBR with performance trends, ROI evidence, and next-quarter plan
inputs:
- label: Client name
  icon: 🏢
- label: Quarter being reviewed (e.g. Q1 2026)
  icon: 📅
- label: Key wins and challenges to highlight
  icon: 💡
outputs:
- label: Quarter session and deliverable metrics
  icon: 📊
- label: Financial ROI analysis
  icon: 💰
- label: Score comparison vs prior baselines
  icon: 📈
- label: QBR executive summary
  icon: 📄
steps:
- label: ai-work-audit → aggregate sessions and deliverables for quarter
  actor: agent
- label: business-reporting → financial cohort analysis and ROI
  actor: agent
- label: Review metrics — confirm accuracy, add business context
  actor: human
- label: marketing-report → compare scores vs prior quarter baselines
  actor: agent
- label: exec-comms → draft QBR executive summary (SCQA)
  actor: agent
- label: Review QBR, personalize next-quarter recommendations
  actor: human
trigger: '"End of quarter — prepare the QBR"'
timeSavings: ~6 hrs manual QBR prep → ~2 hrs automated (3× faster)
compounding: Each QBR builds on prior baselines — trend visibility improves every quarter
frequency: Quarterly per client
hook: 'Quarter ended.

  No review. No trends. No plan for the next one.'
outcome: QBR with performance trends, ROI evidence, and a next-quarter action plan.
benefits:
- 3× faster
- Trends visible across quarters
- Next-quarter plan built into the review
cta: Prepare your QBR in 2 hours
category: ''
filterGroup: strategy
area: strategy
---

Quarter ended.

QBR with performance trends, ROI evidence, and a next-quarter action plan.
