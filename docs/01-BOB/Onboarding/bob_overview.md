---
title: BOB Overview — What It Is & How It Works
---

# BOB Overview — What It Is & How It Works

What is BOB? How does the tech stack work? What problems does it solve? Start here for a complete conceptual foundation.

---

## What is BOB?

**BOB = Business Operating Brain**

BOB is an AI-powered system that helps businesses run better by making intelligent decisions and automating work. It's like having a smart business advisor available 24/7 — but it's not a chatbot for small talk.

### Key difference from ChatGPT

| ChatGPT | BOB |
|---------|-----|
| Generic AI chat tool | AI system designed specifically for **business operations** |
| Answers questions | **Solves business problems**: sales, finance, HR, strategy, operations |
| No memory of your business | **Understands your company**: customer lists, processes, decisions, history |
| Each conversation is separate | **Learns from your vault**: patterns, preferences, past work |
| "Talk to AI" interface | **Integrated into your workflow**: works inside tools you already use |
| One model (GPT) | **Multiple AI models**: Claude, OpenAI, Gemini — you choose |

---

## What Problems Does BOB Solve?

BOB handles questions and tasks across the entire business:

| Business Area | Example BOB Tasks |
|---------------|-------------------|
| **Sales** | Lead scoring, proposal generation, pipeline forecasting, objection handling |
| **Marketing** | Campaign planning, content creation, audience segmentation, competitive analysis |
| **Operations** | Process optimization, vendor evaluation, cost reduction, bottleneck identification |
| **Finance** | Forecasting, budget reviews, supplier negotiations, cash flow analysis |
| **HR** | Hiring decisions, compensation review, skill gap analysis, team structure |
| **Strategy** | Market analysis, competitive positioning, growth planning, risk assessment |

**The pattern:** Wherever you have business data + a decision to make, BOB can help.

---

## How BOB Works (The Tech Stack)

BOB is built on **four layers**. Each layer does one thing:

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: OBSIDIAN (Your Knowledge Hub)                 │
│  • All business data stored as markdown files            │
│  • Notes about customers, deals, processes, decisions   │
│  • Vault = your company's brain (organized, searchable) │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  LAYER 2: ACP PLUGIN (Obsidian Integration)             │
│  • "Agent Client Protocol" plugin in Obsidian           │
│  • Lets you ask BOB questions without leaving Obsidian  │
│  • Sees your vault data, reads/creates notes            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  LAYER 3: CLAUDE CODE (AI Agent Engine)                 │
│  • Receives your question from ACP plugin               │
│  • Searches vault for relevant data                     │
│  • Chooses the right "skill" to use                     │
│  • Runs that skill to generate your answer              │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  LAYER 4: ANTHROPIC API (The AI Model)                  │
│  • Claude, OpenAI, or Gemini model                      │
│  • Does the actual thinking and writing                 │
│  • Can switch providers without changing anything else  │
└─────────────────────────────────────────────────────────┘
```

### What Each Layer Does

**Layer 1 — Obsidian (Knowledge Storage)**
- Your vault is a folder full of markdown files
- Files are organized: `/{company.clients}`, `/{company.root}`, `/{resource.root}`
- BOB reads from this vault to understand your business context
- When BOB creates output, some workflows save it back to the vault during the run; review the output paths shown in the run to see where files landed

**Layer 2 — ACP Plugin (The Interface)**
- ACP = Agent Client Protocol
- It's a plugin that runs inside Obsidian
- You type your question into ACP; it passes it to Claude Code
- ACP also gives Claude Code access to your vault files

**Layer 3 — Claude Code (The Agent)**
- Claude Code is an AI coding assistant from Anthropic
- But BOB uses it as an **agent** — it can think, search, and take actions
- When you ask BOB a question:
  1. Claude Code reads your question
  2. It searches your vault for relevant information
  3. It picks a "skill" (a workflow) to handle your request
  4. It runs that skill
  5. It returns the answer to you

**Layer 4 — The AI Model (The Brain)**
- The actual AI doing the thinking
- Could be Claude (Anthropic), GPT-4 (OpenAI), or Gemini (Google)
- You can switch without changing Layers 1–3
- Think of it like swapping out the engine in a car — the rest still works

---

## The Data Flow: How a Question Becomes an Answer

Let's trace what happens when you ask BOB a question:

```
You (in Obsidian):
"Analyze our top 10 customers and recommend which ones to prioritize for upsell"
        ↓
