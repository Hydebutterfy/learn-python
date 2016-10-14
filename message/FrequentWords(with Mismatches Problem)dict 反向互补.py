def reverse_string(seq):
    return seq[::-1]

def complement(seq):
#return the complementary sequence string.
    seq=seq.upper()
    basecomplement={"A":"T","C":"G","G":"C","T":"A","N":"N"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)

def reversecomplement(seq):
    #return the reverse complement of the dna string.
    seq=reverse_string(seq)
    seq=complement(seq)
    return seq

def HammingDistance(p, q):
    hamming_distance=0
    for i in range(len(p)):
        if p[i]!= q[i]:
            hamming_distance=hamming_distance+1
    return hamming_distance

def ApproximatePatternMatching(Pattern,Genome,d):
    count=0
    for i in range(len(Genome) - len(Pattern) + 1):
        if HammingDistance(Pattern,Genome[i:i+len(Pattern)])<=d:
            count+=1
    return count

def max(list):
    m=list[0]
    for item in list:
        if item > m:
            m = item
    print(m)
    return m


Text=str(input("enter your DNA sequence: ")).upper()
k=int(input("what is the K?"))
d=int(input("enter the mismatch:"))

pattern_dict=dict()
Frequentpattern=[]


for i in range(len(Text)-k+1):
    pattern=Text[i:i+k]
    if pattern not in pattern_dict.keys():
        pattern_dict[pattern]=ApproximatePatternMatching(pattern,Text,d)+ApproximatePatternMatching(reversecomplement(pattern),Text,d)

print(pattern_dict)
max_number=max(list(pattern_dict.values()))

for key in pattern_dict.keys():
    if pattern_dict[key]==max_number and key not in Frequentpattern:
        Frequentpattern.append(key)


print (Frequentpattern)












