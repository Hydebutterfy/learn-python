
def PatternCount(symbol, Text):
    return Text.count(symbol)


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


genome=input("what is the genome?")
symbol=input("what is the base?")

print(SymbolArray(genome,symbol))


#花费的时间:n次*[(n/2)次比较]=
