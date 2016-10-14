__author__ = 'chenhaide'
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


def CountDict(Text, k,d): #建立字典记录每一个位置的计数结果
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = ApproximatePatternCount(Text,Pattern,d)
    print(Count)
    return Count


def ApproximatePatternCount(Text, Pattern,d):   #计数patten 在序列中的数量
    try:
        text_len = len(Text)
        pattern_len = len(Pattern)
        count = 0
        for i in range(text_len - pattern_len + 1):
            if HammingDistance(Pattern,Text[i:pattern_len + i])<=d:
                count = count+1

        return count

    except:
        print("Something wrong in the input")


def max(list):   #取字典中的最大数值
    m=list[0]
    for item in list:
        if item > m:
            m = item
    print(m)
    return m


def FrequentWords(Text, k,d):  #主函数
    FrequentPatterns = []
    Count = CountDict(Text, k,d)
    m = max(list(Count.values()))
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    #return FrequentPatterns
    return remove_duplicates(FrequentPatterns)

def remove_duplicates(list): # 去处重复部分
    return set(list)


Text=str(input("enter your DNA sequence: "))
k=int(input("what is the K?"))
d=int(input("enter the mismatch:"))




print (' '.join(FrequentWords(Text, k,d) ))


#FrequentWords(Text, k)
#FrequentPatterns ← an empty set
#for i ← 0 to |Text| − k
#Pattern ← the k-mer Text(i, k)
#Count(i) ← PatternCount(Text, Pattern)
#maxCount ← maximum value in array Count
#for i ← 0 to |Text| − k
#if Count(i) = maxCount
#add Text(i, k) to FrequentPatterns
#remove duplicates from FrequentPatterns
#return FrequentPatterns


