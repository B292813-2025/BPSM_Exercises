#!/usr/bin/python
asc= ['xkn59438','yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
import re

#Q1
for number in asc:
 if re.search('5',number):
  print(number)

#Q2
for number in asc:
 if re.search(r'e',number) or re.search(r'd',number):
  print(number)

#Q3
for number in asc:
 if re.search(r'de',number):
  print(number)

#Q4
for number in asc:
 if re.search(r'd.e',number):
  print(number)

#Q5
for number in asc:
 if re.search(r'd',number) and re.search(r'e',number):
  print(number)

#Q6
for number in asc:
 if re.search(r'^[xy]',number):
  print(number)

#Q7
for number in asc:
 if re.search(r'^[xy]',number) and re.search(r'e$',number):
  print(number)

#Q8
for number in asc:
 digits = re.findall(r'\d',number)
 if len(digits)>=3:
  print(number)

#Q9
for number in asc:
 digits = set(re.findall(r'\d',number))
 if len(digits)>=3:
  print(number)

#Q10
for number in asc:
 if re.search(r'\d{3}',number):
  print(number)

#Q11
for number in asc:
 if re.search(r'd[arp]$',number):
  print(number)
