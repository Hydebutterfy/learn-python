
def global_alignment(v, w):
    global scoring_matrix_dict
    global penalty
    n=len(v)
    m=len(w)
    '''Returns the global alignment of v and w subject to the given scoring matrix and indel penalty sigma.'''

    # Initialize the matrices.
    S = [[0]*(m+1) for _ in range(n+1)]
    backtrack = [[0]*(m+1) for _ in range(n+1)]


    # Initialize the edges with the given penalties.
    for i in range(1, n+1):
        S[i][0] = -i*penalty
    for j in range(1, m+1):
        S[0][j] = -j*penalty


    # Fill in the Score and Backtrack matrices.
    for i in range(1, n+1):
        for j in range(1, m+1):
            scores = [S[i-1][j]-penalty,S[i][j-1]-penalty,S[i-1][j-1]+int(scoring_matrix_dict[v[i-1]+w[j-1]])]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Quick lambda function to insert indels.
    insert_indel =lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned,w_aligned =v,w

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j = len(v), len(w)
    max_score = str(S[i][j])

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in range(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in range(j):
        v_aligned = insert_indel(v_aligned, 0)

    return v_aligned, w_aligned

def middle_column_score(v, w):
    global scoring_matrix_dict
    global penalty
    #print(v,w)
    n=len(v)
    m=len(w)
    #print(type(m))
    #'''Returns the score of the middle column for the alignment of v and w.'''
    # Initialize the score columns.  列起始分数
    S = [ [i*j*penalty for j in range(-1, 1)] for i in range(n+1) ]
    S[0][1] = -penalty
    backtrack = [0]*(n+1)
    #print(S)
    #print(backtrack)


    # Fill in the Score and Backtrack matrices. 填充分数和路径
    #mid_m = m / 2 + 1      print(int(mid_m))
    for j in range(1, int(m/2+1)):
        for i in range(0, n+1):
            #print(j,i)
            if i == 0:
                S[i][1] = -j * penalty
            else:
                scores = [ S[i-1][0]+int(scoring_matrix_dict[v[i-1]+w[j-1]]),  S[i][0]-penalty, S[i-1][1]-penalty]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])
        #print(S)
        if j!= int(m/2):
            S=[  [row[1]]*2   for row in S]
        #print(S)

    #print(S)
    #print([row[1] for row in S])
    #print("?",backtrack)
    return [row[1] for row in S], backtrack





def middle_edge(v,w):
    global scoring_matrix_dict
    global penalty
    '''Returns the middle edge in the alignment graph of v and w.'''
    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    source_to_middle =middle_column_score(v,w)[0]


    # Get the score of the middle column from the middle to sink.  Reverse the order as the computations are done in the opposite orientation.
    middle_to_sink,  backtrack = map( lambda l: l[::-1],
                                      middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1])
                                      )

    # Get the componentwise sum of the middle column scores.
    #print(source_to_middle,middle_to_sink)
    scores =list(map(sum, zip(source_to_middle, middle_to_sink)))  #zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
    #print(scores)


    # Get the position of the maximum score and the next node.
    max_middle = max(range(len(scores)), key=lambda i: scores[i])
    #print(max_middle)


    if max_middle == len(scores) - 1:
        next_node = (max_middle, int(len(w)/2) + 1)

    else:
        next_node = [  (max_middle + 1, int(len(w)/2) + 1), (max_middle, int(len(w)/2) + 1),
                       (max_middle + 1, int(len(w)/2)),]  [backtrack[max_middle] ]


    #print(max_middle, int(len(w)/2))
    #print(next_node)
    return (max_middle, int(len(w)/2)), next_node



def space_efficient_global_alignment(v, w):
    '''Return the global alignment of v and w using a linear space algorithm.'''
    global scoring_matrix_dict
    global penalty

    def linear_space_alignment(top, bottom, left, right):
            '''Constructs the global alignment path using linear space.'''
            if left == right:
                return [v[top:bottom], '-'*(bottom - top)]

            elif top == bottom:
                return ['-'*(right - left), w[left:right]]

            elif bottom - top == 1 or right - left == 1:
                return global_alignment(v[top:bottom], w[left:right])


            else:
                # Get the middle edge and the corresponding nodes.
               mid_node, next_node = middle_edge(v[top:bottom], w[left:right])

               # Shift the nodes appropriately, as they currently don't alighn with the top/left starting points.
               mid_node = tuple(map(sum, zip(mid_node, [top, left])))
               next_node = tuple(map(sum, zip(next_node, [top, left])))

               # Get the character in each alignment corresponding to the current middle edge.
               # (Take the index modulo the string length to avoid IndexErrors if we reach the end of a string but still have -'s to append.)
               current = [['-', v[mid_node[0] % len(v)]][next_node[0] - mid_node[0]],
                          ['-', w[mid_node[1] % len(w)]][next_node[1] - mid_node[1]]]

               # Recursively divide and conquer to generate the alignment.
               A = linear_space_alignment(top, mid_node[0], left, mid_node[1])
               B = linear_space_alignment(next_node[0], bottom, next_node[1], right)
               return [A[i] + current[i] + B[i] for i in range(2)]

    # Get the alignment and alignment score.
    v_aligned, w_aligned =linear_space_alignment(0, len(v), 0, len(w))

    score = sum([-penalty if '-' in list(pair) else int(scoring_matrix_dict[pair[0]+pair[1]])  for pair in zip(v_aligned, w_aligned)    ]   )
    #for pair in zip(v_aligned, w_aligned):
    #    if '-' not in pair:
    #        print(scoring_matrix_dict[pair[0] + pair[1]])
    #        print(list(pair))

    return  str(score),v_aligned, w_aligned




#获得打分矩阵
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def main():
    global scoring_matrix_dict
    global penalty
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
    #print(len(scoring_matrix_dict))   打分矩阵


    #序列输入
    V = input("what is the v string:")
    W = input("what is the w string:")
    #V="PLEASANTLY"
    #W="MEANLY"
    penalty=5


    # Get the alignment.
    alignment = space_efficient_global_alignment(V, W)

    #输出结果
    # Print and save the answer.
    print('\n'.join(alignment))


if __name__ == '__main__':
    main()