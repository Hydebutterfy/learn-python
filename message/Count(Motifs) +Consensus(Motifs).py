
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
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

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m=0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

Motifs=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in fileread:
    dna = i.strip()
    Motifs.append(dna.upper())



print (Consensus(Motifs))