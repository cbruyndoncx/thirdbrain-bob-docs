---
type: knowledge-base
title: "BOB User Manual — 3. Getting Started"
description: "From installation to a first real deliverable — the guided first-run path"
status: draft
created: 2026-08-07
modified: 2026-10-17
tags: [bob, user-manual, wiki]
---

# 3. Getting Started

Here's the whole journey at a glance: **Install → Connect → Ask → First win.** The goal of your first session is not to learn everything — it's to produce one real, useful deliverable and see where it was saved.

## Part A — Install (one time)

Four steps, in order: get the vault and open it in Obsidian, install what the vault needs on your computer, install the Agent Client plugin, and connect your AI account. Which of them you must do depends on where you start. Find your situation below.

**Pages this guide names.** All of them are in the vault itself:

| Name | What it is |
|------|-----------|
| `getting_started` | The getting-started page in the top folder of your vault. It has the automated setup, the manual steps and an installation flowchart |
| `quickstart` | A wiki page (`02-Setup/quickstart`) for a vault that is already installed: a five-minute check that Obsidian, the Agent Client panel and the AI answer |
| `ts_install` | The installation troubleshooting page (`05-Troubleshoot/ts_install`): "command not found", Node or uv missing, plugins not loading |
| the environment checklist | A wiki page (`01-BOB/Onboarding/environment_checklist`): commands you run in a terminal to see whether your machine already has what BOB needs, before you install anything |

**If you are in this situation, do this.**

| Your situation | Do this | Detail |
|----------------|---------|--------|
| Someone installs and configures BOB with you (done-for-you setup) | Nothing to install. Run the five-minute check in `quickstart`, then continue with Part B below | `quickstart` |
| You have not got the vault yet | Members get the vault ZIP and the skill pack ZIPs from the Skool community's classroom, where each product has its own course or lesson carrying the current ZIP and its checksum file (see "Where to get the files" below). Download it, extract it to a folder you choose (for example `Documents/my-agent-vault`), then in Obsidian choose **Open folder as vault**, select the folder, and click **Trust author and enable plugins** when asked | `getting_started`, Manual Setup, Step 2 |
| Obsidian is not installed | Download it from obsidian.md/download and install it for your operating system | `getting_started`, Step 1 |
| You want the fastest route | Open a terminal in the vault folder and run the automated setup: `bash 00-CORE/Agents/skills/bob-install/scripts/setup.sh` (WSL, macOS, Linux) or `setup.ps1` with PowerShell on native Windows. It sets up system tools, AI tools, Obsidian setup, plugins, skill links, optional tools and API keys in seven phases, and only installs what is missing. Run its Full Audit option first to see what you have without changing anything | `getting_started`, Automated Setup |
| Windows, and WSL2 is not installed | Install WSL2 with Ubuntu first: in an administrator PowerShell run `wsl --install`, restart, open Ubuntu and create a Linux user. Then install Node.js, npm and uv, and Claude Code inside Ubuntu. Claude Code on Windows needs WSL2 | `claude-code-installation-on-windows-using-wsl` (all commands) and `install_wsl2_claude_code` (the full guide) |
| Windows, you already have a fully set-up Windows-native developer environment (Node.js, Python, git) | The environment checklist allows a pure Windows and PowerShell path for this case only; for everyone else it recommends WSL2 | the environment checklist |
| Mac or Linux | Install Node.js 18+ and npm (`brew install node` on Mac, `sudo apt install nodejs npm` on Linux), then Claude Code with `npm install -g @anthropic-ai/claude-code`, and uv (some skills use Python scripts) | `getting_started`, Step 4 |
| You already use Obsidian and want to add BOB's AI to it | Install the Agent Client plugin (next row), then the agent tools | `agent-client-installation` |
| The vault's plugins are not installed yet | They are not downloaded automatically. In Obsidian open **Settings, Community plugins, BRAT**, open BRAT's settings and click **Check for updates**. If some fail because of GitHub's request limit (60 per hour without a token), wait 5 to 10 minutes and click again. A GitHub token, with no special scopes, raises the limit to 5,000 per hour | `getting_started`, Step 3 |
| You need the Agent Client plugin by itself | In Obsidian enable Community plugins, install BRAT, choose **BRAT, Add Beta Plugin**, paste `https://github.com/RAIT-09/obsidian-agent-client`, and enable Agent Client if it is not enabled automatically | `agent-client-installation`, section 1 |
| You do not know what your machine has | Run the checks in the environment checklist in a terminal (Mac Terminal, Linux terminal or the WSL2 Ubuntu shell); nothing is installed by it | the environment checklist |
| A command is not found, or plugins do not load | Reload your shell (`source ~/.bashrc` or `~/.zshrc`), check Node 20+ with `node --version`, and make sure community plugins are enabled | `ts_install` |

