filename1 = input("Enter file1 name: ")

fileread1 = open(filename1,"r")


genome=fileread1.read().upper()


#file= input("Enter file name: ")
#fread = open(file,"r")
#genome=fread.read().upper()

k=int(input("k:"))
L=int(input("L:"))
t=int(input("t:"))


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


def Frequentarray(Text):  #主函数
    pattern_dict=dict()
    for i in range(L-k+1):
        if Text[i:i+k] in pattern_dict.keys():
            pattern_dict[Text[i:i+k]]=pattern_dict[Text[i:i+k]]+1
        elif reversecomplement(Text[i:i+k]) in pattern_dict.keys():
            pattern_dict[reversecomplement(Text[i:i+k])] = pattern_dict[reversecomplement(Text[i:i+k])] + 1

        else:
            pattern_dict[Text[i:i+k]]=1





    for key in pattern_dict.keys():
        if pattern_dict[key]>=t and key not in fre_pattern:
            fre_pattern.append(key)





fre_pattern=list()
length=len(genome)
for i in range(length-L+1):
    Text=genome[i:i+L]
    Frequentarray(Text)



print (fre_pattern)









