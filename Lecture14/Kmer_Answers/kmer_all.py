#!/usr/bin/python
dna="ATGCATCATGCTATCGAT"
k=2 # kmer size
n=2 # more than this number found
with open('k_mer.txt','w') as out:
 for i in range(0,len(dna)):
  tab =' '
  if len(dna[i:i+2]) == 1:
   break 
  out.write(f'{i*tab}{dna[i:i+2]}\n')

my_file = open('k_mer.txt').read().splitlines()
AT_count = 0
TA_count = 0
CG_count = 0
GC_count = 0
for i in range(0,len(my_file)):
 if 'AT' in my_file[i]:
  AT_count = AT_count+1
 if 'TA' in my_file[i]:
  TA_count = TA_count+1
 if 'CG' in my_file[i]:
  CG_count = CG_count+1
 if 'GC' in my_file[i]:
  GC_count = GC_count+1

with open('kmer2.txt','w') as out:
 if AT_count >= n:
  out.write(f'AT appears {AT_count} times\n')
 if TA_count >= n:
  out.write(f'TA appears {TA_count} times\n')
 if GC_count >= n:
  out.write(f'GC appears {GC_count} times\n')
 if CG_count >= n:
  out.write(f'GC appears {CG_count} times\n')
