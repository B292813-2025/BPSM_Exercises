#!/usr/bin/python3
import os
import sys
my_file = open('exonsAJ.txt').read()
window_size = 30
offset = 3
no_tab = my_file.replace("\n","")
for i in range(0,len(no_tab)-window_size+1,offset):
 window_seq = no_tab[i:i + window_size]
 g = no_tab[i:i + window_size].count('G')
 c = no_tab[i:i + window_size].count('C')
 percentage = 100*(g+c)/len(no_tab[i:i + window_size])
 filename = f"window_{i+1}_{i+window_size}.fasta"
 with open(filename,"w") as out:
  out.write(f">AJ223353.1 Homo sapiens mRNA for histone H2B, clone pJG4-5-15\nWindow {i+1}-{i+window_size}: {window_seq} with GC% {percentage}\n")
