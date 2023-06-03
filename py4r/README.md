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

### 1.1.2 Objects
- python has 2 operating modes:
    1. interactive : writing code in cells and running each cell
    2. standard : writing and running whole file
- python3 is not backword compatible
    Backward compatibility refers to the ability of a system, software, or protocol to function properly and support older versions or implementations. When a system is backward compatible, it ensures that newer versions or updates can work seamlessly with older versions or implementations without causing any compatibility issues or breaking existing functionality.
    
- python consists of objects
    - **mutable**: values can be changed after being created
    - **immutable**: values cannot be changed after being created/initialized
        
- `Module`: A module is a single file or script that contains reusable code. It typically consists of functions, classes, or variables that serve a specific purpose. Modules are used to organize code into logical units and promote code reusability. In many programming languages, modules can be imported and used in other scripts or programs to leverage their functionality.

- `Library`: A library (also known as a "software library" or "code library") is a collection of precompiled code modules that provide specific functionality or services. Libraries are designed to be reused by multiple programs or projects and can contain a set of modules or classes focused on a particular domain or purpose. Developers can include a library in their projects to access its functionality without having to rewrite the code from scratch.

- `Package`: A package is a directory or folder that contains multiple Python modules and possibly sub-packages. Packages are used to organize related modules and provide a hierarchical structure to manage larger codebases. A package typically includes an __init__.py file, which makes it a package in Python. Packages can be imported and used in Python scripts or projects to access the contained modules.

- `Framework`: A framework is a set of pre-written code and tools that provides a foundation or structure for building larger applications. It offers a reusable design or architecture, defines rules and conventions, and provides a collection of functions or classes for solving specific problems. Frameworks can include libraries, modules, and other components. They are typically more comprehensive and opinionated compared to libraries. Developers use frameworks to accelerate development by leveraging the pre-built components and established patterns they provide.

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
## Part 1.2

# Week 2: Python Libraries and Concepts used in Research
Introduction to Python modules commonly used in scientific computation, such as NumPy.

# Weeks 3 & 4: Case Studies
This collection of six case studies from different disciplines provides opportunities to practice Python research skills.

# Week 5: Statistical Learning
This new module covers linear and logistic regression as well as random forest regression and classification with an opportunity to practice Python research skills in a two-part case study.