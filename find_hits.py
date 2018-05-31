import sys

filename = sys.argv[1]

def positive_hits(filename):
    filehandle1 = open(filename, 'r')
    true_positives = []
    false_positives = []
    for lines in filehandle1:
        if lines.startswith("#"):
            #lists = lines.split()
            if lines[2] == "1":
                true_positives.append(lines[2])
            elif lines[2] == "0":
                false_positives.append(lines[2])
    print("True positives: ")
           
    print(len(true_positives))
    true_positive=len(true_positives)
    print("False positives: ")
    print(len(false_positives))
    false_positive=len(false_positives)
    return true_positive, false_positive

def negative_hits(filename):
    filehandle1 = open(filename, 'r')
    false_negatives = []
    for lines in filehandle1:
        if lines.startswith("#"):
            #lists = lines.split()
            if lines[2] == "0":
                false_negatives.append(lines[2])

    print("False negatives: ")
    print(len(false_negatives))
    false_negative=len(false_negatives)
    return false_negative
    
def calc_f1(filename):
    true_positive, false_positive=positive_hits(filename)
    false_negative=negative_hits(filename)
    precission=true_positive/(true_positive+false_negative)
    recall=true_positive/false_negative
    
    f1=2*(precission*recall)/(precission+recall)
    print("f1 score: "+str(f1))
    
    
#positive_hits(filename)
#negative_hits(filename)
calc_f1(filename)
#if __name__ == "__main__":
    # Write the commands here with paths to input.
    #print(find_hits("10_hits"))