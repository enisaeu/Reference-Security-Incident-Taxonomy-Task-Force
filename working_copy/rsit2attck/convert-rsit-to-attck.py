from __future__ import print_function

""" machinetag2human.py
Copyright 2018 Aaron Kaplan <kaplan@cert.at>
Updated fby Koen Van Impe <koen.vanimpe@cudeso.be>
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import sys
import json
import uuid
import random

rsit_taxonomy = "machinetag.json"
# Put files in the galaxy and cluster folder
# /var/www/MISP/app/files/misp-galaxy/galaxies
# /var/www/MISP/app/files/misp-galaxy/clusters
rsit_galaxy = "galaxies/rsit.json"
rsit_cluster = "clusters/rsit.json"
namespace = "rsit"
description = "Reference Security Incident Classification Taxonomy"
name = "RSIT"
author = "Koen Van Impe"
version = 1
source = "https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force"

def print_galaxy(predicates):
    uuid_galaxy = str(uuid.uuid4())
    predicates_list = False
    predicates_comma = ""
    translate_galaxy = {}
    for el in predicates:
        if predicates_list:
            predicates_comma = ","
        else:
            predicates_comma = ""
            predicates_list = ""
        predicates_list = """ %s%s "%s" """ % (predicates_list, predicates_comma, el["expanded"])
        translate_galaxy[el["value"]] = el["expanded"]

    f = open(rsit_galaxy, "w")
    f.write("""
{
    "description": "%s",
    "icon": "map",
    "kill_chain_order": {
      "%s": [
        %s
      ]
    },
    "name": "%s",
    "namespace": "%s",
    "type": "%s",
    "uuid": "%s",
    "version": %s
  }
  
    """ % (description, name, predicates_list, description, name, namespace, uuid_galaxy, version ))
    return translate_galaxy


def get_entry_related_attck(attck):
    related_list = False
    related_comma = ""
    for el in attck:
        if 'dest-uuid' in el:
            if related_list:
               related_comma = ","
            else:
                related_comma = ""
                related_list = """ "related": ["""
            related_list = """ %s%s 
                            { 
                                "dest-uuid": "%s", 
                                "tags": [
                                    "estimative-language:likelihood-probability=\\"likely\\""
                                    ],
                                "type": "similar"
                            } """ % (related_list, related_comma, el['dest-uuid'])

    if related_list:
        related_list = """%s]""" % (related_list)
    return related_list


def print_cluster(values, translate_galaxy):
    uuid_cluster = str(uuid.uuid4())

    values_list = False
    values_comma = ""
    for el in values:
        predicate = translate_galaxy[el["predicate"]]
        entries = el["entry"]
        for entry in entries:
            uuid_cluster_value = str(uuid.uuid4())
            related = ""
            if 'attck' in entry:
                related = get_entry_related_attck(entry['attck'])
                related_comma = ","
            else:
                related_comma = ""
            
            if values_list:
                values_comma = ","
            else:
                values_comma = ""
                values_list = ""
            values_list = """ %s%s 
                {
                    "description": "%s",
                    "meta": {
                    "cfr-type-of-incident": "%s",
                    "kill_chain": [
                        "%s:%s"
                    ]
                    },
                    "uuid": "%s",
                    "value": "%s:%s"%s
                    %s
                }""" % (values_list, values_comma, entry["description"], entry["expanded"], name, predicate, uuid_cluster_value, predicate, entry["expanded"], related_comma, related)


    f = open(rsit_cluster, "w")
    f.write("""{
    "authors": [
      "%s"
    ],
    "category": "%s",
    "description": "%s",
    "name": "%s",
    "source": "%s",
    "type": "%s",
    "uuid": "%s",
    "values": [
        %s
    ],
    "version": %s
  }""" % (author, namespace, namespace, namespace, source, namespace, uuid_cluster, values_list, version))
    
    
with open(rsit_taxonomy) as f:
    data = json.load(f)

    predicates = data.get("predicates")
    values = data.get("values")
    translate_galaxy = print_galaxy(predicates)
    print_cluster(values, translate_galaxy)

    print("Galaxy (%s) and cluster (%s) file created from taxonomy %s" % (rsit_galaxy, rsit_cluster, rsit_taxonomy ))
    print("Copy the directoreis into the MISP directory (/var/www/MISP/app/files/misp-galaxy/.")