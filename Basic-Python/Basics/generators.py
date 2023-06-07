def mygen():
    yield 1
    yield 2
    yield 3

g = mygen();
print(g)

for i in g:
    print(i)