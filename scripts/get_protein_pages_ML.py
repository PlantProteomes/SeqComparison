# Margaret Li
# 7/13/22
# Desc

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)

# lists for storing data
statuses = []
n_observations = []
pc_percent = []
n_experiments = []

# parameters
search_page = 'https://db.systemsbiology.net/sbeams/cgi/PeptideAtlas/GetProtein'
build_id = 540

# open file of identifiers
ident_file = open(
    'C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\organellar_ATCG.txt', 'r')
lines = ident_file.readlines()

# iterate through each identifier and get information
for identifier in lines:
    identifier = identifier.strip()

    # construct url for protein profile page
    url = f"{search_page}?atlas_build_id={build_id}&protein_name={identifier}&apply_action=QUERY&SBEAMSentrycode=skdjf7398d"

    # check status code to see if page is accessible
    webpage = requests.get(url)
    if str(webpage) != "<Response [200]>":
        print(
            f"ERROR returned with status {str(webpage)} identifier={identifier} build_id={build_id}")
        exit()

    # find the html page (soup)
    soup = bs(webpage.content, features="html.parser")
    # print(soup)

    ## find relevant info ##

    # find status
    line = soup.find('span', {'class': 'pseudo_link'})
    # print(line)
    status = line.b.text
    # print(line.b.text)
    statuses.append(status)

    # find total observations
    div = soup.find('div', id='getprotein_overview_div')

    for data in div.find_all('tr', class_='hoverable'):
        if "Total Observations" in str(data):
            for td in data.find_all('td', class_='value'):
                # print(td)
                psm = td.b.text
                # print(psm)
    if psm == "":
        n_observations.append("n/a")
    else:
        n_observations.append(psm)

    # find protein coverage
    #span = soup.find_all('span', class_ = 'white_bg')
    pc_texts = soup.findAll('b', {'style': 'color:red;'})
    # print(pc_texts)
    for tag in pc_texts:
        if "%" in tag.text:
            pc = tag.text
    # print(pc)
    pc_percent.append(pc)

    # find number of experiments
    experiments_count = 0
    links = soup.findAll('a')
    for link in links:
        if "/sbeams/cgi/PeptideAtlas/ManageTable.cgi?TABLE_NAME=AT_SAMPLE&sample_id=" in str(link.get('href')):
            experiments_count += 1
            # print(link)
    # print(experiments_count)
    n_experiments.append(experiments_count)

# close file after reading
ident_file.close()

# log information into a dataframe
df = pd.DataFrame()
df['Status'] = statuses
df['Number of PSMs'] = n_observations
df['Sequence Coverage'] = pc_percent
df['Number of Experiments'] = n_experiments
#print(df)

# write to excel
writer = pd.ExcelWriter(
    "C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\organellar_data.xlsx")
# write dataframe to excel
df.to_excel(writer, "chloroplast")
writer.save()
print('DataFrame is written successfully to Excel File.')

'''
Improvements:
- faster?
- read directly from google sheets instead of txt
- write to google sheets instead of to data frame and then excel
'''
