---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: New Supplier Onboarding — New supplier
  description: New supplier.
  socialImage: https://img.youtube.com/vi/vRWRL3MV8i4/maxresdefault.jpg
skillName: pb-new-supplier-onboarding
youtubeId: vRWRL3MV8i4
published: '2026-03-30'
privacy: public
title: New supplier.
thumbnail: https://img.youtube.com/vi/vRWRL3MV8i4/maxresdefault.jpg
subtitle: Supplier profiled, evaluated, contracted, and ready for first PO
inputs:
- label: Supplier company name and website
  icon: 🏢
- label: Services/products to be provided
  icon: 📦
- label: Expected annual spend and terms
  icon: 💰
outputs:
- label: Supplier profile with contacts
  icon: 👤
- label: Kraljic classification
  icon: 📊
- label: Contract checklist review
  icon: ✅
- label: Ready-for-PO supplier record
  icon: 📄
steps:
- label: Create supplier profile in 20-COMPANY/30-SUPPLIERS/
  actor: agent
- label: strategic-sourcing → classify supplier using Kraljic matrix
  actor: agent
- label: strategic-sourcing → generate RFx or negotiation brief
  actor: agent
- label: Negotiate terms, sign contract, agree pricing and SLA
  actor: human
- label: strategic-sourcing → run contract checklist review
  actor: agent
- label: Update supplier profile with contract terms, prepare for first PO
  actor: agent
trigger: '"Decision to engage a new supplier"'
timeSavings: ~4 hrs manual → ~1 hr automated (4× faster)
compounding: Supplier profiles and Kraljic data build procurement intelligence
frequency: Per new supplier
hook: 'New supplier.

  No profile. No evaluation. No contract terms documented.'
outcome: Supplier profiled, evaluated, contracted, and ready for the first PO.
benefits:
- 4× faster
- Evaluation scorecard — not gut feel
- Contract terms documented from day one
cta: Onboard a new supplier in 1 hour
category: ''
filterGroup: operations
area: operations
---

New supplier.

Supplier profiled, evaluated, contracted, and ready for the first PO.
