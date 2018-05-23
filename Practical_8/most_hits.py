import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
outfile = sys.argv[3]
id_name = []
with open(infile1, 'r') as f1:
    for line in f1:
        line = line.strip("\n")
        id_name.append(line)

#print (id_name)

hit_dict = {}
with open(infile2, 'r') as f2:
    for x, line in enumerate(f2):
        line.strip("\n")
        lis = line.strip("\n").split(" ")
        #print (lis)
        key = x
        for a in id_name:
            #print (element)
            hit = 0
            #print(a)
            for b in lis:
                if a == b:
                    #print (b)
                    hit = hit + 1
                    hit_dict[key] = hit
                
#print (hit_dict) 

best_hit1 = max(hit_dict, key=lambda key: hit_dict[key])
x = sorted(hit_dict.items(),key=(lambda i: i[1]))
best_hit2 = x[-2][0]
#print (best_hit1)
#print (best_hit2)
with open(outfile, 'w') as w:
    with open(infile2, 'r') as f2:
        for x, line in enumerate(f2):
            if x == best_hit1:
                w.write(str(line))
            if x == best_hit2:
                w.write(str(line))

