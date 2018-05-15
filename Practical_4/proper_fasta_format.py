def write_fasta(filename, outputname):
    inputfile2 = filename
    filehandle2 = open(inputfile2, 'r')
    output = open(outputname,'w')
    for lines in filehandle2:
        if lines.startswith(">"):
            output.write("\n" + lines)
        
        else:
            info = lines.strip()
            output.write(info)
      
    output.close()
    
    
if __name__ == "__main__": 
    print(write_fasta("10.fa.txt.pfa","10_oneline.fasta"))