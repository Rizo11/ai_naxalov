def sum_array(arr):
    if not arr or len(arr) == 1 or len(arr) == 2:
        return 0
    max = arr[0]
    min = arr[0]
    sum = 0
    
    for i in arr:
        if min == i or max == i: continue
        elif min > i or max < i:
            if min > i:
                sum += min
                min = i
            else:
                sum += max
                max = i
        else:
            sum += i
    return sum



# f = open('test.txt').read().split()
# f = [int(i) for i in f]
# print(sum(f))

f = open('test.txt', 'a')
f.append("Assalomu Alaykum")
