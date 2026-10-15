---
description: Create sales demo scripts that solve buyer problems instead of touring features. A demo is a story — the prospect's story — with your product as the turning point. Every feature shown connects to a pain the prospect stated in discovery.
title: demo-script
---

# demo-script

Create sales demo scripts that solve buyer problems instead of touring features. A demo is a story — the prospect's story — with your product as the turning point. Every feature shown connects to a pain the prospect stated in discovery.

| | |
|---|---|
| **Area** | Sales & Clients |
| **Category** | sales |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Sales] |

Create tailored sales demo scripts structured around buyer pain points.

## How you ask

- “Write a demo script for the Acme Corp prospect — 30 minutes, live format”
- “Prep a demo for Rachel Kim at GlobalTech, she's evaluating us against Salesforce”
- “Create a recorded demo walkthrough for the decision makers who missed the live call”
- “Build a slide-supported demo script for the executive presentation next Tuesday”

## Inputs

- client_company_overview — Client company profile — name, industry, size, offering, key contacts. Read when the request is client-scoped; the route asks the user when absent.
- icp — Ideal customer profile — who the output targets.
- offerings — Offerings catalogue — what is being sold.
- profile — Company or client profile — entity and relationship context.
- client_id — Client or prospect identifier (kebab-case)
- prospect_slug — Short identifier for the prospect contact or company (kebab-case)
- demo_duration — 20min, 30min, 45min, or 60min (default 30min) (20min | 30min | 45min | 60min)
- demo_format — live, slide-supported, or recorded (default live) (live | slide-supported | recorded)

## Outputs

- Complete demo script with all required sections
- {client.sales}/demos/{prospect-slug}_demo_script_{YYYY-MM-DD}.md

