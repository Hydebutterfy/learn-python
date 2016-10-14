
def Skew(genome):
    skew={}
    skew[0]=0
    for i in range(1,len(genome)):
        if genome[i]=="G":
            skew[i]=skew[i-1]+1
        elif genome[i]=="C":
            skew[i]=skew[i-1]-1
        else:
            skew[i]=skew[i-1]
    #print(skew)
    return skew

def MinimumSkew(skew_dict):
    positions = [] # output variable
    min_GC=min(skew_dict.values())
    for key in skew_dict.keys():
        if skew_dict[key] == min_GC:
            positions.append(key+1)
    # your code here
    return positions


filename1 = input("Enter file1 name: ")
fileread1 = open(filename1,"r")

genome=str()
for line in fileread1:
    line = line.strip()
    genome=genome+line

#genome=fileread1.read().upper()

#print(genome)

#genome=input("sequence：").upper()
skew_dict=Skew(genome)
#print (skew_dict)

position=MinimumSkew(skew_dict)

print (position)

print(' '.join([str(i) for i in position]))

file2 = open('Salmonella_enterica-2.txt', 'w')
file2.write(genome)

file3 = open('Salmonella_enterica-3.txt', 'w')
file3.write(genome[position[0]:position[0]+500])





#result=[i for i, x in enumerate(skew) if x ==small]

# 用Salmonella_enterica.txt  3343701 3343705 3343706 3343707 3343708 3343709 3343710 3343714