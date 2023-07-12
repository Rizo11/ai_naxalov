def frq():
    num = 15646
    freq = {}
    while num:
        digit = num%10
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
        num //= 10
    
    return freq

print(frq())

# from class_number_project import number
from number import *

n = Number(12321)
print("Get num", n.get_number())
print("is odd:", n.is_odd())
print("is even:", n.is_even())
print("is prime:", n.is_prime())
print("divisors:", n.get_divisors())
print("length:", n.get_length())
print("sum:", n.get_sum())
print("reverse:", n.get_reverse())
print("is palindrome:", n.is_palindrome())
print("digits:", n.get_digits())
print("max:", n.get_max())
print("min:", n.get_min())
print("avg:", n.get_average())
print("median:", n.get_median())
print("range:", n.get_range())
print("frequency:", n.get_frequency())



n = Number(29)
print("Get num", n.get_number())
print("is odd:", n.is_odd())
print("is even:", n.is_even())
print("is prime:", n.is_prime())
print("divisors:", n.get_divisors())
print("length:", n.get_length())
print("sum:", n.get_sum())
print("reverse:", n.get_reverse())
print("is palindrome:", n.is_palindrome())
print("digits:", n.get_digits())
print("max:", n.get_max())
print("min:", n.get_min())
print("avg:", n.get_average())
print("median:", n.get_median())
print("range:", n.get_range())
print("frequency:", n.get_frequency())