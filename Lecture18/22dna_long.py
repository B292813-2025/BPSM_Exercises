#!/usr/bin/python
import re
dna=open('long_dna.txt').read()
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'
all_cuts = []

for match in re.finditer(BpsmI, dna):
 all_cuts.append(match.start() + 3)
for match in re.finditer(BpsmII, dna):
 all_cuts.append(match.start() + 4)

all_cuts.sort()
print(all_cuts)

last_cut = 0
counter = 0
for cut_position in all_cuts:
 counter +=1
 fragment_size = cut_position - last_cut
 print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
 last_cut = cut_position

fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
 str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

fragment_sequences = {}

