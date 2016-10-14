
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


pattern=input("what is the pattern:")
d=int(input("what is the d:"))


out_put=Neighbors(pattern,d)
for i in out_put:
    print(i)

print(out_put)
