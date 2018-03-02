import sys # module needed for command line arguments to get fastq name
from itertools import islice # module for islice

##########################################################################

if (len(sys.argv) > 2):
#    fastq = open(sys.argv[1])
#    fasta = open(sys.argv[2])
    print("reading in input")


elif (len(sys.argv) < 2):
    print("Please supply both fastq and fasta files in that order")
    sys.exit()

###########################################################################

with open(sys.argv[1]) as fq, open(sys.argv[2]) as fa:

    ## Read in the Input.fastq file and save its content to a list
#    fq = fq.readlines()
    ## Do the same for the Input.fasta file
#    fa = fa.readlines()
    ReadIDs = []
    IDs = []

    #for line in fq:
    #    if "read" in line:
    #        ReadIDs.append(line)
    #        print(line.strip())
    #        for ID in ReadIDs:
    #            IDs.append(ID[1:6])
    #            for line in fa:
    #                if any(string in line for string in IDs):
    #                    print(next(fa).strip())
    #                    next(fq)
    #                    print(next(fq).strip())
    #                    print(next(fq).strip())


    for fq_line in fq:
        if "read" in fq_line:
            ID = fq_line[1:6]
            fa.seek(0)
            for fa_line in fa:
                if ID in fa_line:

                    id_line = fq_line.strip()
                    sequence_line = next(fa).strip()
                    next(fq)
                    between_line = next(fq).strip()
                    quality_line = next(fq).strip()
                    if (len(sequence_line) < len(quality_line)):
                        difference = len(quality_line) - len(sequence_line)
                        quality_line = quality_line[:-difference]
                    elif (len(quality_line) < len(sequence_line)):
                        difference = len(sequence_line) - len(quality_line)
                        quality_line += '8' * difference
                    print(id_line)
                    print(sequence_line)
                    print(between_line)
                    print(quality_line)
