import itertools

def PatternToNumber(Pattern):
    bases=['A','C','G','T']
    k = len(Pattern)
    patter_list = [''.join(p) for p in itertools.product(bases, repeat=k)]
    p = patter_list.index(Pattern)
    return p

def ComputingFrequencies(Text, k):
    FrequencyArray=[]

    for i in range(0,4**k):
        FrequencyArray.append(0)

    print(FrequencyArray)

    for i in range(0,len(Text)-k+1):
        Pattern=Text[i:i+k]
        j=PatternToNumber(Pattern)
        FrequencyArray[j]=FrequencyArray[j]+ 1
    print(FrequencyArray)
    return FrequencyArray



seq=input("what is the DNA string Text?")
k=int(input("waht is the k?"))


frequencyarray=ComputingFrequencies(seq,k)


print(' '.join('%s' % id for id in frequencyarray))













