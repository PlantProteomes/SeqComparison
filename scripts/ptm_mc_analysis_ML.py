# Margaret Li
# 8/4/22
# This program takes massive ptm file, get all specified entries (ex: ATCG)
# and generates specified stats for them. Some results are sent
# to excel files

import pandas as pd
import os.path

# if specified file no exist, make the file. Else skip to dataframe
if os.path.exists("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\phospho_atmg.txt") == False:
    with open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\protein_PTM_summary_STY_Phospho.txt") as ptm_file:
        lines = ptm_file.readlines()

    at_file = open("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\phospho_atmg.txt", "w")
    at_file.write(lines[0])

    for line in lines:
        split = line.split("\t")
        identifier = split[0]
        if identifier.startswith("PeptideAtlas_ATMG") and identifier.endswith(".1"):
            at_file.write(line)

    at_file.close()
    print("All ATMG entries written to file!")


## Get Statistics ##

# dataframe with only at*g proteins
df = pd.read_csv(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\phospho_atmg.txt", sep="\t")

print("Statistics:")

# get distinct identifiers
distincts = df["protein"].unique()
print(f"Total number of distinct identifiers: {len(distincts)}")
# f = open("atmg_distincts.txt", "w")
# for distinct in distincts:
    # f.write(distinct + "\n")
# f.close()
print("txt file created!")

# get total number of potential sites
total_sites = df.shape[0]
print(f"Total number of potential sites: {total_sites}")

# get total sites with at least 1 observation
df_1p = df[df["nObs"] > 0]
sites_1p = df_1p.shape[0]
print(f"Total sites with at least 1 observation: {sites_1p}")

# select sites with nP99 and above
df_above = df[(df["nP99"] > 0) | (df["nP100"] > 0) | (df["no-choice"] > 0)]
print(f"Sites with nP99 or above: {df_above.shape[0]}")

# select distinct sites with nP99 and above
n_dist_above = len(df_above["protein"].unique())
print(f"Distinct sites with nP99 or above: {n_dist_above}")

# assemble new dataframe for stats on this ptm/at*g
column = [len(distincts), total_sites, sites_1p, df_above.shape[0], n_dist_above]
df_sum = pd.DataFrame()
df_sum["Mitochondria"] = column


## Writing to Excel##

# writer for probability table
writer1 = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\ptm_analysis.xlsx")
df_above.to_excel(writer1, "atmg")
writer1.save()
print('Dataframe is written successfully to Excel File.')

# writer for generating the c or m column for the stats table
writer2 = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\ptm_stats.xlsx")
df_sum.to_excel(writer2, "atmg")
writer2.save()
print('Dataframe is written successfully to Excel File.')