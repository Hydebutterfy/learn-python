




def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance

def ApproximatePatternMatching(Pattern,Genome,d):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if HammingDistance(Pattern,Genome[i:i+len(Pattern)])<=d:
            positions.append(i)
    return positions


dna=str(input("enter your DNA sequence: ")).upper()
pattern=str(input("enter your pattern:")).upper()
mismatch=int(input("enter the d(mismatch):"))

result=ApproximatePatternMatching(pattern,dna,mismatch)
print(' '.join([str(i) for i in result]))
print(result,len(result))



