import itertools

def NumberToPattern(k,position):
    bases=['A','C','G','T']
    patter_list = [''.join(i) for i in itertools.product(bases, repeat=k)]
    return patter_list[position]

def PatternToNumber(pattern):
    bases = ['A', 'C', 'G', 'T']
    k = len(pattern)
    patter_list = [''.join(p) for p in itertools.product(bases, repeat=k)]
    p = patter_list.index(pattern)
    return p

def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance

def Neighbors(pattern, d):
    k = len(pattern)
    fre_pattern = []
    for i in range(4 ** k):
        pattern_temp = NumberToPattern(len(pattern), i)
        if HammingDistance(pattern_temp, pattern) <= d:
            fre_pattern.append(pattern_temp)
    return fre_pattern


def ApproximatePatterncount(Pattern,Genome,d):
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


Text=str(input("enter your DNA sequence: "))
k=int(input("what is the K?"))
d=int(input("enter the mismatch:"))

Frequentpattern=[]
close=[]
FrequencyArray=[]

for i in range(0,4**k):
    close.append(0)
    FrequencyArray.append(0)

for i in range(len(Text)-k+1):
    Neighborhood=Neighbors(Text[i:k+i], d)
    for j in Neighborhood:
        index=PatternToNumber(j)
        close[index]=1

for i in range(0,4**k):
    if close[i]==1:
        pattern=NumberToPattern(k,i)
        FrequencyArray[i]=ApproximatePatterncount(pattern,Text,d)


max_number = max(FrequencyArray)

for i in range(0,4**k):
    if FrequencyArray[i]==max_number:
        Frequentpattern.append(NumberToPattern(k,i))


print (Frequentpattern)




