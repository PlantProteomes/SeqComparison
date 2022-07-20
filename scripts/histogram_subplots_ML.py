# Margaret and Sagunya
# 7/7/22
# This file reads from a tsv file containing information
# about light and dark proteins and create regular and stacked 
# histograms about molecular weights, GRAVY, and pI.

# imports
import pandas as pd
import matplotlib.pyplot as plt

# read TSV file into pandas DataFrame
df = pd.read_csv("C:\\Users\\smalhotr\\Documents\\SeqComparison\\proteomes\\arabidopsis\\light_and_dark_protein_list.tsv", sep="\t")

# specify related columns
canonical_proteins = df[df['status']=='canonical']
not_observed = df[df['status']=='not observed']


#### Compiled Subplots ####

### Molecular Weights ###

## Regular Graph ##

plt.subplots(3, 2, figsize=(4, 7.5))

plt.subplot(3,2,1)
# parameters for the graph
min = 0
max = 200
binsize = 2
n_bins = int( (max - min) / binsize )

# graph for canonical proteins
# count and floor are y and x axis
# patches might contain the rectangles
canonical_count, x_floor, patches = plt.hist( canonical_proteins['molecular_weight'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)

# graph for dark proteins
dark_count, x_floor, patches = plt.hist( not_observed['molecular_weight'], n_bins, [min,max], label='Dark', density=False, facecolor='b', alpha=0.5)

# formatting for the graph
plt.title(f"Distribution of molecular weight")
plt.xlabel('Molecular weight (kDa)')
plt.ylabel('Proteins')
plt.xlim(min, max)
plt.grid(True)
plt.legend()


## Stacked Graph ##

plt.subplot(3,2,2)
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
plt.title(f"Proportion of canonical to dark proteins")
plt.xlabel('Molecular weight (kDa)')
plt.ylabel('Ratio')
plt.grid(True)


### Gravy ###

## Regular Graph ##

plt.subplot(3,2,3)
min = -2
max = 2
bin_size = 0.1
n_bins = int((max-min)/bin_size)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['gravy'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['gravy'], n_bins, [min,max], label='Dark', density=False, facecolor='b', alpha=0.5)

plt.title(f"Distribution of GRAVY")
plt.xlabel("GRAVY")
plt.ylabel("Proteins")
plt.legend()
plt.xlim(min,max)
plt.grid(True)


## Stacked Graph ##

plt.subplot(3,2,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Proportion of canonical to dark proteins")
plt.xlabel('GRAVY')
plt.ylabel('Ratio')
plt.grid(True)


### pI ###

## Regular Graph ##

plt.subplot(3,2,5)
min = 4
max = 12
binSize = 0.22
binNum = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['pI'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['pI'], n_bins, [min,max], label='Dark', density=False, facecolor='b', alpha=0.5)

plt.xlabel("pI")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Distribution of pI")
plt.xlim(min,max)


## Stacked Graph ##

plt.subplot(3,2,6)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)

plt.xlim(min,max)
plt.ylim(0,1)
plt.title(f"Proportion of canonical to dark proteins")
plt.xlabel('pI')
plt.ylabel('Ratio')
plt.grid(True)

## show graph ##
plt.tight_layout()

plt.show()