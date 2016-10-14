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

Text=str(input("enter your DNA sequence: "))
pattern=str(input("enter your pattern:"))
repattern=reversecomplement(pattern)
Count=[]

length=len(Text)-len(pattern)

for i in range(length+1):
    a=Text[i:len(pattern)+i]
    if a==pattern or a==repattern:
        Count.append(i)

print(Count)