import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import itertools

infile = sys.argv[1]
outfile = sys.argv[2]

def read_line(infile):
    with open(infile, 'r') as f1:
        seq = ""
        for line in f1:
            if ">" not in line:
                seq += line
    return (seq)        

def GC_content(infile):
    seq = read_line(infile)
    g = seq.count("G")
    c = seq.count("C")
    gc = (g+c)*100.0/len(seq)
    print ("GC content: "+str(gc))
    return gc

def dinucleotide_frquency(infile):
    seq = read_line(infile)
    di = ["AG", "AC", "AT", "TG", "TC", "TA", "CG", "CT", "CA", "GC", "GA", "GT"]
    for element in di:
        num = seq.count(element)
        x = num*100.0/len(seq)-1
        print(str(element) + "=" + str(x))


def nucleotide_frquency(infile):
    seq = read_line(infile)
    di = ["A", "C", "T", "G"]
    for element in di:
        num = seq.count(element)
        x = num*100.0/len(seq)-1
        print(str(element) + "=" + str(x))

def translate(infile):
    fasta_sequences = SeqIO.parse(open(infile),'fasta')
    with open(outfile, 'w') as w:    
        for record in fasta_sequences:
            name, sequence = record.id, record.seq
            #print(">"+name)
            #print(sequence)
            translated_seq=sequence.translate()
            #print(translated_seq)
            new_record=SeqRecord(translated_seq, id=record.id, description="")
            SeqIO.write(new_record, w, "fasta")
            #new_sequence = translate(sequence)
            #write_fasta(outfile)
    return outfile
    

def aa_frequency(outfile):
    fasta_sequences = SeqIO.parse(open(outfile),'fasta')
    all_seq=""
    for record in fasta_sequences:
        name, sequence = record.id, record.seq        
        #x=ProteinAnalysis(str(record.seq))
        #print(record.id, x.count_amino_acids())         
        all_seq=all_seq+str(sequence)
    #print(all_seq)
    y=ProteinAnalysis(str(all_seq))
    print("all_seq_n", y.count_amino_acids())
    print("all_seq_%", y.get_amino_acids_percent())
    
def diaa_frequency(outfile):
    fasta_sequences = SeqIO.parse(open(outfile),'fasta')
    all_seq=""
    
    aa=[["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"],
        ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]]
    pla=""
    bla=[]
    
    for record in fasta_sequences:
        name, sequence = record.id, record.seq        
        all_seq=all_seq+str(sequence)

    for el in itertools.product(aa[0], aa[1]):
        pla="".join(el)
        bla.append(pla)
    #print(bla)
    print(len(all_seq))
    
    for element in bla:    
        occurrenceXX = str(all_seq.count(element))
        #print("occurence of "+ element+": "+occurrenceXX)
        percent_occurrenceXX = float(occurrenceXX)/len(all_seq)*100
        #print("percent occurrence of "+ element+": "+str(percent_occurrenceXX))
        print(str(percent_occurrenceXX))


read_line(infile)
#GC_content(infile)
#dinucleotide_frquency(infile)
nucleotide_frquency(infile)
translate(infile)
aa_frequency(outfile)
diaa_frequency(outfile)
