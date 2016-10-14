Skew=input("sequence：")
Skew=Skew.upper()
G_C=[]
for i in range(len(Skew)+1):
    temp=Skew[0:i]
    C=temp.count("C")
    G=temp.count("G")
    print(G-C)
    G_C.append(G-C)

small=min(G_C)

result=[i for i, x in enumerate(G_C) if x ==small]
print (result)