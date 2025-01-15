# Cybersecurity Beginner's Roadmap 🌐

Embark on your cybersecurity journey with this step-by-step guide, designed to take you from a novice to a skilled practitioner. 

---

## 1. **Open-Source Intelligence (OSINT)** 🕵️‍♂️
**OSINT** is the foundation of cybersecurity. It involves gathering publicly available information to better understand your target.

### Tools and Techniques:
- **Shodan:** IoT and internet-facing devices search engine.
- **Maltego:** Data visualization and relationship mapping.
- **Google Dorks:** Advanced Google search operators to uncover sensitive information.

### Practical Example:
Run a simple nmap scan to gather basic information:
```bash
nmap -sS -sV [Target-IP]
```

**Tip:** Start practicing on ethical platforms like [TryHackMe](https://tryhackme.com) or [Hack The Box](https://www.hackthebox.com).

---

## 2. **Scanning** 🔍
Identify open ports, services, and vulnerabilities in your target systems.

### Techniques:
- **Port Scanning:** Using tools like `nmap` to discover open ports and services.
- **Service Enumeration:** Determine what services are running (e.g., FTP, SSH).
- **Vulnerability Scanning:** Use tools like `Nessus` or `OpenVAS` to find weaknesses.

### Example Command:
```bash
nmap -A -T4 [Target-IP]
```
This performs aggressive scanning, including OS detection, version detection, and traceroute.

---

## 3. **Gaining Access** 🚪
Exploit vulnerabilities to gain unauthorized access to systems. This phase requires ethical intent and permission.

### Techniques:
- **Exploitation:** Utilize tools like `Metasploit` to exploit vulnerabilities.
- **Reverse Shells:** Send a shell back to the attacker’s machine for control.
- **Zero Days:** Exploit unpatched vulnerabilities (rare but critical).

### Example:
Use Metasploit to exploit a known vulnerability:
```bash
msfconsole
use exploit/multi/http/struts2_content_type_ognl
set RHOST [Target-IP]
exploit
```

---

## 4. **Stabilizing Access** 🛠️
Once access is gained, stabilize and maintain your connection for further actions.

### Tools and Techniques:
- **Meterpreter:** Advanced payload for interacting with compromised machines.
- **Backdoors:** Persist access even if the system reboots.
- **Reverse Shell Stabilization:** Use Python or other tools to make your shell interactive.

### Example:
Spawn a stable TTY shell:
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

## 5. **Clearing Tracks** 🧹
Remove evidence of your activity to avoid detection.

### Techniques:
- **Log Deletion:** Clear logs in `/var/log` or event viewer (Windows).
- **File Cleanup:** Remove uploaded scripts, exploits, or payloads.
- **Command History:** Clear history on Linux:
```bash
history -c && history -w
```

**Note:** Ethical hackers should document activities for reporting rather than clearing tracks.

---

## Practice Platforms 🖥️
Start your journey with practical labs:
- [TryHackMe](https://tryhackme.com)
- [Hack The Box](https://hackthebox.com)
- [VulnHub](https://vulnhub.com)

---

### Final Notes:
- Always operate within the law. Obtain explicit permission before testing systems.
- Stay updated with the latest vulnerabilities and security trends.
- Join communities and forums to learn from experienced professionals.

---

Start small, keep learning, and stay ethical. 🚀
