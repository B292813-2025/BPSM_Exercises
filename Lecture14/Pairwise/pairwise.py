#!/usr/bin/python
dna = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
for i in range(len(dna)):
 for j in range(i+1,len(dna)):
  similarity_score=0 
  for k in range(len(dna[i])):
   if dna[i][k] == dna[j][k]: 
    similarity_score = similarity_score+1
  similarity_percent = (similarity_score / len(dna[i]))*100
  print(dna[i],"has a similarity of", similarity_percent,'% with', dna[j])


