def gen():
    yield 1
    yield 2
    yield 3

g = gen()
for i in g:
    print(i)


mList = [i for i in range(5)]
mIter = iter(mList)

print(next(mIter))
print(next(mIter))
print(next(mIter))
print(next(mIter))
print(next(mIter))


print("=======================")
def fibonacci(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

for f in fibonacci(10):
    print(f)

a = b = 1

a, b = b, a + b

print(a, b)

x = "Hello, world!" 
y = x[5:]
print(y)


f = [1, 2, 3]
g = f[:]
print(id(f))
print(id(g))

g = f
print(id(g))
