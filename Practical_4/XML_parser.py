# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

#######################################################################################
# Input the genome_against_reference_genome file and use ">" to specify the output file
#######################################################################################

import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]

blastOutputXMLHandle = open (blastOutputXMLFile)

####################
# Make blast records
####################
listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)


for aSingleBlastRecord in listOfBlastRecords:

######################################################################
# Iterate through the records looking at the lengths of the alignments
######################################################################

    for i in range (len (aSingleBlastRecord.alignments)):
        query = aSingleBlastRecord.query
        """ Gives you the query """
        description = aSingleBlastRecord.descriptions[i]
        alignment = aSingleBlastRecord.alignments[i]
        queryseq = alignment.hsps [0].query
        title = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
        print(">" + query + " " + queryseq + " " + ">" + title + " " + alignment.hsps [0].sbjct)
        break


