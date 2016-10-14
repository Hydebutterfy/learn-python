__author__ = 'chenhaide'
Text=str(input("enter your DNA sequence: ")).upper()
k=int(input("what is the K?"))



def reverse_string(seq):
    return seq[::-1]


def complement(seq):
#return the complementary sequence string.
    basecomplement={"A":"T","C":"G","G":"C","T":"A","N":"N"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)


def reversecomplement(seq):
    #return the reverse complement of the dna string.
    seq=reverse_string(seq)
    seq=complement(seq)
    return seq


def PatternCount(Text, Pattern):   #计数patten 在序列中的数量
    try:
        text_len = len(Text)
        pattern_len = len(Pattern)
        count = 0
        for i in range(text_len - pattern_len + 1):
            a = Text[i:pattern_len + i]

            if Pattern == a or Pattern==reversecomplement(a):
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

    text_len= len(Text)
    pattern_dict = dict()
    fre_pattern=[]
    for i in range(text_len - k + 1):
        pattern_dict[Text[i:i + k]] = pattern_dict.get(Text[i:i + k], 0) + 1

    print(pattern_dict)

    max_value=max(list(pattern_dict.values()))

    for key in pattern_dict.keys():
        if pattern_dict[key]==max_value:
            fre_pattern.append(key)

    return fre_pattern


print (' '.join(FrequentWords(Text, k)))









