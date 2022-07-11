# Scripts Directory - ML
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

### **fasta_matrix_ML.py**   
Generates a matrix table of file stats and seq overlaps    
between any number of files. Results read to Excel.     
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

### **organellar_PAextraction.py** 
Reads Arabidopsis_2021-04_newRNA-PEFF.fasta and writes all entries beginning     
with 'PeptideAtlas_" into a new file called PeptideAtlasNonNuclear.peff.    
*(Input: None)*    

### **histogram_subplots_ML.py** 
Generates a panels of histogram subplots from data from tsv file    
light_and_dark_protein_list.tsv.    
*(Input: None)*  
