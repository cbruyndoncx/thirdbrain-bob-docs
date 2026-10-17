# Comprehensive Installation Guide for Obsidian users

> **Folder names below are the default (numbered) layout that BOB ships with.** A workspace
> with its own context pack names the folders differently — `uv run 00-CORE/Agents/skills/context-pack/scripts/resolve_context.py --key skills.root`
> prints the real path for the key named in each case.

This guide provides detailed installation steps for various Agent CLI tools, structured by operating system so you can add it to your pre-existing Obsidian vault.

## 1. Obsidian Plugin Installation (Prerequisite)

Before installing any CLI tools, you need to set up the Agent Client plugin in Obsidian.

1.  In Obsidian settings, go to **Community Plugins** and enable them.
2.  Install the **BRAT** plugin from the Community Plugins browser.
3.  In Obsidian settings, go to **Community Plugins → BRAT → Add Beta Plugin**.
4.  Paste this repo URL: `https://github.com/RAIT-09/obsidian-agent-client`
5.  BRAT will download the latest release and keep it auto-updated.
6.  If not auto-enabled, enable **Agent Client** from the plugin list.

---

## 2. A)  Manual Installation on macOS / Linux / Windows WSL

> **Shortcut:** if you use the recommended `acp-launch` launcher (section 3), you can **skip the per-adapter installs below** — the launcher installs and updates the adapters itself. You still need the agent CLIs you want to log in with (`claude`, `codex`, `gemini`), and Node.js.

### Prerequisites

