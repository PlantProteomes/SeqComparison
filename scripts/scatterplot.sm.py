# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read TSV file (from Github) into pandas DataFrame
url = "https://raw.githubusercontent.com/PlantProteomes/SeqComparison/main/scripts/build2.tsv"
df = pd.read_csv(url, sep="\t")
#df.keys()

df = df.replace(',','', regex=True)
df = df.replace(' %','', regex=True)

#change all columns to int
df['Spectra Searched'] = df['Spectra Searched'].astype(float)
df["Spectra ID'd"] = df["Spectra ID'd"].astype(float)
df['Distinct Peptides'] = df['Distinct Peptides'].astype(float)
df['MS Runs'] = df['MS Runs'].astype(float)
df['Added Canonical Proteins'] = df['Added Canonical Proteins'].astype(float)

#changing from float to string back to float and removing % and , 
spectra_searched = df['Spectra Searched']
spectra_ID = df["%Spectra ID'd"]

'''

for i in range(0, len(spectra_ID)):
  entry = str(spectra_ID[i])
  entry = entry.replace(" %", "")
  spectra_ID[i] = float(entry)

for i in range(0, len(spectra_searched)):
  entry = str(spectra_searched[i])
  entry = entry.replace(",", "")
  spectra_searched[i] = int(entry)

'''

# do the min and max of each column to find the specific numbers for the range
print("Spectra Searched")
print(df['Spectra Searched'].min())
print(df['Spectra Searched'].max())
print("Spectra ID")
print(df["%Spectra ID'd"].min())
print(df["%Spectra ID'd"].max())
print("Distinct Peptide")
print(df["Distinct Peptides"].min())
print(df["Distinct Peptides"].max())
print("MS Runs")
print(df["MS Runs"].min())
print(df["MS Runs"].max())
print("Added Canonical")
print(df['Added Canonical Proteins'].min())
print(df['Added Canonical Proteins'].max())

  
#panel 1 
# parameters for the graph

plt.scatter(x = spectra_searched, y = spectra_ID)

# formatting for the graph
plt.title(f"Spectra Searched vs % Spectra IDed")
plt.xlabel('spectra searched')
plt.ylabel(' % spectra IDed')
plt.grid(True)
plt.xlim(900, 60859455)
plt.ylim(0,15)
plt.show()

#Panel 1.5 (log)
#y
#data = [' % spectra IDed']
# convert y-axis to Logarithmic scale
#plt.yscale("log")
#plt.plot(data)
 
#convert x/y-axis to Logarithmic scale
plt.xscale("log")
#plt.yscale("log")

plt.scatter(x = spectra_searched, y = spectra_ID)
plt.title(f"Spectra Searched vs % Spectra IDed")
plt.xlabel('spectra searched')
plt.ylabel(' % spectra IDed')
#plt.grid(True)
plt.xlim(900, 60859455)
plt.ylim(0,15)
plt.show()
exit()
#Panel 2

distinct_peptides = df["Distinct Peptides"]
plt.scatter(x = spectra_searched, y = distinct_peptides)

# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Peptides")
plt.xlabel('spectra searched')
plt.ylabel(' Distinct Peptides')
plt.grid(True)
plt.xlim(950, 60859455)
plt.ylim(10,400000)
plt.show()

#Panel 3

spectra_searched = df['Spectra Searched']
added_canonical_proteins = df["Added Canonical Proteins"]
plt.scatter(x = spectra_searched, y = added_canonical_proteins)

# formatting for the graph
plt.title(f"spectra searched vs Added Canonical Protiens")
plt.xlabel('spectra searched')
plt.ylabel(' Added Canonical Protiens')
plt.grid(True)
plt.xlim(970, 60859455)
plt.ylim(0, 5000)

plt.show()
#Panel 4

spectra_searched = df['Spectra Searched']
MS_Runs = df["MS Runs"]
plt.scatter(x = spectra_searched, y = MS_Runs)


# formatting for the graph
plt.title(f"Spectra Searched vs MS Runs")
plt.xlabel('spectra searched')
plt.ylabel('MS Runs')
plt.grid(True)

plt.xlim(970, 60859455)
plt.ylim(0,2000)
plt.show()

#Panel 5

Distinct_Peptides = df['Distinct Peptides']
spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x =spectra_IDed, y = Distinct_Peptides)

# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Peptides")
plt.xlabel('spectra IDed')
plt.ylabel('Distinct Peptides')
plt.grid(True)
plt.xlim(0,15)
plt.ylim(0,400000)

plt.show()
#Panel 6

Added_Canonical_Proteins = df['Added Canonical Proteins']
spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x = spectra_searched, y = MS_Runs)

# formatting for the graph
plt.title(f"Added Canonical Proteins vs Specta IDed")
plt.xlabel('Added Canonical Proteins')
plt.ylabel('Spectra IDed')
plt.grid(True)
plt.xlim(970,60859455)
plt.ylim(0,15)



plt.tight_layout()
plt.show()