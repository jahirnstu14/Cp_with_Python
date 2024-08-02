# Nice explanation : https://leetcode.com/problems/min-cost-climbing-stairs/discuss/1256616/C%2B%2BPython-Simple-Bottom-up-DP-From-O(N)-to-O(1)-space-Clean-and-Concise

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # dp[i] is minimum cost to reach to i_th floor
        for i in range(2, n + 1):
            jumpOneStep = dp[i - 1] + cost[i - 1]  # Minimum cost if we jump 1 step from floor (i-1)_th to i_th floor
            jumpTwoStep = dp[i - 2] + cost[i - 2]  # Minimum cost if we jump 2 steps from floor (i-2)_th to i_th floor
            dp[i] = min(jumpOneStep, jumpTwoStep)
        return dp[n]

# Example usage
sol = Solution()
cost = [10, 15, 20]
print(sol.minCostClimbingStairs(cost))  # Output: 15

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(sol.minCostClimbingStairs(cost))  # Output: 6
