from math import log


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

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {}
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(0)

    Counts=Count(Motifs)
    #print(Counts)

    for symbol in "ACGT":
        for i in range(k):
            profile[symbol][i]=Counts[symbol][i]/t

    return profile



Motifs=[]
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in fileread:
    dna = i.strip()
    Motifs.append(dna.upper())

profile=Profile(Motifs)
Entropy=0
for i in range(len(Motifs[0])):
    #Entropy=((profile["A"][i])*log(profile["A"][i],2)+(profile["T"][i])*log(profile["T"][i],2)+(profile["C"][i])*log(profile["C"][i],2)+(profile["G"][i])*log(profile["G"][i],2))
    if profile["A"][i]!=0:
        a=-profile["A"][i]*log(profile["A"][i], 2)
    else:
        a=0
    if profile["T"][i] != 0:
        t = -profile["T"][i] * log(profile["T"][i], 2)
    else:
        t = 0
    if profile["C"][i] != 0:
        c = -profile["C"][i] * log(profile["C"][i], 2)
    else:
        c = 0
    if profile["G"][i] != 0:
        g = -profile["G"][i] * log(profile["G"][i], 2)
    else:
        g = 0
    Entropy+=a+t+c+g


#熵计算


print(profile,Entropy)
