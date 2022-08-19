# Margaret Li
# 8/2/22
# This program uses two methods to update an excel file with
# publication info and repository name from a designated list 
# of arabidopsis identifiers.

import requests
import pandas as pd

publications = []
repos = []

ident_file = open(
    'C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\check_manual_pub_pxds.txt', 'r')
pxds = ident_file.readlines()
ident_file.close()

for pxd in pxds:
    # check strip()
    pxd = pxd.strip()

    url = f"http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID={pxd}&outputMode=json"
    response_content = requests.get(url)

    if response_content.status_code != 200:
        print("ERROR returned with status "+str(response_content.status_code))
        print(response_content.text())
        exit()

    response_dict = response_content.json()

    # get publication
    for entry1 in response_dict["publications"]:
        for entry2 in entry1["terms"]:
            if (entry2["name"] == "Dataset with its publication pending" or
                entry2["name"] == "no publication" or
                    entry2["name"] == "Dataset with no associated published manuscript"):
                publications.append("Dataset with its publication pending")

            elif entry2["name"] == "Reference":
                publications.append(entry2["value"])

    # get repo info
    repo_names = ["PRIDE", "iProX", "jPOST",
                  "MassIVE", "Panorama", "PeptideAtlas"]
    for entry in response_dict["fullDatasetLinks"]:
        for repo in repo_names:
            if entry["name"].startswith(repo):
                repos.append(repo)

    if pxd == "PXD000444":
        repos.append("PRIDE")

json_updated = pd.DataFrame()
json_updated["Publications"] = publications
json_updated["Repository"] = repos

writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\manual_pub_results.xlsx")
json_updated.to_excel(writer, "json")
writer.save()
print('json_updated is written successfully to Excel File.')


##########################################################
## METHOD 2: check with Figure 1 Data ##
publications_check = []
repos_check = []

fig_1 = pd.read_csv(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\prot_central_all_ara.tsv", sep="\t")
identifiers = list(fig_1["Dataset Identifier"])
fig_publications = list(fig_1["Publication"])
fig_repos = list(fig_1["Repos"])

for pxd in pxds:
    pxd = pxd.strip()
    if pxd in identifiers:
        index = identifiers.index(pxd)
        publications_check.append(fig_publications[index])
        repos_check.append(fig_repos[index])
    else:
        publications_check.append("DNE")
        repos_check.append("DNE")

excel_updated = pd.DataFrame()
excel_updated["Publications"] = publications_check
excel_updated["Repository"] = repos_check

excel_updated.to_excel(writer, "excel")
writer.save()
writer.close()
print('excel_updated is written successfully to Excel File.')