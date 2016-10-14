import random

def RandomMotifs(Dna, k, t):
    temp_Motifs = []
    l = len(Dna[0])
    #print(l)

    for i in range(t):
        j=random.randint(0, l-k)
        #print(l-k)
        #print("j=", j)
        temp_Motifs.append(Dna[i][j:j+k])

    return temp_Motifs




##产生一个随机的motif

def RandomizedMotifSearch(Dna, k, t):
    temp_Motifs=RandomMotifs(Dna, k, t)
    l=len(Dna[0])
    #print(l)

    BestMotifs=temp_Motifs
    BestScore = Score(BestMotifs)
    while True:
        profile=Profile(temp_Motifs)
        #print(profile)
        temp_Motifs=Motifs(profile, Dna)
        #print(profile,temp_Motifs)
        #print(temp_Motifs)
        score =Score(temp_Motifs)

        if score<BestScore:
            BestMotifs=list(temp_Motifs)
            BestScore=score

        else:
            return BestMotifs



def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    P_profile = {}
    for symbol in "ACGT":
        P_profile[symbol] = []
        for j in range(k):
            P_profile[symbol].append(0)

    Counts = Count(Motifs)
    #print(Counts)

    for symbol in "ACGT":
        for i in range(k):
            P_profile[symbol][i] = Counts[symbol][i]/ (t+4)

    #print(P_profile)
    return P_profile
##输出motif的概率分布


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    t = len(Motifs)
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    #print(count)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    #print(count)

    return count

def Motifs(profile, Dna):
    k=len(Dna)
    all_motif=[]
    #print(l,k)

    for i in range(k):
        string=Dna[i]
        all_motif.append(ProfileMostProbablePattern(string,profile))

    return all_motif

def ProfileMostProbablePattern(Text,Profile):
    l=len(Text)
    k=len(Profile["A"])
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
        consensus+=frequentSymbol
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

    #print(allscore)
    return allscore


# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(1000):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs


Dna=[]
filename1 = input("Enter file name(Dna): ")
fileread1 = open(filename1,"r")

for i in fileread1:
    dna=i.strip()
    Dna.append(dna.upper())

k=int(input("what is the k:"))
t=len(Dna)

print(Dna,k,t)
print('\n'.join(RepeatedRandomizedMotifSearch(Dna, k, t)))

