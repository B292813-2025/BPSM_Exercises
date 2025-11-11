#!/usr/bin/python
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def rev_seq(seq):
 complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
 comp_seq = ""
 for base in seq:
  comp_seq += complement.get(base, '?')
 rev_seq = comp_seq[::-1]
 return rev_seq


def translate(seq,frame=0):
 seq = seq.upper()
 protein =""
 for i in range(frame,len(seq)-2,3):
  codon = seq[i:i+3]
  protein += gencode.get(codon,"?")
 return protein

dna = input("Enter DNA sequence: ").strip().upper()
frames = int(input("Enter the number of frames desired: "))
print("\n--- Forward Strand ---")
for frame in range(0,frames):
 print(f"Frame {frame+1}: {translate(dna, frame)}\n")

rev_dna = rev_seq(dna)
print("\n--- Reverse Strand ---")
for frame in range(0,frames):
 print(f"Frame {frame+1}: {translate(rev_dna, frame)}\n")
