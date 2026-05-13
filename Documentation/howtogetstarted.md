# HOWTO get started with the Reference Security Incident Taxonomy

Using the Reference Security Incident Taxonomy in your environment doesn't require a lot of effort.

1. Read the [documentation](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/tree/master/Documentation), especially take care of the [use cases](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/Use%20Cases.md) as these can give you additional ideas where to use the RSIT.
2. Check the latest [version](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/tree/master/working_copy) of the taxonomy, both in human readable format and in machine readable
3. Update the [usage page](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/Dependencies%20and%20tool%20mapping.md) if you use it
4. Push changes if you see fit or open an issue if you have questions or comments

## Multiple values

Security incidents often don't fall into one single classification. For example an incident can involve an attacker conducting multiple login attempts (Intrusion Attempts / Login attempts) with the purpose of gaining -unauthorized- access to information (Information Security / Unauthorised access to information). Another example is where an infected system (Malicious Code / Infected System) communicates with an external server to receive commands (Malicious Code / C2 Server).

When multiple values apply, the **primary** classification of an incident is the **intent** of the attacker, whereas the **secondary** classification can then be the means, or the transport mechanism, used to conduct the attack. For the above example, the infected system is the primary classification, where the C2 Server would be the secondary classification.

Linking this to the [Unified Kill Chain](https://www.csacademy.nl/images/scripties/2018/Paul-Pols---The-Unified-Kill-Chain.pdf) the **primary** classification is in fact the **action on objectives**. The **secondary** classifications are then those actions taken to get the **initial foothold** or to do **network propagation**. 

Note that in some cases it's worth splitting an incident into different sub-incidents, where each incident covers one of the different steps.

## Implementation

### TheHive

For TheHive you can use the build-in tagging system. Use "cat1:XYZ" and "cat2:ABC" to describe the classification (with cat1) and the specific incident examples (with cat2).

