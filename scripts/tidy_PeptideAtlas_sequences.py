#!/bin/env python3

import os
import sys
import re
from Bio import SeqIO

reference_data = {}

hard_coded_chrs = {
    'PeptideAtlas_ATCG00040.1': 'ChrC:2056-3636 REVERSE LENGTH=504',    # Length is fixed, but coords not quite right
    'PeptideAtlas_ATCG00890.1': 'ChrC:94941-96795 REVERSE LENGTH=512',    # Length is fixed, but coords not quite right
    'PeptideAtlas_ATCG00360.1': 'ChrC:42584-43751 REVERSE LENGTH=168'    # Length is fixed, but coords not quite right
}


input_file = '../proteomes/arabidopsis/ATCG_reference.tsv'
counter = 0
with open(input_file) as infile:
    for line in infile:
        counter += 1
        if counter == 1:
            continue
        line = line.strip()
        columns = line.split("\t")
        identifier = columns[1]
        print(identifier)
        reference_data[identifier] = { 'name': columns[5], 'symbols': columns[6], 'function': columns[7] }

input_file = '../proteomes/arabidopsis/ATMG_reference.tsv'
counter = 0
with open(input_file) as infile:
    for line in infile:
        counter += 1
        if counter == 1:
            continue
        line = line.strip()
        columns = line.split("\t")
        identifier = columns[1]
        reference_data[identifier] = { 'name': columns[6], 'symbols': columns[7], 'function': columns[8] }


proteins = {}

input_file = '../proteomes/arabidopsis/PeptideAtlasNonNuclear.peff'
output_file_all = '../proteomes/arabidopsis/PeptideAtlas_all_tidied.fasta'
output_file_best = '../proteomes/arabidopsis/PeptideAtlas_bestsequence_tidied.fasta'
output_attributes = '../proteomes/arabidopsis/PeptideAtlas_attributes.tsv'
counter = 0

with open(os.path.join(input_file)) as infile:
    print(f"INFO: Reading {input_file}")
    for record in SeqIO.parse(infile, 'fasta'):
        sequence = str(record.seq)
        match = re.match(r'^(\S+)\s*(.*)$', record.description)
        if match:
            identifier = match.group(1)
            description = match.group(2)
        else:
            print(f"ERROR: Unable to parse description line: {record.description}")
            exit()

        print(identifier)
        ####print(f"=={description}==")

        if identifier in proteins:
            print(f"ERROR: protein {identifier} was already seen!")
            exit()

        entry = {}

        match = re.search(r'\\PName=(.+?)\\', description)
        if match:
            entry['PName'] = match.group(1)
            description = re.sub(r'\\PName=(.+?)\\', '\\\zzxxccvv', description)
            description = re.sub(r'zzxxccvv', '', description)

        if '\TaxName=Arabidopsis thaliana' in description:
            entry['TaxName'] = 'Arabidopsis thaliana'
            description = re.sub(r'\\TaxName=Arabidopsis thaliana', '', description)

        if 'OS=Arabidopsis thaliana' in description:
            entry['TaxName'] = 'Arabidopsis thaliana'
            description = re.sub(r'OS=Arabidopsis thaliana', '', description)

        match = re.search(r'\\Length=(\d+)', description)
        if match:
            entry['Length'] = int(match.group(1))
            if entry['Length'] != len(sequence):
                print(f"ERROR: Length mismatch: {entry['Length']} != {len(sequence)}")
                exit()
            description = re.sub(r'\\Length=(\d+)', '', description)

        match = re.search(r'\\NcbiTaxId=(\d+)', description)
        if match:
            entry['NcbiTaxId'] = int(match.group(1))
            description = re.sub(r'\\NcbiTaxId=(\d+)', '', description)

        match = re.search(r'\\GName=(\S+)', description)
        if match:
            entry['GName'] = match.group(1)
            description = re.sub(r'\\GName=(\S+)', '', description)

        match = re.search(r'\\PE=(\d+)', description)
        if match:
            entry['PE'] = int(match.group(1))
            description = re.sub(r'\\PE=(\d+)', '', description)

        match = re.search(r'\\SV=(\d+)', description)
        if match:
            entry['SV'] = int(match.group(1))
            description = re.sub(r'\\SV=(\d+)', '', description)

        match = re.search(r'\\VariantSimple=(\S+)', description)
        if match:
            entry['VariantSimple'] = match.group(1)
            description = re.sub(r'\\VariantSimple=(\S+)', '', description)


        match = re.search(r'OX=(\d+)', description)
        if match:
            entry['OX'] = int(match.group(1))
            description = re.sub(r'OX=(\d+)', '', description)

        match = re.search(r'PE=(\d+)', description)
        if match:
            entry['PE'] = int(match.group(1))
            description = re.sub(r'PE=(\d+)', '', description)

        match = re.search(r'SV=(\d+)', description)
        if match:
            entry['SV'] = int(match.group(1))
            description = re.sub(r'SV=(\d+)', '', description)

        match = re.search(r'GN=(\S+)', description)
        if match:
            entry['GN'] = match.group(1)
            description = re.sub(r'GN=(\S+)', '', description)

        match = re.search(r'(Chr.+LENGTH=\d+)', description)
        if match:
            entry['Chr'] = match.group(1)
            description = re.sub(r'Chr.+LENGTH=\d+', '', description)

        match = re.search(r'(chr.+LENGTH=\d+)', description)
        if match:
            entry['Chr'] = match.group(1)
            entry['Chr'] = re.sub(r'^chr', 'Chr', entry['Chr'])
            description = re.sub(r'chr.+LENGTH=\d+', '', description)

        description = re.sub(r'201606', '', description)

        if 'with all high frequency RNA edits applied' in description:
            entry['RNAedit'] = True
            description = re.sub(r'with all high frequency RNA edits applied', '', description)

        if 'with high frequency RNA edits applied' in description:
            entry['RNAedit'] = True
            description = re.sub(r'with high frequency RNA edits applied', '', description)

        if 'all high frequency RNA edits are included' in description:
            entry['RNAedit'] = True
            description = re.sub(r'all high frequency RNA edits are included', '', description)

        if 'all high frequence RNA edits are included' in description:
            entry['RNAedit'] = True
            description = re.sub(r'all high frequence RNA edits are included', '', description)

        if 'contains all of the high frequency RNA edits' in description:
            entry['RNAedit'] = True
            description = re.sub(r'contains all of the high frequency RNA edits', '', description)

        if 'contains all high frequency RNA edits' in description:
            entry['RNAedit'] = True
            description = re.sub(r'contains all high frequency RNA edits', '', description)

        if 'Contains all of the high frequency RNA edits' in description:
            entry['RNAedit'] = True
            description = re.sub(r'Contains all of the high frequency RNA edits', '', description)

        if 'with all high and low frequency RNA edits applied' in description:
            entry['RNAedit_HighLow'] = True
            description = re.sub(r'with all high and low frequency RNA edits applied', '', description)

        if 'has all high frequency RNA edits' in description:
            entry['RNAedit'] = True
            description = re.sub(r'has all high frequency RNA edits', '', description)

        done = False
        while not done:
            description = description.strip()
            match = re.search(r'\|$', description)
            if match:
                description = re.sub(r'\|$', '', description)
            else:
                match = re.search(r'^\|', description)
                if match:
                    description = re.sub(r'^\|', '', description)
                else:
                    done = True

        match = re.match(r'^sp\|([A-Z0-9]+)\|([A-Z0-9]+_ARATH)', description)
        if match:
            entry['sp'] = match.group(0)
            description = re.sub(r'^sp\|[A-Z0-9]+\|[A-Z0-9]+_ARATH', '', description)
        description = description.strip()

        match = re.match(r'^tr\|([A-Z0-9]+)\|([A-Z0-9]+_ARATH)', description)
        if match:
            entry['tr'] = match.group(0)
            description = re.sub(r'^tr\|[A-Z0-9]+\|[A-Z0-9]+_ARATH', '', description)
        description = description.strip()

        match = re.match(r'^(Symbols: .+?) \|', description)
        if match:
            entry['Symbols'] = match.group(1)
            description = re.sub(r'^Symbols: .+? \|', '', description)
        description = description.strip()

        print(f"=={description}==")

        entry['description'] = description
        entry['identifier'] = identifier
        entry['sequence'] = sequence
        proteins[identifier] = entry

        counter += 1
        #if counter > 16:
        #    exit()

