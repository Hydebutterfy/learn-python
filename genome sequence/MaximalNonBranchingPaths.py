#MaximalNonBranchingPaths(Graph)
#        Paths ← empty list
#        for each node v in Graph
#            if v is not a 1-in-1-out node
#                if out(v) > 0
#                    for each outgoing edge (v, w) from v
#                        NonBranchingPath ← the path consisting of the single edge (v, w)
#                        while w is a 1-in-1-out node
#                            extend NonBranchingPath by the outgoing edge (w, u) from w
#                            w ← u
#                        add NonBranchingPath to the set Paths
#        for each isolated cycle Cycle in Graph
#            add Cycle to Paths
#        return Paths
##
#A node v in a directed graph Graph is called a 1-in-1-out node if its indegree and outdegree are both
# equal to 1, i.e., in(v) = out(v) = 1.  We can rephrase the definition of a "maximal non-branching path"
# from the main text as a path whose internal nodes are 1-in-1-out nodes and whose initial and final nodes
# are not 1-in-1-out nodes.  Also, note that the definition from the main text does not handle the special
# case when Graph has a connected component that is an isolated cycle, in which all nodes are 1-in-1-out nodes.
#
#

#数字版
import re


def Count(dict):
    key_count_dict={}
    value_count_dict = {}
    value_list=[]

    for key in dict.keys():
        key_count_dict[key]=len(dict[key])
        value_list+=dict[key]
    #print(value_list)

    for i in value_list:
        if i not in value_count_dict.keys():
            value_count_dict[i]=value_list.count(i)

    for i in key_count_dict.keys():
        if i not in value_count_dict.keys():
            value_count_dict[i]=0
    for i in value_count_dict.keys():
        if i not in key_count_dict.keys():
            key_count_dict[i]=0


    #print(key_count_dict,value_count_dict)


    return key_count_dict,value_count_dict




def MaximalNonBranchingPaths(Graph):
    key_count_dict, value_count_dict = Count(Graph)
    #print(key_count_dict, value_count_dict)
    Paths=[]
    for i in Graph.keys():
        if value_count_dict[i]!=1 or key_count_dict[i]!=1:
            if value_count_dict[i]>0:
                for j in Graph[i]:
                    NonBranchingPath=[i]
                    NonBranchingPath.append(j)
                    while value_count_dict[j]==1 and  key_count_dict[j]==1:
                        NonBranchingPath+=Graph[j]
                        j=Graph[j][0]
                    Paths.append(NonBranchingPath)

    for i in Graph.keys():
        if value_count_dict[i]==0:
            isolated_cycle=[i]
            j=Graph[i][0]
            #print(j)
            isolated_cycle.append(j)
            #print(isolated_cycle)
            #print(key_count_dict[j],value_count_dict[j])
            while  key_count_dict[j]==1and value_count_dict[j]==1:
                isolated_cycle+=Graph[j]
                j=Graph[j][0]

            Paths.append(isolated_cycle)

    list=[]
    for i in range(len(Paths)):
        list+=Paths[i]


    for i in Graph.keys():
        if i not in list and key_count_dict[i]==1 and key_count_dict[i]==1:
            list.append(i)
            isolated_cycle = [i]
            j = Graph[i][0]
            isolated_cycle.append(j)
            list.append(j)
            while key_count_dict[j] == 1 and value_count_dict[j] == 1 and j!=i:
                isolated_cycle += Graph[j]
                j = Graph[j][0]
                list.append(j)

            Paths.append(isolated_cycle)


    #print(Paths)
    return Paths





Eulerian=[]
filename = input("Enter file name: ")
fileread = open(filename, "r")

for i in fileread:
    read = i.strip()
    Eulerian.append(read.upper())

#print(Eulerian)

E_dict = {}

for i in Eulerian:
    # print(i)
    temp_list = re.findall('\d+', i)
    # = [int(s) for s in i if s.isdigit()]
    # print(temp_list)
    key = temp_list[0]
    E_dict[key] = temp_list[1:]
#print(E_dict) #收集数据

print_list=MaximalNonBranchingPaths(E_dict)

for i in range(len(print_list)):
    temp_str=""
    for j in range(len(print_list[i])):
        temp_str+=print_list[i][j]+"->"
    print(temp_str[:-2])





#print(E_dict)
# print(first)
#g_list = []
#g_list.append(first)
# print(list)
#Prefix = first
#Suffix = "a"
#while first != Suffix:
#    Suffix = E_dict[Prefix][0]
    # print(Prefix,Suffix)
#    del E_dict[Prefix][0]
 #   g_list.append(Suffix)
 #   Prefix = Suffix

#print(g_list)

#E_dict = {k: v for k, v in E_dict.items() if v}
# for k in dict.keys():
#   if dict[k] == []:
#      del dict[k]  去处空键

#if E_dict != {}:
 #   for i in E_dict.keys():
  #      if i in g_list:
   #         key = i
    #        break

    #cycle(E_dict, key)



#print(g_list)
#print_pattrn = ""

#for i in g_list[0:-1]:
#    print(i)
 #   print_pattrn = print_pattrn + i + "->"

#print(print_pattrn[0:-2])



#Eulerianpattern(not balance).txt



#MaximalNonBranchingPaths(Graph).txt
# print(E_dict)