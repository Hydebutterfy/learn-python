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





String_pattern= []
filename = input("Enter file name: ")
fileread = open(filename, "r")

for i in fileread:
    read = i.strip()
    String_pattern.append(read.upper())

#print(String_pattern)


E_dict = {}
for i in String_pattern:
    key=i[:-1]
    value=i[1:]
    if key not in E_dict.keys():
        E_dict[key]=[]

    E_dict[key].append(value)


print_list=MaximalNonBranchingPaths(E_dict)
print(print_list)


for i in range(len(print_list)):
    temp_str=print_list[i][0]
    for j in range(1,len(print_list[i])):
        temp_str+=print_list[i][j][-1]
    print(temp_str)

#Contig Generation Problem.txt