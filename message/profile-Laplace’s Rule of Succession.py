Motifs=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in fileread:
    dna = i.strip()
    Motifs.append(dna.upper())


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    t=len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol=Motifs[i][j]
            count[symbol][j] += 1
    print (count)
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    print(t,k)

    profile = {}

    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(0)

    Counts=Count(Motifs)
    #print(Counts)

    for symbol in "ACGT":
        for i in range(k):
            profile[symbol][i]=Counts[symbol][i]/(t+4)

    return profile


print (Profile(Motifs))

#防止出现概率是O的情况,人为让每个碱基的初始数量是1.