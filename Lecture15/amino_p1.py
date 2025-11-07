#!/usr/bin/python
def percentage(sequence,base):
 length=len(sequence)
 count=sequence.count(base.upper())
 per=(count/length)*100
 return round(per)
