# Margaret Li
# 02/22/22
# This program reads a given fasta file and parses through all
# identifiers in it. The program finds the identifiers with the lowest
# value in pcode P00# for each gene and writes identifier +
# corresponding sequence to a new fasta file

import argparse
import re
from Bio import SeqIO

class Lowest_Pvalue:
    
    def __init__(self):
        # gene names as keys and pcodes as values
        self.ident = {} 
        # gene names as keys and sequences for pcodes as values
        self.seq = {}

    # reads given file, separate identifiers and sequences and store
    # this info into a compare object
    def read(self, filename):
        print("INFO: Reading " + filename)
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq) 

                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                # if identifiers are parseable store appropriate values. Else print error statement
                if match:
                    identifier = match.group(1)

                    # split identifier at '-' to get pcode
                    split = identifier.split('_')
                    # gene name
                    gn = split[0]
                    # pcode
                    pcode = split[1] 

                    # if this gene name has not been logged
                    # to the dict, add it and create a list 
                    # of pcodes as value
                    if gn not in self.ident:
                        pcodes = [] 
                        pcodes.append(pcode)
                        self.ident[gn] = pcodes

                        sequences = []
                        sequences.append(sequence)
                        self.seq[gn] = sequences

                    # if contains gene name, just add pcode
                    else:
                        self.ident[gn].append(pcode)
                        self.seq[gn].append(sequence)

                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()


    # this function assembles identifier entries with the lowest pvalues
    # and writes them to a text file called "fasta_lowest_pvalue.txt"
    # in the same directory as the program
    def getLowestPvalue(self, filename):
        # create txt file that would contain all the 
        # entries in lowest p value form
        pfile = open(filename , "w") 

        # loop through identifiers in self.ident to 
        # find entries with lowest pvalue for each 
        for gn in self.ident:
            # used to store min pcode
            min = 1000

            # for each identifier, find entry with lowest p value by comparing last number
            for pcode in self.ident[gn]:
                # get value of last number
                pnumber_index = len(pcode) - 1
                pvalue = int(pcode[pnumber_index])
                if pvalue < min:
                    min = pvalue
                    # used to track index of corresponding sequence
                    seq_index = self.ident[gn].index(pcode)

            # assemble file entry for txt file with lowest pvalue
            gene_entry = ">" + gn + "_" + "P00" + str(min)
        
            # write this entry into txt file
            pfile.write(gene_entry + "\n")
            pfile.write(self.seq[gn][seq_index] + "\n")
            
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

    # create class object and use filename inputted by user
    # to read given fasta file
    fastaFile = Lowest_Pvalue() 
    filename = args.files[0]

    # read input file
    fastaFile.read(filename)

    output_filename = re.sub(r'\.[a-zA-Z0-9]+$','.pisoform.fasta',filename)

    # write identifier entries with lowest p values to txt file
    fastaFile.getLowestPvalue(output_filename)

    print("")
    print("INFO: Done...")
    

if __name__ == "__main__":
    main()