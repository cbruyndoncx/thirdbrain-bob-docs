---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Fix My Marketing — BOB Workflow
  description: Fix My Marketing
  socialImage: https://img.youtube.com/vi/GswU6hTvq2U/maxresdefault.jpg
skillName: pb-fix-my-marketing
youtubeId: GswU6hTvq2U
published: '2026-08-01'
privacy: public
title: Fix My Marketing
thumbnail: https://img.youtube.com/vi/GswU6hTvq2U/maxresdefault.jpg
subtitle: Scored marketing audit + 60-day content and visibility plan with first articles drafted
inputs:
- label: Website URL
  icon: 🌐
- label: Social media profile URLs (LinkedIn, Instagram, Facebook, X, TikTok, YouTube)
  icon: 🌐
- label: Current marketing spend and channels (if known)
  icon: 📋
- label: Target audience or ICP description
  icon: 🎯
- label: Key competitors (2-3 names or URLs)
  icon: 🌐
- label: Specific pain points or focus areas (optional)
  icon: 📦
outputs:
- label: Marketing Audit.pdf
  icon: 📊
- label: Gap List.md
  icon: 📋
- label: Content Strategy.md
  icon: ✏️
- label: Social Calendar.md
  icon: 📱
- label: 3 Priority Articles.md
  icon: ✏️
steps:
- label: vault-preflight → verify client context completeness and flag blocking gaps before proceeding
  actor: agent
- label: product-marketing-context → establish or verify marketing foundation
  actor: agent
- label: brand-voice-generator → establish or verify brand voice guidelines
  actor: agent
- label: website-audit → full SEO + GEO site analysis
  actor: agent
- label: social-media-audit → platform-level social presence audit
  actor: agent
- label: marketing-report → merge all findings into scored report + PDF
  actor: agent
- label: Review audit results — prioritize gaps and set focus areas
  actor: human
- label: content-strategy → 60-day topic clusters and content calendar from audit gaps
  actor: agent
- label: social-content → 60-day social posting calendar aligned to strategy
  actor: agent
- label: Review plan — approve topics and select quick-win pieces to draft
  actor: human
- label: seo-content-machine → draft first 3 priority articles from plan
  actor: agent
- label: content-scorer → quality gate all drafts ≥ 70
  actor: agent
trigger: '"New client or own business needs a marketing health check and action plan"'
timeSavings: 'Typical run: 3-5 hours active, 1-2 sessions'
compounding: Each run refines templates and context — 10 automated steps improve with accumulated data
frequency: Monthly or per campaign
hook: 'Your marketing needs fixing.

  But nobody can tell you which part.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: marketing
---

Scored marketing audit + 60-day content and visibility plan with first articles drafted


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