- **Node.js and npm:** Make sure you have Node.js and npm installed. You can check with `node -v` and `npm -v`. If not installed, you can download it from [nodejs.org](https://nodejs.org/). The `which node` command will show you the path, which you will need later.

### Claude Code
The Agent Client Protocol provides an ACP implementation of Claude Code that can be integrated.

1.  **Install the CLI tool:**
    ```bash
    npm install -g @agentclientprotocol/claude-agent-acp
    ```
2.  **Find the installation path:**
    ```bash
    which claude-agent-acp
    ```
    (Example output: `/usr/local/bin/claude-agent-acp`)

### Codex
ZED editor provides an ACP implementation of Codex that can be integrated. 
1.  **Install the CLI tool:**
    ```bash
    npm install -g @zed-industries/codex-acp
    ```
2.  **Find the installation path:**
    ```bash
    which codex-acp
    ```
    (Example output: `/usr/local/bin/codex-acp`)

### Gemini CLI

Gemini has native support in experimental mode, that is configured in later step.
1.  **Install the CLI tool:**
    ```bash
    npm install -g @google/gemini-cli
    ```
2.  **Find the installation path:**
    ```bash
    which gemini
    ```
    (Example output: `/usr/local/bin/gemini`)

---

## 2. B) If WSL Mode (Recommended for Windows)

### Configure WSL Mode

WSL Mode runs agents inside Windows Subsystem for Linux, providing better compatibility and a more Unix-like environment.

1. Enable **WSL Mode** in **Settings → Agent Client**
2. Use Linux-style paths (e.g., `/usr/local/bin/node`, `/usr/local/bin/claude-agent-acp`)
3. Refer to the **macOS/Linux** examples above for path configuration

## 2.C) Native installation on Windows 


==**DO NOT USE THIS YET, THIS WILL NOT INTEGRATE WITH OBSIDIAN**==

### Prerequisites

- **Node.js and npm:** Make sure you have Node.js and npm installed. You can check with `node -v` and `npm -v`. If not installed, you can download it from [nodejs.org](https://nodejs.org/). The `where.exe node` command will show you the path, which you will need later.

### Claude Code

1.  **Install the CLI tool:**
    ```cmd
    npm install -g @agentclientprotocol/claude-agent-acp
    ```
2.  **Find the installation path:**
    ```cmd
    where.exe claude-agent-acp
    ```
    (Example output: `C:\Users\Username\AppData\Roaming\npm\claude-agent-acp.cmd`)

### Codex

1.  **Install the CLI tool:**
    ```cmd
    npm install -g @zed-industries/codex-acp
    ```
2.  **Find the installation path:**
    ```cmd
    where.exe codex-acp
    ```
    (Example output: `C:\Users\Username\AppData\Roaming\npm\codex-acp.cmd`)

### Gemini CLI

1.  **Install the CLI tool:**
    ```cmd
    npm install -g @google/gemini-cli
    ```
2.  **Find the installation path:**
    ```cmd
    where.exe gemini
    ```
    (Example output: `C:\Users\Username\AppData\Roaming\npm\gemini.cmd`)
---

## 3. Recommended: The `acp-launch` Auto-Updating Launcher (macOS / Linux / WSL)

The manual installs above work, but they leave you maintaining separately-versioned adapters — every upstream release means another round of `npm install -g`, and the plugin breaks silently when an install path moves. The recommended setup replaces all hardcoded adapter paths with **one launcher script**, `~/bin/acp-launch`, that installs each adapter into its own local cache and keeps it current automatically. One file holds all the logic, so every agent — including custom ones — gets identical behavior.

**Easiest way to create it:** run the ACP doctor with `--fix` (see below) — it generates `~/bin/acp-launch` from its built-in template. The doctor's template is the single source of truth for the launcher's content.

**Usage:**

```
acp-launch <agent>[@version] [extra args...]    launch a registered agent
acp-launch npm:<package>[@version] [args...]    launch any npm ACP adapter
acp-launch --list                               show registered agents
acp-launch --update [agent]                     force an update check on next launch
```

Registered agents: `claude`, `codex`, `gemini`, `qwen` (npm adapters, auto-updating) and `goose` (native ACP via `goose acp`, updated by its own installer).

In the plugin settings (section 5), every agent gets the **same command** — only the args differ:

| Agent | Command | Args |
|-------|---------|------|
| Claude Code | `/home/you/bin/acp-launch` | `claude` |
| Codex | `/home/you/bin/acp-launch` | `codex` |
| Gemini CLI | `/home/you/bin/acp-launch` | `gemini` (the launcher adds `--experimental-acp` itself) |
| any custom agent | `/home/you/bin/acp-launch` | `npm:@vendor/their-acp-adapter` |

**Passing parameters:** anything after the agent name is passed through to the adapter — add extra args in the plugin's Args field after the agent name, e.g. `gemini --model gemini-2.5-pro`.

**Adding a custom agent permanently:** either use the `npm:<package>` form directly in the plugin config (no edit needed), or add one line to the `PKG` registry at the top of the script (plus a `DEFAULT_ARGS` entry if it needs a flag).

**How it works:** each agent is installed into its own cache under `~/.local/share/acp-launch/<agent>` and refreshed **at most once per 24 hours** (configurable via `ACP_MAX_AGE_HOURS`). Within that window, launches run the cached install directly — sub-second start, no npm registry contact, fully offline-capable. The launcher path never changes, so the plugin config never goes stale.

**Update behavior:**
- First launch of the day (per agent) checks the registry and installs any newer version; subsequent launches are instant.
- `acp-launch --update` (or `--update <agent>`) forces an update check on the next launch.
- Pinned versions (`claude@0.58.1` in the plugin Args field) are never re-fetched until the pin changes — the no-file-edit way to hold back a misbehaving release.
- If an update check fails (offline), the launcher falls back to the existing install and keeps working.

**Verify the setup** with the ACP doctor script, which checks the runtime, agent CLIs, the launcher (including a live ACP handshake per agent with `--handshake`), login state, and the plugin config itself:

```bash
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py            # diagnose
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py --fix      # create/repair the launcher, install missing CLIs
uv run 00-CORE/Agents/skills/acp-doctor/scripts/acp_doctor.py --report   # also write a diagnostic note into the vault
```

> The doctor is the certified `acp-doctor` skill — you can also just ask the agent: "acp doctor, check my agents".

---
## 4. Installation Overview Table

The pure native windows installation that are becoming available , are currently not working reliably.

> With the recommended launcher (section 3) the configured path is always the same — `~/bin/acp-launch` — and the path-finding commands below only matter for the manual route.

| Operating System    | CLI Tool    | Supported ? | Path Finding Command (manual route) |
| ------------------- | ----------- | ----------- | ----------------------------------- |
| macOS / Linux / WSL | any (launcher) | Y        | `which acp-launch`                  |
| macOS / Linux / WSL | Claude Code | Y           | `which claude-agent-acp`            |
| macOS / Linux / WSL | Codex       | Y           | `which codex-acp`                   |
| macOS / Linux / WSL | Gemini CLI  | Y           | `which gemini`                      |
| Windows             | Claude Code | No          | `where.exe claude-agent-acp`        |
| Windows             | Codex       | No          | `where.exe codex-acp`               |
| Windows             | Gemini CLI  | No          | `where.exe gemini`                  |

### Install the frontmatter hooks (every machine)

After the CLIs work, install the vault's write-time hooks for each agent you use. Claude Code,
Codex and Antigravity each have their own config file. The hooks are per machine: syncing the
vault does not carry them to a new laptop. The steps and the checks are in
[[install-agent-hooks|Install the frontmatter hooks]].

----

## 5. Plugin Configuration

## 5.1 Agent Client
### CLI Agent Provider
Once you have installed your desired CLI tools and found their paths, you need to configure the Agent Client plugin in Obsidian:

1.  Open **Settings → Agent Client**.
2.  **Node.js path**: Enter the absolute path to your Node.js executable (e.g., `/usr/local/bin/node` or `C:\Program Files\nodejs\node.exe`).
3.  Configure your preferred agents. **Recommended (launcher, section 3)** — same command for every agent, agent name as the argument:
    -   **Claude Code**: command `/home/you/bin/acp-launch`, args `claude`
    -   **Codex**: command `/home/you/bin/acp-launch`, args `codex`
    -   **Gemini CLI**: command `/home/you/bin/acp-launch`, args `gemini` (no `--experimental-acp` needed — the launcher adds it)

    **Manual route (section 2)** — absolute adapter paths instead:
    -   **Claude Code Path**: (e.g., `/usr/local/bin/claude-agent-acp`)
    -   **Codex Path**: (e.g., `/usr/local/bin/codex-acp`)
    -   **Gemini CLI Path**: (e.g., `/usr/local/bin/gemini`, args `--experimental-acp`)

    API keys are usually unnecessary — the agents use your subscription logins.
4.  You can also add any other ACP-compatible agents in the **Custom Agents** section — with the launcher, use command `/home/you/bin/acp-launch` and args `npm:@vendor/their-acp-adapter`.

### Export options
![[Agent Client Export Configuration Options.png]]

* #### Review default folder locations
* Decide on your folder structure and update the default export folder and filenaming convention and image location if necessary

#### Ensure all chats saved locally
* Enable all auto-export options

