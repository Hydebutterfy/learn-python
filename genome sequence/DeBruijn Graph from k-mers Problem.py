def Prefix(pattern):
    #print(pattern[:k-1])
    return pattern[:k-1]
    #前缀

def Suffix(pattern):
    #print(pattern[1:k])
    return pattern[1:k]
    #后缀


reads=[]
filename = input("Enter file name: ")
fileread = open(filename,"r")

for i in fileread:
    read=i.strip()
    reads.append(read.upper())

k=len(reads[0])
n=len(reads)



node=dict()

for edge in reads:
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



