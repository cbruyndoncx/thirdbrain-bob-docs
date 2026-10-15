---
title: Environment Checklist — Pre-Installation Verification
---

# Environment Checklist — Pre-Installation Verification

Verification checklist to confirm a target machine is ready for BOB installation. You're not installing anything yet — just checking what's already there and what's missing.

---

## Choose Your Path

BOB runs on a **Unix-style shell**. There are two supported paths:

### ✅ Recommended — Mac, Linux, or Windows + WSL2 (bash)

This is the primary path. All commands below assume **bash** (Mac Terminal, Linux terminal, or WSL2 on Windows).

- **Mac users**: open Terminal — you're done, skip to checks
- **Linux users**: open your terminal — skip to checks
- **Windows users**: install **WSL2** with Ubuntu first. WSL2 gives you a real Linux environment on Windows. It is the recommended path because:
  - All AI tooling (Claude Code, npm, uv, git) works natively
  - Skills using bash scripts run without translation
  - Stable, fewer surprises than mixing PowerShell + native Windows tools
  - See [install_wsl2_claude_code](../../02-Setup/AI-Tools/install_wsl2_claude_code.md) for setup

### ⚠️ Alternative — Pure Windows + PowerShell

Use this **only** if you already have a fully-configured Windows-native developer setup (Node.js, Python, git all installed natively) and you do not want to install WSL2. PowerShell-equivalent commands are listed in the *PowerShell alternative* notes under each check.

For everyone else: **install WSL2 and use bash**. It will save you hours of compatibility issues with AI agent tooling.

---

## Instructions

1. Open your **bash terminal** (Mac Terminal / Linux terminal / WSL2 Ubuntu shell)
2. Run each command below
3. Note the **version number** and **✅ Pass** or **❌ Missing**
4. If something is missing, refer to troubleshooting or the installation guide

---

## Operating System & Platform

### OS & Kernel

```bash
# In bash, run:
uname -a
```

**Expected**: Linux kernel (WSL2 reports "WSL2" in the string), Darwin (Mac), or your Linux distro

**Your result**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ Mac (Darwin)
- [ ] ✅ Linux (Ubuntu / Debian / Fedora / etc.)
- [ ] ✅ Windows + WSL2 (kernel string contains `WSL2`)
- [ ] ❌ Pure Windows / unsupported

> **PowerShell alternative** (pure-Windows path only):
> ```powershell
> [System.Environment]::OSVersion.VersionString
> ```
> Expected: Windows 10 (build 19041+) or Windows 11.

---

### WSL2 Status (Windows users only)

If you are on Windows, verify WSL2 is installed and you have a Linux distro running:

```powershell
# In PowerShell (Windows), run:
wsl --list --verbose
```

**Expected output**:

```
NAME      STATE           VERSION
Ubuntu    Running         2
```

- [ ] ✅ WSL2 installed and running (proceed in your WSL Ubuntu shell)
- [ ] ⚠️ WSL2 installed but stopped — start with `wsl`
- [ ] ❌ WSL2 not installed — install it before continuing: [install_wsl2_claude_code](../../02-Setup/AI-Tools/install_wsl2_claude_code.md)

Mac and Linux users skip this section.

---

## Programming Languages & Runtimes

### Node.js & npm

```bash
# In bash, run:
node --version
npm --version
```

**Expected**: Node 18+, npm 9+

- Node: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- npm: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ Node 18+ and npm 9+ detected
- [ ] ⚠️ Detected but older version
- [ ] ❌ Node or npm not found

> **PowerShell alternative**: same commands work in PowerShell if you have native-Windows Node installed.

---

### Python

```bash
# In bash, run:
python3 --version
```

**Expected**: Python 3.10 or higher
**Your result**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ Python 3.10+ detected
- [ ] ⚠️ Detected but older version
- [ ] ❌ Python not found

**Note**: Python is needed for some skills, not required for initial BOB installation.

> **PowerShell alternative**: `python --version` (note: no `3` suffix on native Windows).

---

### uv (Python Package Manager)

```bash
# In bash, run:
uv --version
```

**Expected**: uv 0.4+
**Your result**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ uv detected
- [ ] ❌ uv not found

**Note**: uv is a modern Python package manager. Will be installed in Week 1 if missing.

---

## Git (Version Control)

```bash
# In bash, run:
git --version
```

**Expected**: git 2.30+
**Your result**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ git detected
- [ ] ⚠️ Detected but older version
- [ ] ❌ git not found

