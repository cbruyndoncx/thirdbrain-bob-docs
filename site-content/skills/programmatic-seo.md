---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: programmatic-seo — ThirdBrain BOB skill
  description: Build SEO-optimized pages at scale using templates and data. Create pages that rank, provide value, and avoid thin content penalties.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: programmatic-seo
catLabel: marketing-seo
area: marketing
desc: Generates template-based pages at scale, creates dynamic meta tags and URL structures from data sources, builds hub-and-spoke internal linking, and publishes to…
summary: Build SEO-optimized pages at scale using templates and data. Create pages that rank, provide value, and avoid thin content penalties.
difficulty: advanced
inputType: url
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- url — Site base URL the pages publish under — sets `site.url` in the project config (`pseo_init.py --url`) and the sitemap `--base-url`
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- marketing-context — Marketing context for content strategy.
- icp — ICP — defines search intent and page audience. Company uses icp.md; clients use ideal_customer_profiles_index.md.
- target-audience — Audience + positioning context (Target Audience / Customer Language sections) for page angles and keywords.
outputs:
- generated-pages (markdown)
- hub-pages (markdown)
- prefer a permanent directory)
- pseo-strategy (markdown)
- pseo-strategy-scratch (markdown)
- review-report (markdown)
- sitemap (xml)
- '{scope.marketing.seo}/programmatic/{project-name}/generated/{slug}.md'
- '{scope.marketing.seo}/programmatic/{project-name}/hubs/{category-slug}.md'
- '{scope.marketing.seo}/programmatic/{project-name}/pseo-strategy-{pattern}-{YYYY-MM-DD}.md'
- '{scope.marketing.seo}/programmatic/{project-name}/review-report-{YYYY-MM-DD}.md'
- '{scope.marketing.seo}/programmatic/{project-name}/sitemap.xml'
prompts:
- Create template pages for our city-specific landing pages
- Build location pages at scale for our service business
- Generate comparison pages for our top 50 competitors
- Set up hub-and-spoke internal linking for our directory
---
