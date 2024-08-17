# logic : Question Approach
# Now, we know we have 4 primes = {2, 3, 5, 7} and 5 evens = {0, 2, 4, 6, 8}

# if index == 0
# then there can be any of one evens at even position, so 5 ways
# ans = 5

# if index == 1
# then there was 1 even at index = 0, and at this odd index there can be one of 4 primes
# ans = 5* 4(this pos)

# if index == 2
# then at this even index there can be one of 5 evens
# ans = (5*4) * 5(this pos)

# so, continuing the pattern we can see, it's like, 5*4*5*4*5*4*5..... ans so on
# here no. of 4s = no. of odd positions = n/2
# no. of 5s = no. of even positions = (n-n/2)

# ans = pow(4,count4) * pow(5,count5)

class Solution:
    def __init__(self):
        self.p = int(1e9 + 7)

    # Function to calculate (x^y) % p efficiently
    def power(self, x, y):
        res = 1
        x = x % self.p  # Update x if it is more than or equal to p
        if x == 0:
            return 0

        while y > 0:
            # If y is odd, multiply x with the result
            if y & 1:
                res = (res * x) % self.p

            # y is even now
            y = y >> 1  # y = y // 2
            x = (x * x) % self.p

        return res

    def countGoodNumbers(self, n):
        count_of_4s = n // 2
        count_of_5s = n - count_of_4s
        ans = (self.power(4, count_of_4s) % self.p * self.power(5, count_of_5s) % self.p) % self.p
        return int(ans)

# Example usage:
sol = Solution()
print(sol.countGoodNumbers(50))  # Adjust the input value as needed
