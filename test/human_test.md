
# REFERENCE TAXONOMY INCIDENT  Taxonomy (human readable version)


This is the Reference Security Incident Classification Taxonomy.

See the [machine readable version](machinev1) as well. It should have an identical contents to the human readable version.
Note that the 1st column is mandatory, the 2nd colum is an optional but desired field.

Version: 1
Generated from [machine readable version](machinev1)


| CLASSIFICATION (1ST COLUMN)                                   | INCIDENT EXAMPLES (2ND COLUMN)        | Description / Examples |
|---------------------------------------------------------      |------------------------------------   |------------------------|
| abusive-content | spam | Or 'Unsolicited Bulk Email', this means that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having a functionally comparable content. |
| abusive-content | Harmful Speech | Discreditation or discrimination of somebody e.g. cyber stalking, racism and threats against one or more individuals). |
| abusive-content | Child/Sexual/Violence/... | Child Pornography, glorification of violence, ... |
| malicious-code | Virus | Software that is intentionally included or inserted in a system for a harmful purpose. A user interaction is normally necessary to activate the code. |
| malicious-code | Worm | see 'virus' |
| malicious-code | Trojan | see 'virus' |
| malicious-code | Spyware | see 'virus' |
| malicious-code | Dialer | see 'virus' |
| malicious-code | Rootkit | see 'virus' |
| malicious-code | Malware | see 'virus' |
| malicious-code | Botnet drone | see 'virus' |
| malicious-code | Ransomware | see 'virus' |
| malicious-code | Malware configuration | see 'virus' |
| malicious-code | C&C | see 'virus' |
| information-gathering | Scanning | Attacks that send requests to a system to discover weak points. This includes also some kind of testing processes to gather information about hosts, services and accounts. Examples: fingerd, DNS querying, ICMP, SMTP (EXPN, RCPT, ...), port scanning. |
| information-gathering | Sniffing | Observing and recording of network traffic (wiretapping). |
| information-gathering | Social Engineering | Gathering information from a human being in a non-technical way (e.g. lies, tricks, bribes, or threats). |
| intrusion-attempts | Exploiting of known Vulnerabilities | An attempt to compromise a system or to disrupt any service by exploiting vunerabilities with a standardised identifier such as CVE name (e.g. buffer overflow, backdoor, cross site scripting, etc.) |
| intrusion-attempts | Login attempts | Multiple login attempts (Guessing / cracking of passwords, brute force). |
| intrusion-attempts | New attack signature | An attempt using an unknown exploit. |
| intrusions | Privileged Account Compromise | A successful compromise of a system or application (service). This can have been caused remotely by a known or new vulnerability, but also by an unauthorized local access. Also includes being part of a botnet. |
| intrusions | Unprivileged Account Compromise | see 'Privileged Account Compromise' |
| intrusions | Application Compromise | see 'Privileged Account Compromise' |
| intrusions | Bot | see 'Privileged Account Compromise' |
| intrusions | defacement | see 'Privileged Account Compromise' |
| intrusions | compromised | see 'Privileged Account Compromise' |
| intrusions | backdoor | see 'Privileged Account Compromise' |
| availability | DoS | Denial of Service. |
| availability | DDoS | Distributed Denial of Service. |
| availability | Sabotage | Sabotage. |
| availability | Outage (no malice) | Outage (no malice). |
| information-content-security | Unauthorised access to information | Besides local abuse of data and systems, the security of information can be endangered by successful compromise of an account or application. In addition, attacks that intercept and access information during transmission (wiretapping, spoofing or hijacking) are possible.  Human/configuration/software error can also be the cause. |
| information-content-security | Unauthorised modification of information | see 'Unauthorised access to information' |
| information-content-security | dropzone | see 'Unauthorised access to information' |
| fraud | Unauthorized use of resources | Using resources for unauthorized purposes including profit-making ventures (E.g. the use of e-mail to participate in illegal profit chain letters or pyramid schemes). |
| fraud | Copyright | Offering or Installing copies of unlicensed commercial software or other copyright protected materials (Warez). |
| fraud | Masquerade | Type of attacks in which one entity illegitimately assumes the identity of another in order to benefit from it. |
| fraud | Phishing | Masquerading as another entity in order to persuade the user to reveal a private credential. |
| vulnerable | Open for abuse | Open resolvers, world readable printers, vulnerability apparent from Nessus etc scans, virus, signatures not up to date, etc. |
| other | other | All incidents which don't fit in one of the given categories should be put into this class. |
| test | Test | Meant for testing. |
