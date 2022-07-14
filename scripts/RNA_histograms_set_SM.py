

# imports
import pandas as pd
import matplotlib.pyplot as plt


#read TSV file (from Github) into pandas DataFrame
url = "https://raw.githubusercontent.com/PlantProteomes/SeqComparison/main/proteomes/arabidopsis/ExpressionMetrics-AllGenes.tsv"
df = pd.read_csv(url, sep="\t")

# specify right part of data
canonical_proteins = df[df['Category']=='Canonical']
not_observed = df[df['Category']=='Unobserved']

canonical_proteins.keys()

#panel 1 
#number of data sets detected in
#number of data sets detected in (whole range)

plt.subplot(2,3,1)
# parameters for the graph
min = 5
max = 5673
binsize = 55
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

plt.subplot(2,3,4)
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



#number of data sets detected in (zoomed in the beginning)
plt.subplot(2,3,2)
# parameters for the graph
min = 5
max = 500
binsize = 8
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

plt.subplot(2,3,5)
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

#regular graph (zoomed in the end)

plt.subplot(2,3,3)
# parameters for the graph
min = 5600
max = 5673
binsize = 3
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

#Stacked graph (zoomed in)
plt.subplot(2,3,6)
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

plt.tight_layout()
plt.show()


#panel 2
#percent of Datasets Detected in ##
#regular Graph (zoomed in)

plt.subplot(2,3,1)
min = 0.09
max = 100
bin_size = 0.5
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

#stacked graph (zoomed in)
#print(canonical_proteins['Percent of Datasets Detected in '])

plt.subplot(2,3,4)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

# put the array of fractions in stair function to make stacked histograms
plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)


plt.title(f"Percent of Datasets Detected In")
plt.xlabel("Percent of Datasets Detected In")
plt.ylabel("Ratio")
plt.xlim(min,max)
plt.grid(True)

#regular Graph (whole range)

plt.subplot(2,3,3)
min = 50
max = 100
bin_size = 0.5
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

#stacked graph (whole range)
#print(canonical_proteins['Percent of Datasets Detected in '])

plt.subplot(2,3,6)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

# put the array of fractions in stair function to make stacked histograms
plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)


plt.title(f"Percent of Datasets Detected In")
plt.xlabel("Percent of Datasets Detected In")
plt.ylabel("Ratio")
plt.xlim(min,max)
plt.grid(True)

plt.subplot(2,3,2)
min = 0
max = 50
bin_size = 0.8
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

#stacked graph (whole range)
#print(canonical_proteins['Percent of Datasets Detected in '])

plt.subplot(2,3,5)
canonical_fraction = canonical_count / ( canonical_count + dark_count )
dark_fraction = dark_count / ( canonical_count + dark_count )

# put the array of fractions in stair function to make stacked histograms
plt.stairs(canonical_fraction, x_floor, color='g', alpha=0.5, fill=True)
plt.stairs(dark_fraction*0+1, x_floor, baseline=canonical_fraction, color='b', alpha=0.5, fill=True)


plt.title(f"Percent of Datasets Detected In")
plt.xlabel("Percent of Datasets Detected In")
plt.ylabel("Ratio")
plt.xlim(min,max)
plt.grid(True)


plt.tight_layout()
plt.show()



# PANEL 3
### All Average TPM ###
## Regular Graph (whole range) ##

plt.subplot(2,2,1)
min = 0
max = 13808.5202
binSize = 0.0001
n_bins = int((max-min)/binSize)

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

## Regular Graph (zoomed in) ##

