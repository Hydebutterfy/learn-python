__author__ = 'chenhaide'

#先列举所有可能的组合4**k,再取最大可能值

import itertools


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

def ApproximatePatternMatching(Pattern,Genome,d):
    count=0
    for i in range(len(Genome) - len(Pattern) + 1):
        if HammingDistance(Pattern,Genome[i:i+len(Pattern)])<=d:
            count+=1
    return count

def max(list):
    m=list[0]
    for item in list:
        if item > m:
            m = item
    print(m)
    return m

def remove_duplicates(list): # 去处重复部分
    return set(list)

Text=str(input("enter your DNA sequence: ")).upper()
k=int(input("what is the K?"))
d=int(input("enter the mismatch:"))

Frequentpattern=[]
clump=[]

for i in range(0,4**k):
    clump.append(0)

for i in range(0,4**k):
    pattern=NumberToPattern(k,i)
    print(pattern)
    clump[i]=ApproximatePatternMatching(pattern,Text,d)+ApproximatePatternMatching(reversecomplement(pattern),Text,d)
    print(clump[i])

max_number=max(clump)

for i in range(0,4**k):
    if clump[i]==max_number:
        Frequentpattern.append(NumberToPattern(k,i))

print (remove_duplicates(Frequentpattern))


