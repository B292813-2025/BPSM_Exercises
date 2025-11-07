#!/usr/bin/python
def percentage(sequence,res=None):
 if res is None:
  res=['A', 'I', 'L', 'M','F', 'W', 'Y', 'V'] 
 sequence=sequence.upper()
 count=0
 total=len(sequence)
 for aa in sequence:
  if aa in res:
   count+=1
 per=(count/total)*100
 return round(per)

