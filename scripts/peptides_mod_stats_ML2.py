# Margaret Li
# 8/10/22
# descr

import re
import os
import json

# There are 72197592 lines in the original file
# There are 26033386 lines with modifications.

# check if modified file exists. If doesn't,
# make the file by locating all lines with brackets in them
if os.path.exists("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                  "\\arabidopsis\\PTMs\\modified_peptides.peptidoforms") == False:

    whole_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                      "\\arabidopsis\\PTMs\\PeptideAtlasInput_concat.PAidentlist.peptidoforms",
                      "r", newline="\n")

    mod_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                    "\\arabidopsis\\PTMs\\modified_peptides.peptidoforms", "w")

    while True:
        line = whole_file.readline()
        if "[" in line:
            mod_file.write(line)

        if not line:
            break

    whole_file.close()
    mod_file.close()


# initialize dictionaries that store mod info
# open updated file
mod_counts = {}
amino_mod_counts = {}

mod_file = open(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\modified_peptides.peptidoforms", "r")
# updating the two dictionaries with info from file
counter = 0
while True:
    line = mod_file.readline().strip()
    
    if not line:
        break

    counter += 1
    if line != "":
        #print("")
        #print(f"DEBUG: {line}")

        # find all matches inside [] with letter before
        # ie M[oxidation] is a match
        matches = re.findall(r'([A-Za-z]\[.+?\])', line)

        # get the n-terminus mod if the line has one
        if line[0] == "[":
            start = 0
            end = line.find("]")
            n_term_mod = line[start: end + 1]
            #print(f"SPECIAL: n-term {n_term_mod}")
            matches.append(n_term_mod)
        
        #print(f"DEBUG: all matches {matches}")
        
        # update count with residue mod and count for
        # just mod categories
        for amino_mod in matches:
            # get all instances of mods in line
            mod_match = re.search("\[(.*?)\]", amino_mod)
            # get mod category from inside a residue mod
            mod_cat = mod_match.group(1)
            #print(f"DEBUG: cat {mod_cat}")

            ## counting mods without amino ##
            if mod_cat in mod_counts:
                mod_counts[mod_cat] += 1
            else:
                mod_counts[mod_cat] = 1

            ## counting residue mods ##
            if amino_mod in amino_mod_counts:
                amino_mod_counts[amino_mod] += 1
            else:
                amino_mod_counts[amino_mod] = 1

print(f"DEBUG: counter {counter}")

dict_file = open(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\peptide_mod_dicts_new.txt", "w")
dict_file.write(json.dumps(amino_mod_counts))
dict_file.write(json.dumps(mod_counts))
print("Dictionaries successfully written to file.")

'''
questions:
- where does the blank line come from?
Blank line.
26033387
Dictionaries successfully written to file.

sorting things alphanumerically
put numbers at the end of the bars
get the percentages for each. perhaps a table

same for the second graph

how many with any modification
how many with no modification
include in description

vertical two panel plot with the graphs A, B in word doc page

build 2 directory
2 column table

common denom will be the pep with any modifications
'''
