#    CyclopeptideSequencing(Spectrum)
#        Peptides ← a set containing only the empty peptide
#        while Peptides is nonempty
#            Peptides ← Expand(Peptides)
#            for each peptide Peptide in Peptides
#                if Mass(Peptide) = ParentMass(Spectrum)
#                    if Cyclospectrum(Peptide) = Spectrum
#                        output Peptide
#                    remove Peptide from Peptides
#                else if Peptide is not consistent with Spectrum
#                    remove Peptide from Peptides
#先一个,再在一个的基础上加一,每个检测mass是否在表中,筛选出2个,再在两个的上再加一\

#dict_Cyclospectrum = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I/L": 113, "N": 114,"D": 115, "K/Q": 128, "E": 129, "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186}


import re

def Expand(Peptides,aa_dict):
    peptides=[]
    #print(Peptides)
    for i in Peptides:
        for j in aa_dict.keys():
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


def CyclopeptideSequencing(Spectrum):
    global dict_Cyclospectrum
    Peptides=[]
    for i in Spectrum:
        if i in dict_Cyclospectrum.values():
            for j in dict_Cyclospectrum.keys():
                if dict_Cyclospectrum[j]==i and j not in Peptides:
                    Peptides.append(j)
    #print(Peptides)
    dict_Cyclospectrum = {k: v for k, v in dict_Cyclospectrum.items() if k in Peptides}
    #print(dict_Cyclospectrum)

    ParentMass=Spectrum[-1]
    #print(ParentMass)
    return_peptides=[]

    while Peptides!=[]:
        Peptides=Expand(Peptides,dict_Cyclospectrum)
        #print(Peptides)
        del_list=[]
        for Peptide in Peptides:
            #print("pep is ",Peptide)
            if mass(Peptide)==ParentMass:
                if Cyclospectrum(Peptide)==Spectrum:
                    return_peptides.append(Peptide)

                del_list.append(Peptide)

            elif mass(Peptide) not in Spectrum:
                del_list.append(Peptide)

        for i in del_list:
            Peptides.remove(i)

        #print(Peptides)

    return return_peptides


#print(dict_Cyclospectrum)
input_Spectrum=str(input("what is the Spectrum?"))
Spectrum=re.findall('\d+', input_Spectrum)
new_Spectrum=[int(x) for x in Spectrum]
#print(Spectrum,new_Spectrum)

dict_Cyclospectrum = {"G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101,
                      "C": 103, "I": 113, "N": 114, "D": 115, "K": 128, "E": 129,
                      "M": 131, "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186}

AA_list=CyclopeptideSequencing(sorted(new_Spectrum))
print(AA_list)
Spectrum_list=[]
l=len(AA_list[0])
for i in AA_list:
    temp_aa=i
    temp_Spectrum=""
    for j in range(l):
        temp_Spectrum+=str(dict_Cyclospectrum[i[j]])+"-"

    Spectrum_list.append(temp_Spectrum[:-1])

print(' '.join(Spectrum_list))



