


def SymbolToNumber(base):
    if base=="A":
        return 0
    elif base=="C":
        return 1
    elif base=="G":
        return 2
    else:
        return 3


def PatternToNumber(Pattern):
    if Pattern =="":
        return 0
    symbol=Pattern[-1]
    Prefix=Pattern[0:-1]
    return 4*PatternToNumber(Prefix)+SymbolToNumber(symbol)



bases=['A','C','G','T']

pattern= input("waht is the pattern").upper()



print(PatternToNumber(pattern))



