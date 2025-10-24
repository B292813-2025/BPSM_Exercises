#!/usr/bin/python3
# start of the sequence up to and including the sixty-third BASE
import os
import sys
with open("plain_genomic_seq.txt") as my_file:
 my_file = my_file.read()
 exon1 = my_file[:62]
 exon2 = my_file[90:] #the second exon runs from the ninety-first BASE to the end of the sequence
 intron = my_file[62:90]

#save exon1 and exon2 to a file
with open("exons.txt","w") as CR_plain:
 CR_plain.write(exon1 + exon2)

#save intron to a separate file
with open("intron.txt","w") as NCR_plain:
 NCR_plain.write(intron)

