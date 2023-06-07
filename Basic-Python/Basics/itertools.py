# product ,permutation,combinations,accumulate,groupby and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate


a = [1,4,3,2]
b = [2,3]
prod = product(a,b)
perm = permutations(a)
comb =combinations(a,2)
acc = accumulate(a)
print(list(prod))
print(list(perm))
print(list(comb))
print(list(acc))