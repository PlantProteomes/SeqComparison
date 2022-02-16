# Margaret Li
# 02/05/22
# This program compares two files the the goal of identifying distinct
# identifiers. Note: isoforms are ignored

import argparse
import re
from Bio import SeqIO

class Compare_fasta:
    

    def __init__(self):
        self.identifiers = {} # dictionary of ident with keys as ident and values as count
        self.sequences = {} # dictionary of seq with keys as seq and values as count

  
    # reads given file, separate identifiers and sequences and store
    # this info into a compare object
    def read(self, filename):
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)
                # add sequence and count to dict
                if sequence not in self.sequences:
                    self.sequences[sequence] = 1  
                else:
                    self.sequences[sequence] += 1

                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                # if identifiers are parseable store appropriate values. Else print error statement
                if match:
                    identifier = match.group(1)

                    # assuming that if there is a dash, it is used
                    # for suffix. Assuming that there are no
                    # excess spaces like "- 2"
                    split = identifier.split('-')
                    primary = split[0] # primary form of ident

                    if primary not in self.identifiers:
                        self.identifiers[primary] = 1 # add identifier and count to dict
                    else:
                        self.identifiers[primary] += 1 # add identifier and count to dict
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()
            

# takes list of identifiers or sequences and type of data as parameter.
# it tallies total number of ident/seq, distinct ones, and redundancies
    def file_stats(self, is_dict, type):
        total = len(is_dict)  # stores total # of entries. Will update this figure
        num_redund = 0  # total redundancies

        # loop through dict and update redundancy # and total # of entries
        for item in is_dict:
            if is_dict[item] != 1:
                num_redund += 1
                total += (is_dict[item] - 1) # -1 because every one has been accounted once already

        #print results
        print("There is a total of " + str(total) + " " + type + ", " + str(num_redund) +
              " " + "redundancies, and " + str(len(is_dict)) + " distinct " + type + ".")


# takes unique i/s from each file (obtained from calling file_stats) and 
# finds overlapping (shared b/w two files) i/s also returns a set of overlapping 
# identifiers. Returns set of overlapping i/s 
    def compare(self, dict1, dict2, type):
        num_overlap = 0  # counts overlap of i/s
        # overlap = set()  # set of overlapping idents. will be returned

        # determines unique list1 elements overlapping elements between
        # dict1 and dict2
        for item in dict1:
            if item in dict2:
                num_overlap += 1
                # overlap.add(item)

        # print results
        print("There are " + str(num_overlap) + " overlapping " + type + ".")
        print("There are " + str(len(dict1) + len(dict2) -
              2 * num_overlap) + " unique " + type + " overall.")
        # just for uniprot UP000005640
        print("There are " + str(len(dict1) - num_overlap) + " " + type + " unique to file 1.")
        print("There are " + str(len(dict2) - num_overlap) + " " + type + " unique to file 2.")
        
        
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
    # prints none when didn't provide dup seq command
    print(args.show_duplicate_sequences)

    file1_fasta_stats = Compare_fasta() # create object for one file
    filename = args.files[0]
    file1_fasta_stats.read(filename)

    print("Comparing\n"+
    filename + "\nwith")

    file2_fasta_stats = Compare_fasta() #create object for second file
    filename = args.files[1]
    file2_fasta_stats.read(filename)
    print(filename)
    print("")

    ##### IDENTIFIER COMPARISON #####
    # these two lines confirm stats for each file 
    print("File stats for each file in order of input")
    file1_fasta_stats.file_stats(file1_fasta_stats.identifiers, "identifiers")
    file2_fasta_stats.file_stats(file2_fasta_stats.identifiers, "identifiers")
    print("")
    print("Stats Comparison")
    # this line does the comparing of unique sequences
    file1_fasta_stats.compare(file1_fasta_stats.identifiers, file2_fasta_stats.identifiers, "identifiers")

if __name__ == "__main__":
    main()
