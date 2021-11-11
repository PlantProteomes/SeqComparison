import argparse
from Bio import SeqIO

'''
very rough draft of argparse. Will update with version from repo-issue

#argparser parsing file names from user input
argparser = argparse.ArgumentParser(description = 'Compare two FASTA files and display stats')
parser.add_argument('file1', help = 'Name of the first file to compare')
parser.add_argument('file2', help = 'Name of the second file to compare')
args = parser.parse_args()
'''


#reads given file, separate identifiers, sequences, and descriptions, and organize
#this information into a dictionary with the list of identifiers being the key and
#the list of sequences being the value
def read (filename):
    matched = {} #stores identifiers and sequences of a file as two lists
    ident = [] #list of identifiers in a file
    seq = [] #list of sequences in a file

    with open(filename) as infile:
        for record in SeqIO.parse(infile, 'fasta'):
            sequence = str(record.seq)
            seq.append(seq) #add sequence to list

            #parse line and separate entry into identifier and description
            match = re.match(r'^(\S+)\s*(.*)$', record.description)

            if match:
                identifier = match.group(1)
                description = match.group(2)
                ident.append(identifier) #add identifier to appropriate list
            else:
                print(f"ERROR: Unable to parse description line: {record.description}")
                exit()
        matched[ident] = seq
    return matched


#takes list of identifiers or sequences and type as parameter.
#it tallies total number of ident/seq, distinct ones, and redundancies
def file_stats (is_list, type):
    total = len(is_list) #total number of entries
    index = {} #stores i/s and their counts
    num_redund = 0 #total redundancies
    num_dist = 0 #distinct i/s
    
    #loops through list and update term and count in dictionary
    for item in is_list:
        if item in index:
            index[item] += 1
        else:
            index[item] = 1

    #loops through dictionary and counts total redundancies/distinct elements
    for element in index:
        if index[element] > 1:
            num_redund += 1
        else:
            num_dist += 1
    print("There is a total of " + str(total) + " " + type + ", " + str(num_redund) + " " + "redundancies, and " + str(num_dist) + " distinct " + type + ".")
 
#will update
def compare (list1, list2, is_id):
    overlap = 0 #counts overlap of identif
    unique = {} #put unique elements in set to avoid overcounting
    overlap_id = {}
    for item in list1:
        if item not in unique:
            unique.add(item)
            if item in list2:
                overlap += 1
                if is_id == True:
                    overlap_id.add(item)
    print ("There are " + str(len(unique) - overlap) + " unique " + type + ".")
    print ("There are " + str(overlap) + " overlapping " + type + ".")
    return overlap_id

#will update
def compare_seq (id1, id2, seq1, seq2, overlap_id):
    index1 = 0
    index2= 0
    overlap = 0
    for item in overlap_id:
        index1 = id1[item, index1]
        index2 = id2[item, index2]
        if seq1[index1] == seq2[index2]:
             overlap += 1
    print ("Of the overlapping identifiers, " + str(overlap) + " have the same sequences.")
        
                    

    