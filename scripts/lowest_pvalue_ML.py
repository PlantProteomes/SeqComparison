# Margaret Li
# 02/16/22
# This program reads a given fasta file and parses through all
# identifiers in it. The program finds the identifiers with the lowest
# value in pcode P00# for each gene and writes results to a
# specified txt file

import argparse
import re
from Bio import SeqIO

class Lowest_Pvalue:
    
    def __init__(self):
        # gene names as keys and pcodes as values
        self.ident = {} 

    # reads given file, separate identifiers and sequences and store
    # this info into a compare object
    def read(self, filename):
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):

                '''still need this?'''
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
                    # if contains gene name, just add pcode
                    else:
                        self.ident[gn].append(pcode)

                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()


    # this function assembles identifier entries with the lowest pvalues
    # and writes them to a text file called "fasta_lowest_pvalue.txt"
    # in the same directory as the program
    def getLowestPvalue(self):
        # create txt file that would contain all the 
        # entries in lowest p value form
        pfile = open("fasta_lowest_pvalue.txt" , "w") 

        # loop through identifiers in self.ident to 
        # find entries with lowest pvalue for each 
        for gn in self.ident:
            min = 100
            # for each identifier, find entry with lowest p value by comparing last number
            for pcode in self.ident[gn]:
                # get value of last number
                pvalue = int(pcode[3])
                if pvalue < min:
                    min = pvalue
            # assemble file entry for txt file with lowest pvalue
            file_entry = gn + "_" + "P00" + str(min) +"\n"
        
            # write this entry into txt file
            pfile.write(file_entry)
            

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

    # create class object and use filename inputted by user
    # to read given fasta file
    fasta_file = Lowest_Pvalue() 
    filename = args.files[0]
    fasta_file.read(filename)

    # write identifier entries with lowest p values to txt file
    fasta_file.getLowestPvalue()

    print("")
    print("Please make sure that you have a txt file in the same directory as \
    the program")


if __name__ == "__main__":
    main()