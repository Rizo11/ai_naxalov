# file = open('test.txt', 'r')

# with open('py4r/meme1.jpeg', 'rb') as file:
#     for line in file:
#         # do something with each line
#         print(line.decode('utf-8'))  # strip() removes any whitespace at the beginning or end of the line


# with open('test.txt', 'a') as file:
#     file.write('Hello, world!\n')
#     file.write('This is a new line.\n')


# try:
#     with open("filename.txt", "r") as file:
#         # print("fdf")
#         # File operations here
# except FileNotFoundError:
#     print("File not found.")
# except PermissionError:
#     print("Permission denied.")

import os

# Absolute path
# file_path = "/path/to/filename.txt"

# Using os.path
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "filename.txt")

print(base_dir, file_path)


def process_line(line):
    # Process the line here, for example, convert it to uppercase
    print("line")
    return line.title()

def process_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            print("file")
            yield process_line(line.strip())


for i in process_file("test.txt"):
    print(i)


# Generate even numbers from 0 to 10
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# Generate a decreasing sequence
decreasing_sequence = list(range(10, 0, -2))
print(decreasing_sequence)


print(dir(str))

lst = ['s', 5, {}, set(), (1,)]
lst.extend((1, 2, 3))

print(len(lst))
print(lst.index(3, 2, len(lst)))
print(lst)


print(lst[::-1])
print(lst)

# while lst:
#     print(lst.pop())


from collections import namedtuple

# Example: Using a namedtuple to represent a Point
# Point = namedtuple('Point', ['x', 'y'])
# point_list = [Point(1, 2), Point(3, 4), Point(5, 6)]

# for i in point_list:
#     print(i.x)


string1 = "hello"
string2 = "123abc"
string3 = "_variable"
string4 = "if"

print(string1.isidentifier())  # True
print(string2.isidentifier())  # False
print(string3.isidentifier())  # True
print("string4".isidentifier())  # True


str = 'I eat food'
print(str.replace(' ', ','))
print(str)

print('x'.center(5, '*'))
print('x'.center(6, '*'))
print('x'.center(4, '*'))
