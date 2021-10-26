#!/bin/env python3

import re
from Bio import SeqIO

filename = '../proteomes/maize/original/mitochondrion.2.fasta'
with open(filename) as infile:

    print(f"INFO: Reading {filename}")
    for record in SeqIO.parse(infile, 'fasta'):
        sequence = str(record.seq)
        match = re.match(r'^(\S+)\s*(.*)$', record.description)
        if match:
            identifier = match.group(1)
            description = match.group(2)
        else:
            print(f"ERROR: Unable to parse description line: {record.description}")
            exit()
        print(f"{identifier} - {description}")
