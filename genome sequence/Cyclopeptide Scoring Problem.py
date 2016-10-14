import re
def Cyclospectrum(Peptide):
    global dict_Cyclospectrum

    longer_Peptide=Peptide+Peptide
    list_Cyclospectrum=[0]
    for i in range(1,len(Peptide)):
        for j in range(len(Peptide)):
            temp_aa=longer_Peptide[j:j+i]
            temp_Cyclospectrum=0
            #print(temp_aa)
            for k in temp_aa:
            #print(k)
                temp_Cyclospectrum+=dict_Cyclospectrum[k]
            list_Cyclospectrum.append(temp_Cyclospectrum)

    temp_Cyclospectrum=0
    for i in Peptide:
        temp_Cyclospectrum+=dict_Cyclospectrum[i]
    list_Cyclospectrum.append(temp_Cyclospectrum)
    #print(sorted(list_Cyclospectrum))
    return sorted(list_Cyclospectrum)


dict_Cyclospectrum = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
                      "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163,
                      "W": 186}

input_Spectrum=str(input("what is the Spectrum?"))
Spectrum=re.findall('\d+', input_Spectrum)
experimental_spectrum=[int(x) for x in Spectrum]

AA=input("what is the AA?")

new_Spectrum=Cyclospectrum(AA)
score=0

for i in experimental_spectrum:
    if i in new_Spectrum:
        new_Spectrum.remove(i)
        score+=1

print(score)

