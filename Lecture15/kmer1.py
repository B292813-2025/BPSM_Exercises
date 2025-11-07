#!/usr/bin/python
def kcount(dna, ksize, minfreq):
 if ksize > len(dna):
  return f"K-mer length {ksize} is longer than DNA ({len(dna)} bases)"
 if ksize < 2:
  return "K-mer size must be at least 2 bases"
 dna = dna.upper()
 kmers = []
 for i in range(len(dna) - ksize + 1):
  kmers.append(dna[i:i+ksize])
 for kmer in set(kmers):
  if kmers.count(kmer) > minfreq:
   print(kmer,kmers.count(kmer))


