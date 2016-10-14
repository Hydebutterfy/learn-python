#k-Universal Circular String Problem: Find a k-universal circular string.
#     Input: An integer k.
#     Output: A k-universal circular string.
import re
import random


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






String_pattern= []
k=int(input("what is the k?"))
for i in range (2**k):
    #print (i)
    #print(str(bin(i))[2:].zfill(k))
    String_pattern.append(str(bin(i))[2:].zfill(k))

print(String_pattern)



E_dict = {}
for i in String_pattern:
    key=i[:-1]
    value=i[1:]
    if key not in E_dict.keys():
        E_dict[key]=[]

    E_dict[key].append(value)

print(E_dict) # 收集数据


#print(E_dict)
#print(first)

first = random.sample(E_dict.keys(), 1)[0]
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
print_pattrn = str(g_list[0])

for i in g_list[1:-k+1]:
    print_pattrn+=i[-1]

print(print_pattrn)

#for i in g_list[:-2]:
 #   print(i)
  #  print_pattrn = print_pattrn + i + "->"

#print(print_pattrn[0:-2])