**Note**: Required for managing BOB vault updates.

---

## Disk Space & System Resources

### Available Disk Space

```bash
# In bash, run:
df -h
```

**Look for**: A drive/partition with **10+ GB free** where the BOB vault will live.

**Your result**:
- Drive/path: \_\_\_\_\_\_\_\_\_\_\_\_
- Free space: \_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ 10+ GB available
- [ ] ⚠️ Less than 10 GB available
- [ ] ❌ Very low disk space

> **PowerShell alternative**:
> ```powershell
> Get-Volume
> ```

---

### RAM

```bash
# In bash, run:
free -h        # Linux / WSL2
# OR on Mac:
sysctl hw.memsize | awk '{print $2/1024/1024/1024 " GB"}'
```

**Expected**: 8+ GB RAM
**Your result**: \_\_\_\_\_\_\_\_\_\_\_\_

- [ ] ✅ 8+ GB RAM
- [ ] ⚠️ 4–8 GB RAM (works but slower)
- [ ] ❌ Less than 4 GB RAM

> **PowerShell alternative**:
> ```powershell
> $totalRAM = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB
> Write-Host "Total RAM: $totalRAM GB"
> ```

---

## Optional: Check for Key Software

### Obsidian

Obsidian is a desktop app (installed on the host OS, not inside WSL2). Check on your host:

- **Mac**: look in `/Applications/Obsidian.app`
- **Linux**: `which obsidian` or check your app launcher
- **Windows (host)**: `Test-Path "C:\Program Files\Obsidian"` in PowerShell

**Your result**: ✅ / ❌

- [ ] ✅ Not installed yet — install via getting_started
- [ ] ✅ Already installed (note version)

---

### Claude Code

```bash
# In bash, run:
which claude
claude --version
```

**Expected**: Not installed yet
**Your result**: ✅ / ❌

- [ ] ✅ Not installed yet — install via [claude-code-installation-on-windows-using-wsl](../../02-Setup/AI-Tools/claude-code-installation-on-windows-using-wsl.md)
- [ ] ✅ Already installed (note version)

> **PowerShell alternative**: `Get-Command claude -ErrorAction SilentlyContinue`

---

## Summary Table

Fill this in after running all checks:

| Component | Status | Version/Details | Notes |
|-----------|--------|-----------------|-------|
| OS / Shell | ✅/❌ | Mac / Linux / WSL2 / pure Win | |
| WSL2 (Windows only) | ✅/❌ | | |
| Node.js | ✅/❌ | | |
| npm | ✅/❌ | | |
| Python | ✅/❌ | | |
| uv | ✅/❌ | | |
| git | ✅/❌ | | |
| Disk space | ✅/❌ | \_\_ GB free | |
| RAM | ✅/❌ | \_\_ GB | |
| Obsidian | ✅/❌ | | |
| Claude Code | ✅/❌ | | |

---

## What Happens Next

**If everything is ✅:**
- You're ready to install BOB — see getting_started (DIY) or [quickstart](../../02-Setup/quickstart.md) (DFY)

**If some items are ❌ or ⚠️:**
- Note the missing items
- If you're on Windows without WSL2 → install WSL2 first: [install_wsl2_claude_code](../../02-Setup/AI-Tools/install_wsl2_claude_code.md)
- For other missing items, follow the relevant install guide under `{vault.wiki}/02-Setup/`
- If you have a technical lead, share these results with them

---

## Troubleshooting Commands

If a command doesn't run, try these:

| Issue | Fix |
|-------|-----|
| Command not found in WSL2 | Try `which <command>` to see if it's on PATH |
| Command not found in PowerShell | Switch to WSL2 (`wsl`) — it's the recommended environment |
| Permission denied | Try `sudo <command>` (may prompt for password) |
| WSL2 won't start | In PowerShell as Admin: `wsl --shutdown` then `wsl` |

---

## Tips

1. **Use WSL2 on Windows.** PowerShell-only setups work but are higher friction with AI tooling — every hour saved on environment trouble is an hour Vaishavi can spend learning BOB.
2. **Copy & paste is your friend** — right-click in terminal to paste (not Ctrl+V in WSL)
3. **Capture version numbers** — useful if you hit issues later
4. **Don't guess on errors** — copy the exact message; check [quickstart](../../02-Setup/quickstart.md#troubleshooting) or your install guide
5. **Exact text matters** — version numbers and details help troubleshooting
