# Sagunya and Margaret
# 8/11/22
# descr

import matplotlib.pyplot as plt
import json

dict_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\peptide_mod_dicts.txt", "r")

# read file with dictionaries
dict1 = dict_file.readline()
amino_mod_counts = json.loads(dict1)
plt.barh(list(amino_mod_counts.keys()), list(amino_mod_counts.values()))
plt.show()

dict2 = dict_file.readline()
mod_counts =json.loads(dict2)
plt.barh(list(mod_counts.keys()), list(mod_counts.values()))
plt.show()

# general graph stuff:
# add title and labels
# perhaps shrink the font a little on the mods
## put numbers at the end of the table
#
# for EACH dict:
# calculate the percentages of counts and store as list (26033386 is the denom)
# make a two-column table with number and percentages
## set the row indices as the modifications
# put the lists/dicts in a pandas dataframe
# export the dataframe to excel