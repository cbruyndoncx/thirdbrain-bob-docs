---
description: Obsidian-native inbox management. Classify, prioritize, and batch-process emails so the owner focuses on decisions, not inbox management.
title: email-triage
---

# email-triage

Obsidian-native inbox management. Classify, prioritize, and batch-process emails so the owner focuses on decisions, not inbox management.

- **Area:** Foundational
- **Category:** productivity
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Drafts Gmail triage decisions in Obsidian, classifies threads by sender and urgency, suggests replies for routine messages, and produces weekly digests.

## How you ask

- “Triage my unread emails and prioritize the inbox”
- “Draft responses for routine emails in my inbox”
- “Organize my Gmail labels for this week's messages”
- “Summarize all client communications from the past 3 days”

## Inputs

- owner_people — Owner's own person notes — match sender email frontmatter to known contacts.
- client_deals — Deal notes — identify emails from active deal contacts.
- client_invoices — Invoice notes — identify payment-related emails.
- client_people — Person notes — match sender email frontmatter to known contacts.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- email-config — loaded from your vault context

## Outputs

- Config file generated from the template on first run; read on subsequent runs.
- email-thread (markdown)
- inbox-digest (markdown)
- temporary-inbox-triage (json)
- temporary-weekly-email (json)
- weekly-email-report (markdown)

