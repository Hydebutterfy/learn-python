import re

Source=input("what is the source:")
Sink=input("what is the sink:")


filename="path.txt"
fileread=open(filename, "r")
Path=[]
for i in fileread:
    read = i.strip()
    Path.append(read.upper())

#print(Path)

incoming={}  #点:上游点

outcoming={}  #点:下游点

Weight={}    #每段路径的值(固定)

score_point={} #点的值:
score_temp={}  #终点为某一点的值,有路径:值

Lu={}

arcs=[]  #路径
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

for i in Path:
    temp_list=re.findall('\d+', i)
    #print(temp_list)
    if temp_list[0] in outcoming.keys():
        outcoming[temp_list[0]].append(temp_list[1])
    else:
        outcoming[temp_list[0]]=[]
        outcoming[temp_list[0]].append(temp_list[1])

    if temp_list[1] in incoming.keys():
        incoming[temp_list[1]].append(temp_list[0])
    else:
        incoming[temp_list[1]]=[]
        incoming[temp_list[1]].append(temp_list[0])

    w_key=str(temp_list[0])+"->"+str(temp_list[1])
    Weight[w_key]=temp_list[2]
    score_temp[w_key]="0"

    if temp_list[0] not in score_point.keys():
        score_point[temp_list[0]]="0"
    if temp_list[1] not in score_point.keys():
        score_point[temp_list[1]]="0"

#print(incoming)
#print(outcoming)
#print(Weight)
#print(score_point)
#print(score_temp)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vertices=list(score_point.keys())
for key in vertices:
    if key not in incoming.keys():
        incoming[key]=[]


delete_list=[]
for i in outcoming.keys():
    if outcoming[i]==[] and i!=Sink:
        delete_list.append(i)
for i in delete_list:
    outcoming.pop(i)

#print(outcoming)
#print(incoming)
#print(Source,Sink)
#print(vertices)
#print(Weight)
#print(score_point)
#print(score_temp)


tempvalues=list(incoming.values())
#print(tempvalues)
#print(tempvalues.count([]))

while tempvalues.count([])>1:
    tempkey=list(incoming.keys())
    for i in tempkey:
        if incoming[i]==[] and i!=Source:
            #print(i)
            incoming.pop(i)
            if i in outcoming.keys():
                for j in outcoming[i]:
                    incoming[j].remove(i)
                outcoming.pop(i)

    tempvalues=list(incoming.values())

#去除不是source 和sink的相关输入输出。
#…………………………………………………………………………………………
#print(outcoming)
#print(incoming)
#print(Lu,arcs)

vertices=list(incoming.keys())

for key in incoming.keys():
    Lu[key]=""

for i in outcoming.keys():
    for j in outcoming[i]:
        temp=i+"->"+j
        arcs.append(temp)


delete_list=[]
for i in arcs:
    if i not in Weight.keys():
        delete_list.append(i)
for i in delete_list:
    Weight.pop(i)
    score_temp.pop(i)

print(Lu)
print(arcs)
print(vertices)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
while arcs!=[]:
    v=""
    for i in vertices:
        if incoming[i]==[]:
            for j in arcs:
                k=re.findall('\d+',j)
                if k[0]==i:
                    v=i
                    break
        if v==i:
            break

    print(v)
    print(vertices)
    #vertices.remove(v)
    #print(vertices)

    for u in outcoming[v]:
        #print(v,u)
        key=v+"->"+u
        score_temp[key]=str(int(Weight[key])+int(score_point[v]))
        if int(score_temp[key])>int(score_point[u]):
            score_point[u]=score_temp[key]
            Lu[u]=key

        arcs.remove(key)
        #print(arcs)

        incoming[u].remove(v)



    outcoming.pop(v)
    incoming.pop(v)
    vertices.remove(v)
    #print(outcoming,incoming)

    #print(outcoming[v])


#print(outcoming, incoming, Lu)
#print(Source, Sink, vertices)
#print(Weight, score_point, score_temp)
#print(Lu)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bestpath=Sink
v=Sink
#print(v)
while v!=Source:
    print(Lu[v])

    temp=re.findall('\d+',Lu[v])
    bestpath=temp[0]+"->"+bestpath
    v=temp[0]

print(bestpath)
print(score_point[Sink])




####


#Backtracking:
#BestPath = empty_set; // initialize
#v := Sink; // go from the sink backwards by marked arcs until v=Source
#Add L(v) to BestPath; // add the last arc of the best path ending at the current vertex
#v := B(L(v)); // go to the start vertex of this arc enduntil.
#Output BestPath.

# 用path, 参数是11 32(起点和终点)