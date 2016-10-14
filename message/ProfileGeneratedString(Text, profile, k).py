import random

Text="AAACCCAAACCC"
n = len(Text)
profile={'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
k=2



def Pr(pattern, profile):
    Profile=1
    for j in range(k):
        #print(float(profile[pattern[j]][j]))
        #print(Profile)
        Profile=Profile*float(profile[pattern[j]][j])
        #print(Profile)
    return Profile

def Normalize(Probabilities):
    all_probability=0
    for i in Probabilities.keys():
        #print(i)
        all_probability+=Probabilities[i]
    #print(all_probability)
    for j in Probabilities.keys():
        Probabilities[j]=Probabilities[j]/all_probability


    return Probabilities

def WeightedDie(Probabilities):
    tem_p=random.uniform(0,1)
    #print(tem_p)
    check_p=0
    for i in Probabilities.keys():
        if Probabilities[i]+check_p>=tem_p>=check_p:
            return i
        check_p += Probabilities[i]

def ProfileGeneratedString(Text, profile, k):
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)

    probabilities=Normalize(probabilities)

    return WeightedDie(probabilities)

print(ProfileGeneratedString(Text, profile, k))