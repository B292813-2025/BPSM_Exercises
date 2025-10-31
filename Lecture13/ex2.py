#!/usr/bin/python
my_file=open('exons.txt').read()
position = ["5","58","72","133","190","276","340","398"] 
seq = open('genomic_dna2.txt').read()
exons = ""
for i in range(0,len(position),2):
 start = int(position[i])
 end = int(position[i+1])
 exon = seq[start-1:end]
 exons += exon

with open('conc_exon_seg.txt','w') as out:
 out.write(exons)
 out.write('\n')
