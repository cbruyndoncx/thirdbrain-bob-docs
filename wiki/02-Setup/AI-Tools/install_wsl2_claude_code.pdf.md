---
type: knowledge-base
title: "Install WSL2 + Claude Code on Windows"
status: final
created: 2026-04-20
modified: 2026-04-20
tags: [learning/tools, setup, wsl2, claude-code, windows]
headerTemplate: |
  <div style="display:flex;justify-content:space-between;align-items:center;width:100%;padding:8px 24px;font-size:10px;"> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNDAgNjAiIHdpZHRoPSIyNDAiIGhlaWdodD0iNjAiPgogIDxkZWZzPgogICAgPGxpbmVhckdyYWRpZW50IGlkPSJicmFuZEdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMGQ5NDg4Ii8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzA4OTFiMiIvPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM+CiAgPCEtLSBMb2dvbWFyazogYW5nbGVkIGJyYWNrZXQgcGFpciAtLT4KICA8cGF0aCBkPSJNOCwzMCBMMjIsMTYgTDIyLDIyIEwxNCwzMCBMMjIsMzggTDIyLDQ0IFoiIGZpbGw9InVybCgjYnJhbmRHcmFkKSIvPgogIDxwYXRoIGQ9Ik00MiwzMCBMMjgsMTYgTDI4LDIyIEwzNiwzMCBMMjgsMzggTDI4LDQ0IFoiIGZpbGw9InVybCgjYnJhbmRHcmFkKSIvPgogIDwhLS0gV29yZG1hcmsgYXMgc2luZ2xlIHRleHQgd2l0aCB0c3BhbiBmb3IgbmF0dXJhbCBnbHlwaCBmbG93IC0tPgogIDx0ZXh0IHg9IjUyIiB5PSIzOCIgZm9udC1mYW1pbHk9IidJbnRlcicsJ1NlZ29lIFVJJyxzeXN0ZW0tdWksc2Fucy1zZXJpZiI+CiAgICA8dHNwYW4gZm9udC1zaXplPSIyOCIgZm9udC13ZWlnaHQ9IjcwMCIgbGV0dGVyLXNwYWNpbmc9IjIiIGZpbGw9InVybCgjYnJhbmRHcmFkKSI+QlJOPC90c3Bhbj48dHNwYW4gZm9udC1zaXplPSIxOCIgZm9udC13ZWlnaHQ9IjMwMCIgZmlsbD0iIzA2YjZkNCIgZHk9Ii0yIj4oLjwvdHNwYW4+PHRzcGFuIGZvbnQtc2l6ZT0iMTgiIGZvbnQtd2VpZ2h0PSIzMDAiIGZpbGw9IiMwNmI2ZDQiPik8L3RzcGFuPjx0c3BhbiBmb250LXNpemU9IjI4IiBmb250LXdlaWdodD0iMzAwIiBsZXR0ZXItc3BhY2luZz0iMSIgZmlsbD0iIzA2YjZkNCIgZHk9IjIiPmN4PC90c3Bhbj4KICA8L3RleHQ+Cjwvc3ZnPgo=" style="height:20px;" alt="Company Logo" /> <span style="flex:1;"></span> <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OCA0OCIgd2lkdGg9IjQ4IiBoZWlnaHQ9IjQ4Ij4KICA8ZGVmcz4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYnJhbmRHcmFkIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj4KICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzBkOTQ4OCIvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiMwODkxYjIiLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgPC9kZWZzPgogIDwhLS0gQW5nbGVkIGJyYWNrZXQgcGFpciAtLT4KICA8cGF0aCBkPSJNNiwyNCBMMTgsMTAgTDE4LDE2IEwxMSwyNCBMMTgsMzIgTDE4LDM4IFoiIGZpbGw9InVybCgjYnJhbmRHcmFkKSIvPgogIDxwYXRoIGQ9Ik00MiwyNCBMMzAsMTAgTDMwLDE2IEwzNywyNCBMMzAsMzIgTDMwLDM4IFoiIGZpbGw9InVybCgjYnJhbmRHcmFkKSIvPgo8L3N2Zz4K" style="height:20px;" alt="Client Logo" /> </div>
footerTemplate: |
  <div style="width:100%;padding:4px 24px;font-size:9px;text-align:center;color:#999;"> <span class="pageNumber"></span> </div>
printBackground: false
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
