---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: email-triage — ThirdBrain BOB skill
  description: Obsidian-native inbox management. Classify, prioritize, and batch-process emails so the owner focuses on decisions, not inbox management.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: email-triage
catLabel: productivity
area: foundational
desc: Drafts Gmail triage decisions in Obsidian, classifies threads by sender and urgency, suggests replies for routine messages, and produces weekly digests.
summary: Obsidian-native inbox management. Classify, prioritize, and batch-process emails so the owner focuses on decisions, not inbox management.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- owner_people — Owner's own person notes — match sender email frontmatter to known contacts.
- client_deals — Deal notes — identify emails from active deal contacts.
- client_invoices — Invoice notes — identify payment-related emails.
- client_people — Person notes — match sender email frontmatter to known contacts.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- email-config — loaded from your vault context
outputs:
- Config file generated from the template on first run; read on subsequent runs.
- email-thread (markdown)
- inbox-digest (markdown)
- temporary-inbox-triage (json)
- temporary-weekly-email (json)
- weekly-email-report (markdown)
prompts:
- Triage my unread emails and prioritize the inbox
- Draft responses for routine emails in my inbox
- Organize my Gmail labels for this week's messages
- Summarize all client communications from the past 3 days
---
