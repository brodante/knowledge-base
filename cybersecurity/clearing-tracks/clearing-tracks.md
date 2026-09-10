---
layout: default
title: Clearing Tracks
permalink: /cybersecurity/clearing-tracks/
---

# Clearing Tracks 🧹

The fifth and final phase of the penetration testing methodology: removing evidence of your activity from the target system while maintaining access.

## What This Phase Is About

After gaining and stabilizing access, you must **erase logs, artifacts, and forensic evidence** so the engagement goes undetected — and so the client can't be blamed for incidents you caused during testing.

> ⚠️ **Ethics first:** Log clearing is only legitimate during **authorized penetration tests** with explicit rules of engagement. Defensive teams use anti-forensics knowledge to build better detection, and red teamers rely on it for realistic stealth simulations. Doing this on systems you don't own is a crime.

## 1. Log Deletion

### Linux
```bash
# Wipe specific log files
echo "" > /var/log/auth.log
echo "" > /var/log/syslog
shred -u /var/log/auth.log   # overwrite + delete

# Clear bash history
history -c
rm ~/.bash_history
unset HISTFILE
```

### Windows — Event Logs
```powershell
# Clear event logs (requires admin)
wevtutil cl Security
wevtutil cl System
wevtutil cl Application

# Or via the Event Viewer GUI
# Windows Logs → right-click each log → Clear Log
```

## 2. Covering Command History

```bash
# Never write to history at all
export HISTSIZE=0
export HISTFILESIZE=0

# Run commands without logging
<space>command        # prefix with space if HISTCONTROL=ignorespace
```

## 3. Removing Uploaded Files & Tools

- Delete tools/scripts you uploaded: `rm /tmp/exploit.py`
- Remove persistence artifacts you created (SSH keys, cron jobs, services, registry keys)
- **Important:** keep your own report documenting *everything* you did — a good pentest **never** fully erases evidence of engagement, it just prevents *casual* detection.

## 4. Anti-Forensics & OPSEC

- **Timestamp manipulation** — `touch -t YYYYMMDDhhmm file` to backdate files
- **Memory-only implants** — tools like Meterpreter run in RAM, leaving minimal disk artifacts
- **Encrypted C2 traffic** — hide command-and-control traffic in TLS/HTTPS
- **Living off the land** — use built-in OS tools (PowerShell, wget, python) so you don't drop binaries

## Detection Defenders Should Use

The better you are at erasing tracks, the more defenders should practice:

- **Centralized logging** — ship logs to a remote SIEM (Splunk, ELK) the attacker can't touch
- **File integrity monitoring** — Tripwire, Auditd, Wazuh
- **Endpoint detection** — EDR tools flaging `wevtutil cl`, `shred`, and history clearing
- **Command-line auditing** — PowerShell Script Block Logging

## Practice Legally ✅

- **[TryHackMe](https://tryhackme.com/)** — Log analysis & detection rooms
- **[Wazuh](https://wazuh.com/)** — free open-source SIEM for learning detection
- **[GTFOBins](https://gtfobins.github.io/)** — bypassing restrictions with standard binaries

## The Complete Roadmap

You've now covered the full offensive lifecycle:

1. [OSINT](../osint/) — information gathering
2. [Scanning](../scanning/) — discovering targets
3. [Gaining Access](../gaining-access/) — exploitation
4. [Stabilizing Access](../stabilizing-access/) — persistence
5. **Clearing Tracks** — you are here 🙂

[← Back to Cybersecurity Hub](../)

<!-- 愛をこめて ダンテが作りました -->
