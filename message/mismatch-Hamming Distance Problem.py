astring=input("string 1:")
bstring=input("string 2:")

print(len(astring),len(bstring))
def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance

print(HammingDistance(astring,bstring))


