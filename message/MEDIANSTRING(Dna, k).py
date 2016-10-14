#Median String Problem: Find a median string.
#Input: A collection of strings Dna and an integer k.
#Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern.

#MEDIANSTRING(Dna, k)
#distance ← ∞
#for each k - mer Pattern from AA…AA to TT…TT
#if distance > d(Pattern, Dna)
 #   distance ← d(Pattern, Dna)
  #  Median ← Pattern
#return Median

import itertools

Dna=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")
for i in fileread:
    dna = i.strip()
    Dna.append(dna.upper())

print(Dna)

k=int(input("What is the k:"  ))




def NumberToPattern(k,position):
    bases=['A','C','G','T']
    patter_list = [''.join(i) for i in itertools.product(bases, repeat=k)]
    return patter_list[position]

def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance

def d(pattern,Dna):

    k=len(Dna)
    l=len(Dna[0])
    distance=[]
    for i in range(k):
        distance.append(len(pattern))

    for i in range(k):
        for j in range(l-len(pattern)+1):
            if distance[i]>HammingDistance(pattern,Dna[i][j:j+k]):
                distance[i]=HammingDistance(pattern,Dna[i][j:j+k])

    print(distance)

    all_distance=0
    for i in range(k):
        all_distance+=distance[i]

    return all_distance




def MEDIANSTRING(Dna, k):
    distance=float("inf")
    for i in range(0,4**k):
        pattern=NumberToPattern(k,i)
        temp_dis=d(pattern,Dna)
        if distance>temp_dis:
            distance=temp_dis
            Median=pattern
    return Median




print (MEDIANSTRING(Dna, k))