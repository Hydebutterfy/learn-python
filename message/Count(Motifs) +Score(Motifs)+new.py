
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


Motifs=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in fileread:
    dna = i.strip()
    Motifs.append(dna.upper())

#k = len(Motifs[0])
#l=len(Motifs)


print (Score(Motifs))