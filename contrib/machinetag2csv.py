#!/usr/bin/env python3


""" machinetag2csv.py
Copyright 2023 Aaron Kaplan <aaron@lo-res.org>

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""

import sys
import json
# from datetime import datetime

if len(sys.argv) != 2:
    print(f"syntax: {sys.argv[0]}  <inputfile>", file=sys.stderr)
    sys.exit(-1)

infile = sys.argv[1]


data = dict()
predicates = dict()

sep = ";"       # the CSV separator


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
  "namespace": "rsit"
}

===============================
"""


def print_header(data):
    print("""classification;type;description/examples""")


def print_entries(data):
    for predicate in data['predicates']:
        predicates[predicate['value']] = predicate['expanded']

    for entry in data['values']:
        for t in entry['entry']:
            desc = t.get('description', '')
            pred = predicates[entry['predicate']]
            rsit_type = t['expanded']
            print(f'"{pred}"{sep}"{rsit_type}"{sep}"{desc}"')


if __name__ == '__main__':
    try:
        with open(infile) as f:
            data = json.load(f)
            print_header(data)
            print_entries(data)
    except Exception as e:
        print(f"could not open or parse json input file. Reason: {str(e)}")
        sys.exit(-2)
