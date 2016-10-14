def ProfileMostProbablePattern(Text,Profile):
    l=len(Text)
    k=len(Profile["A"])
    profile_list=[]
    for i in range(l - k + 1):
        pattern = Text[i:i + k]
        profile_list.append(Pr(pattern, Profile,k))

    max_profile = max(profile_list)
    position = profile_list.index(max_profile)

    return Text[position:position + k]

def Pr(pattern, profile,k):
    temp_Profile=1

    for j in range(k):
        #print(float(profile[pattern[j]][j]))
        #print(temp_Profile)
        temp_Profile=temp_Profile*float(profile[pattern[j]][j])
        #print(temp_Profile)
    return temp_Profile

def Motifs(profile, Dna):
    l=len(Dna[0])
    k=len(Dna)
    all_motif=[]
    print(l,k)

    for i in range(k):
        string=Dna[i]
        all_motif.append(ProfileMostProbablePattern(string,profile))

    return all_motif



Dna=[]
filename1 = input("Enter file name(Dna): ")
fileread1 = open(filename1,"r")

for i in fileread1:
    dna=i.strip()
    Dna.append(dna.upper())

profile={}
filename2 = input("Enter file name(profile): ")
fileread = open(filename2,"r")

for i in "ACGT":
    profile[i]=fileread.readline().split()

print(profile, Dna)

print(Motifs(profile, Dna) )



#Write a function Motifs(Profile, Dna) that takes a profile matrix Profile corresponding to a list of strings Dna as input and returns a list of the Profile-most probable k-mers in each string from Dna. Then add this function to Motifs.py.
