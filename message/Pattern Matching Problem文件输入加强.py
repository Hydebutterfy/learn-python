

filename1 = input("Enter file1 name: ")
filename2 = input("Enter file2 name: ")

fileread1 = open(filename1,"r")
fileread2 = open(filename2,"r")


dna=fileread1.read().upper()
pattern=fileread2.read().upper()



def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
       if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions


print(PatternMatching(pattern,dna))
print(' '.join([str(i) for i in PatternMatching(pattern,dna)]))

#seq3 和4