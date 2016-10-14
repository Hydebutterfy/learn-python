



def middle_column_score(v, w):
    global scoring_matrix_dict
    global penalty
    n=len(v)
    m=len(w)
    #'''Returns the score of the middle column for the alignment of v and w.'''
    # Initialize the score columns.
    S = [   [i*j*penalty for j in range(-1, 1)] for i in range(n+1)   ]
    S[0][1] = -penalty
    backtrack = [0]*(len(v)+1)
    print(S)



def middle_edge(v,w):
    global scoring_matrix_dict
    global penalty
    #'''Returns the middle edge in the alignment graph of v and w.'''
    # Get the score of the middle column from the source to the middle.  The backtrack matrix is unnecessary here.
    #source_to_middle = \
    middle_column_score(v,w)
    #[0]





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
#V = input("what is the v string:")
#W = input("what is the w string:")

V="PLEASANTLY"
W="MEASNLY"
penalty=5
# Get the middle edge.
#middle=\
middle_edge(V,W)

#print(Backtrack,n,m)
#print('\n'.join(OutputLCS(Backtrack,V,W,n,m)))

