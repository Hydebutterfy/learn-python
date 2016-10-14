# EulerianCycle(Graph)
# form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
# while there are unexplored edges in Graph
# select a node newStart in Cycle with still unexplored edges
# form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
# Cycle ← Cycle’
# return Cycle
#
#
# Eulerianpattern
import re
import random


def not_balance(dict):
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

    print(key_count_dict,value_count_dict)

    for key in key_count_dict.keys():
        if key not in value_count_dict.keys() or key_count_dict[key]>value_count_dict[key]:
            first=key
            break

    for key in value_count_dict.keys():
        if key not in key_count_dict.keys() or value_count_dict[key] > key_count_dict[key]:
            last = key
            break

    #print(first,last)

    return str(first),str(last)




def cycle(dict, key):
    global g_list
    list = []
    list.append(key)
    # print(list)
    Prefix = key
    Suffix = "a"
    while key != Suffix:
        Suffix = dict[Prefix][0]
        # print(Prefix,Suffix)
        del dict[Prefix][0]
        list.append(Suffix)
        Prefix = Suffix
    print(list)
    position =g_list.index(key)
    g_list = g_list[0:position] + list + g_list[position + 1:]

    dict = {k: v for k, v in dict.items() if v}
    # for k in dict.keys():
    #   if dict[k] == []:
    #      del dict[k]  去处空键

    if dict != {}:
        for i in dict.keys():
            if i in g_list:
                next_key= i
                break

        cycle(dict,next_key)



Eulerian = []
filename = input("Enter file name: ")
fileread = open(filename, "r")

for i in fileread:
    read = i.strip()
    Eulerian.append(read.upper())

# print(Eulerian)


E_dict = {}
for i in Eulerian:
    # print(i)
    temp_list = re.findall('\d+', i)
    # = [int(s) for s in i if s.isdigit()]
    # print(temp_list)
    key = temp_list[0]
    E_dict[key] = temp_list[1:]



# print(E_dict) 收集数据

first,last= not_balance(E_dict)
if last not in E_dict.keys():
    E_dict[last]=list(first)
else:
    E_dict[last].append(first)

print(E_dict)
# print(first)
g_list = []
g_list.append(first)
# print(list)
Prefix = first
Suffix = "a"
while first != Suffix:
    Suffix = E_dict[Prefix][0]
    # print(Prefix,Suffix)
    del E_dict[Prefix][0]
    g_list.append(Suffix)
    Prefix = Suffix

print(g_list)

E_dict = {k: v for k, v in E_dict.items() if v}
# for k in dict.keys():
#   if dict[k] == []:
#      del dict[k]  去处空键

if E_dict != {}:
    for i in E_dict.keys():
        if i in g_list:
            key = i
            break

    cycle(E_dict, key)



print(g_list)
print_pattrn = ""

for i in g_list[0:-1]:
    print(i)
    print_pattrn = print_pattrn + i + "->"

print(print_pattrn[0:-2])



#Eulerianpattern(not balance).txt




# print(E_dict)