---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: marketing-report — ThirdBrain BOB skill
  description: Orchestrates a comprehensive marketing assessment by running multiple marketing skills in parallel, then merging results into a unified scored report.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: marketing-report
catLabel: marketing-content
area: marketing
desc: Generates a scored PDF marketing report combining website audit, SEO, CRO, content, social, email, and paid advertising analysis into a single deliverable.
summary: Orchestrates a comprehensive marketing assessment by running multiple marketing skills in parallel, then merging results into a unified scored report.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- url — Domain URL of the website being assessed — every sub-agent analyses this site, and the domain names the report files
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company or client profile.
- icp — ICP for audience and targeting.
- marketing-context — Marketing context for positioning.
- tone-of-voice — Tone of voice guide.
outputs:
- Phase 2 sub-agent findings, one JSON per category (website-seo-geo, cro, content, social, email-paid), written to `{base_path}/research/` beside the report and read back for scoring and the PDF. Left in place after the run.
- marketing-report-company-markdown (markdown)
- marketing-report-company-pdf (pdf)
- marketing-report-markdown (markdown)
- marketing-report-pdf (pdf)
prompts:
- Generate a full marketing report for our website
- Run a marketing assessment with SEO, CRO, and content scores
- Create a marketing scorecard for our client's business
- Analyze our marketing performance across all channels
---
