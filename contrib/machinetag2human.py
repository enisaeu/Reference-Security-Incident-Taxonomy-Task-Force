#!/usr/bin/env python3

""" machinetag2human.py 
Copyright 2018 Aaron Kaplan <kaplan@cert.at>

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""

import sys
import json
from datetime import datetime

if len(sys.argv) != 2:
    print("syntax: %s  <inputfile>" %sys.argv[0], file=sys.stderr)
    sys.exit(-1)

infile = sys.argv[1]

data = dict()


"""
===============================
example entry of the input file:

{
  "values": [
    {
      "entry": [
        {
          "description": "Or 'Unsolicited Bulk Email', this means that the recipient has not granted verifiable permission for the message to be sent and that the message is sent as part of a larger collection of messages, all having a functionally comparable content.",
          "expanded": "spam",
          "value": "spam"
        },
        {
          "description": "Discreditation or discrimination of somebody e.g. cyber stalking, racism and threats against one or more individuals).",
          "expanded": "Harmful Speech",
          "value": "harmful-speech"
        },
        {
          "description": "Child Pornography, glorification of violence, ...",
          "expanded": "Child/Sexual/Violence/...",
          "value": "violence"
        }
      ],
      "predicate": "abusive-content"
    },
 [
   {
      "description": "Meant for testing.",
      "expanded": "Test",
      "value": "test"
    }
  ],
  "version": 1,
  "description": "Reference Security Incident Classification Taxonomy",
  "namespace": "RSIT"
}

===============================
"""




def print_header(data):
    print("""
# REFERENCE TAXONOMY INCIDENT  Taxonomy (human readable version)


This is the %s.

See the [machine readable version](machinev1) as well. It should have an identical contents to the human readable version.
Note that the 1st column is mandatory, the 2nd colum is an optional but desired field.

Version: %s
Generated from [machine readable version](machinev1) on %s


| CLASSIFICATION (1ST COLUMN)                                   | INCIDENT EXAMPLES (2ND COLUMN)        | Description / Examples |
|---------------------------------------------------------      |------------------------------------   |------------------------|""" %(data['description'], data['version'], str(datetime.now())))



def print_entries(data):
    for entry in data['values']:
        classification = entry['predicate']
        for t in entry['entry']:
            d = t.get('description', '')
            print('| %s | %s | %s |' %(classification, t['expanded'], d))



if __name__ == '__main__':

    try: 
        with open(infile) as f:
                data = json.load(f)
                print_header(data)
                print_entries(data)
    except  Exception as ex:
        print("could not open or parse json input file. Reason: %s" %str(ex))
        sys.exit(-2)
    
