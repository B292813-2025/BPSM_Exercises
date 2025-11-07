#!/usr/bin/python
def counter(DNA,threshold=50):
 bases = ['A','T','G','C']
 count=0
 total=len(DNA)
 for base in DNA.upper():
  if base not in bases:
   count+=1
 per = (count/total)*100
 if round(per) > threshold:
  return True
 else:
  return False
