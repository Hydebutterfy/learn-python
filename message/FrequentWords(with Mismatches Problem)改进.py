__author__ = 'chenhaide'

#先列举所有可能的组合

import itertools

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

Text=str(input("enter your DNA sequence: "))
k=int(input("what is the K?"))
d=int(input("enter the mismatch:"))

Frequentpattern=[]
clump=[]

for i in range(0,4**k):
    clump.append(0)

for i in range(0,4**k):
    pattern=NumberToPattern(k,i)
    clump[i]=ApproximatePatternMatching(pattern,Text,d)

max_number=max(clump)

for i in range(0,4**k):
    if clump[i]==max_number:
        Frequentpattern.append(NumberToPattern(k,i))

print (remove_duplicates(Frequentpattern))
print (len(remove_duplicates(Frequentpattern)))



