---
description: Produce high-performing ad creative at scale — headlines, descriptions, and primary text designed to drive clicks and conversions — and refine based on actual performance metrics.
title: ad-creative
---

# ad-creative

Produce high-performing ad creative at scale — headlines, descriptions, and primary text designed to drive clicks and conversions — and refine based on actual performance metrics.

- **Area:** Marketing
- **Category:** marketing ads
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing

Writes ad copy for Google Ads, Meta, and LinkedIn — headlines, descriptions, primary text, and full variations.

## How you ask

- “Generate Google RSA headlines for our SaaS free trial campaign”
- “Write 20 Meta ad variations for our product launch”
- “Iterate on these LinkedIn ad results — here's the performance data”
- “Bulk produce 50 headline variations across 5 angles for Google Ads”

## Inputs

- platform — Target platform — Google RSA, Meta, LinkedIn, TikTok, X (google-rsa | meta | linkedin | tiktok | x)
- product-context — Product canonical record — features, pricing, positioning.
- audience — Target audience and intent
- constraints — Tone, compliance, or format constraints
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- icp — ICP — buyer persona for ad angle and pain framing.
- tone-of-voice — Tone of voice — keeps ad register on-brand.
- performance-data — Campaign metrics — CTR, conversions, impressions per ad
- existing-copy — Current ad copy with associated metrics
- platform — Target platform (google-rsa | meta | linkedin | tiktok | x)
- platform — Target platform and format requirements (google-rsa | meta | linkedin | tiktok | x)
- count — Number of variations needed

## Outputs

- ad-creative-set (markdown)
- bulk-creative (markdown)
- csv-upload (csv)
- iteration-report (markdown)
- {scope.marketing.sea}/creatives/ad-bulk-{campaign}-{YYYY-MM-DD}.csv
- {scope.marketing.sea}/creatives/ad-bulk-{campaign}-{YYYY-MM-DD}.md
- {scope.marketing.sea}/creatives/ad-creative-{campaign}-{YYYY-MM-DD}.md
- {scope.marketing.sea}/creatives/ad-iteration-{campaign}-{YYYY-MM-DD}.md

