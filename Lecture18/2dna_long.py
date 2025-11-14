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
