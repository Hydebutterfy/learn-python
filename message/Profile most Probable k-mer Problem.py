#Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
# Input: A string Text, an integer k, and a 4 x k matrix Profile.
# Output: A Profile-most probable k-mer in Text.
def Pr(pattern, profile):
    temp_Profile=1
    for j in range(k):
        #print(float(profile[pattern[j]][j]))
        #print(temp_Profile)
        temp_Profile=temp_Profile*float(profile[pattern[j]][j])
        #print(temp_Profile)
    return temp_Profile



def ProfileMostProbablePattern(Text, k, Profile):
    l=len(Text)
    profile_list=[]
    for i in range(l - k + 1):
        pattern = Text[i:i + k]
        profile_list.append(Pr(pattern, Profile))

    max_profile = max(profile_list)
    position = profile_list.index(max_profile)

    return Text[position:position + k]



string=input("what is the string:")
Profile={}
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in "ACGT":
    Profile[i]=fileread.readline().split()

#print(string)
# print(Profile)
#print(profile["A"][0],profile["A"][1],profile["A"][2],profile["A"][3])
k=len(Profile["A"])

print(ProfileMostProbablePattern(string,k,Profile))




