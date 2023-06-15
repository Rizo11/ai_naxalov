def same_case(a, b): 
    # your code here
    if (not ((a >= 'A' and a <= 'Z') or (a >= 'a' and a <= 'z'))):
        return -1
    elif (not ((b >= 'A' and b <= 'Z') or (b >= 'a' and b <= 'z'))):
        return -1
    elif ((a > 'Z' and b > 'Z') or (a < 'a' and b < 'a')):
        return 1
    else:
        return 0



def max(a, b, c):
    if (a > b):
        if (a > c):
            return a
        return c
    else:
        if (b > c):
            return b
        return c


def expression_matter(a, b, c):
    if (a == b == c == 1):
        return 3
    
    k = [a, b, c]
    
    k.sort()
    
    if (k[0] == 1):
        return k[2]* (k[1] + k[0])
    
    else:
        return k[0]* k[1] * k[2]


strr = 'muhammadrizo'

print(len(strr))

def star(str):
    return '*'*len(str)

print(star("1"))
print(star("11"))

print("aasa\oooewlinedf\bjk")

print('\101')
print('\x411')



import string

print(string.digits)


print("fsdfdf fdf ts".title())


u = 6
a = "Even" if u%2 else "Odd"

print(a)