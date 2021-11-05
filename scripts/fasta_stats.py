#!/bin/env python3

import os
import sys
import re
from Bio import SeqIO


a, b, c = set(), set(), set()
entries= 0
all_space = 0


def get_set(set1, set2, set3):
    a.add(set1)
    b.add(set2)
    if not all_space:
        c.add(set3)
    global entries
    entries += 1


def Open_File(current_File):
    with open(os.path.join(current_File)) as infile:
        print(f"INFO: Reading {current_File}")
        for record in SeqIO.parse(infile, 'fasta'):
            global all_space
            sequence = str(record.seq)
            match = re.match(r'^(\S+)\s*(.*)$', record.description)
            if match:
                identifier = match.group(1)
                description = match.group(2)
                all_space = False
            else:
                print(f"ERROR: Unable to parse description line: {record.description}")
                exit()
            get_set(record.seq, identifier, description)


Open_File(sys.argv[1])
print(f"There are {entries} entries")
print(f"There are {len(a)} distinct sequences. There are {entries - len(a)} redundant sequences ")
print(f"There are {len(b)} distinct identifiers. There are {entries - len(b)} redundant  identifiers")
print(f"There are {len(c)} distinct descriptions. There are {entries - len(c) if len(c) != 0 else len(c)} redundant "
      f"descriptions")