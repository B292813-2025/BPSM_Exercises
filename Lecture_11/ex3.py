#!/usr/bin/python3
dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut='GAATTC'
position=dna.find(cut)+1
first_half = dna[:position]
second_half = dna[position:]
print('original',dna,'\n1st half is:',first_half,'\n2nd half is:',second_half)
print('length of first sequence is:',len(first_half))
print('length of second sequence is:',len(second_half))
