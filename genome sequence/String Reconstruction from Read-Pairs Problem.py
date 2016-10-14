#String Reconstruction from Read-Pairs Problem.txt
import re,random


def String(pattern):
    string=""
    for p in pattern[:-1]:
        string+=p[0]

    string+=pattern[-1]

    #print(string)
    return string


def cycle(dict, key,k):

    global g_first_list,g_second_list

    first_list=[]
    second_list=[]

    first_list.append(key[:k-1])
    second_list.append(key[-k+1:])
    #print(first_list,second_list)

    Prefix = key
    Suffix = "a"
    while key != Suffix:
        l = len(dict[Prefix][0])
        i = random.randint(0, l - 1)
        first_suffix = dict[Prefix][0][i]
        second_suffix = dict[Prefix][1][i]
        Suffix = first_suffix + second_suffix
        del dict[Prefix][0][i], dict[Prefix][1][i]
        first_list.append(first_suffix)
        second_list.append(second_suffix)
        Prefix = Suffix
    # print(Prefix,Suffix)

    mix = []
    for i in range(len(g_first_list)):
        mix.append(g_first_list[i]+g_second_list[i])

    position =mix.index(key)

    g_first_list= g_first_list[0:position]+first_list+g_first_list[position+1:]
    g_second_list=g_second_list[0:position]+second_list+g_second_list[position+1:]


    dict = {k: v for k, v in dict.items() if v!= [[], []]}

    mix = []
    for i in range(len(g_first_list)):
        mix.append(g_first_list[i] + g_second_list[i])

    if dict != {}:
        for i in dict.keys():
            if i in mix:
                next_key= i
                break

        cycle(dict,next_key,k)


def To_balance(dict):
    key_count_dict={}
    value_count_dict = {}
    value_first_list=[]
    value_second_list=[]


    for key in dict.keys():
        key_count_dict[key]=len(dict[key][0])
        value_first_list+=dict[key][0]
        value_second_list+=dict[key][1]

    #print(value_first_list)
    #print(value_second_list)

    key=[]

    for i in range(len(value_first_list)):
        key.append(value_first_list[i]+value_second_list[i])

    #print(key)

    for k in key:
        if k not in value_count_dict.keys():
            value_count_dict[k]=key.count(k)

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


def order_pattern(pattern,k):
    E_dict = {}
    for p in pattern:
        key=p[0][:-1]+p[1][:-1]
        value=[[],[]]
        value[0].append(p[0][1:])
        value[1].append(p[1][1:])

        if key not in E_dict.keys():
            E_dict[key]=value
        else:
            E_dict[key][0].append(value[0][0])
            E_dict[key][1].append(value[1][0])

    #print(E_dict)

    first,last = To_balance(E_dict)

    if last not in E_dict.keys():
        E_dict[last] = [[],[]]

    E_dict[last][0].append(first[:k-1])
    E_dict[last][1].append(first[k-1:])
    #print(E_dict)

    global g_first_list,g_second_list

    g_first_list.append(first[:k-1])
    g_second_list.append(first[k-1:])


    Prefix = first
    Suffix = "a"
    while first!= Suffix:
        l=len(E_dict[Prefix][0])
        i=random.randint(0,l-1)
        #print(l,i)
        first_suffix=E_dict[Prefix][0][i]
        second_suffix=E_dict[Prefix][1][i]

        Suffix=first_suffix+second_suffix
        #print(Prefix,Suffix)
        del E_dict[Prefix][0][i],E_dict[Prefix][1][i]
        g_first_list.append(first_suffix)
        g_second_list.append(second_suffix)
        Prefix = Suffix

    #print(g_first_list)
    #print(g_second_list)
    #print(E_dict)
    E_dict = {k: v for k, v in E_dict.items() if v!=[[],[]]}
    #print(E_dict)
    mix=[]
    for i in range(len(g_first_list)):
        mix.append(g_first_list[i]+g_second_list[i])
    #print(mix)

    if E_dict != {}:
        for i in E_dict.keys():
            #print(i)
            if i in mix:
                key = i
                #print("key=",key)
                break

        cycle(E_dict, key,k)

    return g_first_list[:-1],g_second_list[:-1]

def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    pattern=[]

    for i in range(len(GappedPatterns)):
        pattern.append([])
        pattern[i].append(GappedPatterns[i][:k])
        pattern[i].append(GappedPatterns[i][-k:])
    #print(firstpattern,secondpattern)
    #print(pattern)

    firstpattern,secondpattern=order_pattern(pattern,k)

    #print(firstpattern)
    #print(secondpattern)

    prefixstring=String(firstpattern)
    suffixstring=String(secondpattern)
    #print(prefixstring)
    #print(suffixstring)


    for i in range(k+d,len(prefixstring)):
        #print(prefixstring[i],suffixstring[i - k - d])
        if prefixstring[i]!=suffixstring[i-k-d]:
            return "a"
            #return "there is no string spelled by the gapped patterns"
    return prefixstring+suffixstring[-k-d:len(suffixstring)]


GappedPatterns=[]
g_first_list=[]
g_second_list=[]
filename = input("Enter file name: ")
fileread = open(filename, "r")

for i in fileread:
    read = i.strip()
    GappedPatterns.append(read.upper())

k=int(input("what is the k?"))
d=int(input("what is the d?"))

#print(GappedPatterns)

for i in range(100000):
    print_it=StringSpelledByGappedPatterns(GappedPatterns,k,d)
    if len(print_it)<5:
        g_first_list = []
        g_second_list = []
    else:
        print(print_it)
        break



#print(StringSpelledByGappedPatterns(GappedPatterns,k,d))