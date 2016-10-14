__author__ = 'chenhaide'
Text=str(input("enter your DNA sequence: "))
k=int(input("what is the K?"))

def CountDict(Text, k): #建立字典记录每一个位置的计数结果
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text,Pattern)
    return Count


def PatternCount(Text, Pattern):   #计数patten 在序列中的数量
    try:
        text_len = len(Text)
        pattern_len = len(Pattern)
        count = 0
        for i in range(text_len - pattern_len + 1):
            a = Text[i:pattern_len + i]

            if Pattern == a :
                count = count + 1

        return count

    except:
        print("Something wrong in the input")


def max(list):   #取字典中的最大数值
    m=list[0]
    for item in list:
        if item > m:
            m = item
    return m


def FrequentWords(Text, k):  #主函数
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(list(Count.values()))
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return remove_duplicates(FrequentPatterns)

def remove_duplicates(list): # 去处重复部分
    return set(list)


print (' '.join(FrequentWords(Text, k) ))


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


