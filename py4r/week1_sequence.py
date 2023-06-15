print((1, 2, 3)[-0])        # 0
print((1, 2, 3)[-0:0])      # ()


nums = [2, 4, 6, 10]
x = [12, 14, 16]
nums += x

nums.reverse()

# nums.sort()


sorted(nums)

nums = (1, "2", "three")
print(nums)

x = 12.1
y = 24.61

# packing tuple
coordinate = (x, y)
print(type(coordinate))            # tuple

# unpacking typle
c1, c2 = coordinate
e, r = coordinate

print(e, r)

coordinates = [(i*0.1, i*0.54) for i in range(1, 10)]
print(coordinates)

for (x, y) in coordinates:
    print(x, y)

x=(1,2,3)

print(x.count(3))

ids = set([1, 2, 3, 4])

word = "antidisestablishmentarism"
unique_letters = set(word)
print(unique_letters)
print(len(unique_letters), len(word))

x={1,2,3}
y={2,3,4}
print((x - y) | (y - x))

print(y - x)

x = {1, 2}
y = {1, 2}
print(x.issubset(y))
print(x in y)

age = {}            # initialize 1
age = dict()        # initialize 2


age = {'Rizo': 21, 'Yehia': 22}

age['Rizo'] += 1        # increasing value in dictionary

print(list(age.values()))
print(age.keys())

age['Osama'] = 22
print('Osama' in age)
print(22 in age)


L = [1, 2, 3]
M = list(L)

print(M is L)