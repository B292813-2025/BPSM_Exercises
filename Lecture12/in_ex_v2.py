#!/usr/bin/python3
import os
import sys
with open("AJ223353_no_header.fasta") as my_file:
 my_file = my_file.read()
 #29-409
 exon = my_file[28:409]
 intron1 = my_file[0:28]
 intron2 = my_file[409:]
#save exon1 and exon2 to a file
with open("exonsAJ.txt","w") as CR_plain:
 CR_plain.write(exon)

#save intron to a separate file
with open("intronAJ.txt","w") as NCR_plain:
 NCR_plain.write(intron1 + intron2)
