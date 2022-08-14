# Margaret Li
# 8/4/22
# this program generates stats for acetyl PTM and 
# specifically separate results based on PTM residue

import pandas as pd
import os.path

root_file = "protein_PTM_summary_nK_Acetyl"
df_summary_n = pd.DataFrame()
df_summary_K = pd.DataFrame()
analysis_writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\ptm_analysis.xlsx")
summary_writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\ptm_stats.xlsx")

# get statistics on a ptm file for atcg, atmg, and nuclear
for i in range(0, 3):
    # establish what data we are looking for, atcg, atmg, or nuclear
    if i == 0:
        data_type = "atcg"
        col_name = "Chloroplasts"
    elif i == 1:
        data_type = "atmg"
        col_name = "Mitochondria"
    elif i == 2:
        data_type = "nuclear"
        col_name = "Nuclear"

    # if specified file no exist, make the file. Else skip to dataframe
    if os.path.exists(f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\acetyl_{data_type}.txt") == False:
        with open(f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\{root_file}.txt") as ptm_file:
            lines = ptm_file.readlines()

        at_file = open(
            f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\acetyl_{data_type}.txt", "w")
        at_file.write(lines[0])

        if data_type == "nuclear":
            for line in lines:
                split = line.split("\t")
                identifier = split[0]
                if (identifier.startswith("AT1G") or
                    identifier.startswith("AT2G") or
                    identifier.startswith("AT3G") or
                    identifier.startswith("AT4G") or
                        identifier.startswith("AT5G")):
                    if identifier.endswith(".1"):
                        at_file.write(line)

        if data_type == "atcg" or data_type == "atmg":
            for line in lines:
                split = line.split("\t")
                identifier = split[0]
                if (identifier.startswith(data_type.upper()) and
                        identifier.endswith(".1")):
                    at_file.write(line)

        at_file.close()
        print("Entries written to file!")

    ## Get Statistics ##

    # dataframe with only at*g proteins
    df = pd.read_csv(
        f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\PTMs\\acetyl_{data_type}.txt",
        sep="\t", index_col=False)

    print(f"{data_type} statistics:")

    residues = ["n", "K"]
    # for table in res_tables:
    for residue in residues:
        table = df[df["residue"] == residue]

        # get distinct identifiers
        distincts = table["protein"].unique()
        print(f"Total number of distinct identifiers: {len(distincts)}")

        # get total number of potential sites
        total_sites = table.shape[0]
        print(f"Total number of potential sites: {total_sites}")

        # get total sites with at least 1 observation
        df_1p = table[table["nObs"] > 0]
        sites_1p = df_1p.shape[0]
        print(f"Total sites with at least 1 observation: {sites_1p}")

        # select sites with nP99 and above
        df_above = table[(table["nP99"] > 0) | (
            table["nP100"] > 0) | (table["no-choice"] > 0)]
        #df_above = df_above.reset_index(drop = True)
        print(f"Sites with nP99 or above: {df_above.shape[0]}")

        # select distinct sites with nP99 and above
        n_dist_above = len(df_above["protein"].unique())
        print(f"Distinct sites with nP99 or above: {n_dist_above}")

        # total sum of confident psms
        n_psms = table["nP99"].sum() + table["nP100"].sum() + table["no-choice"].sum()
        print(f"Total PSMs for sites with nP99 or above: {n_psms}")

        # assemble new dataframe for stats on this ptm/at*g
        column = [len(distincts), total_sites, sites_1p,
                  df_above.shape[0], n_dist_above, n_psms]

        if residue == "n":
            df_summary_n[col_name] = column
        else:
            df_summary_K[col_name] = column

        # writer for probability table
        df_above.to_excel(analysis_writer, data_type + "_" + residue)
        analysis_writer.save()
        print(f'{data_type} dataframe is written successfully to Excel File.')
        print("")

# write stats summary to excel
df_summary_n.to_excel(summary_writer, "residue n")
df_summary_K.to_excel(summary_writer, "residue K")
summary_writer.save()
print('Summary dataframes are written successfully to Excel File.')