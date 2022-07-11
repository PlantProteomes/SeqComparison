# name
# date
# project description

# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read TSV file (from Github) into pandas DataFrame
url = "https://raw.githubusercontent.com/PlantProteomes/SeqComparison/main/proteomes/arabidopsis/ExpressionMetrics-AllGenes.tsv"
df = pd.read_csv(url, sep="\t")

# specify right part of data
canonical_proteins = df[df['Category']=='Canonical']
not_observed = df[df['Category']=='Unobserved']

#canonical_proteins.keys()
#generates table
#canonical_proteins


## Panel 1 ##

plt.subplot(2,2,1)
# parameters for the graph
min = 5600
max = 5680
binsize = 2
n_bins = int( (max - min) / binsize )

# graph for canonical proteins
# count and floor are y and x axis
# patches might contain the rectangles
canonical_count, x_floor, patches = plt.hist( canonical_proteins['Number of Datasets Detected In'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)

# graph for unobserved proteins
dark_count, x_floor, patches = plt.hist( not_observed['Number of Datasets Detected In'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

# formatting for the graph
plt.title(f"Number of Datasets Detected in")
plt.xlabel('Number of Datasets Detected In')
plt.ylabel('Proteins')
plt.xlim(min, max)
plt.grid(True)
plt.legend()


plt.subplot(2,2,3)
# get fractions for canonical and dark for each bin
# each is an array of numbers (height)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

# put the array of fractions in stair function to make stacked histograms
plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

# formatting
plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Number of Datasets Detected In")
plt.xlabel('Number of Datasets Detected In')
plt.ylabel('Ratio')
plt.grid(True)


### Percent of Datasets Detected In ###

## Regular Graph ##

plt.subplot(2,2,2)
min = 99
max = 100
bin_size = 0.1
n_bins = int((max-min)/bin_size)

#print(canonical_proteins['Percent of Datasets Detected in '])

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Percent of Datasets Detected in '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Percent of Datasets Detected in '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.title(f"Percent of Datasets Detected In")
plt.xlabel("Percent of Datasets Detected In")
plt.ylabel("Proteins")
plt.legend()
plt.xlim(min,max)
plt.grid(True)


#print(canonical_proteins['Percent of Datasets Detected in '])

plt.subplot(2,2,4)
canonical_count, x_floor, patches = plt.hist( canonical_proteins['Percent of Datasets Detected in '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Percent of Datasets Detected in '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.title(f"Percent of Datasets Detected In")
plt.xlabel("Percent of Datasets Detected In")
plt.ylabel("Proteins")
plt.xlim(min,max)
plt.grid(True)


plt.tight_layout()
plt.show()

# PANEL 2
### All Average TPM ###

## Regular Graph ##

plt.subplot(2,2,1)
min = 0.1
max = 1
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['All Average TPM '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['All Average TPM '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("ALl Average TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"All Average TPM")
plt.xlim(min,max)


## Stacked Graph for All Average TPM##

plt.subplot(2,2,3)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"All Average TPM")
plt.xlabel('All Average TPM')
plt.ylabel('Ratio')
plt.grid(True)


### Tau ###

## Regular Graph ##

plt.subplot(2,2,2)
min = 0.2
max = 1
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Tau'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Tau'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Tau")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Tau")
plt.xlim(min,max)


## Stacked Graph for Tau##

plt.subplot(2,2,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Tau")
plt.xlabel('Tau')
plt.ylabel('Ratio')
plt.grid(True)

## show graph ##
plt.tight_layout()
plt.show()

#Panel 3

### NZ Average TPM ###

## Regular Graph ##

plt.subplot(2,2,1)
min = 0
max = 99
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Average TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Average TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Average TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Average TPM")
plt.xlim(min,max)

## Stacked Graph for NZ Average TPM ##

plt.subplot(2,2,3)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"NZ Average TPM")
plt.xlabel('NZ Average TPM')
plt.ylabel('Ratio')
plt.grid(True) 


### NZ Minimum TPM ###

## Regular Graph ##

plt.subplot(2,2,2)
min = 0
max = 0.3
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Minimum TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Minimum TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Minimum TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Minimum TPM")
plt.xlim(min,max)

## Stacked Graph for NZ Minimum TPM##

plt.subplot(2,2,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"NZ Minimum TPM")
plt.xlabel('NZ Mimimum TPM')
plt.ylabel('Ratio')
plt.grid(True)

## show graph ##
plt.tight_layout()
plt.show()


#Panel 4
### NZ Standard Deviation ###

## Regular Graph ##

plt.subplot(2,2,1)
min = 0
max = 60
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Standard Deviation '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Standard Deviation '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Standard Deviation")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Standard Deviation")
plt.xlim(min,max)


## Stacked Graph for NZ Standard Deviation##

plt.subplot(2,2,3)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"NZ Standard Deviation")
plt.xlabel('NZ Standard Deviation')
plt.ylabel('Ratio')
plt.grid(True)



### Highest Maximun TPM ###

## Regular Graph ##

plt.subplot(2,2,2)
min = 0
max = 500
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Maximum TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Maximum TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Maximum TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Maximum TPM")
plt.xlim(min,max)

## Stacked Graph for Highest Maximum TPM##

plt.subplot(2,2,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Highest Maximum TPM")
plt.xlabel('Highest Maximum TPM')
plt.ylabel('Ratio')
plt.grid(True)

## show graph ##
plt.tight_layout()
plt.show()

#Panel 5

### Highest Median of that Dataset ###

## Regular Graph ##

plt.subplot(2,2,1)
min = 0
max = 25
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Median of that Dataset'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Median of that Dataset'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Median of that Dataset")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Median of that Dataset")
plt.xlim(min,max)

## Stacked Graph for Highest Median of that Dataset##

plt.subplot(2,2,3)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Highest Median of that Dataset")
plt.xlabel('Highest Median of that Dataset')
plt.ylabel('Ratio')
plt.grid(True)


### Highest Difference Between Gene Maximum and Dataset Median ###

## Regular Graph ##

plt.subplot(2,2,2)
min = 0
max = 450
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Difference Between Gene Maximum and Dataset Median'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Difference Between Gene Maximum and Dataset Median'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Difference Between Gene Maximum and Dataset Median")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Difference Between Gene Maximum and Dataset Median")
plt.xlim(min,max)

## Stacked Graph for Highest Difference Between Gene Maximum and Dataset Median##

plt.subplot(2,2,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Highest Difference Between Gene Maximum and Dataset Median")
plt.xlabel('Highest Difference Between Gene Maximum and Dataset Median')
plt.ylabel('Ratio')
plt.grid(True)

## show graph ##
plt.tight_layout()
plt.show()
