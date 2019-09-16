# Reference Taxonomy Working Group Minutes

Meeting: Reference taxonomy meeting Location: Paphos Date: 16/09/2019

## Meeting overview
- RSIT @ FIRST debrief
- Roundtable of participants update 
- Actions from last meeting
- Pull changes
- New Version release

# Minutes:
## RSIT @ FIRST 
During the BoF we had some interesting discussions regarding taxonomy translation and formats.
For this reason the paragraph " Taxonomy translated in the local language" in the page " Dependencies and tool mapping" has been added https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/Dependencies%20and%20tool%20mapping.md.
 
## Roundtable of participants update 
Team using RSIT 3
Team transitioning 3
Team considering the transition 2

# Actions for last meeting overview

## Update of terms in 2nd column and description of Abusive Content #42
agreed in LUX: Child Sexual Exploitation (CSE) 

## multiple values management on the mailing list by 29/03
Multiple value weight 1- 10  
Weight and subweight
Solved since it is at the discretion of the team.
RSIT can give recommendation and good practices

### actions: proposal and examples on multiple values to be shared with the mailing list.

## add other/unknown:
- [x] Merge pull request #46 from sebix/other-unknown

## American vs. British English
follow European Commission's English Style Guide.

 
## Open topics for Cyprus (including action post LUX)
- [ ] Obsolete values - How do we deal with obsolete value
- [ ] Pivot mapping - examples
- [ ] review  "Remove malware-dga-domain as agreed in Vilnius meeting" #32 https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/pull/32 - discuss with CERT-BUND
- [x] review  chg: [machine-tag] version MUST be an unsigned integer  and  Spit versioning into to fields #52 
- [x] review Some descriptions #47
- [x] review other/other -> other/unclassified #55
- [x] review  Add system-compromise #59 - further work on the definition is needed
- [ ] add (data) leak under information content security #61 - further work on the definition is needed
- [ ] taxonomy usage - see actions below
- [ ] translated versions - further work to integrate field in the machine readable version

# actions:
- review  "Remove malware-dga-domain as agreed in Vilnius meeting" #32 - discuss with CERT-BUND
- (data) leak under information content security #61 - further work on the definition is needed
- system-compromise #59 - further work on the definition is needed

# Discussion in Cyprus

## incentive for adoptions and challenges that teams face during the transitions
For example add script to fetch last version of taxonomy and check the possiblitity to add custom fields to ease the adoptio

# action: contact RT-IR and OTRS to see if it is possible to add the taxonomy natively for the new teams 
# action: develop guidelines to help adding the RSIT in existing environments. 


## Changelog Version 1.2 (released 2019/09/15)

- changed everything (hopefully) from american english to british
- changed versioning mechanism to an integer (version field is now 1002)
- machinetag2human.py: formatting changes in the header
- "CSE" is the proper word
- other/other -> other/uncategorized.
- clarified some descriptions in the description fields

# Actions for next meeting:
 
- review  "Remove malware-dga-domain as agreed in Vilnius meeting" #32 - discuss with CERT-BUND
- (data) leak under information content security #61 - further work on the definition is needed
- system-compromise #59 - further work on the definition is needed
- contact RT-IR and OTRS to see if it is possible to add the taxonomy natively for the new teams 
- develop guidelines to help adding the RSIT in existing environments. 
- proposal and examples on multiple values to be shared with the mailing list  
- proposal on how to deal with obsolete value to be shared with the mailing list 



