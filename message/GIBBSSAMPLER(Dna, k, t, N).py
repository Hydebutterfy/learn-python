#GIBBSSAMPLER(Dna, k, t, N)
#randomly select k - mers Motifs = (Motif1, …, Motift) in each string from Dna

#BestMotifs ← Motifs
#for j ← 1 to N
   #i ← Random(t)
   #Profile ← profile matrix constructed from all strings in Motifs except for Motifi
   #Motifi ← Profile - randomly generated k - mer in the i - th sequence
   #if Score(Motifs) < Score(BestMotifs)
         #BestMotifs ← Motifs
#return BestMotifs

import random
k=int(input("what is the k"))
t=int(input("what is the t")) #motif的数量
N=int(input("what is the N"))

Dna=[]
filename = input("Enter file name: ")
fileread = open(filename,"r")

for i in fileread:
    dna=i.strip()
    Dna.append(dna.upper())

l=len(Dna[0])
#_______________________________________________
def RandomMotifs(Dna, k, t):
    temp_Motifs = []
    #global l = len(Dna[0])
    #print(l)

    for i in range(t):
        j=random.randint(0, l-k)
        #print(l-k)
        #print("j=", j)
        temp_Motifs.append(Dna[i][j:j+k])

    #print(temp_Motifs)
    return temp_Motifs
#_______________________________________________
def Score(Motifs):
    #k = len(Motifs[0])
    consensus_temp=Consensus(Motifs)

    score = []
    for i in range(k):
        score.append(0)

    for i in range(k):
        for j in "ATCG":
            if consensus_temp[i]!=j:
                score[i]+=counts[j][i]
    allscore=0
    for i in range(k):
        allscore=allscore+score[i]

    #print(allscore)
    return allscore
#_______________________________________________
def Consensus(Motifs):
    Count(Motifs)
    consensus = ""
    for j in range(k):
        m=0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus+=frequentSymbol
    return consensus
#_______________________________________________
def Count(Motifs):
    global counts
    counts = {}
    t=len(Motifs)
    for symbol in "ACGT":
        counts[symbol] = []
        for j in range(k):
            counts[symbol].append(0)
    #print(count)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            counts[symbol][j] += 1
    #print(counts)

    #return counts
#_______________________________________________
def Profile(Motifs):
    t = len(Motifs)
    #k = len(Motifs[0])
    P_profile = {}
    for symbol in "ACGT":
        P_profile[symbol] = []
        for j in range(k):
            P_profile[symbol].append(0)
    #counts = Count(Motifs)
    #print(Counts)
    Count(Motifs)

    for symbol in "ACGT":
        for i in range(k):
            P_profile[symbol][i] = (counts[symbol][i]+1)/ (t+4)

    #print(P_profile)
    return P_profile
##输出motif的概率分布
#_______________________________________________
def ProfileMostProbablePattern(Text,Profile):
    profile_list=[]
    for i in range(l - k + 1):
        pattern = Text[i:i + k]
        profile_list.append(Pr(pattern, Profile,k))

    max_profile = max(profile_list)
    position = profile_list.index(max_profile)

    return Text[position:position + k]


def Pr(pattern, profile,k):
    temp_Profile=1

    for j in range(k):
        #print(float(profile[pattern[j]][j]))
        #print(temp_Profile)
        temp_Profile=temp_Profile*float(profile[pattern[j]][j])
        #print(temp_Profile)
    return temp_Profile




def GIBBSSAMPLER(Dna, k, t, N):
    temp_Motifs=RandomMotifs(Dna, k, t)

    BestMotifs=list(temp_Motifs)
    BestScore = Score(BestMotifs)
    #print("BB",BestScore,BestMotifs)

    for j in range(100):
        i=random.randint(0,t-1)
        #print("i=",i)
        temp_Motifs.pop(i)
        #print(temp_Motifs)
        profile=Profile(temp_Motifs)
        #print(profile)
        i_motifs=ProfileMostProbablePattern(Dna[i],profile)
        #print(i_motifs)
        temp_Motifs.insert(i,i_motifs)
        #print(temp_Motifs)
        score=Score(temp_Motifs)
        #print(score,BestScore)
        if BestScore>score:
            BestMotifs=list(temp_Motifs)
            BestScore=score

    return BestMotifs

def RepeatedGibbsSampler(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(20):
        Motifs = GIBBSSAMPLER(Dna, k, t, N)
        CurrScore = Score(Motifs)
        #print(CurrScore)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    print(BestScore)
    return BestMotifs

print('\n'.join(RepeatedGibbsSampler(Dna, k, t, N)))











