# Changelog

## Version 1.3 (released 2021-05-26)

### Taxonomy

#### New entries
- Added *System Compromise* in the taxonomy *Intrusions*.
- Added *Leak of confidential information* in taxonomy *Information Content Security*.

#### Changed entries
- All expanded values are now in *CamelCase*:
  - *Exploitation of known Vulnerabilities* -> *Exploitation of Known Vulnerabilities*
  - *Login attempts* -> *Login Attempts*
  - *New attack signature* -> *New Attack Signature*
  - *Unauthorised access to information* -> *Unauthorised Access to Information*
  - *Unauthorised modification of information* -> *Unauthorised Modification of Information*
  - *Unauthorised use of resources* -> *Unauthorised Use of Resources*
  - *DDoS amplifier* -> *DDoS Amplifier*
  - *Potentially unwanted accessible services* -> *Potentially Unwanted Accessible Services*
  - *Vulnerable system* -> *Vulnerable System*
- Changed for better clarity:
  - *Weak crypto* -> *Weak Cryptography*

#### Minor changes
- Enhanced various descriptions, for example:
  - *Harmful Speech*: Replaced *Discretization* by *Bullying, harassment*
  - *Malware Distribution*: Also covers exploit-kits on websites
  - *Unauthorised modification of information*: Also covers defacements.
  - *Vulnerable system*: Also covers XSS vulnerabilities.

### RSIT 2 ATT&CK

Added documentation on the relation between RSIT and the ATT&CK framework,
as well as scripts to convert and usage documentation.

### Documentation

- Merged Acknowledgments and Contributing into the README.
- Spelling fixes over the full repository
- renamed all meeting minutes to the format `{date}-{location}`.
- new usage document covering covering what to classify and multiple classifications
- new document on how to get started
- Major rewording and extension of the README.
- Dependencies and tool mapping: updated Taxonomy users


## Version 1.2  (released 2019/09/15)

  * changed everything (hopefully) from American English to British English
  * changed versioning mechanism to an integer (version field is now 1002)
  * machinetag2human.py: formatting changes in the header
  * "CSE" is the proper word
  * other/other -> other/uncategorized.
  * clarified some descriptions in the description fields


## Version 1.1

  * CSE
  * other -> split to other/unclassified and other/other uncategorized
  * typo fixes

## Version 1

  * added a machinetag readable version from the MISP Taxonomy repositories
  * merged in the existing Reference Taxonomy
  * merged in the description comments from https://www.enisa.europa.eu/topics/csirt-cert-services/community-projects/existing-taxonomies
  * created a script to convert the machinetag version to a human readable markdown version
  * added this CHANGELOG file
  * added a CONTRIBUTING file for GitHub
  * create a test directory, ignore for now please
