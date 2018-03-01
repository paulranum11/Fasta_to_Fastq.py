import sys # module needed for command line arguments to get fastq name
from Bio import SeqIO # module needed for SeqIO

##########################################################################

if (len(sys.argv) > 2):
#    fastq = open(sys.argv[1])
#    fasta = open(sys.argv[2])
    print("reading in input")


elif (len(sys.argv) < 2):
    print("Please supply both fastq and fasta files in that order")
    sys.exit()

###########################################################################

#with open(sys.argv[1]) as fq, open(sys.argv[2]) as fa:

fasta_dict = {record.id: record.seq for record in SeqIO.parse(sys.argv[2], 'fasta')}

def yield_records():
    for record in SeqIO.parse(sys.argv[1], 'fastq'):
        record.seq = fasta_dict[record.id]
        yield record

SeqIO.write(yield_records(), 'Output.fastq', 'fastq')
