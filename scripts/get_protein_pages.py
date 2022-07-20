#!/bin/env python3

import os
import sys
import re
import requests

endpoint = 'https://db.systemsbiology.net/sbeams/cgi/PeptideAtlas/GetProtein'
build_id = 510

identifier = 'ATCG00130.1'

filename = f"zz_{identifier}.html"

if not os.path.exists(filename):
    url = f"{endpoint}?atlas_build_id={build_id}&protein_name={identifier}&apply_action=QUERY"

    response_content = requests.get(url)

    status_code = response_content.status_code
    if status_code != 200:
        print("ERROR returned with status "+str(status_code))
        print(response_content)
        exit()

    with open(filename, 'w') as outfile:
        outfile.write(response_content.text)

    #for line in response_content.text.split("\n"):

with open(filename) as infile:
    for line in infile:
        if 'Identification Status' in line:
            print(line)
        if 'Total Observations' in line:
            print(line)
        if 'Coverage' in line:
            print(line)
