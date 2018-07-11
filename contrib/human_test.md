
# REFERENCE TAXONOMY INCIDENT  Taxonomy (human readable version)


This is the Reference Security Incident Classification Taxonomy.

See the [machine readable version](machinev1) as well. It should have an identical contents to the human readable version.
Note that the 1st column is mandatory, the 2nd colum is an optional but desired field.

Version: 1
Generated from [machine readable version](machinev1) on 2018-07-11 15:31:57.626744


| CLASSIFICATION (1ST COLUMN)                                   | INCIDENT EXAMPLES (2ND COLUMN)        | Description / Examples |
|---------------------------------------------------------      |------------------------------------   |------------------------|
| abusive-content | spam | Or 'Unsolicited Bulk Email', this means that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having a functionally comparable content. |
| abusive-content | Harmful Speech | Discreditation or discrimination of somebody e.g. cyber stalking, racism and threats against one or more individuals). |
| abusive-content | Child/Sexual/Violence/... | Child Pornography, glorification of violence, ... |
| malicious-code | Virus |  |
| malicious-code | Worm |  |
| malicious-code | Trojan |  |
| malicious-code | Spyware |  |
| malicious-code | Dialer |  |
| malicious-code | Rootkit |  |
| malicious-code | Malware |  |
| malicious-code | Botnet drone |  |
| malicious-code | Ransomware |  |
| malicious-code | Malware configuration |  |
| malicious-code | C&C |  |
| information-gathering | Scanning | Attacks that send requests to a system to discover weak points. This includes also some kind of testing processes to gather information about hosts, services and accounts. Examples: fingerd, DNS querying, ICMP, SMTP (EXPN, RCPT, ...), port scanning. |
| information-gathering | Sniffing | Observing and recording of network traffic (wiretapping). |
| information-gathering | Social Engineering | Gathering information from a human being in a non-technical way (e.g. lies, tricks, bribes, or threats). |
| intrusion-attempts | Exploiting of known Vulnerabilities | An attempt to compromise a system or to disrupt any service by exploiting vunerabilities with a standardised identifier such as CVE name (e.g. buffer overflow, backdoor, cross site scripting, etc.) |
| intrusion-attempts | Login attempts | Multiple login attempts (Guessing / cracking of passwords, brute force). |
| intrusion-attempts | New attack signature | An attempt using an unknown exploit. |
| intrusions | Privileged Account Compromise |  |
| intrusions | Unprivileged Account Compromise |  |
| intrusions | Application Compromise |  |
| intrusions | Bot |  |
| intrusions | defacement |  |
| intrusions | compromised |  |
| intrusions | backdoor |  |
| availability | DoS | Denial of Service. |
| availability | DDoS | Distributed Denial of Service. |
| availability | Sabotage | Sabotage. |
| availability | Outage (no malice) | Outage (no malice). |
| information-content-security | Unauthorised access to information |  |
| information-content-security | Unauthorised modification of information |  |
| information-content-security | dropzone |  |
| fraud | Unauthorized use of resources | Using resources for unauthorized purposes including profit-making ventures (E.g. the use of e-mail to participate in illegal profit chain letters or pyramid schemes). |
| fraud | Copyright | Offering or Installing copies of unlicensed commercial software or other copyright protected materials (Warez). |
| fraud | Masquerade | Type of attacks in which one entity illegitimately assumes the identity of another in order to benefit from it. |
| fraud | Phishing | Masquerading as another entity in order to persuade the user to reveal a private credential. |
| vulnerable | Open for abuse |  |
| other | blacklist |  |
| other | unknown |  |
| other | other |  |
| test | Test |  |
