# Margaret Li
# 7/22/22
# This program generates 5 plots (year, instrument, repo, and PTM
# from information from ProteinCentral. Most data is stored in the 
# imported tsv file below. Some information for the PTM graph is
# scraped from protein profiles from ProteomeXChange

import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import os.path
# from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

# read TSV file into pandas DataFrame
df = pd.read_csv("C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\prot_central_all_ara.tsv", sep="\t")

# to store column with only announce years
announce_year = []

# update announce_year
for date in df["Announce Date"]:
    split = date.split("-")
    year = split[0]
    announce_year.append(year)
# list runs from 2012 to 2021
announce_year.reverse()
# update column with announce years
df["Announce Year"] = announce_year


## make keys for each bar graph ##

# distinct entries in panel A
years = df["Announce Year"].unique().tolist()

# distinct entries in panel B
for i in range (0, len(df["Instrument"])):
    if df["Instrument"][i].startswith("instrument model:"):
        split = df["Instrument"][i].split(" ")
        df["Instrument"][i] = split[2].replace(";", "")
    else:
        split = df["Instrument"][i].split(";")
        df["Instrument"][i] = split[0]

instruments = df["Instrument"].unique().tolist()
instruments.remove("instrument")
instruments.remove("instrument model")

# distinct entries in panel for repository
repos = df["Repos"].unique().tolist()


## useful functions ##

# input dataframe, list of possible entries (each logged
# once), and name of respective column into function.
# returns a tally of count of occurences in df column
# for each distinct entry
def tally(categories, df, col_name):
    # list with value at each index corresponding
    # to count of category at the same position in
    # catgories
    length = len(categories)
    tally = [0] * length
    
    # go through entries in a given column
    # add one to tallies list in the right position
    for entry in df[col_name]:
        for i in range(0, len(categories)):
            if entry in categories[i]:
                tally[i] += 1
    return tally

# for adding values in bar charts. x and y
# are the lists for axes of bar chart
def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')


## get tallies for graphs ##

# tally for panel A
years_tally = tally(years, df, "Announce Year")
# tally for panel B
instruments_tally = tally(instruments, df, "Instrument")
# tally for panel repo
repos_tally = tally(repos, df, "Repos")


# make bar graphs for graph A, B, and repo ##

# bar graph for panel A
plt.bar(years, years_tally)
add_labels(years, years_tally)
plt.title("Number of PXDs Over the Years")
plt.xlabel("Announce Year")
plt.ylabel("Number of PXDs")
plt.show()

# graphs for panel B
#fig, ax = plt.subplots()
plt.rc('ytick', labelsize=7)
plt.barh(instruments, instruments_tally)
#bars = ax.barh(instruments, instruments_tally)
#make_axes_area_auto_adjustable(ax)
#add_labels(years, years_tally)
plt.title("PXDs Grouped by Instruments")
plt.xlabel("Number of PXDs")
plt.ylabel("Instrument")
plt.show()

# set plt measurements to normal (so labelsize no longer 7)
plt.rcdefaults()
# graphs for repo panel
plt.bar(repos, repos_tally)
add_labels(repos, repos_tally)
plt.title("Number of PXDs in Each Repository")
plt.xlabel("Repository")
plt.ylabel("Number of PXDs")
plt.show()


#####################################################

## graph for panel D ##

# list of mod terms
mod_terms = ["phosphorylation", "Acetylation", "Ubiquitination", "glycosylation", "Sumoylation", "lipidation"]
# stores tally for panel D
mod_tally = [0] * len(mod_terms)

# put request pages into files and if page exists just read from page
for i in range (0, len(df["Dataset Identifier"])):
    pxd = df["Dataset Identifier"][i]
    if os.path.exists(f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\scripts\\pxd_pages\\zz_{pxd}.json") == False:
        url = f"http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID={pxd}&outputMode=json"
        response_content = requests.get(url)

        # check if page can be reached
        if response_content.status_code != 200:
            print("ERROR returned with status "+str(response_content.status_code))
            print(response_content.text())
            exit()

        # all info from json in lists and dicts
        response_dict = response_content.json()

        # make json object for nice formatting
        json_object = json.dumps(response_dict, indent=4)

        # write to json file
        filename = f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\scripts\\pxd_pages\\zz_{pxd}.json"
        with open(filename, 'w') as outfile:
            outfile.write(json_object)

        print('''INFO: json files created. Please run program again to access
            panel D bar chart.''')

    else:
        # read the dictionary from the json file
        with open(f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\scripts\\pxd_pages\\zz_{pxd}.json") as json_file:
            json_dict = json.load(json_file)

        # check if current term is in title, description, or keywords
        # of the tsv file
        for k in range(0, len(mod_terms)):
            term = mod_terms[k]
            # if tally is found, skip looking at modifications
            if (df["Title"][i].casefold().find(term.casefold()) != -1
                or df["Keywords"][i].casefold().find(term.casefold()) != -1
                or json_dict["description"].casefold().find(term.casefold()) != -1):
                mod_tally[k] += 1
            
            # finally check if term appears in modifications
            else:
                for entry in json_dict["modifications"]:
                    if entry['name'].casefold().find(term.casefold()) != -1:
                        mod_tally[k] += 1

# graph generation
plt.barh(mod_terms, mod_tally)
#add_labels(mod_terms, mod_tally)
plt.title("PXDs Grouped by Post-translational Modifications")
plt.ylabel("Post-translational Modification")
plt.xlabel("Number of PXDs")
plt.show()