**Starter or full vault.** Both install the same way. A full vault stores all its skills; a starter vault stores only the 14 that operate the vault and gets the rest from the skills server (see the starter-vault section below), so a starter vault has one extra step.

**Connect your AI account.** The first time you start Claude Code (`claude` in a terminal) it opens a browser link for Anthropic sign-in; sign in and paste back the token. Claude Code, Codex and Gemini CLI use your subscription login, so the main AI provider needs no API key in Obsidian. Some skills use outside services such as OpenAI, DeepSeek or Gamma: copy `.env.example` to `.env` in the vault and add those keys. Your account is your own, under your own terms, and BOB's supplier is not in the data path. If the Agent Client panel will not open or reports key errors, ask BOB to run `/acp-doctor`, which checks the agent connection.

**Where to get the files.** The vault ZIPs and the skill packs are distributed through the Skool community. Its classroom has a course for the Starter Vault, a course for the Full Vault, and one lesson per skill pack, and each lesson carries the current ZIP and its `.sha256` checksum file. The two PDFs of a release (this guide and the User Manual) are attached where the classroom offers them. Which lesson holds the PDFs is not named in the vault notes, so look in the course for your product. The Full Vault ZIP comes from the Skool community too, with access gated to the VIP tier, and the packs are free. VIP members can also get access to the private GitHub repository that holds the releases, which makes it easier to fork the vault and customise it. After downloading, check the file: with the ZIP and its `.sha256` file in the same folder, `sha256sum -c <name>.zip.sha256` should print OK (the release notes also list each ZIP's SHA-256). This guide's Skool route comes from the release playbook and the course pages; no download address is given here.

**Adding BOB to a vault you already use.** The `vault-upgrade` skill (one of the skills a starter vault stores) merges a BOB release into an existing vault. You give it three folders: your current vault, the extracted new release, and the baseline, which is the release you last installed. It previews first (what it will update, add, preserve, merge or flag as a conflict) and changes nothing until you approve. Your own data folders (personal, company, clients, resources, scratch, task notes, journals) are protected, and the framework folders (skills, templates, schemas, playbooks, Bases) are updated; backups and its staging copy are written beside your vault, never inside it. Ask BOB "upgrade my vault to the latest version", or read `vault-upgrade/SKILL.md`. It needs the baseline: if you never installed a BOB release in that vault, the skill tells you to stop and supply one, and the vault does not describe a first-time route without a baseline.

**What is still not documented.** The sign-in steps for Codex and Gemini CLI are not set out in these pages; see `agent-client-installation`.

For more detail, the full User Manual and the vault wiki pages named above go further. If anything fails, `ts_install` covers the common cases.

### Starter vault only: connect the skills server

A **starter vault** stores only the skills that operate the vault. Every other skill, and all playbooks and value chains, are served by the skills MCP server, so register it once per machine. For Claude Code the command is:

```
claude mcp add --scope user skills -- npx github:cbruyndoncx/ThirdBrain-skills-mcp --lib bob=<skills pack> --exclude-tiers internal,private --dev-status integrated
```

`<skills pack>` is the BOB skills pack for the server: a downloaded `.zip`, or an `https://...zip#sha256=<digest>` address pinned to its checksum. This is the server's skills library, not a vault ZIP or one of the department pack ZIPs. Download it from the Skool community and check it as described above. Check the connection with `claude mcp get skills`. The first call after a restart can take a while because the server scans the whole library before it answers. A full vault does not need this step. Other agent clients register an MCP server in their own way; follow that client's documentation.

If you ask BOB for a skill in a starter vault and it answers from the server, that is expected: the skill is served, not stored.

### First-run check: does the server connect?

1. Run `claude mcp get skills` in a terminal. It shows the registered server and whether it connects. If it does not, re-run the registration command above and check that the `.zip` path is correct.
2. Restart your agent, then wait. The first call after a restart can take a while because the server scans the whole library before it answers.
3. In the Agent Client panel ask: `Search the skills server for a skill that writes proposals.` BOB should name a skill such as `proposal-writer` and read it from the server. Then ask: `Which playbooks do you have?` BOB should list playbooks from the server.
4. If either answer says it cannot reach a server, see [[20-troubleshooting|chapter 20, Troubleshooting]].

This check confirms the connection only. `/bob-doctor` is not documented to test the skills server, so use the commands above for it.

## Part B — Run the readiness check

Before anything else, run the installation doctor:

```
/bob-doctor
```

It checks your whole environment in one pass — operating system, vault location, Obsidian and its required plugins, the AI engine, sign-in state — and reports, in plain English, what's ready and exactly what's still missing. Run it as often as you like; it changes nothing, it only reports. If the agent panel itself misbehaves, its companion `/acp-doctor` diagnoses and repairs the agent connection specifically.

## Part C — How BOB finds your folders: the context pack

BOB never hard-codes your folder names. Every skill asks for a **context key**, a logical name
such as `{company.clients}` (your clients) or `{client.meetings}` (one client's meetings), and the
**context pack** maps each key to a real folder in your vault. That is how BOB knows where to read
your notes and where to save what it writes, and it is why the same skills work on the standard
numbered folder layout and on a vault whose folders carry names of your own.

**On day one there is nothing to set up.** A new vault uses the default pack, which is the
numbered folder layout the vault ships with. A workspace that keeps other folder names needs a
pack of its own; see "Folder names of your own" below.

**Check it once.** Ask BOB `Which pack is active and where did it come from?`, or run:

```
uv run {skills.root}/context-pack/scripts/resolve_context.py --show
```

(`{skills.root}` is the folder that holds your skills.) It shows which pack is active, where it was
found, your workspace folder and its top-level folders. On a new vault it reads "found by
default", which is expected. If a pack was set up for your own folder names, it should name that
pack instead; "found by default" then means the pack is not being found, and
[[20-troubleshooting|chapter 20, Troubleshooting]] explains what to check.

**See where things go.** `resolve_context.py --key company.clients` prints the folder a key means,
and `resolve_context.py --route meeting` prints where a new meeting note is filed. When BOB saves
your first deliverable in Part E, the path it reports comes from this mapping.

**Folder names of your own.** Create a workspace pack (the command is in
[[02-system-overview|chapter 2, System overview]]), change the entries in its `context.yaml`, and
move the folders yourself: the pack only maps, it creates nothing. Obsidian's own settings and the
Bases read folder names literally and need re-rendering from the pack; see
[[21-reference|chapter 21, The context pack]].

**Do not rename folders on the fly.** Renaming a folder in Obsidian does not update the pack, so
skills keep saving to the old location until you change the pack to match.

## Part D — Verify with one question

Open the Agent Client panel and ask something simple:

```
What skills do you have for writing proposals?
```

In a full vault the answer should name skills stored in your vault. In a starter vault it may name skills that BOB read from the skills server instead; that is expected. A healthy install usually answers within about a minute (the first call after a restart can take longer). If you get no skill names, in a starter vault run the first-run check in the server section above, and see [[20-troubleshooting|chapter 20, Troubleshooting]].

## Part E — Your first real win

Ask for something genuinely useful, in plain words. Pick whichever matches your week:

- **Sales-focused?** → "Draft a follow-up email for the prospect I met this week" — BOB reads your meeting notes and drafts it.
- **Content-focused?** → "Turn my latest project notes into a LinkedIn post"
- **Planning-focused?** → "Give me a daily briefing: open tasks, recent notes, what needs attention"
- **Not sure?** → "Look at my vault and suggest three things you could take off my plate this week"

Depending on the workflow, BOB either writes a file into your vault and reports its path, or returns the draft in the conversation for you to review and save (it is not a file until you ask BOB to save it). That's the moment it clicks: from a plain-English request to a saved, usable deliverable.

## Part F — Team use: different skills for different roles

A team shares one BOB, but not every person needs every skill. There are two different routes to skills in a starter vault, and they are not the same operation:

| Route | What it is | Where the skills are |
|-------|-----------|----------------------|
| **Skills server** (remote) | You register the skills MCP server once per machine (see above). BOB fetches skills, playbooks and value chains from it when it needs them | Served; not stored in your vault |
| **Skill pack** (offline) | A ZIP file of skills, downloaded from the Skool classroom. One pack unpacked into a minimal starter vault works on its own | Stored in your vault |

You can use both. BOB uses a local copy of a skill first and asks the server only for skills it does not have locally, and a skill can exist in both places (they are the same skill). The vault does not document a tested procedure for installing several packs into one vault.

There are ten packs: `pack-core` and nine more, mostly one per department (two, `pack-pmbok` and `pack-process`, follow a framework or a method instead).

| Pack | What it is for |
|------|----------------|
| `pack-core` | The common base: the general skills (documents, productivity, product management, sales basics, reporting and vault operations). Over 200 skills. |
| `pack-business` | Business operations, reporting and advisory skills, plus executive coaching and owner productivity (over 40 skills) |
| `pack-enterprise` | HR, finance, compliance, accounts review and enterprise operations (over 30 skills) |
| `pack-marketing` | The full marketing toolkit: strategy, content, SEO audits, ads, analytics, conversion, SEO publishing and automation (over 60 skills) |
| `pack-sales` | Pipeline management, prospect research, qualification and outbound (over 15 skills) |
| `pack-operations` | Manufacturing, supply chain, procurement and logistics (over 10 skills) |
| `pack-pmbok` | The PMBOK 7/8 project management framework (over 15 skills) |
| `pack-process` | Governed business-process orchestration, with the order-to-cash and procure-to-pay case skills (over 10 skills) |
| `pack-media` | Video generation, image creation and media processing (over 10 skills) |
| `pack-engineering` | Engineering consultancy: FIDIC contract analysis, extension-of-time claims, variation orders and delay analysis (9 skills) |

All packs are free. The skill counts include the helper skills a pack bundles. Each of the nine is a self-contained ZIP: it bundles the skills its members depend on, so one pack unpacked into a minimal starter vault works on its own, and none of them depends on another.

**Choosing packs per role.** A team lead matches each person's work to the descriptions above: for example `pack-sales` for the sales team and `pack-marketing` for marketing, with `pack-core` for the general skills everyone uses.

**Setting up the skills server for a team: the options.** The server's own documentation is its README (the `ThirdBrain-skills-mcp` repository named in the registration command), plus the `skills_over_mcp` wiki note. One line per option; read the named source for the detail.

| Option | When to use it | Read |
|--------|----------------|------|
| Register per person | Each person connects their own machine; the documented command uses `--scope user` | `skills_over_mcp`, "Connecting the skills MCP server" |
| Register per vault or folder | Everyone who works in the same vault or project folder should get the server; a project-scoped registration writes a `.mcp.json` file in that folder | `mcp-add` skill (route `install-single`, scope `project`); the server README, "Serving a release pack in a new vault" |
| Any other agent client | A team member uses a client other than Claude Code | `mcp-add` skill (lists the supported clients) |
| Limit skills by tier | Hide some departments' skills from a person: `--exclude-tiers` withholds skills by their `pricing-tier`, and the packs' skills carry their own tiers, so a person's registration can exclude the other departments' tiers. `--dev-status` filters by readiness | The server README, "Configuration"; the pack tiers in `SKILL-PACKS` |
| Several libraries in one server | Serve a general library and a department library under separate names (`--lib NAME=...`) | The server README, "Several libraries in one server" |
| Serve a ZIP, or a release by address | Serve a downloaded ZIP, or a release pinned to its checksum, instead of a folder | The server README, "A zip instead of a folder" and "A published release, by URL" |
| Config file | Change libraries or tier filters without restarting the server (`--config skills.json`) | The server README, "Runtime config file and hardening" |
| Shared HTTP server | One server for several people over HTTP (`--http PORT`, local by default); the README says to place a remote deployment behind authentication | The server README, "Configuration" and "Runtime config file and hardening" |
| Offline packs | Nobody should depend on a server: unpack the packs each role needs | The Skool classroom lessons; `SKILL-PACKS` |

The tier filters apply to the whole server process, so people who need different department sets need different registrations, or different server instances.

**What is still not documented.** Three narrow gaps: a worked example of a team-hosted server with a different skill set for each person (the README documents the filters and says a remote server needs authentication, but gives no per-person setup); whether a department pack's ZIP has been tested as a `--lib` library (the README says a ZIP of skill folders is served like a folder); and whether excluding a tier can withhold a helper skill that another department's skill needs.

## What a first session looks like

| Step | Who does it | Time |
|------|-------------|------|
| Ask in plain English | You | 30 seconds |
| Find context in the vault, pick a skill | BOB | automatic |
| Ask 1–2 clarifying questions if needed | BOB | 1 minute |
| Draft the deliverable | BOB | 1–3 minutes |
| Review, edit, approve | You | as long as it deserves |

> **The one rule that keeps you safe**
> By default BOB produces **drafts**. During a run BOB can write draft files into your vault. Anything that is delivered outside your vault or is hard to undo — sending an email, publishing a post, deleting files, changing an outside system — waits for your explicit "go". This is how BOB's workflows are written, not a lock you can see or switch. You are always the final approver. The full explanation is in [[19-data-safety|chapter 19]], Data Handling & Safety; the short version is in [[05-core-concepts|chapter 5]], Core Concepts, Made Simple.

