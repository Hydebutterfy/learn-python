import re


def LCSBackTrack(v, w):
    # Initialize the matrices.
    n = len(v)
    m = len(w)
    #分数
    s = []
    for i in range(n + 1):
        s.append([])
        for j in range(m + 1):
            s[i].append(0)
    #方向
    Backtrack = []
    for i in range(n):
        Backtrack.append([])
        for j in range(m):
            Backtrack[i].append("")


    #print(s)
    #print(Backtrack)

#填充分数和方向
    for i in range(1, n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                s[i][j] = s[i-1][j-1]+1

            else:
                shu = s[i-1][j]-1
                heng=s[i][j-1]-1
                mismatch = s[i-1][j-1]-1
                s[i][j] = max(heng,shu,mismatch)




            if s[i][j] == s[i-1][j]-1:
                Backtrack[i-1][j-1] = "↓"

            elif s[i][j] == s[i][j-1]-1:
                Backtrack[i-1][j-1] = "→"

            elif s[i][j] == s[i-1][j-1]-1 or s[i][j] == s[i - 1][j - 1]+1:
                Backtrack[i - 1][j - 1] = "↘"



#获取最后一列的最大值，以及出现最大值的最早的位置
    i = max(enumerate(   [s[row][m] for row in range(m, n+1)] ), key=lambda x: x[1])[0]+ m  #为什么要加m，是因为基地是m，开始，但排序从0开始。
    max_score = str(s[i][m])


    print(s)
    print(max_score,i)
    print(Backtrack)
    return Backtrack,i,m


# Backtrack to start of the fitting alignment.

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def OutputLCS(backtrack,v,w,i,j):
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    #LCS_V=''
    #LCS_W=''
    #print(v,w,i,j)
    #global s
    #print(v,w,i,j)
    #print(backtrack)

    while i*j>0:
        print(i,j)
        print(backtrack[i][j])
        if backtrack[i][j] == "↓":
            i -= 1
            w = insert_indel(w, j+1)


        elif backtrack[i][j] == "→":
            j -= 1
            v = insert_indel(v, i+1)

        elif backtrack[i][j] == "↘":
            i-=1
            j-=1

        print(i,j)
        print(w)
        print(v)
    print(i,j)
    return v[i:],w





V= input("what is the v string:") # two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
W= input("what is the w string:")
#V="CGTGACTGGCTGATACTTTCTCCGTTATCCCTGTTCATTACAAATATATTAAAAGCGCTACCTGTGCTATTCATTTAGCCTCTCCCTCGTCGCCTAGGAACGTGAGAAGGGAAGCGAGATTCTAACCACGCACCGAGCTTCAGTGTACATCGGTACATCGTTACGGCATCCCTGATTTAAAGACGAAGTATGTTAAGCATCGGGCCGTGCGCTTGGCAGAGAAGTAATCGGGATGTAGCCGAAAAGGTTAGCACAGACTAGTCAGAAATCGTGTATTGCCTAAGCACTAAGAGAACGTGAAAGACCCGTATCGAGGGACAAGGGCACGGAAGTTAACACGACAGGGAAGGTCTCCCGCAGCTACCGCTATTATGGTGCCAGACAGGCGATATTTCCAGGACGCTGGTTAGTGCTTGGGAGAACGAGCGCAATATTTTTTGATGCTTCCATATCGACCAATTAATGACAATTTTAGATCCGGCACTCACCCTAGGCGGAGTCCATGAACTAAGGAATTCCAGCTGCTATTGCACCACCAATAATGACGTTCATTAGTGACGGAGCAAAGTGTGTTGTATCGTTAATGGTTATTTTCATGGGCTGTACATTAGGCGTAAGACCTAGCGGTAGGGCTGCTTTATGCAGGTACTCCCGTACTGAACAATAGCTACATCTGTTCGAGGACTCTCTGGGACCCTCCGTCCCCAGATCGAAGACCCCGACAGCAATACGTACACGAGTTTTTCCTGGCATTATCCTTAAGAATCAATGTGTCCAATCTTCTTCCTTTAATGCAGTAGAACGGTAGTGCGGGGGACGTGGATCCCTGGTGTGTTGGACTTGAAAGACTTGGTCGTTACTCCTTTGGATATCCG"
#W="GCAACTATCTACAGACCATAGGCAGAGGTCCATCGTGTACGTACAAGACTCTCGATCCCGGTTTTTTAAAGGGGAAAGCAAATGT"
#V="GTAGGCTTAAGGTTA"
#W="TAGATA"
Backtrack, n, m = LCSBackTrack(V, W)
#print(Backtrack,n,m)
print(V[:n],W,n-1,m-1)

print('\n'.join(OutputLCS(Backtrack,V[:n],W,n-1,m-1)))

