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
# do the min and max of each column to find the specific numbers for the range
print("Spectra Searched")
print(df['Spectra Searched'].min())
print(df['Spectra Searched'].max())
print("%Spectra ID")
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

#changing from float to string back to float and removing % and , 

fontname = 'Arial'

#Panel 1.1 (log)
plt.subplot(2,2,1)
plt.xscale("log")
#plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["%Spectra ID'd"])
plt.title(f"Spectra Searched vs %Spectra IDed (log)", fontname = fontname)
plt.xlabel('Spectra Searched')
plt.ylabel(' %Spectra IDed')
#plt.grid(True)
plt.xlim(900,  55629272)
plt.ylim(1,75)
#fig, axe = plt.subplots(figsize=(7, 3.5), dpi=300)
#axe.legend(["tanh", "sin"])
#adding text inside the plot
plt.text(1200, 65, 'A', fontsize = 36)
  

#Panel #2.1 (log)
plt.subplot(2,2,3)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["Distinct Peptides"])
# formatting for the graph
plt.title(f"Spectra Searched vs Distinct Peptides (log)", fontname = fontname)
plt.xlabel('Spectra Searched')
plt.ylabel(' Distinct Peptides')
#plt.grid(True)
plt.xlim(900, 55629272)
plt.ylim(10,400000)
plt.text(1100, 110000, 'C', fontsize = 36)

#Panel 3.1 (log)
plt.subplot(2,2,4)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["Distinct Canonical Proteins"])
plt.title(f"Spectra Searched vs Distinct Canonical Proteins (log)", fontname = fontname)
plt.xlabel('Spectra Searched')
plt.ylabel(' Distinct Canonical Proteins')
#plt.grid(True)
plt.xlim(900,55629272)
plt.ylim(1, 25000)
plt.text(1100, 7000, 'D', fontsize = 36)

#Panel 4.1 (log)
plt.subplot(2,2,2)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df['Spectra Searched'], y = df["MS Runs"])
plt.title(f"Spectra Searched vs MS Runs (log)", fontname = fontname)
plt.xlabel('Spectra Searched')
plt.ylabel('MS Runs')
#plt.grid(True)
plt.xlim(970, 60859455)
plt.ylim(1,2000)
plt.text(1200, 700, 'B', fontsize = 36)
plt.show()

#Panel 2!!!!!!!!
#Panel 5.1 (log)
plt.subplot(2,2,1)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df["Spectra ID'd"], y = df["Distinct Peptides"])
plt.title(f"Spectra IDed vs Distinct Peptides (log)", fontname = fontname)
plt.xlabel('Spectra IDed')
plt.ylabel('Distinct Peptides')
plt.xlim(10,20758985)
plt.ylim(1,400000)
plt.text(1.5, 77000, 'A', fontsize = 36)

#Panel 6

plt.subplot(2,2,2)
plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df["Spectra ID'd"], y = df["Distinct Canonical Proteins"])
plt.title(f"Spectra IDed vs Distinct Canonical Proteins (log)", fontname = fontname)
plt.xlabel('Spectra IDed')
plt.ylabel('Distinct Canonical Proteins')
plt.xlim(10,20758985)
plt.ylim(1,25000)
plt.text(1.5, 6500, 'B', fontsize = 36)

#Panel 7.1 (log)
plt.subplot(2,2,3)
#plt.xscale("log")
plt.yscale("log")

plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Peptides'])
plt.title(f"%Spectra IDed vs Distinct Peptides (log)", fontname = fontname)
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Peptides')
#plt.grid(True)
plt.xlim(1,75)
plt.ylim(10,400000)
plt.text(2, 70000, 'C', fontsize = 36)

#Panel 8.1 (log)
plt.subplot(2,2,4)
#plt.xscale("log")
plt.yscale("log")


plt.scatter(x = df["%Spectra ID'd"], y = df['Distinct Canonical Proteins'])

# formatting for the graph
plt.title(f"%Spectra IDed vs Distinct Canonical Proteins (log)", fontname = fontname)
plt.xlabel('%Spectra IDed')
plt.ylabel('Distinct Canonical Proteins')
#plt.grid(True)
plt.xlim(1,75)
plt.ylim(1, 25000)
plt.text(2, 6000, 'D', fontsize = 36)
plt.tight_layout()
plt.show()