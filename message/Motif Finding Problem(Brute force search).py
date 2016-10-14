#Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.
#     Input: A collection of strings Dna, and integers k and d.
#     Output: All (k, d)-motifs in Dna.

#MOTIFENUMERATION(Dna, k, d)
#Patterns ← an empty set
#for each k - mer Pattern in Dna
    #for each k - mer Pattern’ differing from Pattern by at most d mismatches
         #if Pattern' appears in each string from Dna with at most d mismatches
            #  add Pattern' to Patterns ' \
#'remove duplicates from Patterns
#return Patterns

def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance


def Neighbors(Pattern, d):
    if d==0:
        return Pattern
    if len(Pattern)==1:
        return ["A","C","G","T"]
    Neighborhood=[]
    SuffixNeighbors=Neighbors(Pattern[1:], d)
    for i in SuffixNeighbors:
        if HammingDistance(Pattern[1:], i)<d:
            for j in ["A","T","C","G"]:
                Neighborhood.append(j+i)
        else:
            Neighborhood.append(Pattern[0:1]+i)


    return Neighborhood


def MOTIFENUMERATION(Dna, k, d):
    Patterns=[]
    all_Pattern=[]
    all_Pattern_plus=[]
    num_string=len(Dna)
    for string in Dna:
        for i in range(len(string)-k+1):
            all_Pattern.append(string[i:i+k])
    all_Pattern=set(all_Pattern)
    print (all_Pattern)
    print("1")


    for i in all_Pattern:
        all_Pattern_plus.append(i)
        if d ==0:
            all_Pattern_plus = all_Pattern_plus
        else:
            all_Pattern_plus=all_Pattern_plus+Neighbors(i, d)

   # print(all_Pattern_plus)
    all_Pattern_plus=set(all_Pattern_plus)
    #print(all_Pattern_plus)

    for i in all_Pattern_plus:
        count=[]
        for j in range(0,num_string):
            count.append(int(j))
        print(count)

        temp=Neighbors(i, d)
        #print(temp)

        for m in temp:
            if count!=[]:
                for l in range(0,len(Dna)):
                    #print (count,l)
                    #print(l)
                    if m in Dna[l]:
                        if l in count:
                        #print(m,Dna[l])
                            count.remove(l)

                       # print(m,count[l])
                 #   print(p,l,"1")
                #else:
                    #print (m,Dna[l])

        print(count)
        if count==[]:
            Patterns.append(i)

    print(Dna)
    print(Patterns)
    return set(Patterns)

def Count(Motifs,k):
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t=len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol=Motifs[i][j]
            count[symbol][j] += 1

    return count

def Consensus(Motifs,k):
    count = Count(Motifs,k)
    consensus = ""
    for j in range(k):
        m=0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    print(count,consensus)
    return count,consensus

def Score(Motifs):
    k = len(Motifs[0])
    count,consensus_temp=Consensus(Motifs,k)

    score = []
    for i in range(k):
        score.append(0)

    for i in range(k):
        for j in "ATCG":
            if consensus_temp[i]!=j:
                score[i]+=count[j][i]
    allscore=0
    for i in range(k):
        allscore=allscore+score[i]

    return allscore


Dna=[]
filename = input("Enter file1 name: ")

fileread = open(filename,"r")

for i in fileread:
    dna=i.strip()
    Dna.append(dna.upper())

k=int(input("what is the k:"))
d=int(input("what is the d:"))

Motifs=MOTIFENUMERATION(Dna, k, d)
print(Motifs)

print (Score(list(Motifs)))




