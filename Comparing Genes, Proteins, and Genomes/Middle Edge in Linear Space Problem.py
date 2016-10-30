

def middle_column_score(v, w):
    global scoring_matrix_dict
    global penalty
    print(v,w)
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

    print(S)
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
    middle_to_sink,  backtrack = map(    lambda l: l[::-1],
                                         middle_column_score(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1])
                                         )

    # Get the componentwise sum of the middle column scores.
    print(source_to_middle,middle_to_sink)
    scores =list(map(sum, zip(source_to_middle, middle_to_sink)))  #zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
    print(scores)


    # Get the position of the maximum score and the next node.
    max_middle = max(range(len(scores)), key=lambda i: scores[i])
    print(max_middle)


    if max_middle == len(scores) - 1:
        next_node = (max_middle, int(len(w)/2) + 1)

    else:
        next_node = [  (max_middle + 1, int(len(w)/2) + 1), (max_middle, int(len(w)/2) + 1),
                       (max_middle + 1, int(len(w)/2)),]  [backtrack[max_middle] ]


    print(max_middle, int(len(w)/2))
    print(next_node)
    return (max_middle, int(len(w)/2)), next_node




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
    #V = input("what is the v string:")
    #W = input("what is the w string:")
    V="PLEASANTLY"
    W="MEASNLY"
    penalty=5


    # Get the middle edge.
    middle=middle_edge(V,W)


    #输出结果  map函数是map(函数，参数），进行迭代。 原型：map(function, sequence)，作用是将一个列表映射到另一个列表，
    print( ' '.join(map(str, middle)))




if __name__ == '__main__':
    main()