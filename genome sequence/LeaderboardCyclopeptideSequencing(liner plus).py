import re
def Trim(Leaderboard, Spectrum, N):
    #print(Leaderboard)
    LinearScores_dict={}
    for i in Leaderboard:
        score=LinearScore(i, Spectrum)
        LinearScores_dict[i]=score

    order_score=sorted(LinearScores_dict.values(), reverse=True)
    #print(order_score)
    if len(order_score)>N:
        score=order_score[N-1]
    else:
        score=0

    top_Leaderboard=[]
    for i in LinearScores_dict.keys():
        if LinearScores_dict[i]>=score:
            top_Leaderboard.append(i)
    #print(top_Leaderboard)
    return top_Leaderboard


def LinearScore(Peptide, Spectrum):
    new_Spectrum = Cyclospectrum(Peptide)
    score = 0

    for i in Spectrum:
        if i in new_Spectrum:
            new_Spectrum.remove(i)
            score += 1

    return score

def Expand(Peptides):
    global dict_Cyclospectrum
    peptides=[]
    #print(Peptides)
    for i in Peptides:
        for j in dict_Cyclospectrum.keys():
            peptides.append(i+j)

    return peptides

def mass(Peptides):
    global dict_Cyclospectrum

    mass=0
    for i in Peptides:
        mass+=dict_Cyclospectrum[i]
    return mass


def Cyclospectrum(Peptide):
    global dict_Cyclospectrum

    list_Cyclospectrum = [0]
    for i in range(1, len(Peptide)):
        for j in range(len(Peptide) - i + 1):
            temp_aa = Peptide[j:j + i]
            temp_Cyclospectrum = 0
                # print(temp_aa)
            for k in temp_aa:
                    # print(k)
                temp_Cyclospectrum += dict_Cyclospectrum[k]
            list_Cyclospectrum.append(temp_Cyclospectrum)

    temp_Cyclospectrum = 0
    for i in Peptide:
        temp_Cyclospectrum += dict_Cyclospectrum[i]
    list_Cyclospectrum.append(temp_Cyclospectrum)
        # print(sorted(list_Cyclospectrum))
    return sorted(list_Cyclospectrum)
##--------------------------------------------------------------------------


##--------------------------------------------------------------------------

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    global dict_Cyclospectrum
    Leaderboard=["G","A","S","P","V","T","C","I","N","D","K","E","M","H","F","R","Y","W"]
    LeaderPeptide=Leaderboard[0]
    LeaderPeptide_dict={}
    ParentMass = Spectrum[-1]
    max=""
    #print(Leaderboard,LeaderPeptide,ParentMass)

    while Leaderboard != []:
        Leaderboard=Expand(Leaderboard)
        del_list = []

        for Peptide in Leaderboard:
            if mass(Peptide) == ParentMass:
                score=LinearScore(Peptide, Spectrum)
                if score> LinearScore(LeaderPeptide, Spectrum):
                    LeaderPeptide=Peptide
                    #if str(score) in LeaderPeptide_dict.keys():
                    #    LeaderPeptide_dict[str(score)].append(Peptide)
                    #else:
                    LeaderPeptide_dict[str(score)]=[Peptide]
                    max=str(score)
                elif score==LinearScore(LeaderPeptide, Spectrum):
                    LeaderPeptide_dict[str(score)].append(Peptide)

            elif mass(Peptide)>ParentMass:
                del_list.append(Peptide)

        for i in del_list:
            Leaderboard.remove(i)

        if Leaderboard !=[]:
            Leaderboard=Trim(Leaderboard, Spectrum, N)
    print("max",max)
    print(LeaderPeptide_dict)
    return LeaderPeptide_dict[max]

##--------------------------------------------------------------------------


dict_Cyclospectrum = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I": 113,
                      "N": 114, "D": 115, "K": 128,"E": 129, "M": 131, "H": 137,
                      "F": 147, "R": 156, "Y": 163, "W": 186}

input_Spectrum = str(input("what is the Spectrum?"))
Spectrum = re.findall('\d+', input_Spectrum)
experimental_spectrum = [int(x) for x in Spectrum]

N = int(input("what is the N?"))

AA_list=LeaderboardCyclopeptideSequencing(experimental_spectrum,N)

##--------------------------------------------------------------------------

#l=len(AA)
#temp_Spectrum=""
#for i in AA:
#    temp_aa=i

#    temp_Spectrum+=str(dict_Cyclospectrum[i])+"-"


#print(temp_Spectrum[:-1])
l=len(AA_list[0])
Spectrum_list=[]
for i in AA_list:
    temp_aa=i
    temp_Spectrum=""
    for j in range(l):
        temp_Spectrum+=str(dict_Cyclospectrum[i[j]])+"-"

    Spectrum_list.append(temp_Spectrum[:-1])

print(' '.join(Spectrum_list))
