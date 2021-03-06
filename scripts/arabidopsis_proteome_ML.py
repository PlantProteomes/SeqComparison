# Margaret Li
# 03/27/22
# This program creates a new arabidopsis proteome by combining elements
# from two files (araport11.fasta and tair10.fasta) and deleting 
# some features. The two files are unchanged.

import re
from Bio import SeqIO

class refined_ara_proteome:

    def __init__(self):
        # used to store data for a fasta file
        # form: info[identifier] = [seq, desc, base, number, symbols(added later)]
        self.info = {}

    # reads given file, separate identifiers and sequences and store
    # this info into an object
    def read(self, filename):
        print("INFO: Reading " + filename)
        with open(filename) as infile:

            for record in SeqIO.parse(infile, 'fasta'):
                # parse line and separate entry into identifier and description
                match = re.match(r'^(\S+)\s*(.*)$', record.description)

                # if identifiers are parseable store appropriate values. Else print error statement
                if match:
                    identifier = match.group(1)
                    description = match.group(2)
                    sequence = str(record.seq)

                    # store value associated with identifier. this number
                    # appears after '.' in the identifier
                    split_ident = identifier.split(".")
                    base = split_ident[0]
                    number = split_ident[1]

                    # store sequence descri and number as a list and
                    # store as value for ident base key
                    info_parts = []
                    info_parts.append(sequence)
                    info_parts.append(description)
                    info_parts.append(base)
                    info_parts.append(number)

                    # symbols added later
                    self.info[identifier] = info_parts
                else:
                    print(
                        f"ERROR: Unable to parse description line: {record.description}")
                    exit()


    # makes three types of deletions from the araport11.fasta file
    def deletions(self, primaries, atmg_list, atcg_list):
        # stores keys of big dictionary so deletions
        # can be made to the big dictionary during
        # iteration of this one
        ident_list = list(self.info.keys())
        # for debugging purposes
        atmg_count = 0
        atcg_count = 0
        primaries_count = 0

        # iterate over the big dictionary and delete terms
        for identifier in ident_list:
            # get base of identifier (part before suffix .n)
            base = self.info[identifier][2]
            # identify first 4 letters of base
            first = base[0:4]    

            # delete ATMG entries that are not found in 
            # a keep list with only ATMG entries
            if first == "ATMG" and base not in atmg_list: 
                self.info.pop(identifier)
                #print("DEBUG: deleted gene " + identifier)
                atmg_count += 1

            # delete ATCG entries that are not found in a 
            # keep list with only ATCG entries
            elif first == "ATCG" and base not in atcg_list:
                self.info.pop(identifier)
                #print("DEBUG: deleted gene " + identifier)
                atcg_count += 1

            # delete entries where xxxx.n where n>1 have the same
            # sequence with their xxxx.1 entry
            elif base in primaries and primaries[base] == self.info[identifier][0]:
                if self.info[identifier][3] != "1":
                    self.info.pop(identifier)
                    print("DEBUG: deleted gene " + identifier)
                    primaries_count += 1

        print("DEBUG: deleted atmg: " + str(atmg_count))
        print("DEBUG: deleted atcg: " + str(atcg_count))
        print("DEBUG: deleted xxxx.n entries: " + str(primaries_count))


    # read two text files that contain info the refined proteome
    # must keep. read info into two lists and return. Will be used
    # for deletions()
    def read_keep_files(self):
        atmg_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\scripts\\proteome_atmg.txt", "r")
        atmg_list = atmg_file.readlines()
        atcg_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\scripts\\proteome_atcg.txt", "r")
        atcg_list = atcg_file.readlines()

        # atcg entries come with suffixes. remove suffixes and "/n"
        for i in range(len(atcg_list)):
            atcg_list[i] = atcg_list[i].replace(".1", "")
            atcg_list[i] = atcg_list[i].rstrip()
        
        # atmg comes with "/n". remove them
        for i in range(len(atmg_list)):
            atmg_list[i] = atmg_list[i].rstrip()

        return (atmg_list, atcg_list)

    # find primaries (identifiers with ".1" suffix)
    # and put them in dict with identifier base as key
    # and corresponding sequence as value. return dictionary.
    # dictionary will be used in deletions()
    def find_primaries(self):
        # dictionary that stores primaries
        primaries = {}

        # iterate over big dictionary of all ident, seq, and desc and
        # put all elements with identifier xxxx.1 into primaries
        # with ".1" stripped from the string
        for identifier in self.info:
            if self.info[identifier][3] == "1":
                # primares[base] = sequence
                primaries[self.info[identifier][2]] = self.info[identifier][0]
        return primaries


    # compare araport entries with tair entires. modify
    # descriptions of new proteome
    def compare_tair(self, tair_dict):
        for a_ident in self.info:
            t_ident = "TAIR10_" + self.info[a_ident][2] + ".1"
            # new proteome ident found in tair file, add gene symbol
            # from tair file to new proteome
            if t_ident in tair_dict:
                split_desc = tair_dict[t_ident][1].split('|')
                symbols = split_desc[1]
                self.info[a_ident].append(symbols)
            else:
                self.info[a_ident].append(" Symbols:  ")
         

    # format the new proteome file
    def make_file(self):
        # this open a new text file
        out_file = open("refined_arabidopsis.fasta", "w")
        for identifier in self.info:
            # lay out data that would be included in new file
            sequence = self.info[identifier][0]
            description = self.info[identifier][1]
            symbols = self.info[identifier][4]
            
            # form of entry
            entry = ">" + identifier + "|" + symbols + description

            # write entry into txt file
            out_file.write(entry + "\n")
            # write corresponding sequence
            out_file.write(sequence + "\n")

##########################################################################


def main():
    araport_filename = "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\Araport11.fasta"
    refined = refined_ara_proteome()

    # read main file and store information in a dictionary
    refined.read(araport_filename)

    # make deletions
    primaries = refined.find_primaries()
    print("Number of xxxxx.1 identifiers: " + str(len(primaries)))
    keep_lists = refined.read_keep_files()

    # make deletions to info in the main files. Changes
    # appear in new file. original file is untouched
    refined.deletions(primaries, keep_lists[0], keep_lists[1])

    # read tair file and make changes based on araport comparison
    # to tair file
    tair_filename = "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\TAIR10.fasta"
    tair = refined_ara_proteome()
    tair.read(tair_filename)
    refined.compare_tair(tair.info)
    
    # write things to new file and open this file
    refined.make_file()

    print("INFO: Done. New arabidopsis proteome created!")


if __name__ == "__main__":
    main()
