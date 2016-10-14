#GREEDYMOTIFSEARCH(Dna, k, t)
    #BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    #for each k-mer Motif in the first string from Dna
        #Motif1 ← Motif
        #for i = 2 to t
              #form Profile from motifs Motif1, …, Motifi - 1
              #Motifi ← Profile-most probable k-mer in the i-th string in Dna
        #Motifs ← (Motif1, …, Motift)
        #if Score(Motifs) < Score(BestMotifs)
              #BestMotifs ← Motifs
    #return BestMotifs

#http://www.mrgraeme.co.uk/greedy-motif-search/ 解释

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    #print(BestMotifs)


    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
     #   print(Motifs)
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs

def Pr(pattern, profile):
    temp_Profile=1
    for j in range(k):
        #print(float(profile[pattern[j]][j]))
        #print(temp_Profile)
        temp_Profile=temp_Profile*float(profile[pattern[j]][j])
        #print(temp_Profile)
    return temp_Profile

def ProfileMostProbablePattern(Text, k, Profile):
    l=len(Text)
    profile_list=[]
    for i in range(l - k + 1):
        pattern = Text[i:i + k]
        profile_list.append(Pr(pattern, Profile))

    max_profile = max(profile_list)
    position = profile_list.index(max_profile)

    return Text[position:position + k]

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    #print(count)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    #print(count)

    return count


def Consensus(Motifs):
    count = Count(Motifs)
    k = len(Motifs[0])
    consensus = ""
    for j in range(k):
        m=0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return count,consensus

def Score(Motifs):
    k = len(Motifs[0])
    count,consensus_temp=Consensus(Motifs)

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


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {}
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(0)

    Counts = Count(Motifs)
    #print(Counts)

    for symbol in "ACGT":
        for i in range(k):
            profile[symbol][i] = Counts[symbol][i] / t

    #print(profile)

    return profile



Dna=[]
filename = input("Enter file name: ")
fileread = open(filename,"r")

for i in fileread:
    dna=i.strip()
    Dna.append(dna.upper())

k=int(input("what is the k:"))
t=len(Dna)

print('\n'.join(GreedyMotifSearch(Dna, k, t)))
#用Dna.txt  k=3


# it trades speed for accuracy 提高了速度,但是精确度不高
