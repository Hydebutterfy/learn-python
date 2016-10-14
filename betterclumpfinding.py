__author__ = 'chenhaide'
def Frequencyarray(Text,k):
    Count=[]
    for i in range(len(Text)-k+1):
        pattern=Text[i:i+k]
        Count.append(int(Text.count(pattern)))
    return Count



Genome=input("genome:")
k=int(input("k:"))
L=int(input("L:"))
t=int(input("t:"))


Frequentpatterns=[]####具体的序列
Temp=[]            ##number of
clump=[]           ##判定是否输出具体序列
Text=Genome[0:L]
Temp.extend(Frequencyarray(Text,k))

for i in range(len(Genome)-L):
    clump.append(0)


for i in range(len(Genome)-L):
    Text=Genome[i:i+L]
    temple=Frequencyarray(Text,k)


    for index in range(L-k+1):
        if int(temple[index])>=t:
            clump[i+index]=1

for i in range(len(Genome)-k+1):
    if clump[i]==1:
        Frequentpatterns.append(Genome[i:i+k])

Frequentpatterns=list(set(Frequentpatterns))

print (Frequentpatterns)