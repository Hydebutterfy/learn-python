__author__ = 'chenhaide'

def reverse_string(seq):
    return seq[::-1]

def complement(seq):
#return the complementary sequence string.
    seq=seq.upper()
    basecomplement={"A":"T","C":"G","G":"C","T":"A","N":"N"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)


def reversecomplement(seq):
    #return the reverse complement of the dna string.
    seq=reverse_string(seq)
    seq=complement(seq)
    return seq

def GC(dna):
    "this function computes the GC percentage of a DNA sequence"
    DNA=dna.upper()
    N_bases=DNA.count("N")
    GC_percent=float((DNA.count("G")+DNA.count("C"))*100.0/(len(DNA)-N_bases))
    return GC_percent


