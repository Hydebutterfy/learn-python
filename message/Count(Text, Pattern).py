__author__ = 'chenhaide'
dna=str(input("enter your DNA sequence: "))
pattern=str(input("enter your pattern:"))
text=len(dna)
Pattern_len=len(pattern)
count=0

for i in range(text-Pattern_len+1):
    a=dna[i:Pattern_len+i]
    if a==pattern:
        count=count+1

print(count)  #用于计算基因组组中特定片段的数量

