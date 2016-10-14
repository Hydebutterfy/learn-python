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

print(reversecomplement(input("your seqence:")))