
# RSIT to ATT&CK

Generated from machine readable version. Please **DO NOT** edit this file directly in github, rather use the machinetag.json file.

| Classification | Incident examples | ATT&CK Tactic / Technique     | Description        |
|----------------|-------------------| ------------------------------|--------------------|
| Abusive Content | Spam | [T1566 - Phishing](https://attack.mitre.org/techniques/T1566/)<br><br> | Or 'Unsolicited Bulk Email', this means that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having a functionally comparable content. This IOC refers to resources, which make up a SPAM infrastructure, be it a harvesters like address verification, URLs in spam e-mails etc. |
| Abusive Content | Harmful Speech |  | Discretization or discrimination of somebody, e.g. cyber stalking, racism or threats against one or more individuals. |
| Abusive Content | (Child) Sexual Exploitation/Sexual/Violent Content | [T1566 - Phishing](https://attack.mitre.org/techniques/T1566/)<br><br> | Child Sexual Exploitation (CSE), Sexual content, glorification of violence, etc. |
| Malicious Code | Infected System |  | System infected with malware, e.g. PC, smartphone or server infected with a rootkit. Most often this refers to a connection to a sinkholed C2 server |
| Malicious Code | C2 Server | [T1041 - Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/)<br><br> | Command-and-control server contacted by malware on infected systems. |
| Malicious Code | Malware Distribution |  | URI used for malware distribution, e.g. a download URL included in fake invoice malware spam or exploit-kits (on websites). |
| Malicious Code | Malware Configuration |  | URI hosting a malware configuration file, e.g. web-injects for a banking trojan. |
| Information Gathering | Scanning | [T1046 -  Network Service Scanning](https://attack.mitre.org/techniques/T1046/)<br><br>[T1595 - Active Scanning](https://attack.mitre.org/techniques/T1595/)<br><br>[T1595/002 - Active Scanning: Vulnerability Scanning](https://attack.mitre.org/techniques/T1595/002/)<br><br> | Attacks that send requests to a system to discover weaknesses. This also includes testing processes to gather information on hosts, services and accounts. Examples: fingerd, DNS querying, ICMP, SMTP (EXPN, RCPT, ...), port scanning. |
| Information Gathering | Sniffing | [T1040 -  Network Sniffing](https://attack.mitre.org/techniques/T1040/)<br><br>[T1557 - Man-in-the-Middle](https://attack.mitre.org/techniques/T1557/)<br><br> | Observing and recording of network traffic (wiretapping). |
| Information Gathering | Social Engineering |  | Gathering information from a human being in a non-technical way (e.g. lies, tricks, bribes, or threats). |
| Intrusion Attempts | Exploitation of known Vulnerabilities | [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)<br><br>[T1203 - Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/)<br><br>[T1211 - Exploitation for Defense Evasion](https://attack.mitre.org/techniques/T1211/)<br><br>[T1210 -  Exploitation of Remote Services](https://attack.mitre.org/techniques/T1210/)<br><br> | An attempt to compromise a system or to disrupt any service by exploiting vulnerabilities with a standardised identifier such as CVE name (e.g. buffer overflow, backdoor, cross site scripting, etc.) |
| Intrusion Attempts | Login attempts | [T1110 -  Brute Force](https://attack.mitre.org/techniques/T1110/)<br><br>[T1110/001 - Password Guessing](https://attack.mitre.org/techniques/T1110/001/)<br><br>[T1110/002 - Password Cracking](https://attack.mitre.org/techniques/T1110/002/)<br><br>[T1110/003 - Password Spraying](https://attack.mitre.org/techniques/T1110/003/)<br><br>[T1110/004 - Credential Stuffing](https://attack.mitre.org/techniques/T1110/004/)<br><br> | Multiple login attempts (Guessing / cracking of passwords, brute force). This IOC refers to a resource, which has been observed to perform brute-force attacks over a given application protocol. |
| Intrusion Attempts | New attack signature |  | An attack using an unknown exploit. |
| Intrusions | Privileged Account Compromise | [T1078 - Valid Accounts](https://attack.mitre.org/techniques/T1078/)<br><br> | Compromise of a system where the attacker gained administrative privileges. |
| Intrusions | Unprivileged Account Compromise | [T1078 - Valid Accounts](https://attack.mitre.org/techniques/T1078/)<br><br> | Compromise of a system using an unprivileged (user/service) account. |
| Intrusions | Application Compromise | [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)<br><br> | Compromise of an application by exploiting (un-)known software vulnerabilities, e.g. SQL injection. |
| Intrusions | System Compromise |  | Compromise of a system, e.g. unauthorised logins or commands. This includes compromising attempts on honeypot systems. |
| Intrusions | Burglary |  | Physical intrusion, e.g. into corporate building or data-centre. |
| Availability | Denial of Service | [T1498 -  Network Denial of Service](https://attack.mitre.org/techniques/T1498/)<br><br> | Denial of Service attack, e.g. sending specially crafted requests to a web application which causes the application to crash or slow down. |
| Availability | Distributed Denial of Service | [T1498 -  Network Denial of Service](https://attack.mitre.org/techniques/T1498/)<br><br> | Distributed Denial of Service attack, e.g. SYN-Flood or UDP-based reflection/amplification attacks. |
| Availability | Misconfiguration |  | Software misconfiguration resulting in service availability issues, e.g. DNS server with outdated DNSSEC Root Zone KSK. |
| Availability | Sabotage |  | Physical sabotage, e.g cutting wires or malicious arson. |
| Availability | Outage |  | Outage caused e.g. by air condition failure or natural disaster. |
| Information Content Security | Unauthorised access to information |  | Unauthorised access to information, e.g. by abusing stolen login credentials for a system or application, intercepting traffic or gaining access to physical documents. |
| Information Content Security | Unauthorised modification of information | [T1565 - Data Manipulation](https://attack.mitre.org/techniques/T1565/)<br><br> | Unauthorised modification of information, e.g. by an attacker abusing stolen login credentials for a system or application or a ransomware encrypting data. Also includes defacements. |
| Information Content Security | Data Loss |  | Loss of data, e.g. caused by harddisk failure or physical theft. |
| Information Content Security | Leak of confidential information |  | Leaked confidential information like credentials or personal data. |
| Fraud | Unauthorised use of resources |  | Using resources for unauthorised purposes including profit-making ventures, e.g. the use of e-mail to participate in illegal profit chain letters or pyramid schemes. |
| Fraud | Copyright |  | Offering or Installing copies of unlicensed commercial software or other copyright protected materials (Warez). |
| Fraud | Masquerade |  | Type of attack in which one entity illegitimately impersonates the identity of another in order to benefit from it. |
| Fraud | Phishing | [T1566 - Phishing](https://attack.mitre.org/techniques/T1566/)<br><br> | Masquerading as another entity in order to persuade the user to reveal private credentials. This IOC most often refers to a URL, which is used to phish user credentials. |
| Vulnerable | Weak crypto |  | Publicly accessible services offering weak crypto, e.g. web servers susceptible to POODLE/FREAK attacks. |
| Vulnerable | DDoS amplifier | [T1498 -  Network Denial of Service](https://attack.mitre.org/techniques/T1498/)<br><br> | Publicly accessible services that can be abused for conducting DDoS reflection/amplification attacks, e.g. DNS open-resolvers or NTP servers with monlist enabled. |
| Vulnerable | Potentially unwanted accessible services |  | Potentially unwanted publicly accessible services, e.g. Telnet, RDP or VNC. |
| Vulnerable | Information disclosure |  | Publicly accessible services potentially disclosing sensitive information, e.g. SNMP or Redis. |
| Vulnerable | Vulnerable system |  | A system which is vulnerable to certain attacks. Example: misconfigured client proxy settings (example: WPAD), outdated operating system version, XSS vulnerabilities, etc. |
| Other | Uncategorised |  | All incidents which don't fit in one of the given categories should be put into this class or the incident is not categorised. |
| Other | Undetermined |  | The categorisation of the incident is unknown/undetermined. |
| Test | Test |  | Meant for testing. |
