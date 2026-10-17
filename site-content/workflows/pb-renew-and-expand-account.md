---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Renew And Expand Account
  description: Renew & Expand Account — renewal path and expansion, handled
  socialImage: https://img.youtube.com/vi/VrhtDXKn8IA/maxresdefault.jpg
skillName: pb-renew-and-expand-account
youtubeId: VrhtDXKn8IA
published: '2026-06-29'
privacy: public
title: Renew & Expand Account — renewal path and expansion, handled
thumbnail: https://img.youtube.com/vi/VrhtDXKn8IA/maxresdefault.jpg
subtitle: Renewal path chosen explicitly, expansion opportunity framed commercially, or non-renew branch handled gracefully
inputs:
- label: Client name and `client-id`
  icon: 🏢
- label: Contract / renewal timing or milestone timing
  icon: 📋
- label: Current service scope
  icon: 📋
- label: Known renewal risk or expansion opportunity, if any
  icon: 📝
- label: Revenue at stake and strategic importance
  icon: 📋
outputs:
- label: Renewal Readiness Brief.md
  icon: 📋
- label: Expansion Path Recommendation.md
  icon: 📁
- label: Renewal / Expansion Conversation Script.md
  icon: 📝
- label: Decision Log.md
  icon: 📋
- label: 'If no-renew: Offboarding Branch.md'
  icon: 📋
steps:
- label: vault-preflight → verify client context completeness and confirm there is enough commercial context to make a continuity decision
  actor: agent
- label: client-health-tracker → produce current health snapshot, including at-risk and expansion signals
  actor: agent
- label: 'retention-check → prepare the renewal-readiness brief: value delivered, satisfaction pattern, renewal recommendation, and explicit risks'
  actor: agent
- label: 'Review readiness — decide whether the account is currently in one of three states: `renew`, `renew-expand`, or `non-renew-risk`'
  actor: human
- label: 'client-ascension → if state is `renew` or `renew-expand`, produce the continuity path: ascension map, renewal / expansion script, and recommended commercial structure'
  actor: agent
- label: 'Review continuity path — decide the commercial ask: renew as-is, renew with expansion, restructure, or hold'
  actor: human
- label: Conduct the renewal / expansion conversation or prepare the package for the account owner
  actor: human
- label: 'meeting-intelligence → debrief the continuity conversation: objections, stakeholder signals, pricing pressure, and next-step commitments'
  actor: agent
trigger: '"End of term approaching, continuity decision needed, or account shows credible expansion potential"'
timeSavings: 'Typical run: 2-4 hours across prep, decision, and conversation follow-through'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'The term is ending.

  And nobody has decided what happens next.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Prepares renewal readiness, frames expansion commercially, and handles non-renewals gracefully.

More at brn.cx