ACP Plugin:
Captures your question, passes it to Claude Code
        ↓
Claude Code:
1. Searches your vault: "Find all customer files in /{company.clients}"
2. Reads recent deals, contact history, revenue data
3. Searches for a skill: "Is there an upsell-strategy skill?"
4. Runs that skill with your customer data as input
        ↓
Claude Model (API):
Thinks through your customer data, scores them, ranks by upsell potential
        ↓
Claude Code:
Formats the result as markdown; depending on the workflow, either creates a new note in your vault directly or returns the draft for you to save
        ↓
ACP Plugin:
Shows the answer in Obsidian; if a path was written, it's listed in the run output
        ↓
You:
Review the analysis (and the output paths), edit if needed, ask BOB to save anything not yet saved
```

---

## Why This Stack Matters

| Layer | Why It's There |
|-------|-----------------|
| **Obsidian** | All your data is yours, in files you own. No vendor lock-in. You can search, link, organize it your way. |
| **ACP** | You never leave Obsidian. No switching apps. BOB integrates into your existing workflow. |
| **Claude Code** | It's not just a language model — it's an **agent** that can think, search, and act. It can read your vault, pick the right skill, and execute it. |
| **API** | You can swap the AI model. If Claude is slow, switch to OpenAI. If you prefer Gemini, use that. Same system, different brain. |

---

## What Are "Skills"?

A **skill** is a workflow that BOB can run. Think of it as a mini-program designed for a specific business task.

Examples:
- `lead-qualifier` — reads a lead's profile, scores them, decides if worth pursuing
- `proposal-writer` — interviews you about a deal, drafts a proposal
- `market-sizing-analysis` — researches a market, estimates opportunity size
- `competitive-battlecard` — compares your product to competitors

**How Claude Code picks a skill:**
1. You ask BOB a question
2. Claude Code reads your question
3. It thinks: "What skill would solve this?"
4. It loads that skill (a set of instructions + templates)
5. It runs that skill using your data
6. It returns the result

This vault includes a comprehensive library of skills, covering sales, marketing, operations, finance, HR, and more.

---

## What You'll Install

A working BOB setup has:

✅ **Obsidian** — knowledge management app  
✅ **ACP Plugin** — agent interface inside Obsidian  
✅ **Claude Code** — AI agent engine (runs locally)  
✅ **This vault** — a full library of business skills + your company data  
✅ **API keys** — Claude/OpenAI/Gemini credentials (you choose)  

When it's all installed:
- You open Obsidian
- You type a business question into the ACP panel
- Claude Code searches the vault, picks a skill, runs it
- You get an answer, review it, and the output paths the run wrote to (some workflows save during execution; if a path isn't shown, ask BOB to save the draft)
- **Done** — no app-switching, no chat tabs, no email chains

---

## Key Concepts to Understand

1. **Vault = Your Company's Brain**
   - Every decision, customer, deal, process is in markdown files
   - BOB reads from this vault to understand your context
   - The more structured your vault, the better BOB's answers

2. **Skills = Workflows**
   - Pre-built decision-making processes
   - "Draft a proposal", "Score a lead", "Analyze a market"
   - Claude Code picks the right skill based on your question

3. **Obsidian Never Leaves**
   - You ask BOB inside Obsidian via ACP plugin
   - Answer appears inside Obsidian
   - No context-switching, no ChatGPT tabs, no email chains

4. **Multiple AI Models**
   - Claude, OpenAI, Gemini all work
   - Switch by changing one config file
   - Useful for cost, latency, or feature tradeoffs

5. **Transparent & Auditable**
   - Some playbook runs create a TaskNote step log capturing the playbook, what was invoked, the original user input, and per-step output paths — enough to retrace what BOB did
   - The `audit-trail` skill compiles a readable record of what was run from the agent session logs — an **activity trail, not a cryptographically tamper-proof or hash-chained ledger** (it computes no hashes and does not chain entries). For formal tamper-evidence in client/Mode-3 work, layer on an out-of-band system (signed version history, an external WORM log)
   - All vault data stays in your markdown files — not a black box, you own the data

---

## Next Steps

1. Read through this guide carefully
2. If any section is unclear, research it (links provided above)
3. Verify your environment with the [environment_checklist](environment_checklist.md)
4. Refer back to this guide as you work through installation — the 4 layers will become concrete when you see them running

