# Margaret Li
#

import re
from Bio import SeqIO
import numpy as np
import argparse

class Matrix:
    
    def __init__(self):
        self.identifiers = {}  # dictionary of ident with keys as ident and values as count
        self.sequences = {}  # dictionary of seq with keys as seq and values as count
        self.split_files = [] # list of dictionaries that have each contain file's title and filename
        self.COUNT = len(self.split_files)

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

# Parse the list of files from the user into Title=Filename
    def parse_files_argument(self, files):
        print("Parsing input title=filename arguments")
        
        # for every file in the list, split title and file, log as dict element and append to list
        for title_file in files:
            try:
                title,filename = title_file.split('=')
            except:
                print(f"ERROR: Parameter '{title_file}' should have the format TITLE=FILENAME (e.g. Mito=mitochondria.2.fasta)")
                exit(1)
            split_file = { 'title': title, 'filename': filename } # used for splitting 1 file
            print(split_file)

            # add dict format to list
            self.split_files.append(split_file)
        print('')
         

# creates a matrix used to store overlapping sequences of different
# fasta files, total sequences, distinct sequences, and unique sequences
    def create_matrix(self):
        matrix = []

        # create unique first row with filenames and specs
        first_row = ["Source", "Sequences", "Distinct", "Unique"]
        for file_entry in self.split_files:
            first_row.append(file_entry['title'])
        matrix.append(first_row)

        # updates the matrix with 0 as placeholders and first column
        for i in range(0, self.COUNT):
            row = [0] * (self.COUNT + 4)
            row[0] = self.split_files[i]['title']
            matrix.append(row)

        print("Matix template:")
        print(np.matrix(matrix))
        return matrix


  # currently putting everything I dont know into the parameter
  # construct matrix in main so there are not too many class variables
  # note filenames may not have to be a class variable
    def update_matrix(self, matrix):
        for i in range(0, self.COUNT):
            for j in range(i, self.COUNT): # for the diagonals. only start at i
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
                
                # updating matrix with overlap
                matrix[i + 1][j + 1] = overlap
    
        print(matrix)

##########################################################################

def main():
   
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
                            help='Two or more FASTA files to compare, using notation Title=filename') # NEW

    args = argparser.parse_args()
    master_table = Matrix()
    master_table.split_files = master_table.parse_files_argument(args.files)
    master_table.create_matrix()

    return # why?

    file1_fasta_stats = Matrix()  # create object for one file
    filename = args.files[0]
    file1_fasta_stats.read(filename)

    file2_fasta_stats = Matrix()  # create object for second file
    filename = args.files[1]
    file2_fasta_stats.read(filename)



if __name__ == "__main__":
    main()







