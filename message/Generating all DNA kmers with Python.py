#list(itertools.product(bases, repeat=k))
import itertools
bases=['A','C','G','T']

k = 2

print([''.join(p) for p in itertools.product(bases, repeat=k)])


