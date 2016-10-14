reads=[]
filename = input("Enter file name: ")
fileread = open(filename,"r")

for i in fileread:
    read=i.strip()
    reads.append(read.upper())

k=len(reads[0])

Text=reads[0]
print(Text)

for i in range(1,len(reads)):
    print(Text[-k+1:],reads[i][:k-1])
    if Text[-k+1:]==reads[i][:k-1]:
        Text=Text+reads[i][k-1]

print(Text)

