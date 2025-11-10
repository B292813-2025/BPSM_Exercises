#!/usr/bin/python
sequence= input("Input the sequence ")
base = input("Input the amino acid ")
def percentage(sequence,base):
 length=len(sequence)
 count=sequence.upper().count(base.upper())
 per=(count/length)*100
 return print(round(per),"%")

percentage(sequence,base)
