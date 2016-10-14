
import re


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

    #print(key_count_dict,value_count_dict)

    for key in key_count_dict.keys():
        if key not in value_count_dict.keys() or key_count_dict[key]>value_count_dict[key]:
            first=key
            break

    for key in value_count_dict.keys():
        if key not in key_count_dict.keys() or value_count_dict[key] > key_count_dict[key]:
            last = key
            break

    #print(first,last)

    return first,last




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
    #print(list)
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

#print(E_dict) # 收集数据


first,last= not_balance(E_dict)
#print(first,last)

if last not in E_dict.keys():
    E_dict[last]=[]

E_dict[last].append(first)


#print(E_dict)
#print(first)

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

#print(g_list)

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



#print(g_list)
print_pattrn =str(g_list[0])

for i in g_list[1:-1]:
    #print(i)
    print_pattrn = print_pattrn+i[-1]

print(print_pattrn)



#Eulerianpattern(not balance).txt




# print(E_dict)