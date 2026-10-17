---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Supplier Review Renewal — Supplier contract renewing
  description: Supplier contract renewing.
  socialImage: https://img.youtube.com/vi/p8t7D-tMw-A/maxresdefault.jpg
skillName: pb-supplier-review-renewal
youtubeId: p8t7D-tMw-A
published: '2026-04-01'
privacy: public
title: Supplier contract renewing.
thumbnail: https://img.youtube.com/vi/p8t7D-tMw-A/maxresdefault.jpg
subtitle: Supplier performance assessed, renewal decision made, next steps actioned
inputs:
- label: Supplier ID(s) to review
  icon: 🏢
- label: Review period (e.g. Q1 2026)
  icon: 📅
- label: Performance incidents to note
  icon: ⚠️
outputs:
- label: Performance scorecard with trends
  icon: 📊
- label: Contract lifecycle assessment
  icon: 📋
- label: Renewal recommendation
  icon: 🔄
- label: Negotiation brief or RFx (if needed)
  icon: 📄
steps:
- label: supplier-feedback → 5-dimension performance scorecard
  actor: agent
- label: Review scores, compare to prior periods, flag concerns
  actor: human
- label: strategic-sourcing → contract lifecycle check, Kraljic reassessment
  actor: agent
- label: 'Decide: renew, renegotiate, recompete, or terminate'
  actor: human
- label: strategic-sourcing → prepare negotiation brief or new RFx
  actor: agent
trigger: '"Quarterly review or contract expiring within 90 days"'
timeSavings: ~3 hrs manual → ~1 hr automated (3× faster)
compounding: Scorecard history reveals trends — poor performers flagged before renewal
frequency: Quarterly per supplier
hook: 'Supplier contract renewing.

  But you have no data on whether they''re actually good.'
outcome: Performance assessed, renewal decision made, next steps actioned.
benefits:
- 3× faster
- Scorecard history shows trends
- Renewal decisions backed by evidence
cta: Review your supplier in 1 hour
category: ''
filterGroup: operations
area: operations
---

Supplier contract renewing.

Performance assessed, renewal decision made, next steps actioned.
