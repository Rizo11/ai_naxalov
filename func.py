a = 4
def fn():
    # a += 1
    print(a)


fn()
print(a)

x = 45
for i in range(4):
    x = 3

# print(x)

print("============")
def f1(a, b, c):
    print(a)
    print(b)
    print(c)


print(f1(a=1, c=3, b=2))
print(f1(a=1, b=3, c=2))
    

def my_func(*args):
    print(args)

my_func('a', 'b', 'c', 'd')


def my_funct(**kwargs):
    print(kwargs)
print(my_funct(Age = 45, Job = 'Piper'))

print("**********")

def my_func(man, opt='default', *args, **kwargs):
    print("man:", man)
    print("opt:", opt)
    print("args:", args)
    print("kwargs:", kwargs)

my_func('mandatory value', 'a', 'b', 'c', name='Chris', age=33)

print("********************")
def my_func1(man, *args, opt='default', **kwargs):
    print("man:", man)
    print("args:", args)
    print("opt:", opt)
    print("kwargs:", kwargs)
my_func1('mandatory value', 'a', 'b', 'c', name='Chris', age=33)

x = 5
def fn1():
    x += 1
    print(x)

x = 4  
fn1()
