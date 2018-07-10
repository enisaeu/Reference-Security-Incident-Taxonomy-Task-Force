# Reference Security Incident Classification Taxonomy Task Force ToR
## Scope and overview of the Task Force
ENISA and the European Computer Security Incident Response Team (CSIRT) community have jointly set up a task force with the goal of reaching a consensus on a ‘Reference Security Incident Classification Taxonomy’.
Creating a taxonomy is a difficult task as for instance classifying security incidents is very complex due to overlapping categories and different facets of such incidents. Organisations defining taxonomies are typically driven by their own needs, and since different CSIRTs have distinct expectations, those teams often end up developing their own incident classifications for internal use. In fact, even the ‘Common Taxonomy for LE and CSIRTs’ is an adaptation of the CERT.PT taxonomy, which in turn is based on the eCSIRT.net mkVI taxonomy. Likewise, there have been many taxonomies that are in essence only modifications of other versions.
As the need for information exchange, incident reporting and use of automation in incident response increases, it is becoming evident that developing a set of standardised guidelines is crucial. This common ground would help incident handlers in dealing with technical incidents on a daily basis. Moreover, it could assist policy decision makers by offering a standardised reference for discussing and drafting relevant policies such as the EU cyber security strategy and ‘The Directive on security of network and information systems’ (NIS Directive).
## Aim and Objectives
As mentioned in the 51st TF-CSIRT meeting, “there is the need for a taxonomy list and name everyone could rely on and refer to”. As the need for information exchange, and incident reporting increases, not to mention an increase in the use of automation in incident response, it is becoming evident that there is need for some common ground. This common ground would assist incident handlers dealing with technical incidents on a daily basis to deal with the abovementioned needs. The aim of this task force is to enable the CSIRT community in reaching a consensus on a reference taxonomy. It should be noted that details such as identifying suitable sharing mechanisms are outside of the current scope. The objectives of the task force are the following:
* Develop Reference Document (Classifications, incident types or examples, and definition) using eCSIRT.net as a starting point. 
* Define and develop an Update and Versioning Mechanism
* Host reference document
* Organise regular physical meetings with the stakeholders
* In the 2nd phase broader working group with non-European teams (FIRST) to achieve global consensus on incident reference taxonomy
## Task Force Procedures
### Membership
The membership is open to all TF-CSIRT members and relevant CSIRTs/CERT  communities like CSIRTs Network and FIRST.
It is important that amongst the members of the task force there are members of CSIRT teams, the Common Taxonomy Governance Group (including representatives from ENISA and EC3), tool developers (MISP/IntelMQ/Hive…), and taxonomy owners (owner of eCSIRT.net). 

To become part of the TF, the requester should send an email to ENISA secretariat  CSIRT-Relations@enisa.europa.eu or sign up for a physical meeting during a TF-CSIRT event. In case of physical meeting, please notify in presence to the ENISA secretariat or via email the request for addition to the mailing list. 
A mailing list has been set up in order to facilitate communication between the task force members.
The members are invited to provide feedback on the mailing list and during the meetings.
### Changes and additional new fields
After discussion, the TF decided to implement as of Version 1 of the taxonomy the following principles:
 
* The first column should be considered as being fixed in nature – maximum one change/year.
* The second column is considered as being more adaptable – two to three times/year.
* There must be a clearly defined update process for both columns.
* This process should include the history and version number of the changes (CHANGELOG file, etc.).
* Every new version MUST have a new version number and this version number SHOULD be added as meta-data.
* Old versions MUST remain online.
 
For changes and the addition of new fields, the process is the following:
 
* Members propose change(s) and/or additional field(s) together with their motivation and use case(s) to the mailing list/GitHub at least 30 working days before the next meeting of the task force. 
* The TF will discuss the proposal(s) during the next physical meeting and vote.

Please note that:
* The first column is of the “MUST” (mandatory) type, the second column is of the “SHOULD” (recommended but not mandatory) type. 

### Voting mechanism
There are two voting procedures in place.
The TF can choose between: 
* A remote procedure: an online poll on https://ec.europa.eu/eusurvey/ will be opened and members will have time to cast their vote up until 5 days before the next physical meeting of the TF. Please note that there is one vote per organization.
* Proxy : A member may authorise another member to cast a proxy vote on their behalf , but this must be notified by verifiable digitally  signed  e-mail  in  advance  of  the  meeting,  and  no  member  may  vote  on  behalf of more than one other member.
* Remote participation: conf call facilities should be always ensure for those who cannot physically attend the meeting
### Update and Versioning Mechanism
A *working copy* of the taxonomy is hosted on GitHub. Changes can be proposed by means of a GitHub pull requests. This automatically provides built-in history and versioning.
Proposal:
* Taxonomy text **as a working copy** on GitHub
* Add the JSON in GitHub
* Use GitHub 's "pull request" feature to transparently document change requests. 
* Anyone can add or change text and he/she is allowed to propose these changes on GitHub via pull requests.
* During the following physical meeting, the TF discusses and agrees on the proposed changes  
* Once a major release/new version is approved, a copy is also uploaded also to the TF website.
* The working copy with the next changes will be on GitHub and again serve as edit mechanism.
### Meeting minute’s methodology
Minutes are sent to the mailing list within 5 working days from the end of the physical meeting / conference call. The members have 15 working days to provide feedback. After this, the secretariat has 10 working days to implement the comments and send the final version to the TF mailing list.
### Dependencies and tool mapping
A list of relevant tools that use the taxonomy is updated on GitHub.  Changes can be proposed by means of a GitHub pull requests. This automatically provides built in history and versioning. This allows keeping track of the tools that use the taxonomy and also automatically allows the tool to keep track of new versions of the taxonomy.
### Hosting 
It was agreed to have an intermediate solution for hosting for 2-3 years. The decision was TF-CSIRT website. The location is https://tf-csirt.org/groups/ .

