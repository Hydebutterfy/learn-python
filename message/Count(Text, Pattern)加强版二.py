__author__ = 'chenhaide'

def reverse_string(seq):
    return seq[::-1]

def complement(seq):
#return the complementary sequence string.
    basecomplement={"A":"T","C":"G","G":"C","T":"A","N":"N"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)


def reversecomplement(seq):
    #return the reverse complement of the dna string.
    seq=reverse_string(seq)
    seq=complement(seq)
    return seq


dna=str(input("enter your DNA sequence: ")).upper()
pattern=str(input("enter your pattern:")).upper()

text=len(dna)
Pattern_len=len(pattern)
count=0

for i in range(text-Pattern_len+1):
    a=dna[i:Pattern_len+i]

    if pattern==a or pattern==reversecomplement(a):
        count=count+1


print(count)  #用于计算基因组组中特定片段的数量,统一大小写,反向互补

