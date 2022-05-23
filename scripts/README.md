# Scripts Directory - ML
### **arabidopsis_proteome_ML.py**
Creates a new arabidopsis proteome by combining elements
from two files (araport11.fasta and tair10.fasta) and deleting  
some features. The two files are unchanged.      
*(Input: none)*     

### **compare_fasta_ML2.py**       
Compares 2 fasta files and prints stats of both files including    
overlap and unique sequences     
*(Input: two fasta filenames)*       

### **compare_ident_gn_ML.py**    
Compares the UP file and the SP file with the goal    
of identifying identifiers unique to the UP file    
*(Input: UP and SP filenames in the order of UP and then SP)*   

### **fasta_matrix_ML.py**   
Generates a matrix table of file stats and seq overlaps    
between any number of files. Results read to Excel.     
*(Input: files in the format of "filename that would appear*   
*on the matrix table"="filename" Ex: araport=araport11.fasta)*    

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



