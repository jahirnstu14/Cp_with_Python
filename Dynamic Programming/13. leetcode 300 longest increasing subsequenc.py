# nicely explanation the explain : https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Segment-Tree-Solutions-Picture-explain-O(NlogN)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)   # another way do this :  if nums[i] > nums[j] and dp[i] < dp[j] + 1: dp[i] = dp[j] + 1
                           
        return max(dp)

solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Example test case

# Complexity
# Time: O(N^2), where N <= 2500 is the number of elements in array nums.
# Space: O(N)
