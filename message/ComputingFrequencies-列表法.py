import itertools

filename = input("Enter file name: ")
fileread = open(filename,"r")
genome=fileread.read().upper()


k=int(input("k:"))
L=int(input("L:"))
t=int(input("t:"))


def PatternToNumber(Pattern):
    bases=['A','C','G','T']
    k = len(Pattern)
    patter_list = [''.join(p) for p in itertools.product(bases, repeat=k)]
    p = patter_list.index(Pattern)
    return p


def NumberToPattern(k,position):
    bases=['A','C','G','T']
    patter_list = [''.join(i) for i in itertools.product(bases, repeat=k)]
    return patter_list[position]


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


Frequentpattern=[]
clump=[]
for i in range(0,4**k):
    clump.append(0)

for i in range(0,len(genome)-L+1):
    Text=genome[i:i+L]
    frequencyarray=ComputingFrequencies(Text,k)
    for index in range(0,4**k):
        if frequencyarray[index]>=t:
            clump[index]=1

for i in range(0,4**k):
    if clump[i]==1:
        pattern=NumberToPattern(k,i)
        Frequentpattern.append(pattern)



print(Frequentpattern)



















