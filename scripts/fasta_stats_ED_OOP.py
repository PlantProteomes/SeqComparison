#!/bin/env python3

import re #refers to regular expressions module
from Bio import SeqIO

class FastaStats:

    #### Constructor
    def __init__(self):
        self.entry_counter = 0
        self.stats = {}
        for data_type in [ 'identifiers', 'sequences' ]:
            self.stats[data_type] = {
                'n_redundant_entries': 0,
                'nonredundant_entries': {}
            }

    #this function updates count of redundant identifiers
    def add_datum(self, data_type, value):
        if value in self.stats[data_type]['nonredundant_entries']:
            self.stats[data_type]['n_redundant_entries'] += 1
        else:
            self.stats[data_type]['nonredundant_entries'][value] = True


    def read(self, filename):

        #this will open specified file
        with open(filename) as infile:

            print(f"INFO: Reading {filename}")

            #parses through records line by line
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq) 
                self.entry_counter += 1

                #this line separates the identifier and the description into 2 groups by the space
                match = re.match(r'^(\S+)\s*(.*)$', record.description) #record is a fasta object
                if match: #if this line can be separated and parsed this way
                    identifier = match.group(1) 
                    description = match.group(2)

                    self.add_datum('identifiers', identifier)
                    self.add_datum('sequences', sequence)

                else:
                    print(f"ERROR: Unable to parse description line: {record.description}")
                    exit()


##########################################################################
def main():

    fasta_stats = FastaStats()
    filename = '../proteomes/maize/original/mitochondrion.2.fasta'
    fasta_stats.read(filename)

    #printing out stats collected
    print('')
    print("There is a total of", fasta_stats.entry_counter, "entries.")
    print("There are", len(fasta_stats.stats['identifiers']['nonredundant_entries']), "unique identifiers.")
    print("There are", len(fasta_stats.stats['sequences']['nonredundant_entries']), "unique sequences.")
    print("There are", fasta_stats.stats['identifiers']['n_redundant_entries'], "redundant identifiers.")
    print("There are", fasta_stats.stats['sequences']['n_redundant_entries'], "redundant sequences.")


if __name__ == "__main__":
    main()