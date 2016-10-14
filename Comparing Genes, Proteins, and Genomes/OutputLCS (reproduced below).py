import re

def LCSBackTrack(v, w):
    n=len(v)
    m=len(w)
    Backtrack = []
    for i in range(n):
        Backtrack.append([])
        for j in range(m):
            Backtrack[i].append("")

    s = []   #点的分数
    for i in range(n + 1):
        s.append([])
        for j in range(m + 1):
            s[i].append(0)

    #print(s)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if v[i-1]==w[j-1]:
                c=[s[i-1][j],s[i][j-1],s[i-1][j-1]+1]
                s[i][j]=max(c)

            else:
                s[i][j] = max([s[i - 1][j], s[i][j - 1]])

            if s[i][j]==s[i-1][j]:
                Backtrack[i-1][j-1]="↓"
            elif s[i][j]==s[i][j-1]:
                Backtrack[i-1][j-1]="→"
            elif s[i][j]==s[i-1][j-1]+1 and v[i-1]==w[j-1]:
                Backtrack[i-1][j-1]="↘"
    print(s)
    return Backtrack,n,m

#def OutputLCS(backtrack, v, i, j):
#    global seq

#    if i ==0 or j == 0:
#        return

#    if backtrack[i][j]=="↓":
#        OutputLCS(backtrack,v,i-1,j)
#    elif backtrack[i][j]=="→":
#        OutputLCS(backtrack,v,i,j-1)
#    else:
#        OutputLCS(backtrack,v,i-1,j-1)
#        seq=seq+v[i]
#        print(seq)

#def OutputLCS(backtrack, v, i, j):
#    LCS=''
#    while i>=0 and j>=0:
#        if backtrack[i][j]=="↘":
#            LCS+=v[i]
#            print(i)
#            i=i-1
#            j=j-1
#        elif backtrack[i][j]== "↓":
#            i=i-1

#        else:
#           j=j-1
            #LCS+="-"
#    return LCS[::-1]

def OutputLCS(backtrack, v, i, j):
    LCS=''
    while i>=0 and j>=0:
        if backtrack[i][j]=="↘":
            LCS+=v[i]
            print(i)
            i=i-1
            j=j-1
        elif backtrack[i][j]== "→":
            j=j-1

        else:
            i=i-1
            #LCS+="-"
    return LCS[::-1]



v=input("what is the V:")
w=input("what is the W:")


Backtrack,n,m=LCSBackTrack(v, w)
#seq=''
print(Backtrack,n,m)

print(OutputLCS(Backtrack,v,n-1,m-1))

