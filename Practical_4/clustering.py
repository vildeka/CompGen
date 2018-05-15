#from itertools import izip

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

def parse_fasta(infile2):
    hit_dict = {}
    with open(infile2) as f2:
        for line2 in f2:
            line2.strip("\n")
            key = line2.split(None, 1)[0]
            value = line2.split(None, 1)[1].strip("\n")
            #print(key)
            #print(value)
            set_key(hit_dict, key, value)
            #hit_dict[l1] = [l2]
            #hit_dict[key].append(l2)
                
        return(hit_dict)

def get_cluster(dictionary, outfile):    
    cluster_id = []
    with open(outfile, 'w') as w:
        for key, value in dictionary.items():
            if len(value) == 3:
                #print(str(key) +' '+ str(value[0]) +' '+ str(value[1]) +' '+ str(value[2]))
                cluster_id.append(key)
                w.write(str(key) +' '+ str(value[0]) +' '+ str(value[1]) +' '+ str(value[2]) + "\n")
    return(cluster_id)

def get_sequences(reference, proteom1, proteom2, proteom3, outfile):
    #cluster_id = get_cluster(parse_fasta('../CompGen/all.besthits2'),'../CompGen/clustring.txt')
    hit_dict = parse_fasta('../CompGen/all.besthits2')
    prot1_dict = {}
    prot2_dict = {}
    prot3_dict = {}
    ref_dict = {}
    with open(proteom1, 'r') as f1, open(proteom2, 'r') as f2, open(proteom3, 'r') as f3, open(reference, 'r') as f4:
        f = [l for l in (line.strip() for line in f1) if l]
        for x, line in enumerate(f2):
            if line[0] == ">":
                key = line[1:]
                #print(key)
            elif x % 3 == 1:
                A = line.strip("\n")
                prot1_dict[key] = A
            elif x % 3 == 2:
                #print(x)
                pass
        print(prot1_dict)
        print('-----------------------------------------------------------')
        
        f = [l for l in (line.strip() for line in f2) if l]
        for x, line in enumerate(f):
            if line[0] == ">":
                key = line[1:]
                #print(key)
            elif x % 3 == 1:
                A = line.strip("\n")
                prot2_dict[key] = A
            elif x % 3 == 2:
                #print(x)
                pass
        print(prot2_dict)
        print('-----------------------------------------------------------')
        
        f = [l for l in (line.strip() for line in f3) if l]
        for x, line in enumerate(f):
            if line[0] == ">":
                key = line[1:]
                #print(key)
            elif x % 3 == 1:
                A = line.strip("\n")
                prot3_dict[key] = A
            elif x % 3 == 2:
                #print(x)
                pass
        print(prot3_dict)
        print('-----------------------------------------------------------')
        
        f = [l for l in (line.strip() for line in f4) if l]
        for x, line in enumerate(f):
            if line[0] == ">":
                key = line[1:]
                #print(key)
            elif x % 3 == 1:
                A = line.strip("\n")
                ref_dict[key] = A
            elif x % 3 == 2:
                #print(x)
                pass
        print(ref_dict)
        
        '''with open(outfile, 'w') as w:
            with open(infile2) as f2:
                for element in cluster_id:'''
            
    

if __name__ == '__main__':
    parse_fasta('../CompGen/all.besthits2')
    get_cluster(parse_fasta('../CompGen/all.besthits2'),'../CompGen/clustring.txt')
    get_sequences('../CompGen/10_oneline.fasta', '../CompGen/16_oneline.fasta', '../CompGen/44_oneline.fasta','../CompGen/49_oneline.fasta', '../CompGen/cluster_sequece.fasta')
    
'''for value in dictionary.values():
            if len(value) == 3:
                #print(value)
                print(dictionary[value])  ''' 
'''
for line1 in zip(f1, f2, f3, f4):
            #if line[0] == line[0]
            #line.startswith() = x #in infile1, infile2, infile3:
                l1 = line1.split(None, 1)[0]
                l2 = line1.split(None, 1)[0]
                l3 = line1.split(None, 1)[0]
                l4 = line1.split(None, 1)[0]
                if l1 == l2 == l3 == l4:
                    w.write(line1+line2+line3+'\n')
                elif l1 != l2:
                    pass'''
                    
                    
'''for line1 in f1:
            #if line[0] == line[0]
            #line.startswith() = x #in infile1, infile2, infile3:
                l1 = line1.split(None, 1)[0]
                #print(l1)
                if line1[0] == ">":
                    key = line1.strip("\n")
                    #print(key)
                for line2 in f2:
                    l2 = line2.split(None, 1)[0]
                    #print(l2)
                   
                    for key in hit_dict:
                        print(key)
                        if key == l2:
                            print(line2)'''
