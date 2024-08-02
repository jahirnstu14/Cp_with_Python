# same problem : https://takeuforward.org/data-structure/maximum-sum-of-non-adjacent-elements-dp-5/

# without dynamic programming with complexity 0(n)

def rob(nums):
    a, b = 0, 0
    
    for i in range(len(nums)):
        if i % 2 == 0:
            a = max(a + nums[i], b)
        else:
            b = max(a, b + nums[i])
    
    return max(a, b)

# Example input
nums = [1, 2, 3, 1]
print(rob(nums))  # Output: 4


# with dynamic programming 

# my favourite solution is : https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

# ✔️ Solution - II (Dynamic Programming - Tabulation)

# In this case, dp[i] will denote maximum loot that we can get by considering till ith index. At every index,

# We can keep same loot as we had at previous index - dp[i-1]
# Or, we can rob the current house and add it to the loot we have at i-2th index - A[i] + dp[i-2]

class Solution:
    def rob(self, A):
        if len(A) == 1:
            return A[0]
        dp = A[:]  # Copy the list A to dp
        dp[1] = max(A[0], A[1])
        for i in range(2, len(A)):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])
        return dp[-1]

# Example usage
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.rob(nums))  # Output: 4

# Time Complexity : O(N), just single iteration is performed from 2 to N to compute each dp[i].
# Space Complexity : O(N), required for dp.

# ✔️ Solution - III (Space-Optimzed Dynamic Programming)

# We can observe that the above dp solution relied only on the previous two indices in dp to compute the value of current dp[i]. So, we dont really need to maintain the whole dp array and can instead just maintain the values of previous index (denoted as prev below) and previous-to-previous index (denoted as prev2) and we can calculate the value for current index (cur) using just these two variables and roll-forward each time.

class Solution:
    def rob(self, A):
        prev2, prev, cur = 0, 0, 0
        for i in A:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur

# Example usage for LeetCode submission
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.rob(nums))  # Output: 4

# Time Complexity : O(N)
# Space Complexity : O(1), only constant extra space is used.

