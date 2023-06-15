### Ternary operator
- `variable = true_statement if condition else false_statement`


# Data Types


## Sequence types
These are types that represent a sequence of values, such as strings, lists, tuples, and range objects.

### String
```python
s1 = 'Hello World'
s2 = "Hello World"
s3 = '''Hello World'''

s = s1 + s2         # Hello WorldHello World
s = s1 * 3          # Hello WorldHello WorldHello World

s1 = '41'
s2 = '14'
print (s1 > s2)     # True, comparison is done element by element in sequence types
```
- `len(object)` - returns the # of elements in object
```python
s = "code"
print(len(s) * '*')         # ****
```

- **escape sequence**
```python
print("This is a backslash: \\")
# Output: This is a backslash: \

print('She said, \'Hello.\'')
# Output: She said, 'Hello.'

print("He said, \"Hello.\"")
# Output: He said, "Hello."

print("He said, \"Hello.\"")
# Output: He said, "Hello."

print("This is a bell sound: \a")
# Output: This is a bell sound: [system beep]


print("This is a backspace: abc\bdef")
# Output: This is a backspace: abdef


print("Page 1\fPage 2\fPage3")
# Page 1
#       Page 2
#             Page3

print("This is a linefeed:\nHello")
# Output: This is a linefeed:
# Hello


print("This is a carriage return:\rHello")
# Output: Hellois a carriage return:

print("This is a tab:\tHello")
# Output: This is a tab:    Hello

```

### Lists

### Tuples

## Set types
These are types that represent an unordered collection of unique elements, such as set objects and frozenset objects.

## Mapping types
These are types that represent a collection of key-value pairs, such as dictionaries.

## Numeric types
These are types that represent numerical values, such as integers, floating-point numbers, and complex numbers.

## Boolean type
This type represents the truth values True and False.

## Binary types
These are types that represent binary data, such as bytes and bytearray objects.

## None type
This type represents a null or empty value and is represented by the keyword None.

## Integer
## Float
## String
## Boolean

### loops

## `range`
## `for`
```python
for i in iterable:
    print(i)

for i in 'string':
    print(i)

for i in [1, 2, 3, 4, 5]:
    print(i)
# output:
# 1
# 2
# 3
# 4
# 5
```

## `break` and `continue`

## 