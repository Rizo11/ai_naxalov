from string import *

print(ascii_lowercase)
print(ascii_uppercase)


print("print(punctuation)       #", punctuation)
print("print(whitespace)        #", whitespace)
print("print(printable)         #", printable)

str = 'that day was June 15, 15:27'
print('str = \'that day was June 15, 15:27\'')
print('print(str.isalpha())     #', str.isalpha())
print('print(str.isdigit())     #', str.isdigit())
print('print(str.islower())     #', str.islower())
print('print(str.isupper())     #', str.isupper())
print('print(str.isspace())     #', str.isspace())
str = 'and'
print('print(str.isidentifier())    #', str.isidentifier())

text = "Hello, World!"
index = text.find("World"[1, 3])
print(index)  # Output: 7
