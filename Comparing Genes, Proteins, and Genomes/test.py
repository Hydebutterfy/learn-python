import re
#opening_penalty op
#extension penalty ep
def LCSBackTrack(v, w,op,ep):

    global s
    n = len(v)
    m = len(w)
    # Initialize the matrices.
    s=[     [   [0 for j in range(m+1)] for i in range(n+1)] for k in range(3)]
    Backtrack=[ [ [0 for j in range(m + 1)] for i in range(n+ 1)] for k in range(3)]


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












 def middle_column_score(v, w):
     global scoring_matrix_dict
     global penalty
     n=len(v)
     m=len(w)
     #'''Returns the score of the middle column for the alignment of v and w.'''
     # Initialize the score columns.
     S = [   [i*j*penalty for j in range(-1, 1)] for i in range(n+1)   ]
     S[0][1] = -sigma
     backtrack = [0]*(len(v)+1)

     # Fill in the Score and Backtrack matrices.
     for j in xrange(1, len(w)/2+1):
         for i in xrange(0, len(v)+1):
             if i == 0:
                 S[i][1] = -j*sigma
             else:
                 scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                 S[i][1] = max(scores)
                 backtrack[i] = scores.index(S[i][1])

         if j != len(w)/2:
             S = [[row[1]]*2 for row in S]

     return [row[1] for row in S], backtrack


def middle_edge(v,w):
    global scoring_matrix_dict
    global penalty
    #'''Returns the middle edge in the alignment graph of v and w.'''
    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle = middle_column_score(v,w)[0]

    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink, backtrack = map(lambda l: l[::-1], middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    # Get the componentwise sum of the middle column scores.
    scores = map(sum, zip(source_to_middle, middle_to_sink))

    # Get the position of the maximum score and the next node.
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)/2 + 1), (max_middle, len(w)/2 + 1), (max_middle + 1, len(w)/2),][backtrack[max_middle]]

    return (max_middle, len(w)/2), next_node

    # Print and save the answer.
    print ' '.join(map(str, middle))
    with open('output/textbook/Textbook_05K.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, middle)))



#获得打分矩阵
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
scoring_matrix=open("BLOSUM62.txt", "r")
first_line=scoring_matrix.readline()
# print(first_line.strip())
aa_list=first_line.split()
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

# Get the middle edge.
middle=middle_edge(V,W)

#print(Backtrack,n,m)
#print('\n'.join(OutputLCS(Backtrack,V,W,n,m)))

