---
description: Orchestrates a comprehensive marketing assessment by running multiple marketing skills in parallel, then merging results into a unified scored report.
title: marketing-report
---

# marketing-report

Orchestrates a comprehensive marketing assessment by running multiple marketing skills in parallel, then merging results into a unified scored report.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing] |

Generates a scored PDF marketing report combining website audit, SEO, CRO, content, social, email, and paid advertising analysis into a single deliverable.

## How you ask

- “Generate a full marketing report for our website”
- “Run a marketing assessment with SEO, CRO, and content scores”
- “Create a marketing scorecard for our client's business”
- “Analyze our marketing performance across all channels”

## Inputs

- url — Domain URL of the website being assessed — every sub-agent analyses this site, and the domain names the report files
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company or client profile.
- icp — ICP for audience and targeting.
- marketing-context — Marketing context for positioning.
- tone-of-voice — Tone of voice guide.

## Outputs

- Phase 2 sub-agent findings, one JSON per category (website-seo-geo, cro, content, social, email-paid), written to `{base_path}/research/` beside the report and read back for scoring and the PDF. Left in place after the run.
- marketing-report-company-markdown (markdown)
- marketing-report-company-pdf (pdf)
- marketing-report-markdown (markdown)
- marketing-report-pdf (pdf)

## Seen in these workflows

- [Full Marketing Analysis in 12 Minutes](../workflows/marketing-report.md)

