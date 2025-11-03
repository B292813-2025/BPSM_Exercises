#!/usr/bin/python
import csv
tab_data = open('data.csv').read()
with open('data.csv') as tab_data:
 reader = csv.reader(tab_data)
 with open('Q5A.txt','w') as out:
  for line in reader:
   species = line[0].strip()
   sequence = line[1].strip()
   gene_name = line[2].strip()
   expression_level = line[3].strip()
   A_T = sequence.count('a')+sequence.count('t')
   perc_AT = A_T/len(sequence)
   if perc_AT > 0.65:
    out.write(f'{gene_name}\thigh\n')
   elif perc_AT < 0.45:
    out.write(f'{gene_name}\tlow\n')
   else:
    out.write(f'{gene_name}\tmedium\n')
