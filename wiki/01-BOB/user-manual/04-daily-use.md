---
type: knowledge-base
title: "BOB User Manual — 4. Working with BOB Day to Day"
description: "The core loop, the three ways to invoke BOB, and where results are saved"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---

# 4. Working with BOB Day to Day

Every interaction with BOB follows the same shape. Once you've seen it three times, it's second nature.

## The core loop

1. **You ask** — a question or task, in plain English, in the Agent Client panel
2. **BOB picks a skill** (or asks which one you meant)
3. **BOB asks clarifying questions** if the request is ambiguous
4. **BOB does the work** — reads the vault, drafts content, runs analysis
5. **BOB returns the output** — some workflows save files during the run (paths are shown); others return a draft for you to save
6. **You review** — check the output and its paths, edit if needed, approve or send back for revision

The vault is both BOB's **input** (it reads your context) and its **output** (results are saved back as files). When in doubt, check the paths the run reported — if no path is shown, the draft hasn't been saved yet.

## Three ways to invoke BOB

### 1. Natural language — the default

```
Draft a follow-up email to the prospect we met last Tuesday
```

BOB infers the right skill, reads recent meeting notes, and drafts the email. **Use this most of the time** — BOB is good at picking skills.

### 2. Explicit skill name

```
/proposal-writer
```

Loads exactly that skill and runs its workflow. **Use when** you know precisely which skill you want, or BOB picked the wrong one. The full index of installed skills lives in [[SKILLS]] at the vault root.

### 3. Playbooks — multi-step recipes

```
Run the new-client-onboarding playbook
```

A playbook chains several skills into one repeatable process, with checkpoints between steps. **Use for** recurring multi-step work — onboarding, monthly close, weekly reviews.

## Where results are saved

BOB respects the vault's structure. Outputs go to predictable places:

| Output type | Saved to |
|-------------|----------|
| Client deliverables | `{client.projects}` |
| Marketing content | `{company.marketing}/{channel}/` |
| Research | `{resource.root}` |
| Personal notes / inbox | `{me.inbox}` |
| Meeting notes | the relevant `20-MEETINGS/` folder |
| Tasks | `{output.tasks}` |

When a workflow saves a file, BOB tells you the path before it writes, and you can override it. A workflow that returns a draft in the conversation saves nothing until you ask BOB to save it.

## Habits that get the best results

- **Point BOB at context.** "Using the notes in the Acme folder, draft an upsell proposal" beats "draft an upsell proposal" every time.
- **Iterate in the same conversation.** "Good draft — shorter, and drop the intro" keeps the thread's context. Don't start over.
- **Save what's good, edit the rest yourself.** If a draft is 80% there, save it and polish in Obsidian directly — faster than three rounds of tiny tweak requests.
- **Keep the vault tidy.** BOB reads the vault for context; a stale or messy vault produces noisy answers. Review your inbox folder weekly.

## Patterns to avoid

| Don't | Why |
|-------|-----|
| Ask for something no skill covers and accept the answer blindly | Check [[SKILLS]]; unsupported requests get generic, unreliable answers |
| Paste secrets or API keys into the chat | Chat content is sent to the AI provider — keep credentials in configuration files |
| Treat output as final without review | BOB drafts; **you** approve — always review business-critical output |
| Run BOB on out-of-date vault data | If a client folder is six months stale, "current state" advice will be wrong |

