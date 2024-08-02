# explanation link : https://takeuforward.org/data-structure/dynamic-programming-climbing-stairs/

# and another solution : https://leetcode.com/problems/climbing-stairs/discuss/25459/Memoization-with-recursion-top-down-approach-%2B-Dynamic-Programming-bottom-up

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        
        return b

# Example usage
sol = Solution()
print(sol.climbStairs(5))  # Output: 8
