#StringSpelledByGappedPatterns(GappedPatterns, k, d)
#FirstPatterns ← the sequence of initial k-mers from GappedPatterns
# SecondPatterns ← the sequence of terminal k-mers from GappedPatterns
#PrefixString ← StringSpelledByGappedPatterns(FirstPatterns, k)
#SuffixString ← StringSpelledByGappedPatterns(SecondPatterns, k)
#for i = k + d + 1 to |PrefixString|
#     if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
#     return "there is no string spelled by the gapped patterns"
# return PrefixString concatenated with the last k + d symbols of SuffixString
#StringSpelledByGappedPatterns.txt
def String(pattern,k):
    string=""
    for p in pattern[:-1]:
        string+=p[0]

    string+=pattern[-1]

    #print(string)
    return string


def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    firstpattern=[]
    secondpattern=[]
    for pattern in GappedPatterns:
        firstpattern.append(pattern[:k])
        secondpattern.append(pattern[-k:])
    #print(firstpattern,secondpattern)

    prefixstring=String(firstpattern,k)
    suffixstring=String(secondpattern,k)

    print(prefixstring,suffixstring)
    for i in range(k+d,len(prefixstring)):
        if prefixstring[i]!=suffixstring[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return prefixstring+suffixstring[-k-d:len(suffixstring)]


GappedPatterns=[]
filename = input("Enter file name: ")
fileread = open(filename, "r")

for i in fileread:
    read = i.strip()
    GappedPatterns.append(read.upper())

k=int(input("what is the k?"))
d=int(input("what is the d?"))

print(GappedPatterns)

print(StringSpelledByGappedPatterns(GappedPatterns,k,d))