outfile = open(output_attributes, 'w')
column_titles = [ 'identifier', 'symbols', 'name', 'function', 'Symbols', 'PName', 'NcbiTaxId', 'TaxName', 'Length', 'GName', 'OX', 'PE', 'SV', 'GN',
    'Chr', 'RNAedit', 'RNAedit_HighLow', 'sp', 'tr', 'description']
reference_keys = [ 'name', 'symbols', 'function' ]
row = "\t".join(column_titles)
print(row, file=outfile)

for identifier,protein in proteins.items():
    gene_identifier = re.sub(r'\.\d$', '', identifier)
    dot_one_identifier = gene_identifier + '.1'
    if dot_one_identifier in reference_data:
        for key in reference_keys:
            protein[key] = reference_data[dot_one_identifier][key]
    else:
        print(f"ERROR: Did not find {dot_one_identifier} in reference")

    columns = []
    for column_title in column_titles:
        if column_title in protein:
            value = str(protein[column_title])
            columns.append(value)
        else:
            value = ''
            if column_title == 'Chr' and column_title in proteins[dot_one_identifier]:
                value = str(proteins[dot_one_identifier][column_title])
                proteins[identifier][column_title] = value
            if column_title == 'Chr' and value == '':
                if dot_one_identifier in hard_coded_chrs:
                    value = hard_coded_chrs[dot_one_identifier]
                    proteins[identifier][column_title] = value
            columns.append(value)
    row = "\t".join(columns)
    print(row, file=outfile)
outfile.close()


#### Create a list of genes
genes = {}
for identifier,protein in proteins.items():
    gene_identifier = re.sub(r'\.\d$', '', identifier)
    genes[gene_identifier] = 1

#### Write the best FASTA file
with open(output_file_best,'w') as outfile:
    gene_list = list(genes.keys())
    for gene_identifier in sorted(gene_list):
        identifier = gene_identifier + '.2'
        if identifier not in proteins:
            identifier = gene_identifier + '.1'
        if identifier not in proteins:
            print(f"ERROR: did not find {identifier}")
            exit()
        protein = proteins[identifier]
        symbols = re.sub(r'/',', ',protein['symbols'])
        symbols = re.sub(r'^"','',symbols)
        symbols = re.sub(r'"$','',symbols)
        name = re.sub(r'^"','',protein['name'])
        name = re.sub(r'"$','',name)
        edits_note = ''
        if 'RNAedit' in protein and protein['RNAedit']:
            edits_note = ' | RNA edits applied'
        print(f">{identifier} | Symbols: {symbols} | {name} | {protein['Chr']}{edits_note}", file=outfile)
        print(protein['sequence'], file=outfile)
outfile.close()