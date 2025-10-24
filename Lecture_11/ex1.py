#!/usr/bin/python3
DNA_seq='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
seq=len(DNA_seq)
A_seq = DNA_seq.count("A")
T_seq = DNA_seq.count("T")
end_res = (A_seq+T_seq)/seq
print(int(end_res*100))

