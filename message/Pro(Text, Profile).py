pattern=input("what is the string:")

profile={}
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in "ACGT":
    profile[i]=fileread.readline().split()

print(pattern,profile)

#print(profile["A"][0],profile["A"][1],profile["A"][2],profile["A"][3])
k=len(pattern)

def Pr(pattern, profile):
    Profile=1
    for j in range(k):
        print(float(profile[pattern[j]][j]))
        print(Profile)
        Profile=Profile*float(profile[pattern[j]][j])
        print(Profile)
    return Profile

print(Pr(pattern, profile))


