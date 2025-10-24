#!/usr/bin/python3
dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=dna[:63]
exon2=dna[90:]
coding_seq=exon1+exon2
print('This is the coding sequence',coding_seq)
percent=(len(coding_seq)/len(dna))*100
print(percent,"% of the DNA is coding")
intron=dna[len(exon1):90]
lw_intron=intron.lower()
w1=exon1+lw_intron+exon2
print('this is the sequence with introns lowercase and exons uppercase\n',w1)
