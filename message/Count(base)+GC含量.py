__author__ = 'chenhaide'
DNA=input("what is the sequence?")
print (len(DNA))

#计算碱基长度
dna=str(input("what is  your dna sequence?"))
dna=dna.upper()
no_C=dna.count("C")
no_G=dna.count("G")
dna_length=len(dna)
GC_percent=(no_C+no_G)*100/dna_length
print(GC_percent)


def GC(dna):
    "this function computes the GC percentage of a DNA sequence"
    DNA=dna.upper()
    N_bases=DNA.count("N")
    GC_percent=float((DNA.count("G")+DNA.count("C"))*100.0/(len(DNA)-N_bases))
    return (GC_percent)

print("your GC percent is :",GC(input("your DNA sequence:")))