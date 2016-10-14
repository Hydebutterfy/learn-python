import re

##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def ManhattanTourist(n, m, Down, Right):
    s=[]
    for i in range (n+1):
        s.append([])
        for j in range(m+1):
            s[i].append(0)

    #print(s)
    for i in range(1,n+1):
        s[i][0]=s[i-1][0]+Down[i-1][0]

    for j in range(1,m+1):
        s[0][j]=s[0][j-1]+Right[0][j-1]

    #print(s)
    for i in range (1,n+1):
        for j in range(1,m+1):
            c=[s[i-1][j]+Down[i-1][j],s[i][j-1]+Right[i][j-1]]
            s[i][j]=max(c)

    return s[n][m]



##^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
n=int(input("what is the N:"))
m=int(input("what is the M:"))

down=[]
for i in range(n):
    down.append([])

right=[]
for j in range(n+1):
    right.append([])

#print(down,right)


downread = open("down.txt","r")
count=0

for i in downread:
    temp1=i.strip()
    temp2= re.findall('\d+', temp1)
    down[count]= [int(x) for x in temp2]
    count+=1
print(down)

rightread=open("right.txt","r")
count=0
for i in rightread:
    temp1=i.strip()
    temp2= re.findall('\d+', temp1)
    right[count]= [int(x) for x in temp2]
    count+=1

print(right)

print(ManhattanTourist(n,m,down,right))


#输入n m() 16 10