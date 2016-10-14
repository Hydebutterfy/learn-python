def Prefix(pattern):
    #print(pattern[:k-1])
    return pattern[:k-1]
    #前缀

def Suffix(pattern):
    #print(pattern[1:k])
    return pattern[1:k]
    #后缀


Text=input("what is the text?")
k=int(input("what is the k?"))

list=[]

for i in range(len(Text)-k+1):
    list.append(Text[i:i+k])

node=dict()

for edge in list:
    prefix = Prefix(edge)
    suffix = Suffix(edge)
    if prefix not in node.keys():
        node[prefix]=[]
        node[prefix].append(suffix)
    else:
        node[prefix].append(suffix)

print (node)

for key in node.keys():
    print(key,"->",','.join(node[key]))



