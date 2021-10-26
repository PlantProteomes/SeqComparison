#!/bin/env python3

import re #refers to regular expressions module
from Bio import SeqIO

#variables used for tallying stats
entryCounter = 0
i_dict = {}
s_dict = {}
i_redund = 0
s_redund = 0

#this will open specified file
filename = '../proteomes/maize/original/mitochondrion.2.fasta'
with open(filename) as infile:
    
    print(f"INFO: Reading {filename}")

    #this function updates count of redundant identifiers
    def repeatsI (key, value):
        global i_dict
        global i_redund
        if key in i_dict:
            i_redund += 1
        else:
            i_dict[key] = value

    #this function updates count of redundant sequences
    def repeatsS (key, value):
        global s_dict
        global s_redund
        if key in s_dict:
            s_redund += 1
        else:
            s_dict[key] = value
    
    #parses through records line by line
    for record in SeqIO.parse(infile, 'fasta'):
        sequence = str(record.seq) 
        entryCounter += 1
        
        #this line separates the identifier and the description into 2 groups by the space
        match = re.match(r'^(.+?)\s+(.*)$', record.description) #record is a fasta object
        if match: #if this line can be separated and parsed this way
            identifier = match.group(1) 
            description = match.group(2)

            repeatsI(identifier, sequence)
            repeatsS(sequence, identifier)

        else:
            print(f"ERROR: Unable to parse description line: {record.description}")
            exit()
        print(f"{identifier} - {description}")
    
    #printing out stats collected
    print('')
    print("There is a total of", entryCounter, "entries.")
    print("There are", entryCounter - i_redund, "unique identifiers.")
    print("There are", entryCounter - s_redund, "unique sequences.")
    print("There are", i_redund, "redundant identifiers.")
    print("There are", s_redund, "redundant sequences.")
    
