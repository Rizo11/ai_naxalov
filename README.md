### Table of Contents
- [Week 1: Basics of Python 3](#week-1-basics-of-python-3)
  - [Part 1.1: Objects and Methods](#part-11-objects-and-methods)
    - [1.1.2 Objects](#112-objects)
    - [1.1.3 Modules and Methods](#113-modules-and-methods)
    - [1.1.4 Numbers and Basic Calculations](#114-numbers-and-basic-calculations)
    - [1.1.5 random.choice(seq)](#115-randomchoiceseq)
    - [1.1.6 Expressions and booleans](#116-expressions-and-booleans)
  - [Part 1.2: Sequence objects](#part-12-sequence-objects)
    - [1.2.1 Slicing](#121-slicing)
    - [1.2.2 Lists](#122-lists)
    - [1.2.3 Tuples](#123-tuples)
    - [1.2.4 Ranges](#124-ranges)
    - [1.2.5 Strings](#125-strings)
    - [1.2.5 Sets](#125-sets)
    - [1.2.6 Dictionaries :closed\_book:](#126-dictionaries-closed_book)
    - [1.2.7 JSON (Javascript Object Notation):bookmark: vs. Dictionary :closed\_book:](#127-json-javascript-object-notationbookmark-vs-dictionary-closed_book)
    - [1.2.8 File handling](#128-file-handling)
  - [Part 1.3: Manipulating objects](#part-13-manipulating-objects)
    - [Part 1.3.1 Dynamic Typing](#part-131-dynamic-typing)
  - [Part 1.4:](#part-14)
  - [Part 1.5:](#part-15)
- [Week 2: Python Libraries and Concepts used in Research](#week-2-python-libraries-and-concepts-used-in-research)
- [Weeks 3 \& 4: Case Studies](#weeks-3--4-case-studies)
- [Week 5: Statistical Learning](#week-5-statistical-learning)

# Week 1: Basics of Python 3
Review of basic Python 3 language concepts and syntax.
1. `yield`: used to create generator functions. The yield keyword is used to define the points at which the generator function should pause and "yield" a value

2. `generator function`: a type of function that can be paused and resumed, which allows it to generate a sequence of values rather then returning all of them at once

        1. create generator function with `yield`
        2. create a generator object
        3. iterate through to use return values

        - generator functions do not execute the body of the function immediately upon calling. Instead, they return a generator object that can be iterated over using a loop or by calling next() explicitly
        - genrators are usefull to deal with large datasets or when generating all values takes too much memory.
        - using generators you can generate values as you go and effectively deal with large or infinite sequences
    ```python
    def my_generator():
    yield 1
    yield 2
    yield 3

    # Create an instance of the generator
    gen = my_generator()

    # Retrieve values from the generator
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 3

    # another way
    for g in gen:
        print(g)

    # another way
    try:
    while True:
        value = next(gen)
        print(value)
    except StopIteration:
        pass
    ```
3.  `next()`: is used to retrieve the next item from an iterator. It is often used in conjunction with objects that implement the iterator protocol. Function takes an iterator as an argument and returns the next item in the sequence.

    ```python
    a, b = b, a + b

    #same as
    a = b
    b = a + b
    ```

## Part 1.1: Objects and Methods

### 1.1.1 Module, Package, Lib, Framework
- `Module`: A module is a single file or script that contains reusable code. It typically consists of functions, classes, or variables that serve a specific purpose. Modules are used to organize code into logical units and promote code reusability. In many programming languages, modules can be imported and used in other scripts or programs to leverage their functionality: any `.py` or `.c` file
<p align="center">
  <img src="/home/rizo/ai_naxalov/assets/mod_pkg.jpg" alt="Alt text">
</p>

- `Package`: A package is a directory or folder that contains multiple Python modules and possibly sub-packages.A package typically includes an __init__.py file, which makes it a package in Python.

<p align="center">
  <img src="/home/rizo/ai_naxalov/assets/pkg13.jpg
  " alt="Alt text">
</p>

- `Packages` are a collection of related `modules` that aim to achieve a common goal. Finally, the Python standard `library` is a collection of `packages` and `modules` that can be used to access built-in functionality.  For example, the `numpy` library is a collection of packages and modules that provides functionality for numerical computing in Python.

- `Framework`: A framework is a set of pre-written code and tools that provides a foundation or structure for building larger applications. It offers a reusable design or architecture, defines rules and conventions, and provides a collection of functions or classes for solving specific problems. Frameworks can include libraries, modules, and other components. They are typically more comprehensive and opinionated compared to libraries. Developers use frameworks to accelerate development by leveraging the pre-built components and established patterns they provide.


### 1.1.2 Objects
- python has 2 operating modes:
    1. interactive : writing code in cells and running each cell
    2. standard : writing and running whole file
- python3 is not *backword compatible*
    Backward compatibility refers to the ability of a system, software, or protocol to function properly and support older versions or implementations. When a system is backward compatible, it ensures that newer versions or updates can work seamlessly with older versions or implementations without causing any compatibility issues or breaking existing functionality.
    
- python consists of objects
    - **mutable**: values can be changed after being created
    - **immutable**: values cannot be changed after being created/initialized
- Each *python object* has the following characteistics
    * **Type**: represents objects category or class. It determines the behavior and operations that can be performed on the object. The `type()` function can be used to retrieve the type of an object. For example, `type(5)` returns `<class 'int'>`, indicating that the object is of type "integer".

    * **Value**: The value of an object represents the actual data stored in the object. It could be a number, a string, a list, or any other data that the object represents. For example, the value of a string object "Hello" is the sequence of characters "H", "e", "l", "l", and "o".

    * **Identity**: The identity of an object is a unique identifier associated with it. It distinguishes one object from another, even if they have the same type and value. The identity of an object is guaranteed to be unique during its lifetime. The id() function can be used to retrieve the identity of an object. For example, id("Hello") returns a unique identifier for the string object.
        ```python
        f = [1, 2, 3]
        g = f[:]
        print(id(f))    # 2994211457152
        print(id(g))    # 2994211497728

        g = f
        print(id(g))    # 2994211457152
        ```
    
- pythond objects have associated **attributes** and **behaviors**
    1. **Attributes**:
        *   *Instance Variables*: Objects can have **instance variables**, which are specific to each instance of the class. These variables store data unique to the object.
        *   *Class Variables*: are shared among all instances of a class. They are defined at the class level and hold data that is shared across instances.
    2. **Methods**:
        * Methods are functions defined within a class and are associated with objects of that class.
        * *Instance Methods*: These methods operate on specific instances of the class and can access instance variables and other instance-specific data.
        * *Class Methods*: Class methods are defined with the `@classmethod` decorator and operate on the class as a whole rather than specific instances. They can access class variables and perform operations related to the class itself.
        * *Static Methods*: Static methods are defined with the `@staticmethod` decorator and do not have access to instance or class-specific data. They are utility methods that are not tightly tied to a specific instance or class.
    3. **Special Methods (Magic Methods)**:
        * define how objects behave in specific situations. Examples include `__init__()` for object initialization, `__str__()` for string representation, `__len__()` for determining length, and many more.
    ```python
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

    ```
    ```python
    import numpy as np
    x = np.array([1, 2, 3, 4, 5])

    x.shape     # data attribute
    x.mean()    # method
    ```

- *singleton objects in python*
  - is an object that is intended to have only one instance throughout the program's execution
  - regardless of how many times you attempt to create an instance of a singleton object, you will always receive the same instance
  ```python
  class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    obj1 = SingletonClass()
    obj2 = SingletonClass()

    print(obj1 is obj2)  # True
  ```
  - built-in objects that are considered *singletons*
    1. `None`: The object representing the absence of a value.
    2. `True`: The object representing the boolean value "true".
    3. `False`: The object representing the boolean value "false".
    4. `NotImplemented`: The object representing the absence of implementation for a specific operation.
        ```python
        class MyClass:
            def __eq__(self, other):
                return NotImplemented

        obj1 = MyClass()
        obj2 = MyClass()

        print(obj1 == obj2)  # Output: NotImplemented
        ```
        * `MyClass` that overrides the `__eq__()` method, which is used for equality comparison (`==`). In this case, the implementation of the method simply returns `NotImplemented`
    5. `Ellipsis`: The object representing an ellipsis (...) used in slicing or indexing operations to indicate a range or omission of elements
       ```python
        my_list = [1, 2, 3, 4, 5]
        print(my_list[1:3])         # Output: [2, 3]
        print(my_list[1:3, ...])    # Output: [2, 3, 4, 5]

        import numpy as np

        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # selects the second element from each row
        print(arr[..., 1])  # Output: [2, 5, 8]


       ``` 

### 1.1.3 Modules and Methods

- **Namespace**
    - is a container that holds identifiers (variable names, function names, class names, etc.) and maps them to corresponding objects.
    - provides a way to organize and differentiate names to avoid naming conflicts and provide a logical structure to your code
    ```python
    import math
    import numpy as np

    # 2 lines below do the same thing
    math.sqrt(4)
    np.sqrt(4)

    # but np is more powerful
    np.sqrt([1, 2, 3, 4])
    # array([1.        , 1.41421356, 2.        ])
    ```
    1. *Global namespaces*
        ```python
        # Global Namespace
        PI = 3.14

        def calculate_area(radius):
            return PI * (radius ** 2)

        ```
    2. *Local Namespace  (Function Namespace)*
        - Each function or method in Python has its own local namespace.
        The local namespace holds the names defined within the function.

        ``` python

        def greet(name):
            message = "Hello, " + name + "!"
            print(message)
        ```
    3. *Class Namespace*
        - holds the names defined within the class, such as methods and class variables.
        ```python
        class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def calculate_area(self):
            return self.length * self.width

        ```
    4. *Built-in Namespace*
        -  contains the names of built-in functions, types, and exceptions provided by Python
        ```python
        import math

        radius = 5
        circumference = 2 * math.pi * radius

        ```
- **Import**
    - provides access to names defined in the imported module, enabling you to use those names in your current code.
    - Here's what happens when you use `import` in Python:

        1. The Python interpreter locates the module: When you execute an `import` statement, Python searches for the specified module in the available locations. It checks the directories listed in the `sys.path` variable, which includes the current directory, standard library directories, and other paths specified in the environment.

        2. The imported module's `namespace` is created from the identifiers of module: Python creates a new `namespace` specific to the imported module. All the names defined in the module become attributes within this `namespace`, accessible using dot notation.

        3. code inside newly created `namespace` will be executed

        4. python uses name provided (np or numpy) to reference new `namespace` and identifiers are available using dotnotation

        ```python
        # math_operations.py

        def add(a, b):
            return a + b

        def multiply(a, b):
            return a * b

        ```

         ```python
        # main.py

        import math_operations

        result = math_operations.add(2, 3)
        print(result)  # Output: 5

        result = math_operations.multiply(4, 5)
        print(result)  # Output: 20
        ```
        - In this example, the import `math_operations` statement imports the module `math_operations.py`. The functions `add` and `multiply` defined in `math_operations.py` become accessible using the `math_operations` namespace.
- `dir()`
    - to get a list of names in the given object's namespace.
    ```python
    name = "Yehia"
    

    dir(name)
    # same as
    dir(str)
    ```
    - to learn more about specific function use `help()`
    ```Python
    help(np.sqrt)

    # not like
    # help(np.sqrt())
    ```


### 1.1.4 Numbers and Basic Calculations
- `int` in python has infinite precision
- The underscore `_` represents the result of the last executed statement in interactive mode
- `math.factorial(x)` - returns `x!`

### 1.1.5 random.choice(seq)
- returns random object from given sequence (nature of sequence doesn't matter)
    ```python
    import random

    random.choice([1, 2, 3, 4, 5, 6, 7])    # random number from given string

    random.choice("abcdefg")                # random string from given string
    ```

### 1.1.6 Expressions and booleans

- `True, False`
- *boolean operations*
    ```python
    and, or, not
    ```
- *comparison opertions* work on single objects or sequences (compares each element in sequence)
    ```python
    [1, 2, 3] >= [1, 2, 4]       # False
    [1, 2, 3] >= [1, 1, 1, 1]    # True
    [1, 2, 3] >= [1, 2, 3, 4]    # False
    ```
    - `==` (same value) compares the content of 2 objects
    ```python
    [1, 2] == [1, 2]    # True
    [1, 2] == [1, 3]    # False
    ```
    - `is` (same identity) compares the references, are they the same object or not, used for identity comparison
    ```python
    [1, 2] is [1, 2]            # False
    [1, 2] is [1, 3]            # False
    [1, 2] is not [1, 2]        # True


    x = [1, 2]
    y = x

    y is x                      # True

    y = x[:]
    
    x is y                      # False
    x == y                      # True
    ```
    - when comparing `float == int`, python converts the `int` to `float` and compares them
    - cases when `is` and `==` give the same result
      - [*Singleton Objects*](#112-objects-singleton-objects-in-python): singleton objects like `True`, `False`, and `None`, both operators will yield the same result because there is only one instance of each object.
      - 

## Part 1.2: Sequence objects

### 1.2.1 Slicing
```python
s = ['a', 'b', 'c']
s[0]        # 'a'
s[-1]       # 'c'

print((1, 2, 3)[-0])            # 0
print((1, 2, 3)[-0:0])          # ()

my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:-1]      # [2, 3, 4]

sliced_list = my_list[-3:]       # [3, 4, 5]

my_list[::-1]                    # [5, 4, 3, 2, 1]
```
### 1.2.2 Lists
```python
nums = [2, 4, 6, 8]

nums[-1]        # 8

nums[-1] = 10       # [2, 4, 6, 10]

# concatenation
x = [12, 14, 16]
nums += x           # [2, 4, 6, 10, 12, 14, 16]

nums.reverse()      # [16, 14, 12, 10, 6, 4, 2]

nums.sort()         # [2, 4, 6, 10, 12, 14, 16]
                    # sorts the given list

sorted(nums)        # returns a new sorted list which was constructed from nums


len(nums)          # returns the length of a sequence

nums.append(4)      # appends 4 to the end of the list
# append, reverse, sort methods return nothing because they are
# in-place methods, meaning they alter the content of the original list. 
```
- mutable data structure
- `extend(iterable)`: addes the specified iterables to the end of the current list
- `index(element, start, end)`: returns the position at the first occurence of the specified value
  - `start` search from (including)
  - `end` till (excluding)
- `count(x)` return the number of times `x` appears in the list
- `pop()` remove last element from the list and return
- split9
```python
lst = ['s', 5, {}, set(), (1,)]

lst.extend((1, 2, 3))                 # ['s', 5, {}, set(), (1,), 1, 2, 3]

lst.index({})                         # 2
lst.count({})                         # 1

lst[::-1]                             # [3, 2, 1, (1,), set(), {}, 5, 's']

while lst:
    print(lst.pop())


# Example: Doubling each element in a list using map()
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))


from collections import namedtuple
# Example: Using a namedtuple to represent a Point
Point = namedtuple('Point', ['x', 'y'])
point_list = [Point(1, 2), Point(3, 4), Point(5, 6)]


# Example: Pairing values from two lists
# iterating multiple lists in once
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
pairs = list(zip(names, ages))


# returns a new sorted list, leaving the original list unchanged.
numbers = [5, 2, 8, 1, 4]
sorted_numbers = sorted(numbers)
```
  
### 1.2.3 Tuples
- immutable
- usually used to store heteregineous items
- usually used when you want to return more than one object in python function
- access by indexing
- 
```python
t = (1, 2, 5, 7)
s = 1, 2                # also tuple

len(t)                  # 4

print(t + (9, 11))      # Concatenation (1, 2, 5, 7, 9, 11)
print(s*3)              # Repetition (1, 2, 1, 2, 1, 2)
print(t[1])             # indexing 2
print(s in t)           # Membership False
print(1 in t)           # Membership True


# tuple methods
t.count(1)              # returns number of timers specified value is used in tuple
t.index(3)              # returns the index(closes to the beginning) of value in tuple

# packing unpacked numbers
a, c, b = 1, 2, 3       # a = 1
                        # b = 2
                        # c = 3
x = 12.1
y = 24.61

# packing tuple
coordinate = (x, y)
type(coordinate)            # tuple

# unpacking typle
(c1, c2) = coordinate       # c1 = 12.1
# c1, c2 = coordinate       # c2 = 24.61
coordinates = [(i*0.1, i*0.54) for i in range(1, 10)]
print(coordinates)

for (x, y) in coordinates:
    print(x, y)

c = (1, 2)
type(c)         # tuple

c = (1)
type(c)         # int

c = (1,)
type(c)         # tuple

c = 1,
type(c)         # tuple
```

- **`zip(iterator1, iterator2, iterator3 ...)`**
- takes iterables(0+) and aggregates them into tuple are return them
- powerful tool for iterating over multiple iterables simultaneously
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
countries = ["USA", "UK", "Canada"]

for name, age, country in zip(names, ages, countries):
    print(f"{name} is {age} years old and lives in {country}")

# Output:
# Alice is 25 years old and lives in USA
# Bob is 30 years old and lives in UK
# Charlie is 35 years old and lives in Canada


# Transposing matrix using zip()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
matrixTr = list(zip(*matrix))
for i in matrixTr:
    print(i)

# output:
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)


# Enumerating pairs: This allows us to print the index along with each item.
items = ["apple", "banana", "orange", "grape"]

for i, item in enumerate(items):
    print(f"Item {i+1}: {item}")
# output:
# Item 1: apple
# Item 2: banana
# Item 3: orange
# Item 4: grape


# Creating dictionaries
keys = ["name", "age", "country", "extra_key_without_value"]
values = ["Alice", 25, "USA"]

person = dict(zip(keys, values))
print(person)
# output:
# {'name': 'Alice', 'age': 25, 'country': 'USA'}
``` 

- Packing & Unpacking (**`*`**)
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


# Unpacking from a Function Return
def get_numbers():
    age = 29
    longitude = 45.55
    latitude = 12.67
    id = "fkfj43u38d"
    return age, longitude, latitude, id

a, *b, c = get_numbers()

print(a)  # 29
print(b)  # [45.55, 12.67]
print(c)  # fkfj43u38d


# Unpacking in Function Arguments
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
result = multiply(*numbers)

print(result)  # 24


```
### 1.2.4 Ranges
- Immutable sequences of integers
- `range(start, stop, step)`
```python
rng = range(5)
print(list(rng))        # [0. 1, 2, 3, 4]

# Generate even numbers from 0 to 10
even_numbers = range(0, 11, 2)

# Generate a decreasing sequence
decreasing_sequence = range(10, 0, -1)
```
### 1.2.5 Strings
- Immutable
```python
str = 'rizo`
print(str[-2:0])        # zo

# 3 * str = str + str + str = 'rizorizori'

dir(str)        # to see attributes of str

str.replace("this", "by this")      # returns a new changed string

str.split(" ")      # returns list

name = 'Ali'

name.upper()        # to make str uppercase
name.lower()        # to make str lowercase
```
- `string[start_included:stop_excluded]`
- `string[start_included:stop_excluded:step]`
- **String constants**
```python
import string

print(string.ascii_lowercase)       # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)       # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.digits)                # 0123456789
print(string.hexdigits)             # 0123456789abcdefABCDEF

print(punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# The whitespace constant includes spaces, tabs, newline characters, carriage returns, and other similar whitespace characters.
print(whitespace)        #  



print(printable)         # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```
- **string modification**
```python
str = 'that day was June 15, 15:27'

print(str.capitalize())         # That day was june 15, 15:27
print(str.title())              # That Day Was June 15, 15:27
print(str.upper())              # THAT DAY WAS JUNE 15, 15:27
print(str.lower())              # that day was june 15, 15:27

str.strip()                     # removes any whitespace at the beginning or end of the line

str = 'I eat food'
print(str.replace(' ', ','))    # return copy of string with all occurences of substr old remplaced by new
'x'.center(5, '*')

```
- **string check**
```python
str = 'that day was June 15, 15:27'
print(str.isalpha())                # False
print(str.isdigit())                # False
print(str.islower())                # False
print(str.isupper())                # False
print(str.isspace())                # False
str = 'and'
print(str.isidentifier())           # False
print("hello".isidentifier())       # True
print("123abc".isidentifier())      # False
print("_variable_".isidentifier())  # True
print("if".isidentifier())          # True
# used to check whether a given string is a valid identifier. An
# identifier is a name used to identify a variable, function,
# class, module, or any other object in Python
```
- **string search**
```python
name = "Emperor Palpatine"

# string.index(substr, start, end)returns the index of a substring inside the string.
# If the substring is not found, it raises an exception.
print(name.index('e'))          # 3

# string.find(substr, start, end) returns the index of first occurence of the substr.
# If not found, it returns -1
print(name.find('e'))           # 3

# string.cunt(substr, start, end) returns the number of non-overlapping
# occurences of substring sub in the range[start, end]
print(name.count('e'))          # 2
```

### 1.2.5 Sets
1. unordered collection of distinct hashable object
2. sets used for immutable objects like numbers and strings, not for dictionaries and lists
3. `set` **mutable**
4. `frozen set`  **immutable** after initialization
5.  cannot be indexed
6.  elements can't be duplicated
```python
ids = set()

ids = set([1, 2, 3, 4])

len(ids)        # 7

ids.add(5)      # {1, 2, 3, 4, 5}

x = {1, 2, 3, 4, 5}
d = {"one": 1, "two":2}
x.update(d)     # {1, 2, 3, 4, 5, 'one', 'two'}


ids.pop()       # removes arbitrary object from set and returns it

ids = set(range(0, 10))         # {0, 1, ... 9}

males = set([1, 2, 3, 4, 5])

# set difference operation
females = ids - males

# set unition
everyone = males | females

# intersection
both = everyone & females


word = "antidisestablishmentarism"
unique_letters = set(word)
print(len(unique_letters))
```
- `set.update(any_iterable)`
  - `list`, `set`, `tuple`, `dict`(`keys` will be added to `set`), `str`(`chars` will be added to `set`)
- `set.remove(element)`: remores specified element from the set
  - :red_circle: error if element doesn't exist
- `set.discard(element)`: remove element from the set
  - :heavy_check_mark: no errors if element doesn't exist
- the `x in y` operation checks whether `x` is a member of the set `y`, whereas the `x.issubset(y)` method checks whether all elements of `x` are also elements of `y`.
```python
x = {1, 2}
y = {1, 2}
print(x.issubset(y))        # True
print(x in y)               # False
```
### 1.2.6 Dictionaries :closed_book:
- mappings from `key` :key: objecs to `value` :lock: objects
- pair `{key: Immutable, value: anything}`
- used fastly to look up in unordered data
- not sequences, do not maintain order
```python

# CRUD
age = {}                        # initialize 1
age = dict()                    # initialize 2
print(type({}))                 # same as initialization of set, but this line will give dictionary type. To create empty set use set()

age = {'Rizo': 21, 'Yehia': 22}

age['Rizo'] += 1                # increasing value in dictionary

print(list(age.values()))       # [22, 22]
print(age.keys())               # dict_keys(['Rizo', 'Yehia'])

age['Osama'] = 21               # will autoatically add Osama to dict

age.get('Rizo', 0)              # get value of 'Rizo'. If not 'Rizo', return 0
age.get('Azamat')               # get value of 'Azamat'. If no 'Azamat', return None

age.pop('Rizo')                 # remove pair with value 'Rizo'. If not 'Rizo', raise exception
age.popitem()                   # remove last pair from dictionary, and return. If dict is empty, raise exception

# checking for membership
print('Osama' in age)
print(22 in age)


age={'Tim':29, 'Jim':31, 'Pam':27, 'Sam':35}
age[0]                          # error because there is no key 0 in the dictionary.
```
- `dict.keys()`: returns immutable list of type `<class 'dict_keys'>` containing dict keys.
- `dict.values()`: returns immutable list of type `<class 'dict_values'>` containing dict values
- `dict.items()`: returns immutable list of typles of type `<class 'dict_items'>` containing key-value pairs
```python
for i in dictionary:            # here you loop through dict keys
    i is dictionary key

for i, j in dictionary:         # to loops through key-value pairs
    i is key, j is value
```
### 1.2.7 JSON (Javascript Object Notation):bookmark: vs. Dictionary :closed_book:
1.  Syntax: Both defined using `{}` and `:`. But in `JSON` both side of `:` should be surrounded by double quotes(`""`)
```python
my_dict = {"key1": "value1", "key2": "value2"}

# JSON
{
  "key1": "value1",
  "key2": "value2"
}
```
2. `JSON` supports *strings*, *numbers*, *boolean* values, *null*, *arrays* (similar to Python lists), and *objects* (similar to Python dictionaries).
3. Accessing Data: In Python, you can use square brackets `[]` to access `dictionary` values. In `JSON`, you can access values using dot notation or square brackets.
```python
value = my_dict["key1"]
"value": my_json.key1
"value": my_json[key1]
```
4. `Dictionary` is a data type, while `JSON` is data representation (file).

- **Serialization** refers to the process of converting an object into a format that can be easily stored, transmitted, or reconstructed at a later time. In the context of programming, serialization is commonly used to convert complex data structures or objects into a serialized form, such as a string or binary representation, that can be saved to a file or sent over a network.

- from `python` to `JSON`:
  - `json.dumps(s)`
  - returns `str`
```python

# from json to python
import json

file = open('data.json', 'r')

data = file.read()

dictionary_py = json.loads(data)


# from python to json
json_obj = json.dumps(dictionary_py)
json_file = open("data.json", 'w')
json_file.write(json_obj)
json_file.close()
```

### 1.2.8 File handling
- `open(file_path, mode='r')`
  - `file_path` is *required* parameter which is for the pathname (*absolute* or *relative to the current working directory*) of the file
  - `mode` is *optional*. By default `r` - reading mode
```python
f = open('my_file.txt')
f = open('C:/MSI-GP-Leopard-75/ai/my_file.txt')


# with statement ensures that the file is properly closed after we're finished with it
with open('test.txt', 'r') as file:
    for line in file:
        # do something with each line
        print(line.strip())  # strip() removes any whitespace at the beginning or end of the line


# with statement ensures that the file is properly closed after we're finished with it
with open('test.txt', 'a') as file:
    file.write('Hello, world!\n')
    file.write('This is a new line.\n')
```
- `file_obj.read(size)`: to read data from `file object`. `size` is `int` to show how many `chars` to read from `file object`.
- `r` open file for read only
- `w` open file for write only (override)
- `a` open file for write only (append)
- `r+` open file for both reading and writing
- `x` create a new file
```python
try:
    with open('myfile.txt', 'x') as file:
        file.write('This is a new file.')
except FileExistsError:
    print('The file already exists.')
```
- `rb` binary mode (e.g images)
- **Best practives**
```python
# 1. use the `with` statement, also known as the `context manager`,
# which automatically takes care of closing the file after you're
# done with it. It ensures proper resource management and exception handling.
with open("filename.txt", "r") as file:
    # File operations here
# File is automatically closed outside the 'with' block


# 2. Specify the file encoding
with open("filename.txt", "r", encoding="utf-8") as file:
    # Read file contents


# 3. Exceptions
try:
    with open("filename.txt", "r") as file:
        # File operations here
        print("File found")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")


# use absolute or os.path for file path
import os

# Absolute path
file_path = "/path/to/filename.txt"

# Using os.path
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "filename.txt")      # /home/rizo/ai/filename.txt


# Validate file existence and permissions
import os

file_path = "filename.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK):
        with open(file_path, "r") as file:
            # Read file contents
    else:
        print("No read access to the file.")
else:
    print("File does not exist.")


# Use file iterators and generators: Python's file objects are
# iterable, so you can iterate over them line by line, which is
# memory-efficient for large files. Or use generator functions
with open("filename.txt", "r") as file:
    for line in file:
        # Process line

def process_line(line):
    # Process the line here, for example, convert it to uppercase
    return line.title()

def process_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield process_line(line.strip())


for i in process_file(file_path):
    # work with processed lines
```

## Part 1.3: Manipulating objects

### Part 1.3.1 Dynamic Typing
- Statically typed: type checking during compile-time
- Dynamically typed: type checking during run-time
- variable, object, reference `x = 3`
  1. create object `3`
  2. create a variable `x`
  3. reference `x` -> `3`
- variable names are always linked to objects not to other variables
- thus variable (`x`) is a reference to given object (`3`)
```python
# immutable objects
x = 3               # create object, create variable, assign a reference
y = x               # object exists, create variable, assign a reference. y is not referencing x, but 3
y = y - 1           # create obj 2, variable exists, assign a reference 
                    # y = 2
                    # x = 3

# mutable objects
l1 = [1, 2, 3, 4]       # create obj, create variable, reference obj
l2 = l1                 # obj created, create variable, reference that same obj.
l2[0] = 12              # l1 = [12, 2, 3, 4] 
                        # l2 = [12, 2, 3, 4]
```
- mutable objects might have the identical content but different ids
```python
l = [1, 2, 3]
m = [1, 2, 3]
print(l == m)               # True
print(l is m)               # False, because id(l) and id(m)


# creating copy without referencing 1 way
L = [1, 2, 3]
M = list(L)         # refer to different object

# creating copy without referencing 2 way
L = [1, 2, 3]
M = L[:]
```

## Part 1.4:

## Part 1.5:


# Week 2: Python Libraries and Concepts used in Research
Introduction to Python modules commonly used in scientific computation, such as NumPy.

# Weeks 3 & 4: Case Studies
This collection of six case studies from different disciplines provides opportunities to practice Python research skills.

# Week 5: Statistical Learning
This new module covers linear and logistic regression as well as random forest regression and classification with an opportunity to practice Python research skills in a two-part case study.