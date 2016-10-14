__author__ = 'chenhaide'

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


def PatternCount(Text, Pattern):

    try:
        print(Text)
        print(Pattern)
        text_len = len(Text)
        pattern_len = len(Pattern)
        count = 0
        for i in range(text_len - pattern_len + 1):
            a = Text[i:pattern_len + i]

            if Pattern == a or Pattern == reversecomplement(a):
                count = count + 1

        return count

    except:
        print("Something wrong in the input")




filename1 = input("Enter file1 name: ")
filename2 = input("Enter file2 name: ")

fileread1 = open(filename1,"r")
fileread2 = open(filename2,"r")


dna=fileread1.read().upper()
pattern=fileread2.read().upper()

number=PatternCount(dna, pattern)

print(number)  #用于计算基因组组中特定片段的数量,统一大小写,反向互补,序列来自文件


