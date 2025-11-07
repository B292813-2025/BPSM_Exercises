#!/usr/bin/python
dna = input("Enter the DNA sequence: ").upper()
ksize = int(input("Enter k-mer length: "))
minfreq = int(input("Enter minimum frequency threshold: "))
def kcount(dna, ksize, minfreq):
 if ksize > len(dna):
  return print("K-mer length", ksize, "is longer than DNA",len(dna),"bases")
 if ksize < 2:
  return print("K-mer size must be at least 2 bases")
 dna = dna.upper()
 kmers = []
 for i in range(len(dna) - ksize + 1):
  kmers.append(dna[i:i+ksize])
 for kmer in set(kmers):
  if kmers.count(kmer) >= minfreq:
   print("the k-mer:",kmer,"appears",kmers.count(kmer),"times")

kcount(dna,ksize,minfreq)
