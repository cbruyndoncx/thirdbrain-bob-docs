---
type: knowledge-base
title: "BOB User Manual — 20. Troubleshooting & FAQ"
description: "Quick answers to the questions new BOB users actually ask"
status: draft
created: 2026-08-07
modified: 2026-11-10
tags: [bob, user-manual, wiki]
---

# 20. Troubleshooting & FAQ

**"Do I need to be technical?"**
Not to use it. You talk to BOB in plain English and never edit code. Installing it yourself is technical (Node, npm, WSL2 on Windows, a terminal), and a few maintenance steps run a command in a terminal; setup is guided — see `ts_install`, the installation troubleshooting page described in the install section, if it fights you.

**"BOB's answer is generic and doesn't reflect my business."**
BOB reads the vault for context. Early on, the vault is thin — add your company profile, key clients, and current projects, and point BOB at specific folders ("using the notes in the Acme folder, …"). Sharpness follows context.

**"Nothing was sent — did it fail?"**
That's on purpose. BOB produces drafts and waits for your "go". If you want something actually sent or published, say so explicitly.

**"Where did my output end up?"**
Every run reports the paths it wrote to. If no path is shown, the result is still a draft in the conversation — ask BOB to save it. Common destinations are listed in [[04-daily-use|chapter 4]].

**"BOB picked the wrong skill."**
Invoke the right one directly with its `/name`, or say "use the proposal-writer skill for this". The full index is [[SKILLS]].

**"I forgot what BOB can do."**
Just describe the job in normal words — routing is BOB's problem, not yours. Or browse [[15-skill-catalog|the Skill Catalog]] and [[SKILLS]].

**"BOB says it has no skill or playbook for this (starter vault)."**
A starter vault stores only the skills that operate the vault; the rest are served by the skills server. BOB looks locally first and then asks the server. Run `claude mcp get skills` to see whether the server is registered and connected. The first call after a restart can be slow because the server scans the library. Setup is in [[03-getting-started|chapter 3]].

**"A served skill fails because an API key is missing."**
A served skill runs outside your vault and does not read the vault's `.env` file. Set the key in your environment (your shell profile, the agent's settings, or the server's configuration). `.env.example` in the vault root lists the keys and the skills that use them.

**"A skill reports an unknown key, or a path that does not exist."**
Skills find folders through context keys. An unknown key shows `Error: unknown key '<key>': neither <your pack> nor the default layout declares it`. Check the spelling, and list the keys your workspace declares with `uv run {skills.root}/context-pack/scripts/resolve_context.py --list`. If a key is known but its folder does not exist, the resolver reports it and stops; create the folder, or correct the key's `path` in your context pack. Run `resolve_context.py --show` and read which pack is active: `found by default` on a workspace that has its own pack means the pack is not being found. See [[21-reference|chapter 21, The context pack]].

**"I renamed a folder and now BOB saves to the old one."**
Skills follow your context pack, so change the folder's entry in `context.yaml` (see [[21-reference|chapter 21, The context pack]]). Obsidian's own settings and the Bases read folder names literally and do not follow the pack, so they need re-rendering from it with the `bob-install` path renderer.

**"Which AI model do I need? Can I use a different one?"**
BOB runs inside a coding-agent CLI — Claude Code, Codex or Gemini CLI — signed in with your own subscription, or with an API key (see [[03-getting-started|chapter 3]]). Switch in the Agent Client panel's model selector. Vault, skills, and habits stay identical; only the "engine" changes.

**"Something feels broken or half-finished."**
Run the doctor skill (`/bob-doctor`). It's a plain-English health check of the whole environment — OS, vault, Obsidian plugins, AI engine, sign-in — reporting what's working, what's missing, and what to do next. It only reports; it never changes anything.

**"The agent panel won't connect / the AI never answers."**
Run `/acp-doctor`. It diagnoses and repairs the agent connection specifically — the runtime, the AI command-line tools, login state, and the plugin's configured paths — and ends with a live connection test.

**"The answer references old information."**
BOB's "current state" is your vault's current state. If a client folder is six months stale, update it — then re-ask.

**"Is my data used to train the AI?"**
On paid business/API terms, the major providers state customer content is not used for training. The precise position depends on your account and configuration — see [[19-data-safety|chapter 19]].

**"Can BOB work fully offline / on-premises?"**
Storage is always local. For the AI processing, a locally hosted model keeps it on your hardware, at the cost of model capability. A skill that calls an outside service (each skill declares this as `outbound`) and fetching skills from the skills server still use the network — see [[19-data-safety|chapter 19]].

