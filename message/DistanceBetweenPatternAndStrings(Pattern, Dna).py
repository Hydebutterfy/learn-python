

import itertools

Dna=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")
for i in fileread:
    dna = i.strip()
    Dna.append(dna.upper())

print(Dna)

Pattern=input("What is the Pattern:"  )




def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance



def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    t=len(Dna)
    l=len(Dna[0])
    distance=0

    for i in range (t):
        hamming_distance=float("inf")
        for j in range(l-k+1):
            if hamming_distance>HammingDistance(Dna[i][j:j+k],Pattern):
                hamming_distance=HammingDistance(Dna[i][j:j+k],Pattern)

        distance+=hamming_distance
    return distance






print (DistanceBetweenPatternAndStrings(Pattern, Dna))