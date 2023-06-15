class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

obj1 = SingletonClass()
obj2 = SingletonClass()

print(obj1 is obj2)  # True


class MyClass:
    def __eq__(self, other):
        return NotImplemented

obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Output: NotImplemented
