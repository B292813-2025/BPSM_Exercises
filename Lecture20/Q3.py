#!/usr/bin/python
from Bio.Seq import Seq
import os
import re
from Bio import Entrez, SeqIO
import subprocess

Entrez.email = "s2837201@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
gene_name = input("Type in your desired gene: ")
tax_group = input("Type in your desired taxonomic group: ")

result = Entrez.read(Entrez.esearch(db="protein", term=f"{tax_group} {gene_name} complete", retmax="20"))


length = 0
counter = 0
for asc in result['IdList']:
 gb_file = Entrez.efetch(db="protein",id=asc,rettype="gb")
 record = SeqIO.read(gb_file, "genbank")
 counter += 1
 length = length + len(record.seq)
 print(counter,record.id,"\t",record.description,"\t",record.seq,"\t",len(record.seq))

mean_length = length/counter

print(f"The mean length is: {mean_length}")
print(f"There are {int(result['Count'])} complete {gene_name} protein records for {tax_group}") 
