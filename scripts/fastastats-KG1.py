#!/bin/env python3

import pandas as pd
import re
from Bio import SeqIO
import argparse

# Create the parser
my_parser = argparse.ArgumentParser(
    description='List the content of fasta file(mitochondrion)')

# Add the arguments
my_parser.add_argument('Stat_test',
                       type=str,
                       help='type of stat to find, includes distinct identifiers, sequences, descriptions and total entries within file.'
                       )
my_parser.add_argument(
    'run', type=str, help='Runs code to execute, type "Run" to execute command')


# Execute the parse_args() method
args = my_parser.parse_args()
input_path = args.Stat_test
input_execute = args.run

if input_execute == "Run":

 # new dataframe  create 3 columns identfier, description, and Sequence column
    df = pd.DataFrame(columns=['Identifier', 'Description', "Sequence"])

    filename = r'C:\Users\kesha\mitochondrion.2.fasta'
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


if input_path == "Total_Entries":
    # total number of entries within the file
    index = df.index
    number_of_rows = len(index)
    print("Total reads: %i" % number_of_rows)
elif input_path == "Distinct_Identifier":
    # total number of repeated identifiers(Listed out in a pivot table with each individual Identifier)
    print(df.pivot_table(columns=['Identifier'], aggfunc='size'))
elif input_path == "Distinct_Description":
    # total number of repeated descriptions(Listed out in a pivot table with each individual Description)
    print(df.pivot_table(columns=['Description'], aggfunc='size'))
elif input_path == "Distinct_Identifier":
    # total number of repeated descriptions(Listed out in a pivot table with each individual Sequence)
    print(df.pivot_table(columns=['Sequence'], aggfunc='size'))
else:
    print("Error, please enter in an appropriate keyword to execute")
