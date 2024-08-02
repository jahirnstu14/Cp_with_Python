# This problem is a little tricky at first glance. However, if you have finished the House Robber problem, this problem can simply be decomposed into two House Robber problems.
# Suppose there are n houses, since house 0 and n - 1 are now neighbors, we cannot rob them together and thus the solution is now the maximum of

# Rob houses 0 to n - 2;
# Rob houses 1 to n - 1.
# The code is as follows. Some edge cases (n < 2) are handled explicitly.

# logic behind the problem :https://leetcode.com/problems/house-robber-ii/discuss/227366/Thinking-process-from-easy-question-to-harder-question-within-the-same-question-set


class Solution:
    def rob(self, nums):
        def robber(nums, l, r):
            pre, cur = 0, 0
            for i in range(l, r + 1):
                temp = max(pre + nums[i], cur)
                pre = cur
                cur = temp
            return cur
        
        n = len(nums)
        if n < 2:
            return nums[0] if n else 0
        return max(robber(nums, 0, n - 2), robber(nums, 1, n - 1))

# Example usage for testing
nums = [2, 3, 2]
solution = Solution()
print(solution.rob(nums))  # Output: 3
