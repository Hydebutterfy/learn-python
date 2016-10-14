import re

def LCSBackTrack(v, w):
    global scoring_matrix_dict
    n = len(v)
    m = len(w)

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
        s[i][0]=s[i-1][0]-5

    #print(m)
    for j in range(1,m+1):
        s[0][j]=s[0][j-1]-5
    # print(m)
    #print(s)

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if v[i - 1] == w[j - 1]:
                s[i][j] = s[i - 1][j - 1] + int(scoring_matrix_dict[v[i - 1] + w[j - 1]])

            else:
                heng = s[i][j - 1] - 5
                shu = s[i - 1][j] - 5
                mismatch = s[i - 1][j - 1] + int(scoring_matrix_dict[v[i - 1] + w[j - 1]])
                s[i][j] = max(heng, shu, mismatch)

            if s[i][j] == s[i - 1][j] - 5:
                Backtrack[i - 1][j - 1] = "↓"

            elif s[i][j] == s[i][j - 1] - 5:
                Backtrack[i - 1][j - 1] = "→"

            elif s[i][j] == s[i - 1][j - 1] + int(scoring_matrix_dict[v[i - 1] + w[j - 1]]):
                Backtrack[i - 1][j - 1] = "↘"
    print(s[n][m])
    print(s)
    return Backtrack, n, m

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def OutputLCS(backtrack,v,w,i,j):
    LCS_V=''
    LCS_W=''
    #print(v,w,i,j)

    while i>=0 and j>=0:
        if backtrack[i][j]=="↘":
            LCS_V+=v[i]
            LCS_W+=w[j]
            #print(i)
            i=i-1
            j=j-1
            #print(LCS_V,LCS_W)
        elif backtrack[i][j]== "→":
            LCS_V+="-"
            LCS_W+=w[j]
            j=j-1


        else:
            LCS_W+="-"
            LCS_V+=v[i]
            i=i-1

    print(i,j)

    while i<0 and j>=0:
        LCS_W+=w[j]
        LCS_V+="-"
        j=j-1

    while j<0 and i>=0:
        LCS_W+="-"
        LCS_V+=v[i]
        i=i-1


    return LCS_V[::-1],LCS_W[::-1]

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

Backtrack, n, m = LCSBackTrack(V, W)
print(Backtrack)
#print(Backtrack,n,m)
print('\n'.join(OutputLCS(Backtrack,V,W,n-1,m-1)))


#输入
#MDEFWYRFTAWNCIVENEMNGFQDRYKTINWTQEQETYMMNRGLMILDRRSLHEYPTRKNHCMTHLQEQGLSHKNVYFRHFLVRLTMQAGRVHEESTLGWWNKKDVIICWAMYFMWWKHMCIPTHFFDPFLWDCECHRSGKSSHEPKMNIQKYKIGHGYPEYNFCWKFFYRNPRFQHGVDDQHIMRHAEMEQTIITVNKREMYMQWFPCLWTDQFLYHRQFHRTQGTNSKGDCNVMLFYDKICQMFPCWIWSVICRWDVIVSALLLKCLYSNAGYRIDMYQFFTYKPQWSLEARYAVTYAKWMQTPMCAPDFINIQPINYRTGLQFGSVCFSQHHAMNSEEYVCCALKGDCFMYWTSPLNYYYDCAEFFMINCMHDDHADVMLRKWVQDRQFNQKCRAWYNWMFAVEEMISDMDQVVDECYYSWSVMVGRRKHMITWIGRGRRAQCFDQWVSRICGWCPDCTYKCRYCWVRGFIQNGLLCLEMELECVGYRCVSFWPVDAHWPKCRPVPSHLRHWTVSVLPKHPYWKKQRIWALEPFYKIVAKFYFCCLDLANFTQHMYIREIKKDVEYYKHTQRWCGLASRFGAWGTGDDELNMMSANRGVEDHKRVSSVSYVEARFNSSIQCIWCVFWLFLIKFPYIGWHGQQHGQKRKPCVSNWLDPKMKKTLWDNRSDYLGWCKHWLKNKWRMDCDAYIAYFYKCNWAGEQLPDLQCRAAFGEWTAHPKYAASCDNKSHGHVNYMTWQVTYCVCNSNHVMCVNYVFYVILGFEVRDWWACEGTQWAFQTHTEE
#YDEFWYRFTAWQIVENQDRRPFGTINWRGLMIDDRISLHEYPTFHCMTHLQEQGLARKNVWFRHFLHRDHHVFWEVYAQRRTMTHCSDKSIGNSGWWNKKDVITHRFCWAMYLHFMWWKHMCIPTHFFDPFRSQKSEMEPKMNQQKYKNGHGYPEYNFCWLIVLFFYRQPRFQHGWEDDGHIMRHTTGEKNFITVNKHEMGYMQWFPCLWTDEFLYHRQPVRTQGTVMLFYPGFDICQMSPCWIRLHSVWDVINCFYDKPSALLLKCLYSNAGYRIDMYQFFTYPEYKKNEDQWSLEARTAVTYALATQWMQTPMCAPDFINIQQINYHYVAPEENTGEQFGSVDYWFRQHHAMNSEEYESSMRKCCALKGLQGYNDCAEFCLHDDHADVMPRYYREKFHPRTQQFNHQCQKCRAWYWRHAVWMFAAEEMISDMDQLVDECFEPGELFYSWSVMVGPRKHMITWTAQNWESGRHHRAQCFHQGWCPDCTYKCRPFEGNLSRYWVRWGCIKCPTMIQNGLLCLEMMWARLECVGKGERCASQWPVDAHFELQGISGHPYQQCPWRAKIKPVPSHLRPINNYDCHPYARIWALPPFYKVAKFMFHCQLVEYYKHTQRWCGGAWGTGGICPNEYKQDELNMMSANRGVEDHKKVSVEIWCVFWLFLIKFLYIGWWKMKSVRFKDPKMKKNPWRMDCDAYIAYFYKCNWAGQQLPDQRMLPQAWQCRAACGEWTAHPKYATPFKMHVCTHCDGHVNVMTWCEMTYCVCWQYGLHASRNHVMCVNPVFCFWGACEGTQWAFQTHIEMFSKE









