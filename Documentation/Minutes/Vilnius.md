 # Reference Taxonomy Working Group Minutes 
Meeting:	Reference taxonomy meeting 
Location:	Vilnius
Date:	26/09/2018

## Meeting overview
- Actions from last meeting
- Actions for this meeting
- Other pending actions
- Review pulled changes
- MISP occurrences
- Licensing for the upcoming versions of the taxonomy
- Naming convention

# Review of the actions:
## Completed actions from last meeting
ENISA
- [x] organize the meeting in Vilnius 
- [x] to set up the remote conf call option for upcoming meetings.
- [x] to consolidate final version of ToR and Use cases 

ENISA and CERT.AT 
- [x] to set up GitHub account
- [x] to start draft user guide/ usage description

CIRCL to provide 
- [x] the frequency of values from MISP 
- [x] the JSON and scheme

TF to start 
- [ ] Review of actions from previous meeting
- [ ] Review pulled changes
- [ ] Discuss MISP occurrences
- [ ] Discuss licensing for the upcoming versions of the taxonomy
- [ ] Define Next steps

## Other pending actions

ENISA to 
- [ ] open the survey on and name of the taxonomy- see last slide

All, no more surveys. The names is decided: Reference Security Incident Taxonomy RSIT

ENISA: More below regarding the difference between TF and WG.

- [ ] to start work on definitions with CESNET-CERTS and CERT-RO – redefine action

ENISA: CERT-RO had some lineup changes and we are already discussing definition in the pull requests so we can discuss how to go further in the ML.

Various: we need to create a list of taxonomy users on the GitHub

- [ ] Minutes – should be store them on the GitHub now that we have one?

Cert.at: we want to check if our comments were integrated. 

# Actions

ENISA : 
- [ ] create a list of taxonomy users on the GitHub
- [ ] we will send cert.at the minutes for Warsaw. The upcoming minutes will be published on the GitHub.

# Review pulled changes 
## General comments:

SWITCH-CERT: how we can build and show C&C

CERT.at: C2 for cert.at goes under malicious code

NRD CS: for us goes under intrusion

ENISA:  if you look at the MISP occurrences, Ransomware and Malware are the most used values:  

## MISP occurences

malicious-code	Virus	Ransomware 129

Malware 43

Worm 1 

Trojan 1

Spyware 1

information-gathering	Scanning	Scanning 1 

intrusion-attempts	Exploiting of known Vulnerabilities	New attack signature 4

intrusions	Privileged Account Compromise	Compromised 5 2 attributes 

Backdoor 4

Defacement 3

availability	DoS	DDoS 7

fraud	Unauthorized use of resources	Phishing 19

Masquerade 1 

Unauthorized use of resources 1

other	other	Other 1

Other Unknown 1

## Restructure malicious code #8

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/8/files 

GOVERCERTLU:  DGA gets complicated. LEA reads differently. 

CESNET: we have a top level category and I think fits better “anomaly”

CERT.at  it is difficult to discuss changes to a group of attributes, please pull changes line by line 

WG ask for clarification on GitHub

CERT-Bund answers on GitHub – see thread there.

ALL: Everything was approved except Malware DGA Domain.

### Actions

- [ ] CERT-Bund has to pull request deletion for Malware DGA Domain so we can delete from the current version.
- [ ] CERT-Bund has to create a new pull request for Malware DGA Domain so that WG can discuss it before Tallinn meeting.  
- [ ] ALL pull changes by individual line

## Use expanded predicates in human format output #12

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/12/commits/    
- [X] Approved – see thread there.

## Some textual revisions. No change of content. #13

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/13/commits/ 
- [X] Approved – see thread there.

## Changes to availability #14

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/14/commits/
- [X] Approved – see thread there.

## Changes to intrusions #15

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/15/commits/
- [X] Approved – see thread there.

## Changes to information-content-security #16

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/16/commits/
- [X] Approved– see thread there.

## Changes vulnerable #17

See thread at https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/17/commits/
- [X] Approved– see thread there.

### Actions
- [ ] WG to discuss proposed  “Availability/Misconfiguration”  https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/24    in Tallinn
- [ ] WG To finalize the DGA domain in Tallinn
- [ ] WG to pull new changes before Tallinn

# MISP taxonomies

ENISA This was covered at the beginning of pull changes.

# Licensing for the upcoming versions of the taxonomy

ENISA on the mailing list we raised the point of the licensing of the new version.

CIRCL For all the MISP taxonomies, we use CC0 1.0 Universal

CERT.at we can use CC0 and ask Don Stikvoort if it is ok for them

ALL agree 

## Actions
- [ ] ENISA to discuss proposed CC solutions to Don Stikvoort
- [ ] WG to acknowledge eCSIRT.net, Jimmy Arvidsson and Don Stikvoort on the Github https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/26 
- [ ] WG to use agreed license for next version  based on the changes approved in Vilnius minus DGA domain

# Naming convention

ENISA: TF-CSIRTs reported to us that “….because TF-CSIRT is a GÉANT task force (Task Force - Computer Security Incident Response Teams) so we cannot form task forces within a task force. For that reason, we support Working Groups that is what we called them in the past.  “

ENISA: for this reason we suggest to change the name in 

Reference Security Incident Taxonomy Working Group – RSIT WG 

All, agreed

# Note after the meeting:
“TF-CSIRT Steering Committee met on 26 September and discussed the Reference Security Incident Taxonomy Working Group. Reference Security Incident Taxonomy Working Group was approved as TF-CSIRT working group by the SC.”

# Next steps
ENISA to 
- [ ] Prepare minutes
- [ ] Prepare for Tallinn meeting
- [ ] Change name from TF to WG
- [ ] Create a list of taxonomy users on the GitHub
- [ ] Coordinate CC discussion and discuss proposed CC solutions to Don Stikvoort
- [ ] Update GitHub

CERT-Bund to
- [ ] Pull request deletion for Malware DGA Domain so we can delete from the current version ASAP.
- [ ] Create a new pull request for Malware DGA Domain so that WG can discuss it before Tallinn meeting.  

ALL WG to
- [ ] Discuss proposed  “Availability/Misconfiguration”  https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/24     in Tallinn
- [ ] Finalize the DGA domain in Tallinn
- [ ] Acknowledge eCSIRT.net, Jimmy Arvidsson and Don Stikvoort on the Github https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/26 
- [ ] use agreed license for next version  based on the changes approved in Vilnius minus DGA domain
- [ ] Pull changes by individual line
- [ ] Prepare accordingly for Tallinn meeting
