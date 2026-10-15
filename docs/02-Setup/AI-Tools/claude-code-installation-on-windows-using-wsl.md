---
title: Claude code installation on Windows 11 using WSL2
---

# Claude Code Installation Guide for Windows 11
> this is a remix of instructions found on claude.ai, unclear who made the initial version, only relevant sections are kept and some added to make it more comprehensive and beginner friendly

Claude Code is Anthropic's official AI-powered coding assistant that runs in your terminal, but it **requires Windows Subsystem for Linux (WSL2)** to work on Windows 11 - it cannot run natively on Windows. This terminal-based tool integrates directly with your development environment to assist with code editing, debugging, testing, git workflows, and project understanding through natural language commands.

---

## Quickstart (Commands Only)

If you're comfortable with terminals, here are all the commands. For detailed explanations, see the full guide below.

### Step 1: Install WSL2 (PowerShell as Administrator)

Right-click Start button → "Terminal (Admin)" or "PowerShell (Admin)"

```powershell
wsl --install
```

### ⚠️ RESTART YOUR COMPUTER

### Step 2: Set up Ubuntu (Ubuntu/WSL Terminal)

After restart, open **Ubuntu** from Start menu (or type `wsl` in any terminal).

Create your Linux username and password when prompted. (Password won't show as you type - this is normal.)

### Step 3: Install everything (Ubuntu/WSL Terminal)

Copy and run these commands one section at a time:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc

# Configure npm for user installs (avoids permission issues)
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Install Claude Code
npm install -g @anthropic-ai/claude-code
```

### Step 4: Verify installation (Ubuntu/WSL Terminal)

```bash
node --version      # Should show v20.x.x
npm --version       # Should show 10.x.x
uv --version        # Should show 0.4.x or higher
claude --version    # Should show version number
```

### Step 5: First run and authentication (Ubuntu/WSL Terminal)

```bash
mkdir ~/my-project
cd ~/my-project
claude
```

Follow the prompts to authenticate with your Anthropic account or API key.

---

## Table of Contents

- [Quickstart (Commands Only)](#quickstart-commands-only) ← Start here if you're comfortable with terminals

1. [System requirements and prerequisites](#1-system-requirements-and-prerequisites)
   - 1.1 [Understanding why Claude Code needs Linux on Windows](#11-understanding-why-claude-code-needs-linux-on-windows)
   - 1.2 [Windows 11 version requirements](#12-windows-11-version-requirements)
   - 1.3 [Hardware requirements](#13-hardware-requirements)
   - 1.4 [Software component breakdown](#14-software-component-breakdown)
   - 1.5 [Terminal emulator choices](#15-terminal-emulator-choices)
   - 1.6 [Checking your internet connection](#16-checking-your-internet-connection)
   - 1.7 [Preparing your mindset](#17-preparing-your-mindset)
2. [Complete installation process](#2-complete-installation-process)
   - 2.1 [Phase 1: Installing WSL2](#21-phase-1-installing-wsl2-windows-subsystem-for-linux)
   - 2.2 [Phase 2: Setting up your Linux environment](#22-phase-2-setting-up-your-linux-environment)
   - 2.3 [Phase 3: Updating and preparing the Linux system](#23-phase-3-updating-and-preparing-the-linux-system)
   - 2.4 [Phase 4: Installing Node.js and npm](#24-phase-4-installing-nodejs-and-npm)
   - 2.5 [Phase 5: Installing uv and uvx](#25-phase-5-installing-uv-and-uvx-python-package-manager)
   - 2.6 [Phase 6: Configuring npm for user installations](#26-phase-6-configuring-npm-for-user-installations)
3. [Installing Claude Code itself](#3-installing-claude-code-itself)
   - 3.1 [Understanding the npm installation process](#31-understanding-the-npm-installation-process)
   - 3.2 [Running the installation command](#32-running-the-installation-command)
   - 3.3 [Understanding what just got installed](#33-understanding-what-just-got-installed)
   - 3.4 [Verifying the installation](#34-verifying-the-installation)
   - 3.5 [First run and authentication](#35-first-run-and-authentication)
   - 3.6 [Understanding authentication options](#36-understanding-authentication-options)
   - 3.7 [Completing the authentication process](#37-completing-the-authentication-process)
   - 3.8 [Troubleshooting authentication issues](#38-troubleshooting-authentication-issues)
4. [Configuration and verification](#4-configuration-and-verification)
   - 4.1 [Understanding Claude Code's configuration system](#41-understanding-claude-codes-configuration-system)
   - 4.2 [Configuring permissions and boundaries](#42-configuring-permissions-and-boundaries)
   - 4.3 [Setting up terminal compatibility](#43-setting-up-terminal-compatibility)
   - 4.4 [Testing core functionality](#44-testing-core-functionality)
   - 4.5 [Testing Windows file system integration](#45-testing-windows-file-system-integration)
   - 4.6 [Customizing Claude Code's behavior](#46-customizing-claude-codes-behavior)
   - 4.7 [Creating your first real interaction](#47-creating-your-first-real-interaction)
   - 4.8 [Saving and backing up your configuration](#48-saving-and-backing-up-your-configuration)
5. [Common troubleshooting issues](#5-common-troubleshooting-issues)
6. [Performance and best practices](#6-performance-and-best-practices)
7. [Your first conversation with Claude Code](#7-your-first-conversation-with-claude-code)
   - 7.1 [Starting Claude Code](#71-starting-claude-code)
   - 7.2 [Things you can ask Claude Code](#72-things-you-can-ask-claude-code)
   - 7.3 [Tips for effective communication](#73-tips-for-effective-communication)
   - 7.4 [Ending your session](#74-ending-your-session)
8. [Conclusion](#8-conclusion)

---

## 1. System requirements and prerequisites

Before diving into the installation, let's understand what Claude Code needs to run properly on your Windows 11 system. Think of these requirements like ingredients for a recipe - missing even one can prevent the final dish from turning out right. I'll explain not just what you need, but why each component matters and how to check if you already have it.

### 1.1 Understanding why Claude Code needs Linux on Windows

Claude Code is built as a command-line tool designed for Unix-like operating systems (Linux and macOS). While Windows is an excellent operating system, it handles certain technical aspects differently than Linux - things like file permissions, process management, and system calls. Rather than creating a separate Windows version, Anthropic chose to leverage Microsoft's Windows Subsystem for Linux (WSL2), which lets you run a real Linux environment inside Windows. This approach ensures Claude Code works exactly the same way across all platforms and gets all the same updates and features.

### 1.2 Windows 11 version requirements

You'll need Windows 11 version 21H2 or later. To check your version, press Windows key + R to open the Run dialog, type `winver`, and press Enter. A window will pop up showing your Windows version. Look for something like "Version 22H2 (OS Build 22621.2428)" - as long as it says 21H2 or higher (like 22H2, 23H2), you're good to go. If you're on an older version, you'll need to update Windows first by going to Settings > Windows Update and installing any available updates.

The reason version 21H2 or later is required is that Microsoft significantly improved WSL2 integration in these versions, including better file system performance and GPU support. While WSL2 technically works on older Windows 11 versions, you'll have a much smoother experience with the newer releases.

### 1.3 Hardware requirements

WSL2 requires virtualization support from your CPU, which virtually all modern processors have, but it needs to be enabled. Your system needs at least 4GB of RAM, though 8GB or more is strongly recommended for comfortable development work. When you run Claude Code alongside your code editor, browser, and other development tools, memory usage adds up quickly. You'll also need about 2-4GB of free disk space for the WSL2 installation and Claude Code itself, plus space for your project files.

To check if virtualization is enabled on your system, open Task Manager (Ctrl + Shift + Esc), click on the Performance tab, select CPU on the left side, and look for "Virtualization: Enabled" on the right side. If it says "Disabled", you'll need to enable it in your computer's BIOS/UEFI settings - the exact steps vary by manufacturer, but typically involve pressing F2, F10, or Delete during startup and looking for options like "Intel VT-x", "AMD-V", or "Virtualization Technology".

### 1.4 Software component breakdown

Let me explain each required software component and why it's necessary. First, WSL2 (Windows Subsystem for Linux 2) is Microsoft's technology for running Linux alongside Windows. The "2" is important - WSL2 uses real Linux kernel technology and is much faster than the original WSL. It's not installed by default on Windows 11, but Microsoft makes it easy to add.

Node.js is a JavaScript runtime that lets you run JavaScript code outside of a web browser. Claude Code is built with JavaScript/TypeScript and distributed through npm (Node Package Manager), which comes bundled with Node.js. Think of Node.js as the engine that powers Claude Code, while npm is like the delivery service that installs it. You need Node.js version 18 or higher because Claude Code uses modern JavaScript features that weren't available in older versions. The LTS (Long Term Support) versions are recommended because they receive security updates for longer and are more stable.

Ubuntu 20.04+ or Debian 10+ are Linux distributions - think of them as different "flavors" of Linux, like how Windows has Home and Pro editions. Ubuntu is recommended for beginners because it's user-friendly and has extensive documentation. The numbers (20.04, 10) refer to version numbers - you need these minimum versions because they include necessary system libraries and package managers that Claude Code depends on.

### 1.5 Terminal emulator choices

While Windows 11 comes with Windows Terminal pre-installed (a modern, feature-rich terminal), you might already have other options like the traditional Command Prompt or PowerShell. For the best experience with Claude Code, Windows Terminal is highly recommended because it properly handles special characters, colors, and Unicode that Claude Code uses for its interface. It also makes it easy to have multiple tabs and switch between Windows and Linux environments.

If you don't see Windows Terminal on your system, you can install it free from the Microsoft Store. Just open the Microsoft Store app, search for "Windows Terminal", and click Install. Other compatible alternatives include ConEmu, Hyper, or even the integrated terminals in VS Code or other development environments, though these might require additional configuration.

### 1.6 Checking your internet connection

You'll need a stable internet connection during installation to download several components: WSL2 and Ubuntu (about 500MB), Node.js (about 30MB), Claude Code and its dependencies (about 50MB), and system updates (varies, but typically 100-200MB). The total download is usually under 1GB, but having a reliable connection prevents frustrating interruptions during setup.

Additionally, Claude Code requires internet access during use to communicate with Anthropic's AI servers. While you can work on local files offline, the AI assistance features need an active connection. If you're behind a corporate firewall or proxy, you might need additional configuration - check with your IT department if you're in a corporate environment.

### 1.7 Preparing your mindset

One final "prerequisite" worth mentioning is patience and a willingness to learn some Linux basics. If you've never used a command line or Linux before, some parts might feel unfamiliar at first. That's completely normal! The command line might seem intimidating compared to clicking buttons in a graphical interface, but it's actually quite logical once you understand the patterns. Think of it like learning to drive a manual transmission after only knowing automatic - there's a learning curve, but you gain much more control and understanding of what's happening under the hood.

---

## 2. Complete installation process

The installation involves six distinct phases that must be completed in order. Think of this like building a house - you need the foundation (WSL2) before you can add the framework (Node.js) and finally the finishing touches (Claude Code itself).

### 2.1 Phase 1: Installing WSL2 (Windows Subsystem for Linux)

To open PowerShell as Administrator on Windows 11, you have several options. The most straightforward method is to right-click the Start button (the Windows icon in your taskbar) and select "Windows Terminal (Admin)" or "PowerShell (Admin)" from the menu that appears. Alternatively, you can press the Windows key on your keyboard, type "powershell", and when you see "Windows PowerShell" appear in the search results, right-click it and select "Run as administrator". You can also use the keyboard shortcut Windows+X followed by pressing A. When prompted by User Account Control asking "Do you want to allow this app to make changes to your device?", click "Yes".

Once PowerShell opens with administrator privileges, you'll see "Administrator: Windows PowerShell" in the title bar. The prompt will typically show something like `PS C:\Windows\system32>`. Now run the following command:

```powershell
wsl --install
```

This command does several things automatically: it enables the required Windows features (Virtual Machine Platform and Windows Subsystem for Linux), downloads and installs the WSL2 kernel update, sets WSL2 as the default version, and installs Ubuntu as the default Linux distribution. The process will show progress bars and status messages. It typically takes 5-10 minutes depending on your internet speed.

After the installation completes, you'll see a message saying "The requested operation is successful. Changes will not be effective until the system is rebooted." Restart your computer by clicking Start, then the power button, and selecting "Restart". This restart is crucial - WSL2 won't work properly without it.

### 2.2 Phase 2: Setting up your Linux environment

After your computer restarts, you need to launch Ubuntu for the first time. You can do this in three ways: click the Start button and type "Ubuntu", then click on the Ubuntu app that appears; or open Windows Terminal and click the dropdown arrow next to the new tab button and select "Ubuntu"; or open any terminal and type `wsl`.

The first time Ubuntu launches, it will take a minute or two to complete installation. You'll see messages like "Installing, this may take a few minutes..." followed by "Installation successful!" Then you'll be prompted to create a Unix username and password. This is an important step that many new users find confusing. The username you create here is for your Linux environment only - it doesn't need to match your Windows username. For example, if your Windows username is "JohnDoe", you could use "john" or "jdoe" or any other valid Linux username. Type your chosen username and press Enter.

Next, you'll be prompted to enter a password. Here's a critical detail: when you type your password, nothing will appear on screen - no asterisks, no dots, nothing. This is a security feature in Linux terminals. Just type your password carefully and press Enter. You'll be asked to retype it to confirm. Choose a password you'll remember because you'll need it for administrative commands (sudo) later. Write it down somewhere safe if needed.

### 2.3 Phase 3: Updating and preparing the Linux system

Now you're inside your Ubuntu environment. The prompt will look something like `username@computername:~$`. The `~` symbol represents your home directory. First, update the package manager to ensure you have access to the latest software. Run these commands one at a time:

```bash
sudo apt update
```

When you run this first sudo command, it will ask for your password - the one you just created. Again, nothing will appear as you type. This command updates the list of available packages. You'll see many lines of output showing it connecting to Ubuntu's servers and downloading package information.

```bash
sudo apt upgrade -y
```

This command upgrades all installed packages to their latest versions. The `-y` flag automatically answers "yes" to the confirmation prompt. This might take several minutes and show a lot of output. Don't worry if you see warnings about kernel updates being held back - this is normal in WSL.

### 2.4 Phase 4: Installing Node.js and npm

Claude Code requires Node.js version 18 or higher. While you could install Node.js through Ubuntu's default repositories, they often contain older versions. Instead, we'll use NodeSource's repository to get the latest LTS version. First, download and run the setup script:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```

This command does several things: `curl` downloads the setup script, `-fsSL` ensures it fails properly on errors and shows a progress bar, the pipe `|` sends the downloaded script to bash to execute it, and `sudo -E` runs it with administrator privileges while preserving environment variables. You'll see output showing it's adding the NodeSource signing key and repository.

Now install Node.js:

```bash
sudo apt install -y nodejs
```

This installs both Node.js and npm (Node Package Manager). The installation will show progress and complete in about a minute. Verify the installation worked:

```bash
node --version
```

This should show something like `v20.11.0` or higher. Then check npm:

```bash
npm --version
```

This should show version 10.x.x or higher.

### 2.5 Phase 5: Installing uv and uvx (Python package manager)

uv is a fast Python package manager that some tools and scripts use. uvx lets you run Python tools without installing them permanently. Even if you don't use Python directly, some AI tools may need these. Install uv with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This downloads and runs the official installer. After it completes, reload your shell configuration:

```bash
source ~/.bashrc
```

Verify the installation:

```bash
uv --version
```

You should see a version number like `0.4.x` or higher. uvx is included with uv, so you can test it with:

```bash
uvx --version
```

If you need Python itself, uv can install it for you:

```bash
uv python install 3.12
```

This installs a standalone Python that uv manages, separate from any system Python.

### 2.6 Phase 6: Configuring npm for user installations

By default, npm tries to install global packages in system directories, which requires sudo and can cause permission issues. We'll configure it to use a directory in your home folder instead. This is a best practice that prevents many common problems. First, create a directory for global npm packages:

```bash
mkdir -p ~/.npm-global
```

The `-p` flag means "create parent directories as needed". The `~/.npm-global` is a hidden directory (the dot makes it hidden) in your home folder. Tell npm to use this directory:

```bash
npm config set prefix ~/.npm-global
```

Now you need to add this directory to your PATH so your system can find the installed programs. The PATH is like a list of places your system looks for commands. Add it to your configuration file:

```bash
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
```

This command appends (`>>`) a line to your `.bashrc` file, which runs every time you open a terminal. The line adds your npm global directory to the beginning of PATH. Apply the changes to your current session:

```bash
source ~/.bashrc
```

This reloads your `.bashrc` file without needing to close and reopen the terminal. You can verify it worked by running:

```bash
echo $PATH
```

You should see `/home/yourusername/.npm-global/bin` at the beginning of the output.

---

## 3. Installing Claude Code itself

Now we arrive at the moment you've been preparing for - actually installing Claude Code. If the previous steps were like preparing a garden bed, this is where we plant the seed. The good news is that if you've followed the previous steps correctly, this part should be smooth and straightforward.

### 3.1 Understanding the npm installation process

Before we run the installation command, let's understand what's about to happen. When you install a package globally with npm (that's what the `-g` flag means), npm downloads the package and all its dependencies from the npm registry, a massive online repository of JavaScript packages. It then places the executable files in your designated global bin directory (remember when we set that up?), making them available as commands you can run from anywhere in your terminal.

Open your WSL Ubuntu terminal if it's not already open. You can verify you're in the right place by checking that your prompt shows your Linux username, not your Windows path. It should look something like `username@computername:~$`. If you see something like `/mnt/c/Users/...`, you're looking at your Windows file system through Linux, which is fine - you can run the installation from anywhere.

### 3.2 Running the installation command

Now, type or copy this command exactly:

```bash
npm install -g @anthropic-ai/claude-code
```

Let me break down what each part means. The `npm install` tells npm to download and install a package. The `-g` flag means "globally" - install this for use anywhere on the system, not just in a specific project. The `@anthropic-ai/claude-code` is the official package name - the `@anthropic-ai` part is Anthropic's namespace on npm (like a username), ensuring you're getting the authentic package, not someone else's project with a similar name.

Here's a crucial point that trips up many Windows users: **do not use sudo with this command**. On traditional Linux systems, you might need sudo for global installations, but remember we configured npm to use your personal directory specifically to avoid this. If you use sudo here, it will install Claude Code in the wrong location and cause permission problems later. Just run the command as your regular user.

When you press Enter, you'll see npm spring into action. The output will show several things happening. First, it contacts the npm registry and downloads the package metadata. Then it analyzes dependencies - Claude Code relies on other packages to work, and npm figures out exactly which versions it needs. You'll see a progress bar as it downloads each package. The output might look something like:

```
⸨⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⸩ ⠧ idealTree:@anthropic-ai/claude-code: timing idealTree:#root Completed in 1234ms
```

Don't worry if you see warnings about optional dependencies or deprecated packages - these are common and usually harmless. What matters is that the installation completes without errors. The whole process typically takes 30 seconds to 2 minutes depending on your internet speed.

### 3.3 Understanding what just got installed

When the installation finishes, npm will show a summary of what it installed. You might see something indicating the installed version, like `+ @anthropic-ai/claude-code@1.0.38`. The plus sign means it was successfully added, and the number after the @ symbol is the version.

What actually happened behind the scenes? npm created a new directory in `~/.npm-global/lib/node_modules/@anthropic-ai/claude-code/` containing all the Claude Code files. It also created a symbolic link (like a shortcut) in `~/.npm-global/bin/` that points to the main Claude Code executable. This is why you can now type `claude` from anywhere and the system knows what to run.

### 3.4 Verifying the installation

Before we celebrate, let's make sure everything installed correctly. Type:

```bash
claude --version
```

This should immediately print the version number. If you see this, congratulations - Claude Code is installed! If instead you see `command not found`, don't panic. This usually means the PATH we configured earlier isn't working properly. Try running `source ~/.bashrc` again to reload your configuration, then try the version command again.

### 3.5 First run and authentication

Now for the exciting part - let's actually start Claude Code. Before running it, navigate to a directory where you have a coding project, or create a test directory:

```bash
mkdir ~/test-claude-project
cd ~/test-claude-project
```

The `mkdir` command creates a new directory, and `cd` changes into it. The `~` symbol is a shortcut for your Linux home directory. Now, simply type:

```bash
claude
```

The first time you run Claude Code, it needs to connect to Anthropic's servers to verify your access. You'll see a welcome message and then be presented with authentication options. This is where Claude Code differs from many command-line tools - it's not just a local program but a connection to Anthropic's AI services.

### 3.6 Understanding authentication options

Claude Code will present you with several authentication methods, and choosing the right one depends on how you want to use and pay for the service. Let me explain each option in detail.

The **Anthropic Console** option is for pay-as-you-go API access. This is ideal if you prefer to pay only for what you use. You'll need to create an account on console.anthropic.com, add a payment method, and generate an API key.

The **Claude Pro/Max subscription** option is for users who have a monthly subscription to Claude through claude.ai. This gives you a certain amount of usage across all Claude interfaces, including Claude Code. This is often the most convenient option for individuals who also use Claude for other tasks.

The **Enterprise options** (AWS Bedrock or Google Vertex AI) are for organizations that have enterprise agreements with these cloud providers. If your company uses these services, you might be instructed to use one of these authentication methods with credentials provided by your IT department.

### 3.7 Completing the authentication process

When you select an option (using arrow keys and Enter), Claude Code will open your default web browser. If you're in WSL and a browser doesn't open automatically, you'll see a URL that you can copy and paste into any browser. The URL will look something like `https://claude.ai/auth/code?...` with a long string of characters.

In the browser, you'll log into your chosen service. If you don't have an account yet, you can create one at this point. For Anthropic Console, you'll need to set up billing. For Claude Pro/Max, you'll need an active subscription. After logging in and authorizing Claude Code, you'll see an authentication token - a long string of random-looking characters.

Copy this entire token (Ctrl+C on Windows), return to your terminal, and paste it (right-click in most terminals, or Ctrl+Shift+V in Windows Terminal) when prompted. Press Enter, and Claude Code will verify the token and save it securely. You should see a success message confirming you're connected.

### 3.8 Troubleshooting authentication issues

If authentication fails, the most common causes are copying the token incorrectly (missing characters at the beginning or end), an expired token (they're only valid for a few minutes), or network connectivity issues. Claude Code will usually give you a helpful error message pointing to the specific problem. You can always restart the authentication process by running `claude` again or using the `/auth reset` command once inside Claude Code.

---

## 4. Configuration and verification

After successfully installing and authenticating Claude Code, you're like a pilot who's started the engine but hasn't taken off yet. This section will help you understand how to configure Claude Code for your specific needs and verify that everything is working properly. Think of this as your pre-flight checklist - making sure all systems are go before you start using Claude Code for real work.

### 4.1 Understanding Claude Code's configuration system

Claude Code uses a layered configuration system, similar to how Git handles configurations. This might seem complex at first, but it's actually quite elegant once you understand the reasoning. There are three levels of settings, each serving a different purpose and taking precedence in a specific order.

The global settings live in `~/.claude/settings.json` in your Linux home directory. These apply to all your projects and contain things like your preferred theme, default behaviors, and authentication tokens. To view this file, you can use the command `cat ~/.claude/settings.json` or open it in a text editor with `nano ~/.claude/settings.json`. Don't worry if the file doesn't exist yet - Claude Code creates it automatically when needed.

Project-specific settings go in `.claude/settings.json` within each project directory. These override global settings for that particular project. For example, you might want Claude Code to be more cautious with changes in your production project but more experimental in your personal projects. When Claude Code starts, it looks for this file in the current directory and applies any settings it finds.

Personal settings are stored in `.claude/settings.local.json` within project directories. This file is for your own preferences that you don't want to share with others if you're working on a team project.

### 4.2 Configuring permissions and boundaries

One of Claude Code's most important features is its permission system. An AI assistant needs explicit boundaries for what it can and cannot do on your computer. Let's explore how to set these up properly.

Start Claude Code in your test project by running `claude` and then type the `/permissions` command. This shows you what Claude Code is currently allowed to do. By default, it has fairly conservative permissions - it can read files, suggest changes, and help with code, but it needs your approval for anything that modifies files or runs commands.

To adjust permissions, use the `/permissions edit` command. This opens an interactive menu where you can toggle different capabilities. For example, you might see options like "Allow file creation", "Allow file modification", "Allow command execution", and "Allow git operations". Use arrow keys to navigate and Space to toggle each permission on or off.

Let me explain what each permission type means in practice. "Allow file creation" lets Claude Code create new files when you ask it to. Without this, it can only show you what the file should contain, and you have to create it manually. "Allow file modification" is similar but for existing files - with it enabled, Claude Code can directly make changes instead of just suggesting them.

"Allow command execution" is more powerful and should be used thoughtfully. With this enabled, Claude Code can run commands on your behalf. This is convenient but also means you're trusting Claude Code to run commands that could potentially affect your system. "Allow git operations" enables features like saving changes to version control - you can skip this if you're not using Git.

### 4.3 Setting up terminal compatibility

Claude Code uses various Unicode characters and ANSI color codes to create its interface. If you see strange characters or the display looks broken, you need to configure terminal compatibility. Type `/config` within Claude Code to access display settings.

The configuration menu lets you choose between different display modes. If you're using Windows Terminal (recommended), select "Modern Terminal" for the best experience with full colors and special characters. If you're using an older terminal or accessing WSL through SSH, you might need to select "Compatible Mode" which uses simpler ASCII characters.

You can also configure color themes here. Claude Code typically offers options like "Dark", "Light", "High Contrast", and "Solarized". Choose what's comfortable for your eyes - if you're not sure, start with "Dark" as it tends to be easier on the eyes during long coding sessions. The theme affects not just Claude Code's interface but also how it syntax-highlights code snippets.

### 4.4 Testing core functionality

Now let's verify that Claude Code is working properly with a series of tests. Think of this as a shakedown cruise - we'll test each major system to ensure it's functioning correctly. First, let's test basic interaction. Type:

```
explain what files are in this directory
```

Claude Code should respond by listing the files in your current directory (which might be empty if you're in the test directory we created) and explaining what it sees. This tests that Claude Code can read your file system properly through WSL.

Next, let's test file creation. Ask Claude Code:

```
create a simple text file with today's date
```

If you have file creation permissions enabled, Claude Code will create a new file for you. If permissions are disabled, it will show you the content but ask you to create the file manually. This tests the permission system and file creation capability.

### 4.5 Testing Windows file system integration

One unique aspect of using Claude Code on Windows through WSL is accessing your Windows files. Let's verify this works correctly. Navigate to your Windows Documents folder:

```bash
cd /mnt/c/Users/[YourWindowsUsername]/Documents
```

Replace `[YourWindowsUsername]` with your actual Windows username. Note that if your username has spaces, you need to escape them with backslashes or wrap the path in quotes, like `/mnt/c/Users/John\ Doe/Documents` or `"/mnt/c/Users/John Doe/Documents"`.

Once there, run Claude Code again and ask:

```
list all the files in this directory
```

Claude Code should successfully show your Windows Documents folder contents. This confirms that the WSL file system bridge is working properly. However, you might notice operations are slightly slower when working with Windows files compared to native Linux files - this is normal due to the file system translation layer.

### 4.6 Customizing Claude Code's behavior

Beyond permissions and display settings, Claude Code has various behavioral configurations you can adjust. Type `/settings` to see all available options. You can configure things like auto-save behavior and how detailed Claude Code's responses are. If you find Claude Code's explanations too long or too short, you can adjust this here.

### 4.7 Creating your first real interaction

With everything configured and verified, let's try something practical. Create a simple test folder:

```bash
mkdir ~/my-first-project
cd ~/my-first-project
claude
```

Now ask Claude Code to help you with something simple:

```
create a simple webpage that displays a welcome message
```

Watch as Claude Code creates the file and explains what it does. You can follow up with questions like "explain what each part does" or "make it look nicer" to see how Claude Code maintains context across the conversation.

### 4.8 Saving and backing up your configuration

Once you have Claude Code configured to your liking, it's wise to back up your settings. Copy your global configuration file to a safe location:

```bash
cp ~/.claude/settings.json ~/claude-backup-settings.json
```

This backup makes it easy to restore your settings if you need to reinstall or set up Claude Code on another machine.

---

## 5. Common troubleshooting issues

The most frequent installation error is **"Claude Code is not supported on Windows"**, which occurs when running npm from Windows CMD or PowerShell instead of WSL. Always ensure you're inside the WSL terminal (Ubuntu). If you encounter **"exec: node: not found"**, WSL is using the Windows Node.js installation instead of the Linux version - reinstall Node.js within WSL and verify that `which node` shows `/usr/bin/node`, not a `/mnt/c/...` path.

Permission errors (EPERM) happen when npm tries to install in system directories. Never use `sudo npm install -g` - instead, configure the user-writable npm prefix as described above. For authentication failures, reset with `/auth reset` and reconfigure with `/auth login`. Path issues can be resolved by ensuring `export PATH=~/.npm-global/bin:$PATH` is in your `~/.bashrc` file.

---

## 6. Performance and best practices

For optimal performance, work within the WSL file system (`/home/...`) rather than accessing Windows files through `/mnt/c/...` when possible. Claude Code may consume significant resources with large codebases, so use file-based workflows for extensive content rather than direct pasting. Start Claude from your project root directory, use descriptive prompts for complex tasks, and always review changes before approving them.

Security best practices include never committing API keys to version control, using GitHub Secrets for CI/CD integration, configuring appropriate file access permissions, and regularly reviewing access controls. The tool stores API keys in an encrypted keychain equivalent and provides fine-grained permission controls for enterprise environments.

---

## 7. Your first conversation with Claude Code

Now that Claude Code is installed and configured, you're ready to start using it. Here are some simple things you can try to get familiar with how it works.

### 7.1 Starting Claude Code

Open your WSL terminal, navigate to any folder, and type:

```bash
claude
```

You'll see Claude Code's welcome message and a prompt waiting for your input. Unlike traditional tools where you type commands, with Claude Code you simply describe what you want in plain English.

### 7.2 Things you can ask Claude Code

Here are some beginner-friendly requests to try:

**Ask questions:**
- "What files are in this folder?"
- "Explain what a .bashrc file does"
- "What's the difference between a file and a directory?"

**Get help with commands:**
- "How do I create a new folder?"
- "What command shows my current location?"
- "How do I copy a file?"

**Create simple files:**
- "Create a text file with a shopping list"
- "Make a simple HTML page that says hello"
- "Create a basic Python script that prints today's date"

### 7.3 Tips for effective communication

- **Be specific** - "Create a file called notes.txt" works better than "make a file"
- **Ask follow-up questions** - Claude Code remembers your conversation, so you can say "now add more to that file"
- **Ask for explanations** - If Claude Code suggests a command, ask "what does that command do?" before approving it
- **Start simple** - Begin with basic requests and gradually try more complex tasks

### 7.4 Ending your session

When you're done, type `exit` or `/quit` to leave Claude Code. Any files created remain in your folder.

---

## 8. Conclusion

While Claude Code requires the additional step of setting up WSL2 on Windows 11, the installation process is straightforward once you understand the Linux environment requirement. The tool provides powerful AI-assisted development capabilities that integrate seamlessly with your existing workflow, offering natural language commands for code editing, debugging, and project understanding. Following this guide ensures a smooth installation experience and helps avoid the common pitfalls Windows users encounter when setting up terminal-based development tools.
