filename1 = input("Enter file1 name: ")

fileread1 = open(filename1,"r")


genome=fileread1.read().upper()

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


def Frequentarray(Text,firstpattern,lastpattern):  #主函数


    if firstpattern in pattern_dict.keys():
        pattern_dict[firstpattern] = pattern_dict[firstpattern]-1

    else:#reversecomplement(firstpattern) in pattern_dict.keys()
        pattern_dict[reversecomplement(firstpattern)] = pattern_dict[reversecomplement(firstpattern)]-1


    relast=reversecomplement(lastpattern)
    if lastpattern in pattern_dict.keys():
        pattern_dict[lastpattern] = pattern_dict[lastpattern]+1
        if pattern_dict[lastpattern] >= t and lastpattern not in fre_pattern:
            fre_pattern.append(lastpattern)

    elif relast in pattern_dict.keys():
        pattern_dict[relast] = pattern_dict[relast] + 1
        if pattern_dict[relast] >= t and relast not in fre_pattern:
            fre_pattern.append(relast)

    else:
        pattern_dict[lastpattern]=1




fre_pattern=list()
length=len(genome)

pattern_dict=dict()
Text=genome[0:L]
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

firstpattern = Text[0:k]



for i in range(1,length-L+1):
    Text=genome[i:i+L]
    lastpattern=Text[L - k:L]
    Frequentarray(Text,firstpattern,lastpattern)
    firstpattern=Text[0:k]



print (fre_pattern)









