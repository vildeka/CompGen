import sys

infile1 = sys.argv[1]
outfile = sys.argv[2]

def read_line(infile1):
    with open(infile1, 'r') as f1:
        seq = ""
        for line in f1:
            if ">" not in line:
                seq += line.strip('\n')
    #print(seq)
    return (seq)
    
def rev_strand(infile1):
    seq = read_line(infile1)
    complement=seq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper() 
    reverse=complement[::-1]
    #print(reverse)
    return reverse
    
    
def start_indices(infile1):
    seq = read_line(infile1)
    start_index=[]
    start = "ATG"
    offset=0
    i = seq.find(start, offset)
    while i >= 0:
        start_index.append(i)
        i = seq.find(start, i + 1)   
    
    rev = rev_strand(infile1)
    start_index_rev=[]
    
    i = rev.find(start, offset)
    while i >= 0:      
        start_index_rev.append(i)   
        i = rev.find(start, i + 1)
    #print(start_index)
    #print(start_index_rev)
    return start_index, start_index_rev
    

def ORF_predictor(infile1):
    seq = read_line(infile1)
    rev = rev_strand(infile1)
    index, index_rev=start_indices(infile1)
    #start_pos = seq.find('ATG')
    nr= 0
    ORF=[]
    names=[]
    ORF_rev=[]
    names_rev=[]
#==============================================================================
#     for start_pos in index:
#         nr= nr+1
#         x1="start_pos_"+ str(start_pos)       
#         names.append(x1)
# #==============================================================================
# #         print(x1)
# #==============================================================================
#         if start_pos >=0:
#             start_to_end=seq[start_pos:]
#             print(start_pos)
#             #print(start_to_end)
#             #print(start_to_end)
#             for i in range(0, len(start_to_end), 3):
#                 stop=["TAA", "TAG", "TGA"]
#                 codon=start_to_end[i:i+3]
#                 ORF.append(codon)
#                 if codon in stop:
#                     #print(ORF)
#                     break
#==============================================================================
                
    for position in range(len(rev)):
        if position in index_rev:
            temp=[]
            for i in range(position,len(rev), 3):
                temp.append(rev[i:i+3])
                if rev[i:i+3] == "TAA" or rev[i:i+3] =="TAG" or rev[i:i+3] =="TGA":
                    break
            ORF_rev.append(temp)
    print(ORF_rev)
                
            
#==============================================================================
#         nr= nr+1
#         x2="start_pos_"+ str(start_pos)       
#         names_rev.append(x2)
#         #print(x2)
#         if start_pos >=0:
#             #ATG_index=int(start_pos)+3
#             #print(ATG_index)
#             start_to_end=seq[start_pos:]
#             #print(start_to_end[:3])
#             for i in range(0, len(start_to_end), 3):
#                 stop=["ATG", "TAA", "TAG", "TGA"]
#                 codon=start_to_end[i:i+3]
#                 #print(codon)
#                 if codon in stop:
#                     ORF_rev.append(start_to_end[:i+3])
#                     #print(ORF_rev)
#                     break
#     return ORF, names, ORF_rev, names_rev
#==============================================================================

def remove_short_orfs(infile1):
    ORF, names, ORF_rev, names_rev=ORF_predictor(infile1)
    #print(ORF)
    #print(names)
    nr=0
    nb=0
    with open(outfile, "w") as w:
        for orf, name in zip(ORF, names): 
            #print(orf)
            if len(orf) > 300:
                nr=nr+1
                w.write(str(">10.ORF_nr_"+str(nr)+" "+ name)+"\n")
                w.write(str(orf)+"\n")
                #print(orf)
                #print(name) 
                
        for orf_rev, name_rev in zip(ORF_rev, names_rev): 
            if len(orf_rev) > 300:
                nb=nb+1
                w.write(str(">10.ORF_rev_nr_"+str(nb)+" "+ name_rev)+"\n")
                w.write(str(orf_rev)+"\n")
                #print(orf_rev)
                #print(name_rev)
                
'''def remove_N(outfile):
    with open(outfile, "r") as r:
         for x, line in enumerate(f2):
            if x % 3 == 1:'''
                                        
            
read_line(infile1)
rev_strand(infile1)
start_indices(infile1)
ORF_predictor(infile1)
remove_short_orfs(infile1)
#remove_N(outfile)

'''def ORF_predictor(infile1):
    forward_strand, reverse_strand = frame_finder(infile1)
    seq = read_line(infile1)
    #index=start_indices(infile1)
    start_pos = seq.find('ATG')
    #for start_pos in index:
    print (">10.ORF_nr_" + str(start_pos))
    if start_pos >=0:
        ATG_index=int(start_pos)+3
        #print(ATG_index)
        start_to_end=seq[ATG_index:]
        #print(start_to_end)
        for i in range(0, len(start_to_end), 3):
            stop=["ATG", "TAA", "TAG", "TGA"]
            codon=start_to_end[i:i+3]
            #print(codon)
            if codon in stop:
                
                ORF= "ATG"+start_to_end[:i+3]
                print(ORF)
                break
            else:
                pass'''
'''def frame_finder(infile1):
    forward_strand = read_line(infile1)
    reverse_strand = rew_strand(infile1)
    
    fwd_1 = []
    fwd_2 = []
    fwd_3 = []
    rev_1 = []
    rev_2 = []
    rev_3 = []
    
    for j in range(0,len(forward_strand), 3):
        fwd_1.append(forward_strand[j:j+3])
        fwd_2.append(forward_strand[j+1:j+4])
        fwd_3.append(forward_strand[j+2:j+5])
        rev_1.append(reverse_strand[j:j+3])
        rev_2.append(reverse_strand[j+1:j+4])
        rev_3.append(reverse_strand[j+2:j+5])
    forward_frames = []
    forward_frames.append(fwd_1)
    forward_frames.append(fwd_2)
    forward_frames.append(fwd_3)
    reverse_frames = []
    reverse_frames.append(rev_1)
    reverse_frames.append(rev_2)
    reverse_frames.append(rev_3)

    #print(forward_frames)
    return forward_frames, reverse_frames'''


'''nr= 0
    ORF=[]
    names=[]
    ORF_rev=[]
    names_rev=[]
    for start_pos in index:
        nr= nr+1
        x1="start_pos_"+ str(start_pos)       
        names.append(x1)
        if start_pos >=0:
            ATG_index=int(start_pos)+3
            #print(ATG_index)
            start_to_end=seq[ATG_index:]
            #print(start_to_end)
            for i in range(0, len(start_to_end), 3):
                stop=["ATG", "TAA", "TAG", "TGA"]
                codon=start_to_end[i:i+3]
                #print(codon)
                if codon in stop:
                    ORF.append("ATG"+start_to_end[:i+3])
                    #print(ORF)
                    break'''
if __name__=="__main__":
    ORF_predictor('10.fa.txt')