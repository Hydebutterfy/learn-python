
def Skew(genome):
    skew={}
    for i in range(len(genome)+1):
        temp=genome[0:i]
        C=temp.count("C")
        G=temp.count("G")
        #print(G-C)
        skew[i]=G-C
    #print(skew)
    return skew

def MinimumSkew(skew_dict):
    positions = [] # output variable
    max_GC=max(skew_dict.values())
    for key in skew_dict.keys():
        if skew_dict[key] == max_GC:
            positions.append(key)
    # your code here
    return positions


#genome=input("sequence：").upper()

filename1 = input("Enter file1 name: ")
fileread1 = open(filename1,"r")
genome=fileread1.read().upper()


skew_dict=Skew(genome)
print (skew_dict)

position=MinimumSkew(skew_dict)

print (position)

print(' '.join([str(i) for i in position]))



#result=[i for i, x in enumerate(skew) if x ==small]

