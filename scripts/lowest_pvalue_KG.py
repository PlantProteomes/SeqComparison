import argparse
import re
from Bio import SeqIO
import os


class pvalue_lowest:

    def __init__(self):
        # stores the vlaues in here
        self.identifier = dict()
        self.entry_counter = 0

    def read(self, filename):

        # this will open specified file
        with open(filename) as infile:

            print(f"INFO: Reading {filename}")

            # parses through records line by line
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)

                match = re.match(r'^(\S+)\s*(.*)$', record.description)
                if match:
                    identifier = match.group(1)
                    split = identifier.split('_')
                    gene = split[0]
                    pnum = split[1]

                    # appends genes wtih multiple copies  that have P001,P002 etc.
                    if gene not in self.identifier:
                        pcodes = []
                        pcodes.append(pnum)
                        self.identifier[gene] = pcodes

                    else:
                        self.identifier[gene].append(pnum)

                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()

    def createFastaPvalue(self):

        pfile = open("lowest_pvalue.txt", "a")

        for gene in self.identifier:
            min = 10
            for pnum in self.identifier[gene]:
                # compares to find the lowest P00XX Number and add to list and adds the lowst version of such i.e P001
                pvalue = int(pnum[3])
                if pvalue < min:
                    min = pvalue
            # credit to margaret's code :)
            file_entry = gene + "_" + "P00" + str(min) + "\n"
            pfile.write(file_entry)
        # counts entries in file
# counts files

    def FileCount(self):
        file = open("lowest_pvalue.txt", "r")
        for line in file:
            if line != "\n":
                self.entry_counter += 1
        file.close()

# deltes file upon request for next set of isoforms
    def DeleteFile(self):
        print("Type DELETE to remove file once finished(No space)")
        Delete = input("Type DELETE OR SAVE")
        if Delete == "DELETE":
            if os.path.exists("lowest_pvalue.txt"):
                os.remove("lowest_pvalue.txt")
            else:
                print("The file does not exist")
        else:
            exit()


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
    for i in range(0, len(args.files)):
        fasta_file = pvalue_lowest()
        filename = args.files[i]
        fasta_file.read(filename)
        fasta_file.createFastaPvalue()
        fasta_file.FileCount()
        print("INFO: Done. File Parsed " + str(fasta_file.entry_counter) +
              " entries. Isoforms sent to txt file")
        fasta_file.DeleteFile()


if __name__ == "__main__":
    main()
