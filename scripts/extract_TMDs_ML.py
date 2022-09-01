# Margaret Li
# 09/01/22
# This program takes mito or plastid uniprot ids and requests
# a json list that contains info about their number of TMDs.
# n_TMDs is counted and exported to an Excel table along with
# the IDs.

import pandas as pd
import requests

# name of the file that has uniprot ids of plastids/mito
id_filename = "plas_uniprot_ids.txt"
# keeps track of number of tmds
n_tmd = []


## Reading file with ids and making an id list ##
# read a file with all identifiers from build2 (202206)
id_file = open(f"C:\\Users\\jli\\OneDrive - Eastside Preparatory School\\"
                "plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\"
                f"{id_filename}", 'r')

# list of all ids
ids = id_file.readlines()
id_file.close()


## Update ids list ##
# iterates thru each id in the list of ids
# and count number of TMDs. 
for id in ids:
    id = id.strip()
    url = (f"https://www.ebi.ac.uk/proteins/api/features?offset=0&size=100"
            f"&accession={id}&types=TRANSMEM")

    response_content = requests.get(url)

    if response_content.status_code != 200:
        print("ERROR returned with status "+str(response_content.status_code))
        print(response_content.text())
        exit()

    # all info from json in lists and dicts
    response_list = response_content.json()

    # update count of TMDs by counting # dictionaries
    # under key features
    count = 0
    if len(response_list) != 0:
        for dict in response_list:
            for entry in dict["features"]:
                count += 1

    n_tmd.append(count)


## Making table and writing to Excel ##
tmd_table = pd.DataFrame()
tmd_table["Uniprot ID"] = ids
tmd_table["# of TMDs"] = n_tmd

# make excel writer
writer = pd.ExcelWriter("C:\\Users\\jli\\OneDrive - Eastside Preparatory"
                        " School\\plantproteomes\\SeqComparison\\proteomes"
                        "\\arabidopsis\\organellar_tmd_counts.xlsx")

# write table to excel
tmd_table.to_excel(writer, "plastid")
writer.save()
print('DataFrame is written successfully to Excel File.')