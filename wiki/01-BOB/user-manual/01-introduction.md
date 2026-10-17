---
type: knowledge-base
title: "BOB User Manual — 1. Introduction"
description: "Purpose, audience, scope, and conventions of the BOB User Manual"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---
![[01-introduction.mp3]]

# 1. Introduction

## Purpose of this manual

This is the user manual for **BOB — the Business Operating Brain**, a product by BRNCX built on the ThirdBrain platform. It is a classical software description: it states what the system does, how it is structured, how you operate each part of it, and where its limits are. Every capability described here is intended to be verifiable against the running system.

It complements, and does not replace, two other document types:

| Document | What it is for |
|----------|----------------|
| This user manual | Understanding and operating the system — complete and referenceable |
| Getting-started guides | The fastest path to a working install (chapter 3 summarises; the wiki's setup section has per-platform detail) |
| Solution manuals | Engagement-specific documents describing a particular deployment, its scope, and its governance |

## Who this manual is for

- **Business users** who run BOB day to day — owners, operators, consultants. Chapters 1–5 and the module chapters (8–13) are written for you first.
- **Evaluators** assessing what the system does before adopting it — read chapters 1, 2, 7, 14, and 19.
- **Administrators** responsible for configuration, upkeep, and data handling — chapters 18–21: administration, data handling and safety, troubleshooting, and the reference.

No programming knowledge is assumed anywhere in this manual.

## How this manual is organised

| Part | Chapters | Contents |
|------|----------|----------|
| Orientation | 1–5 | What BOB is, first use, daily operation, core concepts |
| The system | 6–7 | The workspace you navigate; the data model underneath it |
| Functional modules | 8–13 | Sales & CRM, Marketing, Finance, Operations & Projects, HR, Strategy |
| The machinery | 14–17 | Skills, the skill catalog, playbooks and processes, the operating cadence |
| Operation & assurance | 18–20 | Administration, data handling and safety, troubleshooting |
| Reference | 21–22 | Entity reference and glossary; one-page cheat sheet |

Read chapters 1–5 in order once. Everything after that is designed for direct access — go to the chapter that matches the task in front of you.

## Conventions used

| Convention | Meaning |
|-----------|---------|
| `monospace` | A skill name, command, file name, or something you type literally |
| "Quoted phrases" | Example requests you say to BOB in plain English |
| Folder paths like `{company.clients}` | Locations inside the vault, the folder that holds all your data |
| **You do / BOB does** tables | Workflow steps, split by who performs them |

## Terminology, briefly

Three words carry most of this manual (full glossary in [[21-reference|chapter 21]]):

- **Vault** — the folder of plain files holding all your business data; BOB reads it and writes to it.
- **Skill** — a packaged, written workflow for one business job, with defined inputs, steps, and outputs.
- **Playbook** — a multi-step recipe chaining skills into a repeatable process with checkpoints.

## Version

This manual describes BOB as shipped at the date on the cover. Skills and playbooks evolve; the authoritative, always-current index of installed skills is the `SKILLS` note at the vault root.
