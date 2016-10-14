import random

Dna=[]
filename1 = input("Enter file name(Dna): ")
fileread1 = open(filename1,"r")

for i in fileread1:
    dna=i.strip()
    Dna.append(dna.upper())

k=int(input("what is the k:"))
t=len(Dna)

print(Dna,k,t)

def RandomMotifs(Dna, k, t):
    temp_Motifs = []
    l = len(Dna[0])
    print(l)

    for i in range(t):
        j=random.randint(0, l-k-1)
        print("j=", j)
        temp_Motifs.append(Dna[i][j:j+k])

    return temp_Motifs

print('\n'.join(RandomMotifs(Dna,k,t)))