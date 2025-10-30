#!/usr/bin/python
import string
my_file=open('input.txt').read()
start_string = my_file[0:14]
filtered = my_file.replace(start_string,"")
with open("filtered.txt", "w") as out:
 out.write(filtered)
 sequences = filtered.splitlines()
 len1 = len(sequences[0])
 len2 = len(sequences[1])
 len3 = len(sequences[2])
 len4 = len(sequences[3])
 len5 = len(sequences[4])
 print("Sequence 1 has length", len1)
 print("Sequence 2 has length", len2)
 print("Sequence 3 has length", len3)
 print("Sequence 4 has length", len4)
 print("Sequence 5 has length", len5)
