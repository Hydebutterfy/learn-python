import re
import sys
sys.setrecursionlimit(10000000)

def LCSBackTrack(v, w):
    n=len(v)
    m=len(w)
    Backtrack = []
    for i in range(n):
        Backtrack.append([])
        for j in range(m):
            Backtrack[i].append("")

    s = []
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

def OutputLCS(backtrack, v, i, j):
    global LCS

    if i <0 or j <0:
        return

    if backtrack[i][j]=="↓":
        OutputLCS(backtrack,v,i-1,j)

    elif backtrack[i][j]=="→":
        OutputLCS(backtrack,v,i,j-1)

    else:
        LCS+=v[i]
        OutputLCS(backtrack,v,i-1,j-1)


v=input("what is the V:")
w=input("what is the W:")

Backtrack,n,m=LCSBackTrack(v, w)
LCS=''
print(Backtrack,n,m)
print(OutputLCS(Backtrack,v,n-1,m-1))
print(LCS[::-1])

