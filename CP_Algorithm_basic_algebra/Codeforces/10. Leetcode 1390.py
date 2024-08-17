# one solution 

class Solution:
    def divisors(self, n):
        div_count = 0
        div_sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                div_sum += i
                div_count += 1
                if div_count > 4:
                    return 0
        if div_count == 4:
            return div_sum
        return 0

    def sumFourDivisors(self, nums):
        ans = 0
        for num in nums:
            ans += self.divisors(num)
        return ans

# Function to get user input and call the Solution class
def main():
    # User input for the list of numbers
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the sumFourDivisors method and printing the result
    result = solution.sumFourDivisors(nums)
    print(f"The sum of divisors for numbers with exactly four divisors is: {result}")

if __name__ == "__main__":
    main()
    
    
# Another way of solution for this problem 

from typing import List
from math import sqrt, floor

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisor = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(num // i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                res += sum(divisor)
        return res

def main():
    # User input for the list of numbers
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))

    # Creating an instance of the Solution class
    solution = Solution()

    # Calling the sumFourDivisors method and printing the result
    result = solution.sumFourDivisors(nums)
    print(f"The sum of divisors for numbers with exactly four divisors is: {result}")

if __name__ == "__main__":
    main()































