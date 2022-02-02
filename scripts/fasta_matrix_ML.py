# Margaret Li
# 1/29/22
# This program takes n fasta files from the users that are formatted in 
# the title=filename format. It then constructs a matrix that stores
# overlapping sequences from these files

from Bio import SeqIO
import numpy as np
import argparse

class Matrix:
    
    def __init__(self):
        self.sequences = {}  # dictionary of seq with keys as seq and values as count
        self.split_files = [] # list of dictionaries that have each contain a file's title and filename
        self.COUNT = 0 # number of files compared

    # reads given file and stores sequences as keys in self.sequences and
    # of this sequence as value in the same dict
    def read(self, filename):
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)

                # add sequence and count to dict
                if sequence not in self.sequences:
                    self.sequences[sequence] = 1
                else:
                    self.sequences[sequence] += 1


# takes list of identifiers as parameter.
# it tallies total number of seq, and distinct seqs
    def file_stats(self, seqs):
        # stores total # of entries. Will update this count for redundancies
        total = len(seqs)

        # loop through dict and update total # of entries
        # accounts for redundancies
        for item in seqs:
            if seqs[item] != 1:
                # -1 because every one has been accounted once already
                total += (seqs[item] - 1)

        # return results as tuple. return total and distinct seqs
        return (total, len(seqs))

# takes unique sequences from two file (obtained from calling file_stats) and
# finds shared seq b/w these two files and return this number
    def compare(self, dict1, dict2):
        num_overlap = 0  # counts overlap of i/s

        # lopp through dicts to compare sequences
        for item in dict1:
            if item in dict2:
                num_overlap += 1
        return num_overlap

# Parse the list of files from the user's Title=Filename format
# store info of each file into a dict and add that to the self.split_files list
    def parse_files_argument(self, files):
        print("Parsing input title=filename arguments")
        
        # for every file in the list, split title and file, log as dict element and append to list
        for title_file in files:
            try:
                title,filename = title_file.split('=')
            # incase the formatting is wrong
            except:
                print(f"ERROR: Parameter '{title_file}' should have the format TITLE=FILENAME (e.g. Mito=mitochondria.2.fasta)")
                exit(1)

            # store title and filename of 1 file after split
            split_file = { "title": title, "filename": filename }

            # add dict format to list
            self.split_files.append(split_file)
            print(split_file)

        print('')
         

# creates a matrix used to store overlapping sequences of different
# fasta files, total sequences, distinct sequences, and unique sequences
# only creates template. Actual data is replaced by 0's
# matrix template will be returned
    def create_matrix(self):
        matrix = [] 

        # create unique first row with filenames and specs
        first_row = ["Source", "Sequences", "Distinct", "Unique"]

        # add title of each input file to first_row
        for file_entry in self.split_files:
            first_row.append(file_entry["title"])

        # add first row to matrix
        matrix.append(first_row)

        # updates the matrix with 0 as placeholders and first column
        for i in range(0, self.COUNT):
            row = [0] * (self.COUNT + 4)
            row[0] = self.split_files[i]["title"]
            matrix.append(row)

        # print template
        print("Matrix template:")
        print(np.matrix(matrix))
        print('')

        return matrix


  # updates the matrix template returned from create_matrix()
  # with actual overlapping values and file stats
    def update_matrix(self, matrix):

        # i is the row
        for i in range(1, self.COUNT + 1):
            # first file obj to be compared. Read and take stats
            file1 = Matrix()
            file1.read(self.split_files[i - 1]["filename"])
            stats = file1.file_stats(file1.sequences)

            # update total seqs
            matrix[i][1] = stats[0]
            # update distinct seqs
            matrix[i][2] = stats[1]

            # j is the columm
            for j in range(i + 1, self.COUNT + 1): # acounts for diagonals. start at i

                # second file obj to be compared. Read and take stats
                file2 = Matrix()
                file2.read(self.split_files[j - 1]["filename"])

                # compare the two files and find overlapping i/d
                overlap = file1.compare(
                    file1.sequences, file2.sequences)
                
                # updating matrix with overlap
                matrix[i][j + 3] = overlap
    
        print(np.matrix(matrix))

##########################################################################

def main():
   
    # Add the arguments
    argparser = argparse.ArgumentParser(
        description='Construct matrice of overlapping sequences from FASTA files')
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
    # parse input from users 
    master_table.parse_files_argument(args.files)
    # update count of files inputted
    master_table.COUNT = len(master_table.split_files)
    # create and print matrix template
    matrix = master_table.create_matrix()
    # update matrix with actual values
    master_table.update_matrix(matrix)


if __name__ == "__main__":
    main()

'''
Command Line Input:
python fasta_matrix_ML.py Araport11=C:\Users\jli\SeqFiles\arabidopsis\Araport11.fasta TAIR10=C:\Users\jli\SeqFiles\arabidopsis\TAIR10.fasta UniProtKB=C:\Users\jli\SeqFiles\arabidopsis\UniProtKB.fasta RefSeq=C:\Users\jli\SeqFiles\arabidopsis\RefSeq.fasta ARA-PEP:LW=C:\Users\jli\SeqFiles\arabidopsis\ARA-PEP-LW.fasta ARA-PEP:SIPs=C:\Users\jli\SeqFiles\arabidopsis\ARA-PEP-SIPs.fasta ARA-PEP:sORFs=C:\Users\jli\SeqFiles\arabidopsis\ARA-PEP-sORFs.fasta IowaORFs=C:\Users\jli\SeqFiles\arabidopsis\IowaORFs.fasta
'''