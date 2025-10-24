dna_seq='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
complement=''
for i in dna_seq:
 if i=='A':
  complement+='T'
 if i=='T':
  complement+='A'
 if i=='C':
  complement+='G'
 if i=='G':
  complement+='C'
print("orig:",dna_seq,"\ncomp:",complement)
