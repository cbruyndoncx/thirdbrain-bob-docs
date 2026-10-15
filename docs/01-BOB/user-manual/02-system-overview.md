---
description: What BOB is, the problems it solves, and how it differs from a generic
  AI chat tool
title: BOB User Manual — 2. System Overview
---



# 2. System Overview

You're not installing a chatbot. You're setting up a **Business Operating Brain** — an AI system that knows your company, works inside your own files, and produces real business deliverables: proposals, analyses, reports, follow-ups, plans.

Most AI tools give you a blank chat box and leave the work to you. BOB is different. From day one it comes with a library of over 380 business skills — sales, marketing, finance, operations, HR, strategy — organised and ready to run against your own business data. You stay the owner and the decision-maker. BOB handles the busywork.

## Terms used in this guide

| Term | Plain meaning |
|------|---------------|
| **Vault** | The folder of plain files on your machine that holds your business knowledge, opened in Obsidian |
| **Agent** | The engine that does the work, such as Claude Code, OpenAI Codex or Gemini CLI |
| **ACP plugin** (Agent Client) | The panel inside Obsidian where you type requests to the agent |
| **Skill** | A packaged, written workflow for one business job, with defined inputs, steps and outputs |
| **Playbook** | A multi-step recipe that chains several skills, with checkpoints |
| **Value chain** | One of BOB's core business process flows, such as lead-to-cash; skills are tagged to the ones they serve |
| **MCP server** | The standard way an AI agent connects to an outside tool. BOB's skills MCP server provides skills, playbooks and value chains |
| **Pack** | An offline ZIP of skills; one pack works on its own |
| **Tier** | A label in each skill's header saying which release group it belongs to. Skills tiered `internal` or `private` are not served or shipped |
| **Context key** | A stable name such as `{company.clients}` that a skill uses instead of a folder name |
| **Context pack** | The file that says which folder each context key means in your workspace |

## What makes BOB different from a chat tool

| A generic AI chat | BOB |
|-------------------|-----|
| Answers questions | Solves business problems: sales, finance, HR, strategy, operations |
| No memory of your business | Understands your company: customers, processes, decisions, history |
| Each conversation starts from zero | Draws on your vault — patterns, preferences, past work |
| Output disappears into chat history | Output is saved as files you own, organised and searchable |
| One vendor, one model | You choose both the agent and the model it runs — including local models |

## What problems does BOB solve?

| Business area | Example tasks |
|---------------|---------------|
| Sales | Lead scoring, proposal drafting, pipeline reports, objection handling |
| Marketing | Campaign planning, content creation, social posts, competitive analysis |
| Operations | Process mapping, vendor evaluation, bottleneck identification |
| Finance | Forecasting, invoicing support, period close, cash flow analysis |
| HR | Hiring support, onboarding, performance review preparation |
| Strategy | Market analysis, positioning, growth planning, decision frameworks |

**The pattern:** wherever you have business data plus a decision or deliverable to produce, BOB can help.

## How it works — the four layers

BOB is not one program; it's four layers working together. You only ever touch the top one.

| Layer | What it is | What it does for you |
|-------|-----------|----------------------|
| 1. The vault (Obsidian) | A folder of plain files on your machine | Holds all your business knowledge — customers, deals, processes, decisions. Yours, forever, no lock-in. |
| 2. The interface (ACP plugin) | A panel inside Obsidian | Where you type requests and read answers. You never leave your notes. |
| 3. The agent | The engine that does the work | Reads your question, searches the vault, picks the right skill, runs it. Your choice of client — see below. |
| 4. The AI model | The model your chosen agent runs | Does the actual thinking and writing. Also your choice — see below. |

### Two things you choose

Layers 3 and 4 are both yours to pick, and they are separate decisions.

| You choose | What it means | Options |
|---|---|---|
| **The agent client** (layer 3) | Which agent does the work | Claude Code, OpenAI Codex, Google Gemini CLI — or any client that supports ACP, the agentskills.io standard and `AGENTS.md`, such as Goose or AMP |
| **The model** (layer 4) | Which model that agent runs | A trade-off between speed and cost on one side and depth of reasoning on the other. Some clients also offer paid acceleration of a slower reasoning model. |

Neither choice touches your vault, your skills, or the way you work — that is the point of keeping the layers separate.

> **On specifics.** Which models exist, what they are called, how they are tiered and what they cost is set by the AI providers and changes frequently — sometimes weekly. This manual deliberately names no model and quotes no price. Check your provider's current documentation for anything specific.

The key property: **your data lives in layer 1, as files you control.** Your vault stays on your machine. When BOB uses an AI provider, it sends your request and the relevant extracts to the provider you configured, and that provider processes them under your own agreement with it. [Chapter 19](19-data-safety.md) covers exactly what this means for confidentiality.

## Where the skills come from

BOB reaches its skills, playbooks and value chains in one of two ways, and the rest of your workspace is identical in both.

| | Full vault | Starter vault |
|---|---|---|
| Skills | All stored in your vault | Only the skills that set up and operate the vault are stored locally; every other skill is served by the **skills server** |
| Playbooks and value chains | Stored in your vault | Served by the skills server |
| Catalogues | The `SKILLS`, `PLAYBOOKS` and `VALUE-CHAINS` notes | Ask BOB; the local catalogue lists only the local skills |

The skills server is an MCP server (MCP is the standard way an AI agent connects to an outside tool). BOB asks it for skills on your behalf; you never call it yourself. Notes a served skill writes are filed and validated exactly like notes a local skill writes. Setup is in [chapter 3](03-getting-started.md), the details in [chapter 14](14-skills-system.md).

Skills also never carry a hard-coded folder name. They ask for a **context key** such as `{company.clients}`, and the **context pack** says which folder that key means in your workspace.

To see which pack your workspace is using and where it was found, run `uv run {skills.root}/context-pack/scripts/resolve_context.py --show`. A pack is a `context.yaml` file, either in the top folder of your vault or in a `context-<id>` skill folder under the skills folder. A starter vault includes the `context-pack` skill and its default key file (`assets/default-context.yaml`), but no pack file of its own. With no pack file, every key resolves through that default, which is the numbered folder layout, so nothing needs to be set up on day one. In `--show` that case reads "found by default"; on a workspace that should have its own pack, that line means the pack is not being found.

To create your own workspace pack, run from the `context-pack` skill folder: `uv run scripts/init_context_pack.py --id <your-id> --title "<your workspace name>" --dry-run`, read what it would write, then run it again without `--dry-run`. It creates a `context-<id>` skill folder (by default under the skills folder in your vault) holding a `SKILL.md` and a `context.yaml` for you to edit; `--layout minimal` starts from only the core keys, and it refuses to overwrite an existing pack unless you pass `--force`. Check the result with `validate_context_pack.py --pack <folder>`. Change a pack only when you mean to change the folder mapping; [chapter 21](21-reference.md) explains how.

## What you need before you start

| You need | Details |
|----------|---------|
| A computer you control | Windows, Mac, or Linux — the vault lives here |
| Obsidian | Free knowledge-management app; this is your window into BOB |
| An AI subscription or API key | Claude (recommended), OpenAI, or Gemini — your own account, your own terms |
| No technical skill to *use* BOB | You describe; BOB works, and you never edit code. Installing it yourself is the technical part: it needs Node 20+ and npm, on Windows WSL2 with Ubuntu, and a terminal. Assisted setup does that for you; the self-install path is in [chapter 3](03-getting-started.md). |

