g = zip("abc", [1, 2, 3], (4,)) 
for i in zip("asdf", [1, 2, 4], ('*', '-', '+')):
    print(i)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
matrixTr = list(zip(*matrix))
for i in matrixTr:
    print(i)

print(*matrix)


numbers = [1, 2, 3, 4, 5]

*a, b, c = numbers

print(a, b, c)


keys = ["name", "age", "country", "smth"]
values = ["Alice", 25, "USA"]

person = dict(zip(keys, values))
print(person)


print([1, 2] + [2])


def get_numbers():
    age = 29
    longitude = 45.55
    latitude = 12.67
    id = "fkfj43u38d"
    return age, longitude, latitude, id

a, *b, c = get_numbers()

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)



def multiply(a, b, c):
    return a * b * c

numbers = (2, 3, 4)
result = multiply(*numbers)

print(result)  # 24
