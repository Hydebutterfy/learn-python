string=input("what is the string:")
k=int(input("what is the k:"))

profile={}
filename = input("Enter file1 name: ")
fileread = open(filename,"r")

for i in "ACGT":
    profile[i]=fileread.readline().split()

print(string,k,profile)

#print(profile["A"][0],profile["A"][1],profile["A"][2],profile["A"][3])
l=len(string)

Profile=[]
for i in range(l-k+1):
    Profile.append(1)
print(Profile)


for i in range(l-k+1):
    pattern=string[i:i+k]
    for j in range(k):
        Profile[i]=Profile[i]*float(profile[pattern[j]][j])

print(Profile)

max_profile=max(Profile)

position=Profile.index(max_profile)

print(string[position:position+k])


