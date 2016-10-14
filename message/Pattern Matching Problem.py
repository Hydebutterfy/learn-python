

dna=str(input("enter your DNA sequence: ")).upper()
pattern=str(input("enter your pattern:")).upper()


def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
       if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions


print(PatternMatching(pattern,dna))
print(' '.join([str(i) for i in PatternMatching(pattern,dna)]))