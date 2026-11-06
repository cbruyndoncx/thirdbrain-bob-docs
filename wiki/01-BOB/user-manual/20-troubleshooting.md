---
type: knowledge-base
title: "BOB User Manual — 20. Troubleshooting & FAQ"
description: "Quick answers to the questions new BOB users actually ask"
status: draft
created: 2026-08-07
modified: 2026-10-12
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

**"Can I use a different AI model?"**
Yes — switch in the Agent Client panel's model selector. Vault, skills, and habits stay identical; only the "engine" changes.

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

> **Still stuck?**
> Ask BOB directly: "I'm confused about ___, can you help?" Explaining what you're trying to do is often the fastest fix of all. Deeper guides: the troubleshooting index page `MOC-troubleshoot` in the vault wiki.

