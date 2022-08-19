# Margaret Li
# 8/14/22
# This program takes dictionaries of mod counts
# generated from peptides_mod_stats_ML2.py
# and generates percentages in various ways
# (documented in the program) Outputs are exported
# to excel.

import json
import re
import pandas as pd

print("There are 72,197,592 peptides in total.")
print("There are 26,033,386 peptides with modifications.")
print("")

dict_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\peptide_mod_dicts_new.txt", "r")

# read file with dictionaries + load
# them as dictionaries
dict1 = dict_file.readline()
amino_mod_counts = json.loads(dict1)

dict2 = dict_file.readline()
mod_counts =json.loads(dict2)

dict_file.close()

# amino-specified modification (ASMs): modifications that are 
# counted independently based on the amino acid that 
# is modified. Ex: M[Phospho] is counted as a separate
# entry than S[Phospho]
# in contrast, modifications without specified mods will be
# called non-specified modifications (NSMs)


## GENERATING STATS ##
# counting total amino-specified mods
n_amino_spec_mods = sum(list(amino_mod_counts.values()))

# total modified methionines
# Method: n modified M over total ASMs
n_m_mods = 0

# list of mod percentages out of sum of all ASMs
# Method: each ASM over sum of total ASMs
amino_spec_percentages = {}

# dictionary where key = NSM and value = {amino acid : modified count}
# stores distribution of mods over different amino acids
non_spec_distribution= {}

for asm in amino_mod_counts:
    print(asm)
    print(amino_mod_counts[asm] * 100 / n_amino_spec_mods)
    # get each ASM percentage
    percentage = "{:.2f}".format(amino_mod_counts[asm] * 100 / n_amino_spec_mods)
    percentage = str(percentage) + "%"
    amino_spec_percentages[asm] = percentage

    # counting total modified methionines
    if asm[0] == "M":
        n_m_mods += amino_mod_counts[asm]
    

    # get mod distribution by amino acids

    # get mod category from asm
    mod_name = re.findall("\[(.*?)\]", asm)[0]

    if mod_name not in mod_counts:    
        print(f"{mod_name} not in mod_counts")
        
    dist_percentage = "{:.2f}".format(amino_mod_counts[asm] * 100 / mod_counts[mod_name])
    dist_percentage = str(dist_percentage) + "%"

    if mod_name not in non_spec_distribution:
        dist_list = []
        non_spec_distribution[mod_name] = dist_list


    if asm[0] == "[":
        non_spec_distribution[mod_name].append({"n-terminus" : dist_percentage})
    else:
        non_spec_distribution[mod_name].append({asm : dist_percentage})
       

# counting total non_amino_specified mods
n_non_spec_mods = sum(list(mod_counts.values()))

# dictionary of mod percentages out of sum of all ASMs
non_spec_percentages = {}

for nsm in mod_counts:
    # get each NSM percentage
    percentage = "{:.2f}".format(mod_counts[nsm] * 100 / n_non_spec_mods)
    percentage = str(percentage) + "%"
    non_spec_percentages[nsm] = percentage


## OUTPUT STATS ##
print(f"Total number of modified methionines:")
print(f"Total modified methionines: {n_m_mods}")
M_percentage = "{:.2f}".format(n_m_mods * 100 / n_amino_spec_mods)
print(f"Percentage of modified methionines: {M_percentage}%")

print("")
print(f"Percentages of ASMs over total # ASMs:")
print(amino_spec_percentages)

print("")
print(f"Percentages of NSMs over total # NSMs:")
print(non_spec_percentages)

print("")
print(f"Distribution of modification by amino acid:")
print(non_spec_distribution)


## MAKING TABLES ##
pep_mod_writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\mod_stats_table.xlsx")
residue_table= pd.DataFrame(list(amino_spec_percentages.items()), columns = ['Residue Modification','Percentage'])
col_mods = [0] * 19
col_mods.extend(list(mod_counts.keys()))
residue_table["Modification"] = col_mods


mod_table = pd.DataFrame(list(non_spec_percentages.items()), columns = ['Modification','Percentage'])
residue_table.to_excel(pep_mod_writer, "residue")
mod_table.to_excel(pep_mod_writer, "non-residue")


# get info embedded in distribution dictionary
asm_col = []
asm_percentages = []
dist_table = pd.DataFrame()
# look into a mod category
for category in non_spec_distribution:
    # look into the list of distributions
    for mod_dict in non_spec_distribution[category]:
        # look into a dict in the list
        for key in mod_dict:
            asm_col.append(key)
            asm_percentages.append(mod_dict[key])
dist_table["Residue Modification"] = asm_col
dist_table["Percentage"] = asm_percentages
dist_table.to_excel(pep_mod_writer, "modification type distribution")


# table used to store raw numbers from dictionaries
raw_num_asm = pd.DataFrame()
raw_num_asm["res mod"] = amino_mod_counts.keys()
raw_num_asm["raw numbers"] = amino_mod_counts.values()
raw_num_asm.to_excel(pep_mod_writer, "raw numbers res")

raw_num_nsm = pd.DataFrame()
raw_num_nsm["mod cat"] = mod_counts.keys()
raw_num_nsm["raw numbers"] = mod_counts.values()
raw_num_nsm.to_excel(pep_mod_writer, "raw numbers")
pep_mod_writer.save()