plt.subplot(2,2,2)
min = 0
max = 50
binSize = 0.0001
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['All Average TPM '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['All Average TPM '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("ALl Average TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"All Average TPM")
plt.xlim(min,max)


## Stacked Graph for All Average TPM##

plt.subplot(2,2,4)
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

### All Average TPM ###



# show graph #
plt.tight_layout()
plt.show()


#Panel 4
#Tau 


## Regular Graph (whole range) ##

plt.subplot(2,2,1)
min = 0
max = 1
binSize = 0.01
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Tau'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Tau'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Tau")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Tau")
plt.xlim(min,max)


## Stacked Graph for Tau##

plt.subplot(2,2,3)
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

#Regular Graph (zoomed in)

plt.subplot(2,2,2)
min = 0.9
max = 1
binSize = 0.001
n_bins = int((max-min)/binSize)

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


#Panel 5



## Regular Graph (whole range) ##

plt.subplot(2,2,1)
min = 0.033
max = 14006.0317
binSize = 0.01
n_bins = int((max-min)/binSize)

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

#NZ Average TPM 

#Regular Graph (zoomed in) 

plt.subplot(2,2,2)
min = 0
max = 80
binSize = 0.1
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Average TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Average TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Average TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Average TPM")
plt.xlim(min,max)

## Stacked Graph for NZ Average TPM ##

plt.subplot(2,2,4)
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

## show graph ##
plt.tight_layout()
plt.show()

#panel 6
### NZ Minimum TPM ###


#Regular Graph (whole range)

plt.subplot(2,2,1)
min = 0.0009
max = 30.5154
binSize = 0.22
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Minimum TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Minimum TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Minimum TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Minimum TPM")
plt.xlim(min,max)

## Stacked Graph for NZ Minimum TPM##

plt.subplot(2,2,3)
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

#Regular Graph (zoomed in)

plt.subplot(2,2,2)
min = 0
max = 0.2
binSize = 0.000001
n_bins = int((max-min)/binSize)

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


#Panel 7
### NZ Standard Deviation ###



#Panel 7
### NZ Standard Deviation ###

## Regular Graph (whole range) ##

plt.subplot(2,2,1)
min = 0.0226
max = 28380.8315
binSize = 0.01
n_bins = int((max-min)/binSize)

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

## Regular Graph (zoomed in) ##

plt.subplot(2,2,2)
min = 0
max = 50
binSize = 0.001
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['NZ Standard Deviation '], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['NZ Standard Deviation '], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("NZ Standard Deviation")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"NZ Standard Deviation")
plt.xlim(min,max)


## Stacked Graph for NZ Standard Deviation##

plt.subplot(2,2,4)
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


## show graph ##
plt.tight_layout()
plt.show()

#Panel 8
### Highest Maximun TPM ###



#Panel 8
### Highest Maximun TPM ###

# Regular Graph (whole range)

plt.subplot(2,2,1)
min = 0.0803
max = 207042.6627
binSize = 0.0001
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Maximum TPM'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Maximum TPM'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Maximum TPM")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Maximum TPM")
plt.xlim(min,max)

## Stacked Graph for Highest Maximum TPM##

plt.subplot(2,2,3)
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

# Regular Graph (zoomed in)

plt.subplot(2,2,2)
min = 0
max = 500
binSize = 0.0001
n_bins = int((max-min)/binSize)

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


#Panel 9

### Highest Median of that Dataset ###



#Panel 9

### Highest Median of that Dataset ###

## Regular Graph (whole range) ##

plt.subplot(2,2,1)
min = 0.0389
max = 22.2932
binSize = 0.0001
n_bins = int((max-min)/binSize)

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


## Regular Graph ##

plt.subplot(2,2,2)
min = 0
max = 12
binSize = 0.0001
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Median of that Dataset'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Median of that Dataset'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Median of that Dataset")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Median of that Dataset")
plt.xlim(min,max)

## Stacked Graph for Highest Median of that Dataset##

plt.subplot(2,2,4)
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
## show graph ##
plt.tight_layout()
plt.show()


#Panel 10
### Highest Difference Between Gene Maximum and Dataset Median ###


# Regular Graph (whole range) #

plt.subplot(2,2,1)
min = 0
max = 450
binSize = 0.0001
n_bins = int((max-min)/binSize)

canonical_count, x_floor, patches = plt.hist( canonical_proteins['Highest Difference Between Gene Maximum and Dataset Median'], n_bins, [min,max], label='Canonical', density=False, facecolor='g', alpha=0.5)
dark_count, x_floor, patches = plt.hist( not_observed['Highest Difference Between Gene Maximum and Dataset Median'], n_bins, [min,max], label='Unobserved', density=False, facecolor='b', alpha=0.5)

plt.xlabel("Highest Difference Between Gene Maximum and Dataset Median")
plt.ylabel("Proteins")
plt.grid(True)
plt.legend()
plt.title(f"Highest Difference Between Gene Maximum and Dataset Median")
plt.xlim(min,max)

## Stacked Graph for Highest Difference Between Gene Maximum and Dataset Median##

plt.subplot(2,2,3)
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

## Regular Graph (zoomed in) ##

plt.subplot(2,2,2)
min = -10.7065
max = 207041.8218
binSize = 0.0001
n_bins = int((max-min)/binSize)

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