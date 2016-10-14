
p= int(input("waht is the position?"))
k=int(input("waht is the k?"))


def NumberToSymbol(index):
    if index==0:
        base="A"
    elif index==1:
        base="C"
    elif index==2:
        base="G"
    else:
        base="T"

    return base

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)

    prefixIndex=int(index/4)
    r=int(index%4)
    symbol=NumberToSymbol(r)
    PrefixPattern=NumberToPattern(prefixIndex, k-1)
    print (prefixIndex,r,PrefixPattern,symbol)
    return PrefixPattern+symbol

print (NumberToPattern(p,k))