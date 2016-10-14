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

def has_stop_codon(dna):
    "this function checks if given dna sequence has in frame stop codons."
    DNA=dna.upper()
    stop_codon_found=False
    stop_codons=["TGA","TAG","TAA"]
    for i in range(0,len(DNA)-2):
        codon=DNA[i:i+3]
        if codon in stop_codons:
            stop_codon_found=True
            break
    if stop_codon_found==False:
        DNA=reversecomplement(DNA)
        for i in range(0,len(DNA)-2):
            codon=DNA[i:i+3]
            if codon in stop_codons:
                stop_codon_found=True
                break
    return (stop_codon_found,i)

#define has_stop_codon function here

dna=input("enter your DNA sequence: ")
if(has_stop_codon(dna)[0]):
    print("input sequence has an in frame stop codon.","Position is",has_stop_codon(dna)[1]+1)
else:
    print("input sequence has no in frame stop codons.")



