#!/bin/env python3

import pandas as pd
import re
from Bio import SeqIO
import argparse

# Create the parser
argparser = argparse.ArgumentParser(description='description of program')

# Add the arguments
argparser = argparse.ArgumentParser(
    description='Find duplicate identifiers, sequences, and descriptions in a FASTA file')
argparser.add_argument('--show_duplicate_identifiers', action='count',
                       help='If set, print the duplicate identifiers and their count in the input file')
argparser.add_argument('--show_duplicate_sequences', action='count',
                       help='If set, print the duplicate sequences and their count in the input file')
argparser.add_argument('--show_duplicate_descriptions', action='count',
                       help='If set, print the duplicate descriptions and their count in the input file')
argparser.add_argument('--show_total_reads', action='count',
                       help='If set, print the total number of rows in the input file')
argparser.add_argument('files', type=str, nargs='+',
                       help='Filename of the FASTA file to read')
params = argparser.parse_args()
# Execute the parse_args() method
args = argparser.parse_args()
input_path = args.Stat_test
input_execute = args.run

if input_execute == "Run":

 # new dataframe  create 3 columns identfier, description, and Sequence column
    df = pd.DataFrame(columns=['Identifier', 'Description', "Sequence"])

    filename = r'../proteomes/maize/original/mitochondrion.2.fasta'
    with open(filename) as infile:

        print(f"INFO: Reading {filename}")
        for record in SeqIO.parse(infile, 'fasta'):
            sequence = str(record.seq)
            match = re.match(r'^(.+?)\s+(.*)$', record.description)

            if match:
                identifier = match.group(1)
                description = match.group(2)
                new_row = {'Identifier': match.group(
                    1), 'Description': match.group(2), 'Sequence': sequence}
                df = df.append(new_row, ignore_index=True)

            else:
                print(
                    f"ERROR: Unable to parse description line: {record.description}")
                exit()
            print(f"{identifier} - {description}")


if input_path == "--show_total_reads":
    # total number of entries within the file
    index = df.index
    number_of_rows = len(index)
    print("Total reads: %i" % number_of_rows)
elif input_path == "--show_duplicate_identifiers":
    # total number of repeated identifiers(Listed out in a pivot table with each individual Identifier)
    df2 = df.pivot_table(columns=['Identifier'], aggfunc='size')
    var = []
    for column in df2.columns.values:
        if df2.columns.values > 1:
            var.append(df2[column].tolist())

    print("Total number of repeated identifiers are " % len(var))

elif input_path == "--show_duplicate_sequences":
    # total number of repeated descriptions(Listed out in a pivot table with each individual Description)
    df2 = df.pivot_table(columns=['Description'], aggfunc='size')
    var = []
    for column in df2.columns.values:
        if df2.columns.values > 1:
            var.append(df2[column].tolist())
    print("Total number of repeated are " % len(var))

elif input_path == "--show_duplicate_descriptions":
    # total number of repeated descriptions(Listed out in a pivot table with each individual Sequence)
    df2 = df.pivot_table(columns=['Sequence'], aggfunc='size')
    var = []
    for column in df2.columns.values:
        if df2.columns.values > 1:
            var.append(df2[column].tolist())
    print("Total number of repeated sequences are are " % len(var))
else:
    print("Error, please enter in an appropriate keyword to execute")
