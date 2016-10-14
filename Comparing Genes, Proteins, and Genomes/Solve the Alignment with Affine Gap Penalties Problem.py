import re
#opening_penalty op
#extension penalty ep
def LCSBackTrack(v, w,op,ep):
    global scoring_matrix_dict
    global s
    n = len(v)
    m = len(w)


    # Initialize the matrices.
    s = [     [   [0 for j in range(m+1)] for i in range(n+1)] for k in range(3)]
    Backtrack = [ [ [0 for j in range(m + 1)] for i in range(n+ 1)] for k in range(3)]

    # Initialize the edges with the given penalties.
    for i in range(1, n+ 1):
        s[0][i][0] = -op - (i - 1) * ep   # low
        s[1][i][0] = -op - (i - 1) * ep    # mid
        s[2][i][0] = -10 * op             # up

    for j in range(1, m+1):
        s[2][0][j] = -op - (j - 1) * ep
        s[1][0][j] = -op - (j - 1) * ep
        s[0][0][j] = -10 * op

    # Fill in the scores for the lower, middle, upper, and backtrack matrices.
    for i in range(1, n+ 1):
        for j in range(1, m + 1):
            lower_scores = [s[0][i-1][j] - ep, s[1][i - 1][j] - op]  # 0:继续下  1：从mid转为下 i－1，j不变
            s[0][i][j] = max(lower_scores)
            Backtrack[0][i][j] = lower_scores.index(s[0][i][j])

            upper_scores = [s[2][i][j - 1] - ep, s[1][i][j - 1] - op]  # 0:继续横 1:从mid转为横，i 不变，j－1
            s[2][i][j] = max(upper_scores)
            Backtrack[2][i][j] = upper_scores.index(s[2][i][j])

            middle_scores = [s[0][i][j], s[1][i-1][j-1]+int(scoring_matrix_dict[v[i-1]+w[j-1]]), s[2][i][j]]
            s[1][i][j] = max(middle_scores)
            Backtrack[1][i][j] = middle_scores.index(s[1][i][j])   #0: 往下  1: mid， 2：横着
    print(s)
    return  Backtrack,n,m



def OutputLCS(backtrack,v,w,i,j):
# Initialize the values of i, j and the aligned sequences.
    global s
    # Get the maximum score, and the corresponding backtrack starting position.
    matrix_scores = [s[0][i][j], s[1][i][j], s[2][i][j]]

    max_score = max(matrix_scores)

    backtrack_matrix = matrix_scores.index(max_score)

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]


    # Backtrack to the edge of the matrix starting bottom right.
    while i*j != 0:
        if backtrack_matrix == 0:  # Lower backtrack matrix conditions.
            if backtrack[0][i][j] == 1:
                backtrack_matrix = 1
            i -= 1
            w = insert_indel(w, j)

        elif backtrack_matrix == 1:  # Middle backtrack matrix conditions.
            if backtrack[1][i][j] == 0:
                backtrack_matrix = 0
            elif backtrack[1][i][j] == 2:
                backtrack_matrix = 2
            else:
                i -= 1
                j -= 1

        else:  # Upper backtrack matrix conditions.
            if backtrack[2][i][j] == 1:
                backtrack_matrix = 1
            j -= 1
            v= insert_indel(v, i)

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in range(i):
        w = insert_indel(w, 0)
    for _ in range(j):
        v= insert_indel(v, 0)

    print(max_score)

    return v, w






#获得打分矩阵
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

scoring_matrix = open("BLOSUM62.txt", "r")
first_line = scoring_matrix.readline()
# print(first_line.strip())
aa_list = first_line.split()
# print(aa_list)

scoring_matrix_dict = {}

for other_lines in scoring_matrix:
    temp_list2 = other_lines.split()
    for i in range(1, 21):
        key = aa_list[i - 1] + temp_list2[0]
        key_r = temp_list2[0] + aa_list[i - 1]
        if key not in scoring_matrix_dict.keys():
            scoring_matrix_dict[key] = temp_list2[i]
            scoring_matrix_dict[key_r] = temp_list2[i]


#print(scoring_matrix_dict)
#print(len(scoring_matrix_dict))

V = input("what is the v string:")
W = input("what is the w string:")
#V="PRTEINS"
#W="PRTWPSEIN"
Backtrack,n,m=LCSBackTrack(V, W,11,1)

print(Backtrack)
#print(Backtrack,n,m)

print('\n'.join(OutputLCS(Backtrack,V,W,n,m)))
