class Dog:
    def __init__(self, name, age) -> None:
        self.ism = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.ism} {self.age}"

x = Dog('Qoplon', 7)
y = Dog('Tuzik', 7)


print(x.ism)
x.ism = 'tuzik'
print(x.ism)

print(dir(Dog))
print(dir(x))

print(x.__class__)
print(type(x))

print(x.__str__())

print(type(x) == type(y))
print(x.__class__ == y.__class__)