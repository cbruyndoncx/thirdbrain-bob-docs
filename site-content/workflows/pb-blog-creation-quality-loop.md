---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Blog Creation Quality Loop — BOB Workflow
  description: Blog Creation Quality Loop
  socialImage: https://img.youtube.com/vi/Y32W6AVe2Sw/maxresdefault.jpg
skillName: pb-blog-creation-quality-loop
youtubeId: Y32W6AVe2Sw
published: '2026-08-01'
privacy: public
title: Blog Creation Quality Loop
thumbnail: https://img.youtube.com/vi/Y32W6AVe2Sw/maxresdefault.jpg
subtitle: Publication-ready blog that passes both content quality and business asset audit
inputs:
- label: Blog topic or target keyword
  icon: 🔍
- label: Business goal (traffic, leads, authority, sales support)
  icon: 🏢
- label: Target audience
  icon: 🎯
- label: Funnel stage (awareness, consideration, conversion)
  icon: 📋
- label: CTA goal (book call, contact form, download, etc.)
  icon: 🎙️
- label: 'Scope: company or client-id'
  icon: 🏢
outputs:
- label: Blog Article.md
  icon: ✏️
- label: Quality Scorecard.md
  icon: 📊
- label: Audit Report.md
  icon: 📊
- label: Social Posts.md
  icon: 📱
- label: Published URL
  icon: 🌐
steps:
- label: vault-preflight → verify client/company context completeness and flag blocking gaps
  actor: agent
- label: seo-content-machine → research keywords + write article
  actor: agent
- label: content-scorer → scrub AI patterns and score content quality
  actor: agent
- label: content-scorer (blog-business-audit) → audit blog as a business asset, full mode
  actor: agent
- label: 'Review audit report — decide: publish, polish, or rewrite'
  actor: human
- label: seo-content-machine (rewrite-from-audit) → rewrite targeting audit weaknesses, skip if score >= 7.5
  actor: agent
- label: content-scorer (blog-business-audit) → re-audit rewritten blog, confirm score improved
  actor: agent
- label: Review final draft and approve
  actor: human
- label: social-content → LinkedIn + X posts from final article
  actor: agent
- label: wordpress-publisher → publish article
  actor: agent
trigger: '"Write a blog post and make sure it''s good"'
timeSavings: 'Typical run: 2-3 hours, 1-2 sessions'
compounding: Each run refines templates and context — 8 automated steps improve with accumulated data
frequency: Per content cycle
hook: 'The post is written.

  Whether it''s any good is a matter of opinion.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: marketing
---

Publication-ready blog that passes both content quality and business asset audit


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
