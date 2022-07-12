# Margaret Li
# 1/29/22
# This program takes n fasta files from the users that are formatted in
# the title=filename format. It then constructs a matrix that stores
# overlapping sequences and other stats from these files

from Bio import SeqIO
import numpy as np
import pandas as pd
import argparse


class Matrix:

    def __init__(self):
        # dictionary of seq with keys as seq and values as count
        self.sequences = {}
        # list of dictionaries that have each contain a file's title and filename
        self.split_files = []
        # number of files compared
        self.COUNT = 0

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

# Parse the list of files from the user's Title=Filename format
# store info of each file into a dict and add that to the self.split_files list
    def parse_files_argument(self, files):
        print("Parsing input title=filename arguments")

        # for every file in the list, split title and file, log as dict element and append to list
        for title_file in files:
            try:
                title, filename = title_file.split('=')
            # incase the formatting is wrong
            except:
                print(
                    f"ERROR: Parameter '{title_file}' should have the format TITLE=FILENAME (e.g. Mito=mitochondria.2.fasta)")
                exit(1)

            # store title and filename of 1 file after split
            split_file = {"title": title, "filename": filename}

            # add dict format to list
            self.split_files.append(split_file)
            print(split_file)

        print('')

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
        # counts overlap of i/s
        num_overlap = 0

        # lopp through dicts to compare sequences
        for seq in dict1:
            if seq in dict2:
                num_overlap += 1

        return (num_overlap)

# find unique sequences from iterating over the files and
# deleting these sequences from an inputted dictionary with
# all sequences. Also inputs total files used
    def find_unique(self, file_count, master_seq):
        # keep track of sequences to delete {file # : set of seq to delete}
        deletions = {}
        # put empty sets as values to file # keys
        for i in range(1, file_count + 1):
            deletions[i] = set()

        # get one file from all files except the last
        for i in range(1, file_count + 1):
            # get a sequence from file1
            for seq in master_seq[i]:
                # get a file (file2) after file1
                for j in range(i + 1, file_count + 1):
                    # if a match is found in this file, means
                    # sequence is not unique to either
                    # delete from both
                    if seq in master_seq[j]:
                        deletions[i].add(seq)
                        deletions[j].add(seq)

        # do deletions of not unique sequences
        for k in range(1, file_count + 1):
            for element in deletions[k]:
                del master_seq[k][element]
        
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
            first_row.append("  " + file_entry["title"])

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
        # will be used to store all sequences for the purpose of 
        # finding unique entries in each file
        # {file#, {seq:count, seq:count}}
        # {seq,count} will just be file.seq
        master_seq = {}

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
            for j in range(i + 1, self.COUNT + 1):  # acounts for diagonals. start at i
                # second file obj to be compared. Read and take stats
                file2 = Matrix()
                file2.read(self.split_files[j - 1]["filename"])

                # compare the two files and find overlapping seq
                overlap = file1.compare(
                    file1.sequences, file2.sequences)

                # updating matrix with overlap
                matrix[i][j + 3] = overlap
            
            # updating master_seq for unique column
            master_seq[i] = file1.sequences
        
        # for testing
        #for k in range(1, self.COUNT + 1):
            #print(k)
            #print(len(master_seq[k]))

        # delete not unique seq from master_seq
        file1.find_unique(self.COUNT, master_seq)

        # for testing
        #for k in range(1, self.COUNT + 1):
            #print(k)
            #print(len(master_seq[k]))

        # updating unique column of matrix
        for k in range(1, self.COUNT + 1):
            length = len(master_seq[k])
            matrix[k][3] = length

        # pretty print matrix results in organized table
        df = pd.DataFrame(matrix[1:], columns=matrix[0])
        print(df)


        # create excel writer object
        writer = pd.ExcelWriter("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\arabidopsis_table.xlsx")
        # write dataframe to excel
        df.to_excel(writer, "arabidopsis")
        # save the excels
        writer.save()
        print('DataFrame is written successfully to Excel File.')


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
                           help='Two or more FASTA files to compare, using notation Title=filename')  # NEW

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