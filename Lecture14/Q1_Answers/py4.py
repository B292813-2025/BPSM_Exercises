#!/usr/bin/python
import csv
tab_data = open('data.csv').read()
with open('data.csv') as tab_data:
 reader = csv.reader(tab_data)
 with open('Q4A.txt','w') as out:
  for line in reader:
   species = line[0].strip()
   sequence = line[1].strip()
   gene_name = line[2].strip()
   expression_level = line[3].strip()
   if gene_name.startswith('k') or gene_name.startswith('h') and species != 'Drosophila melanogaster':
    out.write(f'{gene_name}\n')
