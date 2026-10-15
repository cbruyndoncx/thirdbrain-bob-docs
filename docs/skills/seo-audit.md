---
description: Analyze any website for search engine optimization issues, generate scored reports with prioritized recommendations, and benchmark against competitors — all without requiring external API keys.
title: seo-audit
---

# seo-audit

Analyze any website for search engine optimization issues, generate scored reports with prioritized recommendations, and benchmark against competitors — all without requiring external API keys.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing seo |
| **Level** | beginner |
| **Input** | url |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing] |

Audits SEO with technical checks, on-page optimization, content quality, structured data, performance, competitor analysis, and local search presence.

## How you ask

- “Run a comprehensive SEO audit on our website”
- “Check our technical SEO health and find critical issues”
- “Audit our on-page optimization and content quality”
- “Analyze our search performance and competitor rankings”
- “Run a local SEO audit — why don't we show up in the map pack?”
- “Check our NAP consistency — we changed phone numbers last month”

## Inputs

- url — Page or site URL to audit
- url — Root domain to crawl
- max_pages — Crawl ceiling; keeps runtime bounded on large sites
- url — Own site URL
- competitor_urls — Competitor domains to benchmark against
- url — Site to assess for AI answer-engine citability
- buyer_queries — Buyer-intent queries to test citation against
- baseline_audit — Earlier audit report to compare against
- current_audit — Later audit report; runs a fresh audit when omitted
- audit_report — Audit markdown report to render as PDF
- url — Business website URL
- business_name — Exact canonical business name
- location — Primary city/region plus service area
- persona — Buyer persona lens (path or free text) — reuses website-audit's resolution chain
- business_name — Exact canonical business name as it appears on the profile
- location — Primary city/region
- url — Website URL — only needed to check the profile's website link resolves

## Outputs

- Seven pass/fail lines plus the single highest-impact fix
- ai-visibility-report (markdown)
- ai-visibility-report-client (markdown)
- competitor-seo-report (markdown)
- competitor-seo-report-client (markdown)
- full-seo-report (markdown)
- full-seo-report-client (markdown)
- geo-domain-changes (excalidraw)
- local-seo-audit (markdown)
- nap-check (markdown)
- projected-gains (excalidraw)
- quick-seo-report (markdown)
- quick-seo-report-client (markdown)
- seo-comparison-report (markdown)
- seo-comparison-report-client (markdown)
- seo-domain-changes (excalidraw)
- seo-pdf-report (pdf)
- seo-pdf-report-client (pdf)

