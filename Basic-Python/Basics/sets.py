# unorderded ,mutable,no duplicates
myset = set([1,2,3,"hellow"])


for i in myset:
    print(i)

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.pop()

print(my_set)
print(type(my_set))
for i in my_set:
    print(i)

odds = {1,3,5,7};
evens = {2,4,6,8};
primes = {2,3,5,7};
u = odds.union(evens)
print(u)
i = odds.intersection(primes)
print(i)