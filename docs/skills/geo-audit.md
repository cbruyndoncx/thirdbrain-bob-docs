---
description: 'Analyze any website for Generative Engine Optimization: how well AI platforms can discover, understand, and cite the site''s content. Generates scored reports with prioritized recommendations for improving AI citation rates.'
title: geo-audit
---

# geo-audit

Analyze any website for Generative Engine Optimization: how well AI platforms can discover, understand, and cite the site's content. Generates scored reports with prioritized recommendations for improving AI citation rates.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing seo |
| **Level** | beginner |
| **Input** | url |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing] |

Performs Generative Engine Optimization audits for AI citation across ChatGPT, Perplexity, Gemini, Bing Copilot, and Google AI Overviews.

## How you ask

- “Run a GEO audit on our website for AI visibility”
- “Check how well our site is optimized for AI citations”
- “Audit our brand's presence in ChatGPT and Perplexity results”
- “Generate an llms.txt file for our domain”

## Inputs

- marketing_context — Positioning and messaging context.
- url — Page or site to assess for AI answer-engine visibility
- url — Root domain to assess
- buyer_queries — Buyer-intent queries to test citation against
- url — Site to assess
- platform — The AI answer engine to audit citation visibility on — google-ai-overviews, chatgpt, perplexity, gemini, or copilot; all produces one scorecard per platform plus a cross-platform summary. (google-ai-overviews | chatgpt | perplexity | gemini | copilot | all)
- url — Site to generate llms.txt for
- include_paths — Sections to expose; defaults to public content only
- panel_config — Versioned prompt panel; built on first run if absent
- url — Brand domain being tracked
- platforms — Platforms to run; defaults to the panel config
- runs_per_prompt — Runs per prompt per platform; n>=3, defaults to the panel config
- business_name — Exact canonical business name, used verbatim as question 5
- what_they_sell — What the business sells, in the owner's words — the category questions are built from this
- location — Primary town or region; omit for a pure-online business
- top_competitor — The competitor the owner names first; seeds the alternatives question
- platforms — Platforms to ask; defaults to ChatGPT and Perplexity

## Outputs

- One probe per prompt per platform per repeat, typed `geo-prompt-probe`. Never hand-edited — a probe records that a question was asked and answered.
- Ten named/not-named results plus the single highest-impact fix
- geo-audit-pdf (pdf)
- geo-audit-report (markdown)
- llms-txt (markdown)
- llms-txt-client (markdown)
- prompt-panel-pdf (pdf)
- prompt-panel-report (markdown)
- {output_base}` and `{geo_base}` are the GEO folder of the scope's marketing area (`{company.marketing}/GEO/` or `{client.marketing}/GEO/`); with no vault context `{output_base}` is `{output.scratch}` and the prompt panel does not run. Full layout: references/deliverables_and_reporting.md

