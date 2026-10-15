---
title: Install WSL2 + Claude Code on Windows
---

I
# Claude Code on WSL2 — Full Installation Guide

## Part 0: PowerShell versions & opening as Administrator

### Which PowerShell?

There are two:

| Version | Also called | Ships with | Icon color | Command |
|---------|-------------|------------|------------|---------|
| **Windows PowerShell 5.1** | "PowerShell" | Windows 10/11 (built-in) | Blue | `powershell.exe` |
| **PowerShell 7.x** | "PowerShell Core" / "pwsh" | Optional install | Black | `pwsh.exe` |

**For this install, either works.** `wsl --install` is a native Windows command — it doesn't care which PowerShell calls it. If you only see the blue one, use that. No need to install PowerShell 7 just for this.

### How to open PowerShell as Administrator

Pick any of these — they all get you an elevated prompt. You'll see **"Administrator:"** in the title bar when it worked.

**Method 1 — Win+X menu (fastest)**
1. Press **`Win + X`** (or right-click the Start button)
2. Click **"Terminal (Admin)"** (Windows 11) or **"Windows PowerShell (Admin)"** (Windows 10)
3. Click **Yes** on the UAC prompt

**Method 2 — Start menu search**
1. Press **`Win`** key
2. Type `powershell`
3. On the right side, click **"Run as administrator"** (or right-click the result → **Run as administrator**)
4. Click **Yes** on the UAC prompt

**Method 3 — Run dialog**
1. Press **`Win + R`**
2. Type `powershell`
3. Press **`Ctrl + Shift + Enter`** (instead of just Enter — this forces admin)
4. Click **Yes** on the UAC prompt

**Method 4 — Windows Terminal dropdown** (if installed)
1. Open Windows Terminal
2. Click the **`⌄`** dropdown next to the `+` tab
3. Hold **`Ctrl`** and click **"Windows PowerShell"** — opens elevated

**Verify you're actually admin:**
```powershell
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```
Returns `True` if elevated.

---

## Part 1: Install WSL2

**Check if WSL2 is already installed** (in your elevated PowerShell):
```powershell
wsl --status
```
If it shows `Default Version: 2`, skip to Part 2.

### 1.1 Enable WSL2 and install Ubuntu

```powershell
wsl --install -d Ubuntu
```
Does all of: enables WSL + Virtual Machine Platform features, downloads the kernel, installs Ubuntu, sets WSL2 as default.

**Reboot** when prompted.

### 1.2 Create your Linux user

After reboot, Ubuntu launches automatically. Set:
- **Username** (lowercase, no spaces — e.g., `chris`)
- **Password** (you'll need this for `sudo`)

### 1.3 Update the system

Inside Ubuntu:
```bash
sudo apt update && sudo apt upgrade -y
```

---

## Part 2: Install prerequisites

### 2.1 Install Node.js via nvm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts
```

Verify:
```bash
node --version   # v20.x or v22.x
npm --version
```

**Why nvm, not `apt install nodejs`:** Ubuntu's apt ships old Node; Claude Code needs 18+.

### 2.2 Install & configure git

```bash
sudo apt install -y git
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## Part 3: Install Claude Code

### 3.1 Install via npm

```bash
npm install -g @anthropic-ai/claude-code
```

If you hit `EACCES`, **do not use sudo**. Fix npm's global path:
```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code
```

### 3.2 Verify and authenticate

```bash
claude --version
cd ~
claude
```
First launch opens a browser link for Anthropic auth. Sign in, paste the returned token.

---

## Part 4: Windows integration

### 4.1 Install Windows Terminal

From Microsoft Store. Auto-detects your Ubuntu profile — far better than the default console.

### 4.2 Where to keep your code

| Location | Speed | Use for |
|----------|-------|---------|
| `~/projects/` (WSL ext4) | Native Linux speed | Active dev, npm/pip projects |
| `/mnt/c/` or `/mnt/d/` | 5–10× slower | Files Windows apps need (Obsidian vaults) |

**Rule:** Linux-only tooling → `~/`. Windows apps also read it → `/mnt/`.

---

## Part 5: Verify

```bash
cd ~ && mkdir test-claude && cd test-claude
claude
```
Ask: *"what files are in this directory?"* — Claude should use its tools. Exit with `/exit`.

---

## Common issues

| Problem | Fix |
|---------|-----|
| `claude: command not found` | `source ~/.bashrc` or reopen terminal |
| `EACCES` on npm install | Use `~/.npm-global` prefix (never `sudo npm`) |
| Slow file ops on `/mnt/c/` | Move project to `~/` |
| WSL1 instead of WSL2 | `wsl --set-version Ubuntu 2` |
| UAC prompt doesn't appear | You're not on an admin account — ask your IT admin |
| "The Virtual Machine Platform feature is not enabled" | `wsl --install --no-distribution` then reboot, then retry |
