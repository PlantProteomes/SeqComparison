import argparse
import re
from Bio import SeqIO


class Compare_Hseq:
    
    def __init__(self):
        self.identifiers = [] # total number of identifiers
        self.sequences = [] # total number of sequences
        self.distid = [] # distinct identifiers
        self.distseq = [] # distinct sequences
    
    # reads given file, separate identifiers, sequences, and descriptions, and store
    # this info into a compare object
    def read(self, filename):
        with open(filename) as infile:
            for record in SeqIO.parse(infile, 'fasta'):
                sequence = str(record.seq)
                self.sequences.append(sequence)  # add sequence to list

                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                if match:
                    identifier = match.group(1)
                    description = match.group(2)
                    # add identifier to appropriate list
                    self.identifiers.append(identifier)
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()

            print("Just read " + str(len(self.sequences)) +
                  " entries.")  # for testing program

# takes list of identifiers or sequences and type (specify i/s in PLURAL form) as parameter.
# it tallies total number of ident/seq, distinct ones, and redundancies
    def file_stats(self, is_list, type):
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
            num_dist += 1

        # update object attribute if identifier
        if type.lower() == "identifiers":
            self.distid.extend(index.keys())

        # update object attribute if sequence
        if type.lower() == "sequences":
            self.distseq.extend(index.keys())

        print("There is a total of " + str(total) + " " + type + ", " + str(num_redund) +
              " " + "redundancies, and " + str(num_dist) + " distinct " + type + ".")

    # takes unique i/s from each file (obtained from calling file states) and 
    # finds overlapping (shared b/w two files) i/s also returns a set of overlapping 
    # identifiers. So the next function can determine of the overlapping ones, 
    # how many have the same sequences
    def compare(self, list1, list2, type):
        num_overlap = 0  # counts overlap of i/s
        overlap = set()  # list of overlapping id. will be returned
        # determines unique list1 elements overlapping elements between
        # list1 and list2
        for item in list1:
            if item in list2:
                num_overlap += 1
                overlap.add(item)

        print("There are " + str(len(list1) + len(list2) -
              num_overlap) + " unique " + type + ".")
        print("There are " + str(num_overlap) + " overlapping " + type + ".")
        
        return overlap

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

    file1_fasta_stats = Compare_Hseq()
    filename = args.files[0]
    file1_fasta_stats.read(filename)
    # file1_fasta_stats.print_stats()

    file2_fasta_stats = Compare_Hseq()
    filename = args.files[1]
    file2_fasta_stats.read(filename)
    # file2_fasta_stats.print_stats()

    ##### SEQ COMPARISON #####
    # these two lines confirm stats for each file (will be printed)
    file1_fasta_stats.file_stats(file1_fasta_stats.sequences, "sequences")
    file2_fasta_stats.file_stats(file2_fasta_stats.sequences, "sequences")
    # this line does the comparing of unique sequences (will be printed)
    file1_fasta_stats.compare(
        file1_fasta_stats.distseq, file2_fasta_stats.distseq, "sequences")

if __name__ == "__main__":
    main()
