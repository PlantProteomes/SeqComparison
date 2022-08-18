# Margaret Li
# 8/17/22
# descr

import os
import json
import re

if os.path.exists("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                  "\\arabidopsis\\PTMs\\all_pep_amino_counts.txt") == False:

    whole_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                      "\\arabidopsis\\PTMs\\PeptideAtlasInput_concat.PAidentlist.peptidoforms",
                      "r", newline="\n")

    mod_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes"
                    "\\arabidopsis\\PTMs\\all_pep_amino_counts.txt", "w")
    
    amino_counts = {}
    
    while True:
        line = whole_file.readline().strip()
        mod_match = re.search("\[(.*?)\]", line)
        

        for i in range(0, len(line)):
            term = line[i]

            if (term != "[" 
                and term != "]" 
                and term != "-"):

                if term not in amino_counts:
                    amino_counts[term] = 1
                else:
                    amino_counts[term] += 1

        if not line:
            break