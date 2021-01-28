#!/usr/bin/env python

from __future__ import print_function

import sys
import json
import uuid
import random
import re

if len(sys.argv) != 3:
    print("syntax: %s  <inputfile> <outputfile>" %(sys.argv[0],), file=sys.stderr)
    sys.exit(-1)

infile = sys.argv[1]
outfile = sys.argv[2]

data = dict()
predicates = dict()


def print_header(data, outfile):
    f = open(outfile, "w")
    f.write("""
# RSIT to ATT&CK

Generated from machine readable version. Please **DO NOT** edit this file directly in github, rather use the machinetag.json file.

| Classification | Incident examples | ATT&CK Technique              | Description        |
|----------------|-------------------| ------------------------------|--------------------|""")
    f.write("\n")

def print_entries(data, outfile):
    f = open(outfile, "a")
    for predicate in data['predicates']:
        predicates[predicate['value']] = predicate['expanded']

    for entry in data['values']:
        for t in entry['entry']:
            d = t.get('description', '')
            a = t.get('attck', '')
            attck = ""
            for el in a:
                if 'MITRE' in el:
                    if re.match(r'^T\d{4} -',el['MITRE']):
                        # Technique
                        attck = "%s[%s](https://attack.mitre.org/techniques/%s/)<br><br>" %(attck, el['MITRE'], el['MITRE'].split("-")[0].strip())
                    elif re.match(r'^T\d{4}/\d{3} -',el['MITRE']):
                        # SubTechnique
                        attck = "%s[%s](https://attack.mitre.org/techniques/%s/)<br><br>" %(attck, el['MITRE'], el['MITRE'].split("-")[0].strip())
            f.write('| %s | %s | %s | %s |' %(predicates[entry['predicate']], t['expanded'], attck, d))
            f.write("\n")

if __name__ == '__main__':
    if True:
        with open(infile) as f:
            data = json.load(f)

            print_header(data, outfile)
            print_entries(data, outfile)

