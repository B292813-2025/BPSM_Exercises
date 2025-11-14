#!/usr/bin/python
import re
dna=open('long_dna.txt').read()

#list(re.findall(r'(A[CGAT]T)(.)(AAT)',dna))
#list(re.finditer(r'(A[CGAT]T)(.)(AAT)',dna))

BpsmI='A[GATC]TAAT'
for matching in re.finditer(BpsmI, dna): 
    print(matching.start()+3)

last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
 findnum += 1
 cut_position = matching.start() + 3
 fragment_size = cut_position - last_cut
 print('Fragment size is ' + str(fragment_size))
 last_cut = cut_position
 if findnum == len(list(re.finditer(BpsmI, dna))):
  fragment_size = len(dna) - last_cut
  print('Fragment size is ',str(fragment_size))
