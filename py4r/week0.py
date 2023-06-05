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


class Person:
    species = "Human"  # Class variable shared among all instances

    def __init__(self, name, age):
        self.name = name  # Instance variable unique to each instance
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return self.name + " " + str(self.age)
    
    def __len__(self):
        return len(self.__str__())


# Creating instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing instance variables and calling instance methods
print(person1.name)  # Output: Alice
print(person2.age)  # Output: 30
person1.greet()  # Output: Hello, my name is Alice.

# Accessing class variable and calling class method
print(Person.species)  # Output: Human
print(person1.get_species())  # Output: Human

# Calling static method
print(Person.is_adult(25))  # Output: True
print(Person.is_adult(15))  # Output: False

# Calling special method
print(person1)
print(len(person1))



import numpy as np


x = np.array([1, 2, 3, 4, 5, 6])

x = "222222222222222222222222222222222222222222222222222222222222"
y = "222222222222222222222222222222222222222222222222222222222222"
print(x is y)