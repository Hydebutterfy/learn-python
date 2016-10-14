
#def PatternCount(symbol, Text):
 #   return Text.count(symbol)

def PatternCount(symbol, Text):
    text=len(Text)
    Pattern_len=len(symbol)
    count=0

    for i in range(text-Pattern_len+1):
        a=Text[i:Pattern_len+i]
        if a==symbol:
            count=count+1

    return count


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


genome=input("what is the genome?")
symbol=input("what is the base?")

print(FasterSymbolArray(genome,symbol))


#用C的变化来确定细菌基因组复制起始位点。 第一种方法。 也可以基于#G-#C的数量变化来确定。