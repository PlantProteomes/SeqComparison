# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read TSV file (from Github) into pandas DataFrame
url = "https://raw.githubusercontent.com/PlantProteomes/SeqComparison/main/proteomes/arabidopsis/build2_data_contribution.tsv"
df = pd.read_csv(url, sep="\t")
df.keys()

#changing from float to string back to float and removing % and , 
spectra_searched = df['Spectra Searched']
spectra_ID = df["%Spectra ID'd"]


for i in range(0, len(spectra_ID)):
  entry = str(spectra_ID[i])
  entry = entry.replace(" %", "")
  spectra_ID[i] = float(entry)

for i in range(0, len(spectra_searched)):
  entry = str(spectra_searched[i])
  entry = entry.replace(",", "")
  spectra_searched[i] = int(entry)
  

#panel 1 
# parameters for the graph

#plt.xlim(0, 5)
#plt.ylim(0,70)

plt.scatter(x = spectra_searched, y = spectra_ID)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('spectra searched')
plt.ylabel(' % spectra IDed')
plt.grid(True)
#density=False
#facecolor='b'
#alpha=0

plt.show()

#Panel 2
spectra_searched = df['Spectra Searched']
distinct_peptides = df["Distinct Peptides"]
plt.scatter(x = spectra_searched, y = distinct_peptides)

#plt.xlim(0, 5)
#plt.ylim(0,70)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('spectra searched')
plt.ylabel(' Distinct Peptides')
plt.grid(True)
#density=False
#facecolor='b'
#alpha=0

plt.show()

#Panel 3
spectra_searched = df['Spectra Searched']
added_canonical_proteins = df["Added Canonical Proteins"]
plt.scatter(x = spectra_searched, y = added_canonical_proteins)

#plt.xlim(0, 5)
#plt.ylim(0,70)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('spectra searched')
plt.ylabel(' Added Canonical Protiens')
plt.grid(True)
#density=False
#facecolor='b'
#alpha=0

plt.show()

#Panel 4
spectra_searched = df['Spectra Searched']
MS_Runs = df["MS Runs"]
plt.scatter(x = spectra_searched, y = MS_Runs)

#plt.xlim(0, 5)
#plt.ylim(0,70)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('spectra searched')
plt.ylabel('MS Runs')
plt.grid(True)
#density=False
#facecolor='b'
#alpha=0

plt.show()


#Panel 5
Distinct_Peptides = df['Distinct Peptides']
spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x =spectra_IDed, y = Distinct_Peptides)

#plt.xlim(0, 5)
#plt.ylim(0,70)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('spectra IDed')
plt.ylabel('Distinct Peptides')
plt.grid(True)
#density=False
#acecolor='b'
#alpha=0

plt.show()

#Panel 6
Added_Canonical_Proteins = df['Added Canonical Proteins']
spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x = spectra_searched, y = MS_Runs)

#plt.xlim(0, 5)
#plt.ylim(0,70)

# formatting for the graph
plt.title(f"searched vs % IDed")
plt.xlabel('Added Canonical Proteins')
plt.ylabel('Spectra IDed')
plt.grid(True)
#density=False
#facecolor='b'
#alpha=0

plt.show()