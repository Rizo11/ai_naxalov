s1 = '41'
s2 = '40'
print (s1 > s2)

s1 = [1, 2]
s2 = [2, 1]

print(s1 > s2)



# import time

# print("Counting down:")
# for i in range(10, 0, -1):
#     print(f"\r{i}", end="")
#     time.sleep(1)
# print("\rDone!")

print("This is a carriage return:\rHello")


print("This is a tab:\tHello")
# Output: This is a tab:    Hello


def is_palindrome(string):
    l = len(string)
    
    for i in range(l//2):
        if (string[i] != string[0-i-1]):
            return False
    return True

def remove_char(s):
    return s[1:len(s)-1]


print(remove_char("a"))


def is_square(n):
    import math
    return False if math.sqrt(n)*10%10 else True

print(is_square(25))
print(is_square(2))
print(is_square(4))


def count_sheeps(sheep):
    return sum(1 for x in sheep if x)

d = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

print(count_sheeps(d))


def mpg2lp100km(mpg):
    km = 1.609344
    l = 3.785411784
    mpg *= km
    mpg /= l
    
    return 100*mpg

print(mpg2lp100km(42))


def su(li, k, n):
    i = 0

    sum = 0
    while(i < len(li)):
        if (li[i] >= k and li[i] <= n):
            sum += li[i]
        i += 1

    return sum


print(su([1, 2, 3, 4], 1, 3))


def find_smallest_int(arr):
    arr.sort()
    return arr[0]

print(find_smallest_int([1, -2, 3, -4]))


def points(games):
    total_score = 0
    for i in games:
        game = i.split(':')
        x = int(game[0])
        y = int(game[1])
        if x > y:
            total_score += 3
        elif x == y:
            total_score += 1
            
    return total_score

points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])

def add_length(str_):
    arr = str_.split()
    res = []
    for i in arr:
        res.append(i + f' {len(i)}')
        
    return res

add_length('apple ban')

def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    return fib(n-1) + fib(n-2)

str_f = "18547707689471986212190138521399707760"
print(str_f[-1:-5])
print(str_f[25*(len(str_f) // 25):])

import math
def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (1-phi)**n) / math.sqrt(5))

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(100))

print(len([[1, 2, 3], [1, 2, 3]][0]))


def ant(grid, column, row, n, direction = 0):
    for i in range(n):
        val = grid[row][column]
        grid[row][column] = int(not grid[row][column])
        
        # white square
        if val:
            direction += 1
        else:
            if (direction - 1) >= 0:
                direction -= 1
            else:
                direction = 3
    
        direction %= 4
        
        # row
        if (direction % 2):
            # east
            if direction == 1:
                column += 1
                if (len(grid[0])-1 < column):
                    [i.append(0) for i in grid]
            # west
            else:
                if (column > 0):
                    column -= 1
                else:
                    # grid = [i.insert(0, 0) for i in grid]
                    [i.insert(0, 0) for i in grid]
                
        # col
        else:
            # north
            if direction == 0:
                if (row > 0):
                    row -= 1
                else:
                    l = len(grid[0])
                    grid.insert(0, [0 for i in range(l)])
            # south
            else:
                if (row+1 > len(grid)-1):
                    l = len(grid[0])
                    grid.append([0 for i in range(l)])
                row += 1
                
    return grid

grid = [
  [1,0,0,0,1,1,0,0,0,0],
  [0,0,0,0,1,1,1,1,0,0],
]

print(ant(grid, 4, 0, 10, 3))

