#list(itertools.product(bases, repeat=k))
import itertools
bases=['A','C','G','T']

p= int(input("waht is the position?"))
k=int(input("waht is the k?"))

patter_list=[''.join(i) for i in itertools.product(bases, repeat=k)]


print(patter_list[p])



