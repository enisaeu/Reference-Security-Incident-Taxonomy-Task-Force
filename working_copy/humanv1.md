
# REFERENCE TAXONOMY INCIDENT  Taxonomy (human readable version)


This is the Reference Security Incident Classification Taxonomy.

See the [machine readable version](machinev1) as well. It should have an identical contents to the human readable version.
Note that the 1st column is mandatory, the 2nd colum is an optional but desired field.

Version: 1002

Generated from [machine readable version](machinev1). Please **DO NOT** edit this file directly in github, rather use the machinev1 file.


| CLASSIFICATION (1ST COLUMN)                                   | INCIDENT EXAMPLES (2ND COLUMN)        | Description / Examples |
|---------------------------------------------------------      |------------------------------------   |------------------------|
| Abusive Content | Spam | Or 'Unsolicited Bulk Email', this means that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having a functionally comparable content. This IOC refers to resources which make up spam infrastructure, for example, harvesters like address verification, URLs in spam emails, etc. |
| Abusive Content | Harmful Speech | Bullying, harassment or discrimination of somebody, e.g., cyber stalking, racism or threats against one or more individuals. |
| Abusive Content | (Child) Sexual Exploitation/Sexual/Violent Content | Child Sexual Exploitation (CSE), sexual content, glorification of violence, etc. |
| Malicious Code | Infected System | System infected with malware, e.g., a PC, smartphone or server infected with a rootkit. Most often this refers to a connection to a sinkholed command and control server. |
| Malicious Code | C2 Server | Command and control server contacted by malware on infected systems. |
| Malicious Code | Malware Distribution | URI used for malware distribution, e.g., a download URL included in fake invoice malware spam or exploit kits (on websites). |
| Malicious Code | Malware Configuration | URI hosting a malware configuration file, e.g., web injects for a banking trojan. |
| Information Gathering | Scanning | Attacks that send requests to a system to discover weaknesses. This also includes testing processes to gather information on hosts, services and accounts. This includes fingerd, DNS querying, ICMP, SMTP (EXPN, RCPT, etc) port scanning. |
| Information Gathering | Sniffing | Observing and recording of network traffic (i.e. wiretapping). |
| Information Gathering | Social Engineering | Gathering information from a human being in a non-technical way (e.g., using lies, tricks, bribes, or threats). |
| Intrusion Attempts | Exploitation of Known Vulnerabilities | An attempt to compromise a system or to disrupt any service by exploiting vulnerabilities with a standardised identifier such as CVE name (e.g., using a buffer overflow, backdoor, cross site scripting) |
| Intrusion Attempts | Login Attempts | Multiple brute-force login attempts (including guessing or cracking of passwords). This IOC refers to a resource, which has been observed to perform brute-force attacks over a given application protocol. |
| Intrusion Attempts | New Attack Signature | An attack using an unknown exploit. |
| Intrusions | Privileged Account Compromise | Compromise of a system where the attacker has gained administrative privileges. |
| Intrusions | Unprivileged Account Compromise | Compromise of a system using an unprivileged (user/service) account. |
| Intrusions | Application Compromise | Compromise of an application by exploiting (un)known software vulnerabilities, e.g., SQL injection. |
| Intrusions | System Compromise | Compromise of a system, e.g., unauthorised logins or commands. This includes attempts to compromise honeypot systems. |
| Intrusions | Burglary | Physical intrusion, e.g., into a corporate building or data centre. |
| Availability | Denial of Service | Denial of Service attack, e.g., sending specially crafted requests to a web application which causes the application to crash or slow down. |
| Availability | Distributed Denial of Service | Distributed Denial of Service attack, e.g., SYN flood or UDP-based reflection/amplification attacks. |
| Availability | Misconfiguration | Software misconfiguration resulting in service availability issues, e.g., DNS server with outdated DNSSEC Root Zone KSK. |
| Availability | Sabotage | Physical sabotage, e.g., cutting wires or malicious arson. |
| Availability | Outage | An outage caused, for example, by air conditioning failure or natural disaster. |
| Information Content Security | Unauthorised Access to Information | Unauthorised access to information, e.g., by abusing stolen login credentials for a system or application, intercepting traffic or gaining access to physical documents. |
| Information Content Security | Unauthorised Modification of Information | Unauthorised modification of information, e.g., by an attacker abusing stolen login credentials for a system or application, or ransomware encrypting data. Also includes defacements. |
| Information Content Security | Data Loss | Loss of data caused by, for example, hard disk failure or physical theft. |
| Information Content Security | Leak of Confidential Information | Leaked confidential information, e.g., credentials or personal data. |
| Fraud | Unauthorised Use of Resources | Using resources for unauthorised purposes including profit-making ventures, e.g., the use of email to participate in illegal profit chain letters or pyramid schemes. |
| Fraud | Copyright | Offering or installing copies of unlicensed commercial software or other copyright protected materials (also known as Warez). |
| Fraud | Masquerade | Type of attack in which one entity illegitimately impersonates the identity of another in order to benefit from it. |
| Fraud | Phishing | Masquerading as another entity in order to persuade the user to reveal private credentials. This IOC most often refers to a URL, which is used to phish user credentials. |
| Vulnerable | Weak Cryptography | Publicly accessible services offering weak cryptography, e.g., web servers susceptible to POODLE/FREAK attacks. |
| Vulnerable | DDoS Amplifier | Publicly accessible services that can be abused for conducting DDoS reflection/amplification attacks, e.g., DNS open-resolvers or NTP servers with monlist enabled. |
| Vulnerable | Potentially Unwanted Accessible Services | Potentially unwanted publicly accessible services, e.g., Telnet, RDP or VNC. |
| Vulnerable | Information disclosure | Publicly accessible services potentially disclosing sensitive information, e.g., SNMP or Redis. |
| Vulnerable | Vulnerable System | A system which is vulnerable to certain attacks, e.g., misconfigured client proxy settings (such as WPAD), outdated operating system version, cross-site scripting vulnerabilities or weak access control (missing password complexity and length controls, missing or poor authentication factors, presence of default account names/passwords, no Segregation of Duties, etc.). |
| Other | Uncategorised | All incidents which don't fit in one of the given categories should be put into this class or the incident is not categorised. |
| Other | Undetermined | The categorisation of the incident is unknown/undetermined. |
| Test | Test | Meant for testing. |
