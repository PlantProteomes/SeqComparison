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
*Sample input: python compare_fasta_ML2.py ..\proteomes\maize\mitochondrion.2.fasta ..\proteomes\maize\plastid.2.fasta![image](https://user-images.githubusercontent.com/91033739/170550611-364df58c-7c3b-430b-83bf-2e7fa7ee2bb9.png)*

### **compare_ident_gn_ML.py**    
Compares the UP file and the SP file with the goal    
of identifying identifiers unique to the UP file    
*(Input: UP and SP filenames in the order of UP and then SP)*   
*Sample input: python compare_ident_gn_ML.py "..\proteomes\human\uniprot-human-filtered-proteome_UP000005640+AND+organism__Homo+sapiens+(--.fasta" "..\proteomes\human\uniprot-human-filtered-reviewed_yes+AND+organism__Homo+sapiens+(Human)--.fasta"
![image](https://user-images.githubusercontent.com/91033739/170550701-8e1fd233-27f5-4b4e-8d76-d6b9edc95647.png)*

### **fasta_matrix_ML.py**   
Generates a matrix table of file stats and seq overlaps    
between any number of files. Results read to Excel.     
*(Input: files in the format of "filename that would appear*   
*on the matrix table"="filename" Ex: araport=araport11.fasta)*    
*Sample input: python fasta_matrix_ML2.py Araport11=C:\Users\jli\SeqFiles\arabidopsis\Araport11.fasta TAIR10=C:\Users\jli\SeqFiles\arabidopsis\TAIR10.fasta Pseudogenes=C:\Users\jli\SeqFiles\arabidopsis\Pseudogenes.fasta UniProtKB=C:\Users\jli\SeqFiles\arabidopsis\UniProtKB.fasta
![image](https://user-images.githubusercontent.com/91033739/170550761-d64dd181-6f03-4c5b-bc00-5140bde081da.png)*

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
*Sample input: python lowest_pvalue_ML.py ..\proteomes\maize\Zm-B73-REFERENCE-NAM-5.0_Zm00001eb.1.protein.2.fa![image](https://user-images.githubusercontent.com/91033739/170550924-2c7a113b-1c8f-4f6d-98ff-bb24ce3b6cc9.png)*




