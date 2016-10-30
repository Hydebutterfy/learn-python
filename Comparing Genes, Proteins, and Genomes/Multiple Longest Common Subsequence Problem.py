
def multiple_alignment_3(v, w, u):
    '''Returns the alignment of three sequences v, w, and u.'''
    # Initialize the matrices. 起始的矩阵
    S = [       [
                    [ 0 for k in range(len(u)+1)]
                    for j in range(len(w)+1)]
                for i in range(len(v)+1)]

    backtrack = [        [
                             [0 for k in range(len(u)+1)]
                             for j in range(len(w)+1)]
                         for i in range(len(v)+1)]


    # Fill in the Score and Backtrack matrices. 填充矩阵
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            for k in range(1, len(u)+1):
                scores = [S[i-1][j-1][k-1] + int(v[i-1] == w[j-1] == u[k-1]),
                          S[i-1][j][k],
                          S[i][j-1][k],
                          S[i][j][k-1],
                          S[i - 1][j-1][k],
                          S[i-1][j][k-1],
                          S[i][j-1][k-1]]
                backtrack[i][j][k], S[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    print(backtrack)

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned, u_aligned = v, w, u

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j, k = len(v), len(w), len(u)
    max_score = S[i][j][k]

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j*k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            u_aligned = insert_indel(u_aligned, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    # Prepend the necessary preceeding indels to get match lengths.
    while len(v_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        v_aligned = insert_indel(v_aligned, 0)
    while len(w_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        w_aligned = insert_indel(w_aligned, 0)
    while len(u_aligned) != max(len(v_aligned),len(w_aligned),len(u_aligned)):
        u_aligned = insert_indel(u_aligned, 0)

    return str(max_score), v_aligned, w_aligned, u_aligned




def main():

    #序列输入
    #V=input("what is the v string:")
    #W=input("what is the w string:")
    #U=input("what is the u string:")

    #V="GTTTAGATA"
    #W="ACAATTCG"
    #U="GGTGCTTTGA"
    V="TGTTTAAAAATGTCCGCAACCATTTC"
    W="GATATAAAACAGGGATAACTGCAATGG"
    U="CCTGCTACTTTATGCCGTCTCCATATGCG"




    # Get the alignment.
    alignment = multiple_alignment_3(V,W,U)

    #输出结果
    # Print and save the answer.
    print('\n'.join(alignment))


if __name__ == '__main__':
    main()
