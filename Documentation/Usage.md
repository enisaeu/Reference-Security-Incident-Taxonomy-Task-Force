# Usage (Draft)

This document is currently work in progress and should not be considered complete.

## What to classify

The taxonomy can be used to classify data with different size and complexity.
For example, the following - of course incomplete - list gives a gist on what kind of data could be classified with the Taxonomy:

* Incidents: Any small- or large-scale IT-security related incident.
* Tickets: IT-security related "tickets" in ticketing systems.
* IoCs: Atomic "Indicators of Compromise", which can also be part of any of the above data sets.

We will use the term "data record" in the following sections as synonym for these kinds of data.

## Multiple classifications

An often asked question is whether a data record can be classified with more than one taxonomy/type-pair or not.
The taxonomy itself does not have any rule on how it needs to be used and therefore it is perfectly fine to tag an incident with multiple taxonomies & types - this is totally at the discretion of the user.

Often, the clarification depends on the point of view. Some examples:
* C2 server network connection: A network connection between a client computer, infected by a malware, to a Command & Control server: This IoC is both classifiable as "Malicious Code / Infected System" (for the client computer) as well as "Malicious Code / C2 Server" (for the server).
* Phishing page: A hacked website abused as phishing page is both "Information Content Security / Unauthorised modification of information" (for the website) as well as "Fraud / Phishing" (for any user).

A tricky issue is statistics: Does a data record, which is then multiply classified, count for all its classifications, or proportionally? This is, again, left to the user to decided. However, it should be clearly stated in the statistics description, how the numbers are composed.

### Weighting

A possible solution for this could be (manual or automatic) weighting for multiple classifications.

For example, the above "C2 server network connection" could be 80% "Malicious Code / C2 Server" and 20% "Malicious Code / Infected System" if the first is considered more important than the latter.
It is also possible to automatically assign a uniformly distributed weight, so that every classification of a data record gets assigned an equal weight proportion. For the last example, it's 50% each.

Statistics can be created considering the weight of a classification, as the data record counts for different categories according to it's weight. However, this approach hides the total amount of data records per classification and can only be one of multiple perspectives.
