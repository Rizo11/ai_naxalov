def info(i):
    return len(i)

def max_even(i):
    if i%2 == 0:
        return i
    return 0

data = ["Python", "JS", 'C', 'HTML', "Mukhammadrizo"]

data_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(data, key=info))
print(max(data_num, key=(lambda i: i%2)))
print(max(data_num, key=max_even))

x = lambda x: x**2
print(list(map(lambda x: x**2, data_num)))

print(type(info))


# print(max(data_num, key=lambda i: i%2))


from functools import reduce
data_fib = [1, 1, 2, 3, 5]

n = 5

for i in range(n):
    print(reduce(lambda x,y: x+y, data_fib))

print(data_fib)
