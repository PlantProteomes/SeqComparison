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
df["%Spectra ID'd"] = df["%Spectra ID'd"].astype(float)
df['Distinct Peptides'] = df['Distinct Peptides'].astype(float)
df['MS Runs'] = df['MS Runs'].astype(float)
df['Distinct Canonical Proteins'] = df['Distinct Canonical Proteins'].astype(float)
df["Spectra ID'd"] = df["Spectra ID'd"].astype(float)

#changing from float to string back to float and removing % and , 


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
print("Distinct Canonical")
print(df['Distinct Canonical Proteins'].min())
print(df['Distinct Canonical Proteins'].max())
print("Spectra ID'd")
print(df["Spectra ID'd"].min())
print(df["Spectra ID'd"].max())

  '''

'''
#panel 1 (linear)
# parameters for the graph
#spectra_searched = df['Spectra Searched']
#spectra_ID = df["%Spectra ID'd"]
plt.subplot(2,2,1)
plt.scatter(x = df['Spectra Searched'], y = df["%Spectra ID'd"])



# formatting for the graph
plt.title(f"Spectra Searched vs %Spectra IDed")
plt.xlabel('Spectra Searched')
plt.ylabel('%Spectra IDed')
plt.grid(True)
plt.xlim(900, 55629272)
plt.ylim(1,75)

'''
#Panel 1.1 (log)
plt.subplot(2,2,1)
plt.xscale("log")
#plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["%Spectra ID'd"])
plt.title(f"Spectra Searched vs %Spectra IDed (log)")
plt.xlabel('Spectra Searched')
plt.ylabel(' %Spectra IDed')
#plt.grid(True)
plt.xlim(900,  55629272)
plt.ylim(1,75)


#Panel 2
'''
plt.subplot(2,2,1)
#distinct_peptides = df["Distinct Peptides"]
plt.scatter(x = df['Spectra Searched'], y = df["Distinct Peptides"])

# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Peptides")
plt.xlabel('Spectra Searched')
plt.ylabel(' Distinct Peptides')
plt.grid(True)
plt.xlim(900,55629272)
plt.ylim(10,400000)
'''
#Panel #2.1 (log)
plt.subplot(2,2,2)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["Distinct Peptides"])
# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Peptides (log)")
plt.xlabel('Spectra Searched')
plt.ylabel(' Distinct Peptides')
#plt.grid(True)
plt.xlim(900, 55629272)
plt.ylim(10,400000)

'''
#Panel 3
plt.subplot(2,2,1)
#spectra_searched = df['Spectra Searched']
#distinct_canonical_proteins = df["Distinct Canonical Proteins"]
plt.scatter(x = df['Spectra Searched'], y = df["Distinct Canonical Proteins"])

# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Canonical Proteins")
plt.xlabel('Spectra Searched')
plt.ylabel('Distinct Canonical Proteins')
plt.grid(True)
plt.xlim(900,55629272)
plt.ylim(1,25000)
'''
#Panel 3.1 (log)
plt.subplot(2,2,3)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["Distinct Canonical Proteins"])
plt.title(f"Spectra Searched vs Distinct Canonical Proteins (log)")
plt.xlabel('Spectra Searched')
plt.ylabel(' Distinct Canonical Proteins')
#plt.grid(True)
plt.xlim(900,55629272)
plt.ylim(1, 25000)

'''
#Panel 4
plt.subplot(2,2,1)
#spectra_searched = df['Spectra Searched']
#MS_Runs = df["MS Runs"]
plt.scatter(x = df['Spectra Searched'], y = df["MS Runs"])


# formatting for the graph
plt.title(f"Spectra Searched vs MS Runs")
plt.xlabel('Spectra Searched')
plt.ylabel('MS Runs')
plt.grid(True)

plt.xlim(900,55629272)
plt.ylim(1,2000)
'''
#Panel 4.1 (log)
plt.subplot(2,2,4)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["MS Runs"])
plt.title(f"Spectra Searched vs MS Runs (log)")
plt.xlabel('Spectra Searched')
plt.ylabel('MS Runs')
#plt.grid(True)
plt.xlim(970, 60859455)
plt.ylim(1,2000)

plt.show()

'''
#Panel 5

plt.subplot(2,2,1)
#spectra_searched = df["Spectra ID'd"]
#MS_Runs = df["Distinct Peptides"]
plt.scatter(x = df["Spectra ID'd"], y = df["Distinct Peptides"])


# formatting for the graph
plt.title(f"Spectra IDed vs Distinct Peptides")
plt.xlabel('Spectra IDed')
plt.ylabel('Distinct Peptides')
plt.grid(True)

plt.xlim(1,20758985)
plt.ylim(1,400000)
'''
#Panel 5.1 (log)
plt.subplot(2,2,1)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df["Spectra ID'd"], y = df["Distinct Peptides"])
plt.title(f"Spectra IDed vs Distinct Peptides (log)")
plt.xlabel('Spectra IDed')
plt.ylabel('Distinct Peptides')
plt.xlim(1,20758985)
plt.ylim(1,400000)

#Panel 6
'''
plt.subplot(2,2,1)
#Distinct_Peptides = df['Distinct Peptides']
#spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Peptides'])

# formatting for the graph
plt.title(f"%Spectra IDed vs Distinct Peptides")
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Peptides')
plt.grid(True)
plt.xlim(1,75)
plt.ylim(10,400000)
'''
#Panel 6.1 (log)
plt.subplot(2,2,2)
#plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Peptides'])
plt.title(f"%Spectra IDed vs Distinct Peptides (log)")
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Peptides')
#plt.grid(True)
plt.xlim(1,75)
plt.ylim(1,400000)

'''
#Panel 7
plt.subplot(2,2,1)
#Distinct_Canonical_Proteins = df['Distinct Canonical Proteins']
#spectra_IDed = df["%Spectra ID'd"]
plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Canonical Proteins'])

# formatting for the graph
plt.title(f"%Spectra IDed vs Distinct Canonical Proteins")
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Canonical Proteins')
plt.grid(True)
plt.xlim(1,75)
plt.ylim(1,25000)
''' 
#Panel 7.1 (log)
plt.subplot(2,2,3)
#plt.xscale("log")
plt.yscale("log")


plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Canonical Proteins'])

# formatting for the graph
plt.title(f"%Spectra IDed vs Distinct Canonical Proteins (log)")
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Canonical Proteins')
#plt.grid(True)
plt.xlim(1,75)
plt.ylim(1, 25000)

plt.tight_layout()
plt.show()