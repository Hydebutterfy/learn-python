from math import log



profile={'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
Entropy=0
for i in range(12):
    #Entropy=((profile["A"][i])*log(profile["A"][i],2)+(profile["T"][i])*log(profile["T"][i],2)+(profile["C"][i])*log(profile["C"][i],2)+(profile["G"][i])*log(profile["G"][i],2))
    if profile["A"][i]!=0:
        a=-profile["A"][i]*log(profile["A"][i], 2)
    else:
        a=0
    if profile["T"][i] != 0:
        t = -profile["T"][i] * log(profile["T"][i], 2)
    else:
        t = 0
    if profile["C"][i] != 0:
        c = -profile["C"][i] * log(profile["C"][i], 2)
    else:
        c = 0
    if profile["G"][i] != 0:
        g = -profile["G"][i] * log(profile["G"][i], 2)
    else:
        g = 0
    Entropy+=a+t+c+g


#熵计算


print(Entropy)
