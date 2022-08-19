# Scripts Directory - ML

***Note: "Input" refers to CMD input. Please       
check program for the correct internal file input      
format/directory***

### **arabidopsis_proteome_ML(2).py**
Creates a new arabidopsis proteome by combining elements
from two files (araport11.fasta and tair10.fasta) and deleting  
some features. Version 2 means organellar file sequences added.   
no original fasta files are changed.    
*(Input: none)*

### **compare_fasta_ML2.py**       
Compares 2 fasta files and prints stats of both files including    
overlap and unique sequences     
*(Input: two fasta filenames)*    
*Sample input: python compare_fasta_ML2.py ..\proteomes\maize\mitochondrion.2.fasta ..\proteomes\maize\plastid.2.fasta*

### **compare_ident_gn_ML.py**    
Compares the UP file and the SP file with the goal    
of identifying identifiers unique to the UP file    
*(Input: UP and SP filenames in the order of UP and then SP)*          
*Sample input: python compare_ident_gn_ML.py "..\proteomes\human\uniprot-human-filtered-proteome_UP000005640+AND+organism__Homo+sapiens+(--.fasta" "..\proteomes\human\uniprot-human-filtered-reviewed_yes+AND+organism__Homo+sapiens+(Human)--.fasta"*

### **fasta_matrix_ML(2).py**   
Generates a matrix table of file stats and seq overlaps    
between any number of files. Version 2 reads to Excel.     
*(Input: files in the format of "filename that would appear*   
*on the matrix table"="filename" Ex: araport=araport11.fasta)*      
*Sample input: python fasta_matrix_ML2.py Araport11=C:\Users\jli\SeqFiles\arabidopsis\Araport11.fasta TAIR10=C:\Users\jli\SeqFiles\arabidopsis\TAIR10.fasta Pseudogenes=C:\Users\jli\SeqFiles\arabidopsis\Pseudogenes.fasta UniProtKB=C:\Users\jli\SeqFiles\arabidopsis\UniProtKB.fasta*

### **fasta_stats_ML2.py**    
Reads a fasta file and output stats: total entries,   
unique identifiers, unique sequences, redundant identifiers, and    
redundant sequences.     
*(Input: none. Enter file directly in code)*    

### **lowest_pvalue_file_ML.py**
Reads a given fasta file and finds the identifiers with the lowest   
value in pcode P00# for each gene and writes identifier +    
corresponding sequence to a new fasta file   
*(Input: filename)*       
*Sample input: python lowest_pvalue_ML.py ..\proteomes\maize\Zm-B73-REFERENCE-NAM-5.0_Zm00001eb.1.protein.2.fa*

***Note: start of summer internship programs***

## Info Extraction

### **organellar_PAextraction_ML.py** 
Reads Arabidopsis_2021-04_newRNA-PEFF.fasta and writes all entries beginning     
with 'PeptideAtlas_" into a new file called PeptideAtlasNonNuclear.peff.    
*(Input: None)* 

### **check_manual_pub.py**   
Uses two methods (json and checking with an excel file        
to pull publication info for a designated list of identifiers    
*(Input: None)*   

### **extract_ProteomeXchange_ML.py**
This program gets information from specified ProteomeXchange websites    
via json dicts and writes information there to an excel file.   
*(Input: None)*    

### **get_protein_pages_html_ML.py**
This program takes in identifiers and webscrapes (via html) their    
profiles for specified information. Results are stored   
in a dataframe and exported to excel.   
*(Input: None)*    

## Plotting Programs

### **DarkLightHistograms_ML.ipynb**
Generates histograms from tsv file light_and_dark_protein_list.tsv    
and plots them in cell format in an ipynb file. Source: Google   
Colab notebook from shared drive.    
*(Input: None)* 

### **histogram_subplots_ML.py** 
Generates a panels of histogram subplots from data from tsv file    
light_and_dark_protein_list.tsv.    
*(Input: None)*    

### **prot_central_ara_graphs_ML.py**
This program generates 5 plots (year, instrument, repo, and PTM
from information from ProteinCentral. Most data is stored in the 
imported tsv file below. Some information for the PTM graph is
scraped from protein profiles from ProteomeXChange
*(Input: None)* 

## All PTM Programs

### **ptm_analysis_ML.py**
Takes massive ptm files, get all specified entries (ie: ATCG, ATMG, Nuclear)   
and generates specified stats for them. Some results are sent    
to excel files. A summary table and some analysis tables are generated.    
*(Input: None. Update ptm info in code)*

### **acetyl_analysis_ML.py**  
Generates stats for acetyl PTM and  
specifically separate results based on PTM residue (n/K)   
*(Input: None)* 

### **peptide_mod_stats_ML2.py**
This program reads all peptides of the arabidopsis     
proteome and generates stats about how many     
modification types there are and how many        
residue modifications there are.      
*(Input: None)*

### **peptide_mod_percentages_ML.py**
This program takes dictionaries of mod counts
generated from peptides_mod_stats_ML2.py
and generates percentages in various ways
(documented in the program) Outputs are exported
to excel.
*(Input: None)*

### **ptm_visuals.py**
This program generates ptm psm visuals for       
4 ptms based on percentage certainty.     
*(input: None)*    

### **peptides_mod_all_ML.py**
This program generates ptm stats that requires   
accounting for all amino acides regardless   
if modified.   
*(input: None)*  
status: incomplete
