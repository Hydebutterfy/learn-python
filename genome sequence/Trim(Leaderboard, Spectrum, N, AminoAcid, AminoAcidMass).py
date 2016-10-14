import re


def Trim(Leaderboard, Spectrum, N):
    LinearScores_dict={}
    for i in Leaderboard:
        score=LinearScore(i, Spectrum)
        LinearScores_dict[i]=score

    order_score=sorted(LinearScores_dict.values(), reverse=True)
    score=order_score[N-1]

    top_Leaderboard=[]
    for i in LinearScores_dict.keys():
        if LinearScores_dict[i]>=score:
            top_Leaderboard.append(i)

    return top_Leaderboard


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

def LinearScore(Peptide, Spectrum):
    new_Spectrum = Cyclospectrum(Peptide)
    score = 0

    for i in Spectrum:
        if i in new_Spectrum:
            new_Spectrum.remove(i)
            score += 1

    return score




dict_Cyclospectrum = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I": 113,
                      "L": 113, "N": 114,"D": 115, "K": 128, "Q": 128, "E": 129, "M": 131, "H": 137,
                      "F": 147, "R": 156, "Y": 163,"W": 186}

input_Spectrum = str(input("what is the Spectrum?"))
Spectrum = re.findall('\d+', input_Spectrum)
experimental_spectrum = [int(x) for x in Spectrum]

AA_str=str(input("what is the AA?"))
Leaderboard=AA_str.split()

N=int(input("what is the N?"))

print(Leaderboard,experimental_spectrum,N)
print(' '.join(Trim(Leaderboard, experimental_spectrum, N)))

