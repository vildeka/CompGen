#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys
seq_dict = {}
number=int(sys.argv[1])
length=int(sys.argv[2])
inputfile= sys.argv[3]
outfile=sys.argv[4]
aas="ARNDCEQGHILKMFPSTWYV"
def r20():
    return random.randrange(20)
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
        
    seq_dict[i] = s
#print seq_dict

with open(inputfile, 'r') as f:
    with open(outfile, 'w') as w:
        for line in f:
            line = line.strip("\n")
            print line
            sequence = seq_dict[int(line)] 
            w.write(str(sequence))
            print (sequence)
            
