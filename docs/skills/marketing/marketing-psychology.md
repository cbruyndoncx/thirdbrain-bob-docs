---
description: Apply psychological principles and mental models to marketing. Help users understand why people buy, influence behavior ethically, and make better marketing decisions.
title: marketing-psychology
---

# marketing-psychology

Apply psychological principles and mental models to marketing. Help users understand why people buy, influence behavior ethically, and make better marketing decisions.

- **Area:** Marketing
- **Category:** marketing strategy
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Identifies relevant cognitive biases for campaigns, recommends persuasion frameworks, analyzes messaging through behavioral science lens.

## How you ask

- “Which cognitive biases can we leverage in our pricing page?”
- “Apply behavioral science to improve our signup flow messaging”
- “Analyze our messaging through a persuasion framework”
- “Why aren't people converting? Analyze the psychology”

## Inputs

- url — Optional website or asset URL to analyze; an audit needs the asset or its content, while briefs and inline recommendations can proceed without a URL.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- psychology-audit (markdown)
- psychology-brief-client (markdown)
- psychology-brief-company (markdown)
- {client.marketing}/psychology/psychology-brief-{YYYY-MM-DD}.md
- {company.marketing}/psychology/psychology-brief-{YYYY-MM-DD}.md
- {scope.marketing}/psychology/psychology-audit-{asset}.md

