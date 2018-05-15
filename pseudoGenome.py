import sys
inputfile1= sys.argv[1]
inputfile2= sys.argv[2]
outfile = sys.argv[3]
seq_dict = {}

with open(inputfile1, 'r') as f:     
    for line in f:
        line = line.strip("\n")
        l1 = line.split(None, 1)[0]
        sequence = line.split(None, 1)[1].strip("\n")
            
        #print l1
        #print l2
            
        seq_dict[int(l1)] = sequence
        #w.write(str(sequence))
    #print (seq_dict)
    
   
#dictionary = get_seq_dict(inputfile1)
with open(inputfile2, 'r') as f1:    
    with open(outfile, 'w') as w:
        for line in f1:
            line = line.strip("\n")
            #print line
            sequence = seq_dict[int(line)] 
            w.write(str(sequence))
            #print (sequence)
            
