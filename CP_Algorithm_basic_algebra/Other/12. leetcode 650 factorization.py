class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until it is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSteps(18))  # Example output: 8
