---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: gtm-tagging — ThirdBrain BOB skill
  description: Comprehensive GTM reference covering container setup, tags, triggers, variables, data layer implementation, debugging, custom templates, and API automation.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: gtm-tagging
catLabel: marketing-analytics
area: marketing
desc: Configures Google Tag Manager and GA4 containers, tags, triggers, variables, and debugging.
summary: Comprehensive GTM reference covering container setup, tags, triggers, variables, data layer implementation, debugging, custom templates, and API automation.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[Head of Marketing]'
inputs:
- profile — The company profile (`company.profile`) — business model, product type
- tracking-plan — Latest tracking plan from analytics-tracking (`analytics/tracking-plan-{YYYY-MM-DD}.md` under `company.marketing` or `client.marketing`), if any
- url — Website URL the container is installed on, when the task concerns a specific site
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- Fallback only — used when no company or client scope is resolved
- gtm-datalayer (markdown)
- gtm-setup (markdown)
- gtm-tags (markdown)
prompts:
- Set up a new GTM container for our website
- Create a custom tag template in Google Tag Manager
- Debug why my GTM trigger isn't firing on form submissions
- Configure data layer variables for our e-commerce tracking
---
