class Mobile:
    def __init__(self, color, mem) -> None:
        self.color = color
        self.memory = mem

    def getMemory(self, unit="GB"):
        if(unit == "GB"):
            return self.memory
        elif(unit == "KB"):
            return 1000000 * self.memory

x = Mobile("Blue", 256)
print(x.getMemory("KB"))
print(x.getMemory())


print(type(x))
print(x.memory, x.color)




class Person:
    def __init__(self, name) -> None:
        self.name = name


person = Person("Ali")
p1 = Person("Anvar")
p2 = Person("Shavkat")


p1 = Person("Anvar")
p2 = Person("Shavkat")
p3 = Person("Jasur")
persons = [p1, p2, p3]



class Person:
    def __init__(self, name, age ) -> None:
        self.name = name
        self.age = age

person = Person("Ali", 25)