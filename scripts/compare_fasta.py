import argparse
import re
from Bio import SeqIO

# did not change this since last meeting. Will update after functions work
'''
very rough draft of argparse. Will update with version from repo-issue

#argparser parsing file names from user input
argparser = argparse.ArgumentParser(
    description = 'Compare two FASTA files and display stats')
parser.add_argument('file1', help = 'Name of the first file to compare')
parser.add_argument('file2', help = 'Name of the second file to compare')
args = parser.parse_args()
'''


class Compare_fasta:

    # each object would represent a file with a list of string id and a string of seq
    def __init__(self):
        self.identifiers = [] 
        self.sequences = []

    #! unable to test this function for some reason. Issue with filename

    # reads given file, separate identifiers, sequences, and descriptions, and store
    # this info into a compare object
    def read(self, filename):
        ident = []  # list of identifiers in a file
        seq = []  # list of sequences in a file

        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)
                seq.append(sequence)  # add sequence to list

                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                if match:
                    identifier = match.group(1)
                    description = match.group(2)
                    # add identifier to appropriate list
                    ident.append(identifier)
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()
            self.identifiers.extend(ident)
            self.sequences.extend(seq)

# takes list of identifiers or sequences and type as parameter.
# it tallies total number of ident/seq, distinct ones, and redundancies
    def file_stats(is_list, type):
        total = len(is_list)  # total number of entries
        index = {}  # stores i/s and their counts
        num_redund = 0  # total redundancies
        num_dist = 0  # distinct i/s

        # loops through list and update term and count in dictionary
        for item in is_list:
            if item in index:
                index[item] += 1
            else:
                index[item] = 1

        # loops through dictionary and counts total redundancies/distinct elements
        for element in index:
            if index[element] > 1:
                num_redund += 1
            else:
                num_dist += 1
        print("There is a total of " + str(total) + " " + type + ", " + str(num_redund) +
              " " + "redundancies, and " + str(num_dist) + " distinct " + type + ".")


# determines unique identifiers/sequences and overlapping (shared b/w two files) i/s
# also returns a set of overlapping identifiers. So the next function can determine
# of the overlapping ones, how many have the same sequences
    def compare(list1, list2, is_id, type):
        overlap = 0  # counts overlap of identif
        unique = set()  # put unique elements in set to avoid overcounting
        overlap_id = set() # list of overlapping id. will be returned
        for item in list1:
            if item not in unique:
                unique.add(item)
                if item in list2:
                    overlap += 1
                    if is_id == True:
                        overlap_id.add(item)
        print("There are " + str(len(unique) - overlap) + " unique " + type + ".")
        print("There are " + str(overlap) + " overlapping " + type + ".")
        return overlap_id


# determines of the overlapping identifiers, how many sequenses are unique and how
# many overlap
    def compare_seq(id1, id2, seq1, seq2, overlap_id):
        overlap = 0
        for item in overlap_id:
            # search for index of overlapping id and then use this index
            # to compare corresponding sequences.
            index1 = id1.index(item)
            index2 = id2.index(item)
            if seq1[index1] == seq2[index2]:
                overlap += 1
        print("Of the overlapping identifiers, " +
              str(overlap) + " have the same sequences.")


##########################################################################
def main():
    pass


main()

