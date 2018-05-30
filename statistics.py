import sys

infile1 = sys.argv[1]
#infile2 = sys.argv[2]
#outfile = sys.argv[3]

def read_line(infile1):
    with open(infile1, 'r') as f1:
        seq = ""
        for line in f1:
            if ">" not in line:
                seq += line
    return (seq)        

def GC_content(infile1):
    seq = read_line(infile1)
    g = seq.count("G")
    c = seq.count("C")
    gc = (g+c)*100.0/len(seq)
    print (gc)
    return gc

def dinucleotide_frquency(infile1):
    seq = read_line(infile1)
    di = ["AG", "AC", "AT", "TG", "TC", "TA", "CG", "CT", "CA", "GC", "GA", "GT"]
    for element in di:
        num = seq.count(element)
        x = num*100.0/len(seq)-1
        print(str(element) + "=" + str(x))


def aa_frquency(infile1):
    seq = read_line(infile1)
    di = ["AG", "AC", "AT", "TG", "TC", "TA", "CG", "CT", "CA", "GC", "GA", "GT"]
    for element in di:
        num = seq.count(element)
        x = num*100.0/len(seq)-1
        print(str(element) + "=" + str(x))


read_line(infile1)
GC_content(infile1)
dinucleotide_frquency(infile1)


