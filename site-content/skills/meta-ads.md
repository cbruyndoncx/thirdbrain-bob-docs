---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: meta-ads — ThirdBrain BOB skill
  description: Governed interface for Meta Ads Manager automation. This initial scaffold defines the safety contract and workflow boundary; it does not install credentials, ca
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: meta-ads
catLabel: marketing-ads
area: marketing
desc: Prepares Meta Ads dry-run campaign plans from approved strategy and creative inputs and analyzes user-supplied performance exports.
summary: Governed interface for Meta Ads Manager automation. This initial scaffold defines the safety contract and workflow boundary; it does not install credentials, call live mutation endpoints, or launch campaigns.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[paid-ads, ad-creative]'
roles: '[]'
inputs:
- paid-ads-strategy — Approved strategy from the paid-ads skill with objective, audience, budget, and measurement logic.
- creative-brief — Approved creative variants and asset references from ad-creative.
- account-context — Ad account, page, pixel, offer, and destination identifiers supplied without secrets.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- performance-export — User-supplied Meta Ads performance export with spend and outcome metrics.
- campaign-plan — Campaign plan containing objective, budget assumptions, and measurement definitions.
outputs:
- campaign-dry-run (markdown)
- performance-analysis (markdown)
- '{scope.marketing.sea}/campaigns/meta-{campaign}-{YYYY-MM-DD}.md'
- '{scope.marketing.sea}/reports/meta-{campaign}-{YYYY-MM-DD}.md'
prompts:
- Prepare a paused Meta Ads campaign plan from this strategy and creative brief; do not call Meta.
- Analyze this Meta Ads export and recommend pause, hold, or scale without changing the account.
- Check whether this Meta campaign plan has every identifier and approval needed for a future dry run.
---
