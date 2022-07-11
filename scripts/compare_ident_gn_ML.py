# Margaret Li
# 02/10/22
# This program compares the UP file and the SP file with the goal
# of identifying identifiers unique to the UP file

import argparse
import re
from Bio import SeqIO

class Compare_Ident:
    
    def __init__(self):
        self.gn = {} # dictionary of ident with keys as ident and values as count
        self.frag = []
  

    # reads given file, separate identifiers and sequences and store
    # this info into a compare object
    def read(self, filename):
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):

                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                # if identifiers are parseable store appropriate values. Else print error statement
                if match:
                    identifier = match.group(1)
                    description = match.group(2)

                    # finding gene name for comparison for
                    # the entries that have gene name
                    split = description.split(' GN=')
                    if len(split) > 1:
                        second_half = split[1]
                        split2 = second_half.split(' ')
                        gene_name = split2[0]

                        # pair gene name with identifier
                        if gene_name not in self.gn:
                            all_ident = []
                            all_ident.append(identifier)
                            self.gn[gene_name] = all_ident
                        else:
                            self.gn[gene_name].append(identifier)

                    else:
                        self.frag.append(description)
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()


    # compares gene names between two input files and print identifiers
    # unique to the UP file 
    def compare_ident(self, UP_dict, SP_dict):
        ident_count = 0
        print("Here are the identifiers that are unique to the UP file:")
        print("")

        for gene_name in list(UP_dict):
            if gene_name in SP_dict:
                del UP_dict[gene_name]
            else:
                # print(len(UP_dict[gene_name]))
                max = 0
                longest = ""
                for identifier in UP_dict[gene_name]:
                    if len(identifier) > max:
                        max = len(identifier)
                        longest = identifier
                parts = longest.split('|')
                longest = parts[1]
                print(longest)
                ident_count += 1
        
        print("")
        print("There are " + str(ident_count) + " identifiers unique to the UP file.")
        
        
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

    UP_fastastats = Compare_Ident() # create object for one file
    filename = args.files[0]
    UP_fastastats.read(filename)

    print("Comparing\n"+
    filename + "\nwith")

    SP_fastastats = Compare_Ident() #create object for second file
    filename = args.files[1]
    SP_fastastats.read(filename)
    print(filename)
    print("")

    ##### IDENTIFIER COMPARISON #####
    # this line does the comparing and finds unique identifiers
    # MUST have UP file first
    UP_fastastats.compare_ident(UP_fastastats.gn, SP_fastastats.gn)


if __name__ == "__main__":
    main()
