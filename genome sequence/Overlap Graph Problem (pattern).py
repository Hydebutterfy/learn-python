reads=[]
filename = input("Enter file name: ")
fileread = open(filename,"r")

for i in fileread:
    read=i.strip()
    reads.append(read.upper())

k=len(reads[0])
n=len(reads)


def Prefix(pattern):
    #print(pattern[:k-1])
    return pattern[:k-1]
    #前缀

def Suffix(pattern):
    #print(pattern[1:k])
    return pattern[1:k]
    #后缀


for i in range (n):
    suffix=Suffix(reads[i])


    for j in range(n):

        if i !=j:
            prefix=Prefix(reads[j])
            if suffix==prefix:

                print(reads[i],"->",reads[j])


