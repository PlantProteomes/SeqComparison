# Margaret Li
# 7/9/22
# This file reads an updated arabidopsis file, finds all sequences
# with identifiers that start with "PeptideAtlas_"
# and write these entries to a new file called "PeptideAtlasNonNuclear.peff"
import re
from Bio import SeqIO

print("Parsing filename")
filename = "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\Arabidopsis_2021-04_newRNA-PEFF.fasta"

# dictionary used to store info from file
# key = ident and value = seq
database = {}

## PARSE FILE AND UPDATE DICT ##
with open(filename) as infile:
    for record in SeqIO.parse(infile, 'fasta'):
        sequence = str(record.seq)

        # parse line and separate entry into identifier and description
        match = re.match(r'^(\S+)\s*(.*)$', record.description)

        if match:
            identifier = match.group(1)
            if identifier.startswith("PeptideAtlas_"):
                database[">" + record.description] = sequence

        else:
            print(
                f"ERROR: Unable to parse description line: {record.description}")
            exit()


## DEBUG ##
# print(len(database))
# print(database)


## WRITE TO NEW FILE ##
out_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PeptideAtlasNonNuclear.peff", "w")

for entry in database:
    out_file.write(entry + "\n") 
    out_file.write(database[entry] + "\n")

out_file.close()




        