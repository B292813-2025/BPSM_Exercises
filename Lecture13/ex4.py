#!/usr/bin/python
choose = 'xaa.dna'
my_file = open(choose).read().upper().replace("\n","")
for i in range(0,len(my_file),199):
 size = f"{choose} {i+1}-{i+199}.dna.txt"
 with open(size,"a") as out:
  out.write(f"{size}:{my_file[i:i+199]}\n")
