---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: demo-script — ThirdBrain BOB skill
  description: Create sales demo scripts that solve buyer problems instead of touring features. A demo is a story — the prospect's story — with your product as the turning poi
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: demo-script
catLabel: sales
area: sales
desc: Create tailored sales demo scripts structured around buyer pain points.
summary: Create sales demo scripts that solve buyer problems instead of touring features. A demo is a story — the prospect's story — with your product as the turning point. Every feature shown connects to a pain the prospect stated in discovery.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- client_company_overview — Client company profile — name, industry, size, offering, key contacts. Read when the request is client-scoped; the route asks the user when absent.
- icp — Ideal customer profile — who the output targets.
- offerings — Offerings catalogue — what is being sold.
- profile — Company or client profile — entity and relationship context.
- client_id — Client or prospect identifier (kebab-case)
- prospect_slug — Short identifier for the prospect contact or company (kebab-case)
- demo_duration — 20min, 30min, 45min, or 60min (default 30min) (20min | 30min | 45min | 60min)
- demo_format — live, slide-supported, or recorded (default live) (live | slide-supported | recorded)
outputs:
- Complete demo script with all required sections
- '{client.sales}/demos/{prospect-slug}_demo_script_{YYYY-MM-DD}.md'
prompts:
- Write a demo script for the Acme Corp prospect — 30 minutes, live format
- Prep a demo for Rachel Kim at GlobalTech, she's evaluating us against Salesforce
- Create a recorded demo walkthrough for the decision makers who missed the live call
- Build a slide-supported demo script for the executive presentation next Tuesday
---