## Questions before and after you start

These questions came from the ThirdBrain Tech community on Skool.

### Getting started

**"Do I have to learn commands?"**
No. You describe what you want in plain English; BOB picks the right skill or playbook. The [[Prompt Showcase]] gives copy-paste examples for every area of the business.

**"Do I have to use Obsidian?"**
No — but you'll want to. The skills, playbooks, and data model all run without Obsidian, and the AI works the same either way. What you lose without it is the human side: the vault's pre-configured plugins turn it into a workspace with dashboards, diagrams, PDFs, and reports. Without Obsidian you work with plain Markdown files in a folder. Everything still works; it's just much less pleasant day to day.

**"What do I need to run it?"**
A desktop computer — Windows (with WSL), macOS, or Linux — plus Obsidian (free), a coding-agent CLI, and your own AI account. The setup guide in [[03-getting-started|chapter 3]] walks you through all of it.

**"Can I use BOB on my phone?"**
Your notes, yes; the AI workflows, no. Install the Obsidian app on your phone and turn on sync, and your vault is there to read and edit. Obsidian Sync (paid) or a free alternative such as a GitHub-based sync both work. Keep the Agent Client configuration off sync: it points to the AI tools installed on each machine. The AI runs on your desktop, not on the phone.

**"Can I use BOB for more than one business?"**
Yes. Each business entity gets its own company or client profile in the vault. Reference the entity in your prompt and BOB scopes the output to it.

**"Can I add my own skills?"**
Yes. Skills are Markdown files that follow the agentskills.io standard. You can write new skills or fork existing ones; the `skillsmith` skill walks you through it (see [[14-skills-system|chapter 14]]).

### Cost, ownership and data

**"What does it cost to run?"**
You pay for your own AI usage directly, with no markup from us — typically a modest monthly amount, usually in the tens of dollars, depending on volume. There is no subscription to BOB itself.

**"Is this a subscription?"**
No. The Starter Vault is a one-time purchase: you own what you bought, including the future updates of that release line. The current price is on the live shop.

**"What if it's not working for me? Is there a guarantee?"**
Yes — an operational-by-day-30 guarantee. "Operational" is a checkable bar: BOB installed and running, your AI account connected, your vault structure in place, and at least one skill or playbook run end-to-end to a real output. If you are not operational after your first 14 days, we work with you over the next two weeks to get you there by day 30, or you get your money back. It guarantees that the system runs for you, not any particular business result.

**"Where does my data live, and what leaves my machine?"**
On your own machine, as plain Markdown files. Nothing is locked in our cloud, and you can open, edit, or move your data at any time. When you run a skill, the vault context it needs is sent to your AI provider as part of the prompt. The vault connects to other services only when you run a skill that does so, such as publishing to WordPress or LinkedIn. See [[19-data-safety|chapter 19]].

### Skills, packs and editions

**"What is the difference between the Starter Vault and the full vault?"**
The Starter Vault stores only the skills that operate the vault. Every other skill, playbook and value chain is served on demand by the skills MCP server, or added offline from the free skill packs. The full vault stores every skill, playbook and value chain in your vault, where you can fork and customise them. See [[14-skills-system|chapter 14, Where skills come from]].

**"What's the difference between broad and specialist packs?"**
Broad packs are general-purpose bundles that make you productive across a whole area of the business. Specialist packs are narrower and deeper, with tooling that usually takes more technical skill to integrate. All packs are free. What each pack holds is on the [[SKILL-PACKS|Skill Packs]] page.

**"Do I need any packs to start?"**
No. The Starter Vault is a complete system on its own. Add a pack when a specific need or client engagement calls for one.

**"Can I turn skills off?"**
Yes. The skill manager enables or disables skills one by one or by whole pack, so BOB stays focused on the work in front of you. See [[SKILL-PACKS|Skill Packs]].

### For consultants and partners

**"Can I use this for my clients?"**
Yes. BOB is built for white-label delivery: deploy customised vaults for clients under your own brand, with partner pricing and support.

**"Can I deliver a finished service with it, not just notes?"**
That's the point. Playbooks chain skills into complete, billable outcomes — a marketing audit, a monthly close, a project charter pack, an SEO content service — produced to a consistent standard. See [[16-playbooks-processes|chapter 16]].

> **Still stuck?**
> Ask BOB directly: "I'm confused about ___, can you help?" Explaining what you're trying to do is often the fastest fix of all. Deeper guides: the troubleshooting index page `MOC-troubleshoot` in the vault wiki.

