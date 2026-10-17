---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: seo-content-machine — ThirdBrain BOB skill
  description: 'Full-stack SEO content pipeline: research, write, optimize, score, and publish.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: seo-content-machine
catLabel: marketing-seo
area: marketing
desc: Runs an end-to-end SEO content pipeline for WordPress.
summary: 'Full-stack SEO content pipeline: research, write, optimize, score, and publish.'
difficulty: advanced
inputType: url
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- url — Target site URL — the site whose content is researched, rewritten, audited or published (performance research reads it as GSC_SITE_URL)
- scope — `company`, or a client-id under the client root (`client.root`) — a string with one reserved value, not a closed set
- marketing-context — Consolidated marketing context — one file with Target Audience, Customer Language, Differentiation, Problems & Pain Points, and Proof Points sections (assembled by product-marketing-context).
- icp — Deep ICP — buyer profile, scoring, and buying journey. Company uses icp.md; clients use ideal_customer_profiles_index.md (per-segment ICP files).
- brand-voice — Locked brand/tone-of-voice for on-voice drafting.
outputs:
- seo-content-draft (markdown)
- seo-content-draft-client (markdown)
- seo-content-research (markdown)
- seo-content-research-client (markdown)
- '{client.marketing.seo}/drafts/{topic-slug}-{YYYY-MM-DD}.md'
- '{client.marketing.seo}/research/brief-{topic-slug}-{YYYY-MM-DD}.md'
- '{company.marketing.seo}/drafts/{topic-slug}-{YYYY-MM-DD}.md'
- '{company.marketing.seo}/research/brief-{topic-slug}-{YYYY-MM-DD}.md'
prompts:
- Research keywords and write an optimized blog post
- Create an SEO-optimized landing page for our target keyword
- Analyze the SEO performance of our existing blog content
- Publish this article to WordPress with Yoast optimization
- Rewrite this blog based on the audit report
- The audit scored this 6.2 — rewrite targeting the weak areas
---
