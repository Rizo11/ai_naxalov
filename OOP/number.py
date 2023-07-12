class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        num = self.value
        for i in range(2, 1 + int(num**0.5)):
            if num % i == 0:
                return False
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        return [i for i in range(2, self.value+1) if self.value%i == 0]

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return sum([int(i) for i in str(self.value)])

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        num = str(self.value)
        for i in range(len(num)//2):
            if num[i] != num[-1-i]:
                return False
        return True

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [i for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max([i for i in str(self.value)])

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min([i for i in str(self.value)])

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        num = [int(i) for i in str(self.value)]
        return sum(num)/len(num)
    
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        rng = [i for i in str(self.value)]
        ln = len(rng)
        rng = [int(i) for i in str(self.value)]
        if ln%2 == 0:
            return (rng[ln//2] + rng[ln//2-1])/2
        else:
            return rng[ln//2]

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        rng = [int(i) for i in str(self.value)]

        return max(rng) - min(rng)

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        num = self.value
        freq = {}
        while num:
            digit = num%10
            if digit in freq:
                freq[digit] += 1
            else:
                freq[digit] = 1
            num //= 10
        
        return freq
        

# Create a new instance of Number
number = Number(3)
