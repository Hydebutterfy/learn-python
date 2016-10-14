Text=input("what is the text?")
k=int(input("what is the k?"))

list=[]

for i in range(len(Text)-k+1):
    list.append(Text[i:i+k])

print('\n'.join(list))

#CODE CHALLENGE: Solve the String Composition Problem.
#Input: An integer k and a string Text.
#   Output: Compositionk(Text) (the k-mers can be provided in any order).


