#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys
seq_dict = {}
number=int(sys.argv[1])
length=int(sys.argv[2])

aas="ARNDCEQGHILKMFPSTWYV"
def r20():
    
    return random.randrange(20)
with open('randomSeq_dict', 'w') as w:
    for i in range(number):
        s=""
        for j in range(length):
            s+=aas[r20()]
        w.write(str(i) + ' ' + s + '\n')
       
#print seq_dict
