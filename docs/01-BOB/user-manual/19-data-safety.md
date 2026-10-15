---
description: Local-first storage, what is transmitted for AI processing, the drafts-first
  rule, and review discipline
title: BOB User Manual — 19. Data Handling & Safety
---

# 19. Data Handling & Safety

This section states plainly where your information lives, what leaves your machine, and which controls protect you. Precision matters here, so the claims are deliberately narrow.

## Storage is local. Inference is not automatic.

**Local-first describes storage.** The working record — your notes, documents, analyses, and BOB's outputs — is held as plain files on hardware you control. There is no supplier-hosted copy of your vault and no requirement to upload your document library to anyone's platform.

**Inference is a separate question.** When BOB performs an analysis, the specific material needed for that task — your request plus the relevant extracts — is transmitted to the AI provider you have configured and processed under **your own agreement with that provider**. BOB operates bring-your-own-key: the supplier of BOB is not in the data path and holds none of your material.

| What | Where it lives / goes |
|------|----------------------|
| Your vault (all business data) | Your machine, as files you control |
| Task prompts + relevant extracts | Transmitted to your configured AI provider, per task |
| BOB's outputs | Written back to your vault as files |
| Nothing | Held by BOB's supplier |

## What your provider terms govern

On paid business or API terms, the major providers state that customer content is not used to train their models and is retained only briefly. **Paid terms change what the provider may do with transmitted content; they do not change the fact of transmission.** If your requirement is that nothing leaves your premises at all, the answer is a locally hosted model (BOB supports this) — with the trade-off that local models are less capable than the frontier commercial ones.

## The drafts-first rule

Anything hard to undo — sending an email, publishing a post, deleting files, changing external systems — waits for your explicit approval. BOB drafts; you approve. This is not a setting you can forget to enable; it is how the workflows are written.

## Review discipline: AI output is a draft, not a determination

Language models are probabilistic and can err — including by omission. BOB's controls are designed to make errors **detectable**, not to pretend they're impossible:

- **You review before relying.** Business-critical output gets read by a qualified human — you — before it's sent, filed, or acted on.
- **Grounded work cites its sources.** Analytical deliverables reference the vault files they drew from, so any claim can be traced back and checked.
- **Runs are logged.** Playbook and agent runs record what was invoked and what files were produced, so you can retrace what happened.

## Practical safety habits

| Habit | Why |
|-------|-----|
| Keep credentials in configuration, never in chat | Chat content goes to the AI provider |
| Back up the vault like any business-critical folder | It's plain files — any backup tool works |
| Review outward-facing drafts word by word | Your name is on what gets sent |
| Record which provider, account, and terms you use | The one-time check that makes the confidentiality position auditable |

