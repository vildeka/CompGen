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
            elif len(value) == 2:
                #print(str(key) +' '+ str(value[0]) +' '+ str(value[1]) +' '+ str(value[2]))
                cluster_id.append(key)
                w.write(str(key) +' '+ str(value[0]) +' '+ str(value[1]) +"\n")
            elif len(value) == 1:
                #print(str(key) +' '+ str(value[0]) +' '+ str(value[1]) +' '+ str(value[2]))
                cluster_id.append(key)
                w.write(str(key) +' '+ str(value[0]) +"\n")
    return(cluster_id)


if __name__ == '__main__':
    parse_fasta('../Practical_4/all.besthits2')
    get_cluster(parse_fasta('../Practical_4/all.besthits2'),'../all_clustring.txt')

