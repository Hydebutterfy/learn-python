import itertools

def NumberToPattern(k,position):
    bases=['A','C','G','T']
    patter_list = [''.join(i) for i in itertools.product(bases, repeat=k)]
    return patter_list[position]

def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance


pattern=input("what is the pattern:")
d=int(input("what is the d:"))
k=len(pattern)
fre_pattern=[]
for i in range(4**k):
    pattern_temp=NumberToPattern(len(pattern),i)
    if HammingDistance(pattern_temp,pattern)<=d:
        fre_pattern.append(pattern_temp)


print(fre_pattern)
