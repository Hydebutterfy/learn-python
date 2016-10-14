#list(itertools.product(bases, repeat=k))
import itertools
bases=['A','C','G','T']

pattern= input("waht is the pattern")
k=len(pattern)

patter_list=[''.join(p) for p in itertools.product(bases, repeat=k)]
p=patter_list.index(pattern)


print(p)



