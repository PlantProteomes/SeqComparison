#!/bin/env python3

import re  # refers to regular expressions module
from Bio import SeqIO
import json
import argparse


class FastaStats:

    def __init__(self):
        self.entry_counter = 0
        self.stats = {}
        for data_type in ['identifiers', 'sequences', 'descriptions']:
            self.stats[data_type] = {
                'n_redundant_entries': 0,
                'nonredundant_entries': {}
            }

    # this function updates count of redundant identifiers
    def add_datum(self, data_type, value):
        if value in self.stats[data_type]['nonredundant_entries']:
            self.stats[data_type]['n_redundant_entries'] += 1
            self.stats[data_type]['nonredundant_entries'][value] += 1
        else:
            self.stats[data_type]['nonredundant_entries'][value] = 1

    def read(self, filename):

        # this will open specified file
        with open(filename) as infile:

            print(f"INFO: Reading {filename}")

            # parses through records line by line
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)
                self.entry_counter += 1

                # this line separates the identifier and the description into 2 groups by the space
                # record is a fasta object
                match = re.match(r'^(\S+)\s*(.*)$', record.description)
                if match:  # if this line can be separated and parsed this way
                    identifier = match.group(1)
                    description = match.group(2)

                    self.add_datum('identifiers', identifier)
                    self.add_datum('sequences', sequence)

                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()

                # if self.entry_counter > 3:
                #    print(json.dumps(self.stats, indent=2, sort_keys=True))
                #    exit()

    def print_stats(self):

        # printing out stats collected
        print('')
        print("There is a total of", self.entry_counter, "entries.")
        print("There are", len(
            self.stats['identifiers']['nonredundant_entries']), "unique identifiers.")
        print("There are", len(
            self.stats['sequences']['nonredundant_entries']), "unique sequences.")
        print("There are", self.stats['identifiers']
              ['n_redundant_entries'], "redundant identifiers.")
        print("There are", self.stats['sequences']
              ['n_redundant_entries'], "redundant sequences.")

    def compare_stats(self, self2):
        common_pairs = dict()
        for key in self:
            if (key in self2 and self[key] == self2[key]):
                common_pairs[key] = self[key]
                print(common_pairs)

##########################################################################


def main():

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

    args = argparser.parse_args()
    print(args.show_duplicate_sequences)

    file1_fasta_stats = FastaStats()
    filename = args.files[0]
    file1_fasta_stats.read(filename)
    file1_fasta_stats.print_stats()

    file2_fasta_stats = FastaStats()
    filename = args.files[1]
    file2_fasta_stats.read(filename)
    file2_fasta_stats.print_stats()

    file1_fasta_stats.compare_stats(
        file1_fasta_stats.self, file2_fasta_stats.self)


if __name__ == "__main__":
    main()
