genome=input("sequence：").upper()

def Skew(genome):
    skew={}
    for i in range(len(genome)+1):
        temp=genome[0:i]
        C=temp.count("C")
        G=temp.count("G")
        #print(G-C)
        skew[i]=G-C
    #print(skew)
    return skew

#small=min(Skew(genome))

#result=[i for i, x in enumerate(skew) if x ==small]

print (Skew(genome))