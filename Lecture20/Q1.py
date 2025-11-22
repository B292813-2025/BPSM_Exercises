#!/usr/bin/python
from Bio.Seq import Seq
import os
import re
from Bio import Entrez, SeqIO
import subprocess
Entrez.email = "s2837201@ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))

print(f"There are {result['Count']} complete COX1 protein records for Mammals") 
