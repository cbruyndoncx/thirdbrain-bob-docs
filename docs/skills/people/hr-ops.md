---
description: Build HR operational assets — job descriptions and onboarding or training curricula.
title: hr-ops
---

# hr-ops

Build HR operational assets — job descriptions and onboarding or training curricula.

- **Area:** People
- **Category:** human resources
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** HR Manager

Drafts HR operational assets as vault markdown — job descriptions and training or onboarding curriculum outlines.

## How you ask

- “Create a job description for a marketing manager role”
- “Build a training module outline for new employee onboarding”
- “Draft an HR onboarding checklist for remote workers”
- “Write a job description for a customer success lead”

## Inputs

- role — Role the job description covers
- seniority — Level, which sets scope and requirement language
- profile — Company profile — stage and team context for the JD.
- topic — Training subject
- audience — Who is being trained, which sets depth and examples
- profile — Company profile — context for the training curriculum.

## Outputs

- job-description (markdown)
- training-module (markdown)
- {company.hr}/jd_{role-title}.md
- {company.hr}/training_{module-name}.md

