---
description: Plan content that drives traffic, builds authority, and generates leads.
title: content-strategy
---

# content-strategy

Plan content that drives traffic, builds authority, and generates leads.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Creates topic clusters, maps content to buyer journey stages, identifies content gaps through competitor analysis, and prioritizes content opportunities by scoring…

## How you ask

- “Create a topic cluster strategy for our blog”
- “Map our content to buyer journey stages”
- “Identify content gaps through competitor analysis”
- “What should I write about next for our SaaS blog?”

## Inputs

- url — Website URL to analyze for existing content coverage and product/audience fit when building pillars and topic clusters.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- marketing-context — Positioning, narrative, and competitive frame used to set content angle and pillar themes.
- icp — Buyer profile used to map topics to buyer-journey stages and weight customer-impact scoring. Company uses icp.md; clients use ideal_customer_profiles_index.md.
- target-audience — Audience and customer-language context used to prioritize topic clusters against real buyer language.
- tone-of-voice — Editorial register the recommended pillars and topics must be written to match.
- url — Website whose existing content is being audited for optimization opportunities.
- performance-data — Search Console or Analytics export (clicks, impressions, CTR, position, sessions) scored into performance quadrants. Absent, the audit falls back to manual signals (site-prefixed searches, social shares, backlink counts).
- icp — ICP/persona document whose pains and language anchor the trend hunt when the user doesn't supply topics directly.
- topics-or-links — Topics, keywords, links, or thread summaries to mine for trends. Absent, trend hunting runs against the ICP's pains instead.
- keyword-data — Keyword export (Ahrefs / SEMrush / GSC) clustered by topic, buyer stage, intent, and quick wins.
- url — Website compared against competitor content to find coverage gaps.
- marketing-context — Named competitors and positioning that set the comparison set for the gap matrix.

## Outputs

- Content pillars with rationale, prioritized topic list scored on customer impact / content-market fit / search potential / resources, and the topic cluster map.
- Gap matrix scoring competitor topics you don't cover, quick-win keyword clusters (positions 11-20), and validated content gaps with priority.
- Myth vs Reality, Common Mistakes, Framework, Case Snippet, Tooling, Future Lens.
- Prioritized list of existing content by URL and current metrics, performance quadrant, opportunity type (CTR / ranking / conversion / refresh / consolidation), specific action, expected impact, and effort required.
- {scope.marketing.seo}/strategy/content-strategy-{YYYY-MM-DD}.md

## Seen in these workflows

- [What should we write about?](../../workflows/marketing/content-strategy.md)

