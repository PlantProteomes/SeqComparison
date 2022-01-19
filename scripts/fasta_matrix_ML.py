# Margaret Li
#

# import argparse
import re
from Bio import SeqIO
import numpy as np


class Matrix:
    filenames = ["a.fasta", "b.fasta", "c.fasta", "d.fasta"]  # actual filenames not legend
    leg_names = [] # store abbreviated versions of filenames
    COUNT = len(filenames) # number of files inputted by user

    def __init__(self):
        self.identifiers = {}  # dictionary of ident with keys as ident and values as count
        self.sequences = {}  # dictionary of seq with keys as seq and values as count

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
                    if identifier not in self.sequences:
                        # add identifier and count to dict
                        self.identifiers[identifier] = 1
                    else:
                        # add identifier and count to dict
                        self.identifiers[identifier] += 1
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()


# takes list of identifiers or sequences and type of data as parameter.
# it tallies total number of ident/seq, distinct ones, and redundancies
    def file_stats(self, is_dict, type):
        # stores total # of entries. Will update this figure
        total = len(is_dict)
        num_redund = 0  # total redundancies

        # loop through dict and update redundancy # and total # of entries
        for item in is_dict:
            if is_dict[item] != 1:
                num_redund += 1
                # -1 because every one has been accounted once already
                total += (is_dict[item] - 1)

        # return results. return total and distinct
        return [total, len(is_dict)]

# takes unique i/s from each file (obtained from calling file_stats) and
# finds overlapping (shared b/w two files) i/s also returns a set of overlapping
# identifiers. Returns set of overlapping i/s
    def compare(self, dict1, dict2, type):
        num_overlap = 0  # counts overlap of i/s

        # determines unique list1 elements overlapping elements between
        # dict1 and dict2
        for item in dict1:
            if item in dict2:
                num_overlap += 1
        return num_overlap

# prints a legend for shortened versions of filenames. Will be used 
# in the matrix for more convenient reading
    def legend(self):
        print("Legend for how files are represented in the matrix:")
        for i in range (0, self.COUNT):
            short = (self.filenames[i]).replace(".fasta", "")
            self.leg_names.append(short)
            print( short + " - " + self.filenames[i])

         

# creates a matrix used to store overlapping sequences of different
# fasta files, total sequences, distinct sequences, and unique sequences
    def create_matrix(self):
        matrix = []

        # create unique first row with filenames and specs
        first_row = ["Source", "Sequences", "Distinct", "Unique"]
        first_row.extend(self.leg_names) 
        matrix.append(first_row)

        # updates the matrix with 0 as placeholders and first column
        for i in range(0, self.COUNT):
            row = [0] * (self.COUNT + 4)
            row[0] = self.leg_names[i]
            matrix.append(row)
        print(np.matrix(matrix))


  # currently putting everything I dont know into the parameter
  # construct matrix in main so there are not too many class variables
  # note filenames may not have to be a class variable
    def update_matrix(self, filenames, matrix_s):
        file_stats = {}
        for i in range(0, self.COUNT):
            for j in range(i, self.COUNT): # for the diagnals. only start at i
                # this way of creating instances of the class would not cause issues?

                # first file obj to be compared. Read and take stats
                file1 = Matrix()
                file1.read(self.filenames[i])
                file1.file_stats(file1.sequences)

                # second file obj to be compared. Read and take stats
                file2 = Matrix()
                file2.read(self.filenames[i + 1])

                # compare the two files and find overlapping i/d
                overlap = file1.compare(
                    file1.sequences, file2.sequences, "sequences")
                
                # constructing matrix
                matrix_s[i + 1][j + 1] = overlap
    

        print(matrix_s)

##########################################################################

def main():
    test = Matrix()
    test.legend()
    test.create_matrix()
'''
    # Add the arguments
    argparser = argparse.ArgumentParser(
        description='Construct matrice of overlapping ident/seq from FASTA files')
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

    file1_fasta_stats = Matrix()  # create object for one file
    filename = args.files[0]
    file1_fasta_stats.read(filename)

    file2_fasta_stats = Matrix()  # create object for second file
    filename = args.files[1]
    file2_fasta_stats.read(filename)
'''

if __name__ == "__main__":
    main()







