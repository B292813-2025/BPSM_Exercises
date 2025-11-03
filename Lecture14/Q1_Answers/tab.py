#!/usr/bin/python
import csv
tab_data = open('data.csv').read()
with open('data.csv') as tab_data:
 reader = csv.reader(tab_data)
 with open('Q1A.txt','w') as out:
  for line in reader:
   species = line[0].strip()
   sequence = line[1].strip()
   gene_name = line[2].strip()
   expression_level = line[3].strip()
   if species == 'Drosophila melanogaster' or species == 'Drosophila simulans':
    out.write(f'{gene_name}\n')
