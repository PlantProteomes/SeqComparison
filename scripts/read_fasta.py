#!/bin/env python3

import re
from Bio import SeqIO
import argparse

argparser = argparse.ArgumentParser(description='Parse a FASTA file')
argparser.add_argument('files', type=str, nargs='+', help='Filename of the FASTA file to read')
params = argparser.parse_args()

filename = params.files[0]
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
