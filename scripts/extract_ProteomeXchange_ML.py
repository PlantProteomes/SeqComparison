# Margaret Li
# 7/19/22
# This program gets information from specified ProteomeXchange websites
# and writes information there to an excel file.

import requests
import pandas as pd

# lists to store info scraped from json
lab_head = []
references = []
pm_ID = []

# read a file with all identifiers from build2 (202206)
ident_file = open(
    'C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\build2_ident.txt', 'r')
lines = ident_file.readlines()
ident_file.close()

# iterate through each identifier and get information
for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
    identifier = lines[i]
    url = f"http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID={identifier}&outputMode=json"
    response_content = requests.get(url)
    if response_content.status_code != 200:
        print("ERROR returned with status "+str(response_content.status_code))
        print(response_content.text())
        exit()
    # all info from json in lists and dicts
    response_dict = response_content.json()

    # helpful checks
    #print(response_dict["contacts"][0]["terms"][0]["value"])
    #print(json.dumps(response_dict, sort_keys=True, indent=2))

    # check if profile has contacts info
    if 'contacts' not in response_dict:
        print("There are no contacts in this PXD")
        #print(f"There are {len(response_dict['contacts'])} contacts in this PXD")

    # check if profile has publications info
    if 'publications' not in response_dict:
        print("There are no publications in this PXD")

    # get lab head
    no_lab_head = True
    for person in response_dict["contacts"]:
        # look into the dictionaries inside person[terms] list
        # and find dict with lad head under name.
        # after found, look into high level list for contact name
        for entry1 in person["terms"]:
            if entry1["name"] == "lab head":
                no_lab_head = False
                for entry2 in person["terms"]:
                    if entry2["name"] == "contact name":
                        name = entry2["value"]
                        lab_head.append(name)
                        
    # write N/A if entry does not contain lab head info
    if no_lab_head:
        lab_head.append("N/A")
        
    # get reference
    no_reference = True
    no_ID = True
    for entry1 in response_dict["publications"]:
        for entry2 in entry1["terms"]:
            if entry2["name"] == "Reference":
                no_reference = False
                reference = entry2["value"]
                references.append(reference)
            if entry2["name"] == "PubMed identifier":
                no_ID = False
                id = entry2["value"]
                pm_ID.append(id)

    # write N/A if entry does not contain publication info
    if no_reference:
        references.append("N/A")
    
    # write N/A if entry does not contain PubMed ID
    if no_ID:
        pm_ID.append("N/A")

# print(len(lab_head))
# print(len(publication))

# create dataframe to store new info
df = pd.DataFrame()
df['Lab Head'] = lab_head
df['Reference'] = references
df['PubMed ID'] = pm_ID

# write information to excel
writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\build2_ProteomeXchange_info_final.xlsx")
# write dataframe to excel
df.to_excel(writer)
writer.save()
print('DataFrame is written successfully to Excel File.')