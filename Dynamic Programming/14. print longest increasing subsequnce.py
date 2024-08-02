# problem link :https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=printing-longest-increasing-subsequence

# another nice discussion : https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> (int, List[int]):
        if not nums:
            return 0, []
        
        sub = []
        sub_index = []
        prev_index = [-1] * len(nums)
        
        for i, num in enumerate(nums):
            idx = bisect.bisect_left(sub, num)
            
            if idx == len(sub):
                sub.append(num)
                sub_index.append(i)
            else:
                sub[idx] = num
                sub_index[idx] = i
            
            if idx > 0:
                prev_index[i] = sub_index[idx - 1]
        
        lis_length = len(sub)
        lis_path = []
        k = sub_index[-1]
        
        while k != -1:
            lis_path.append(nums[k])
            k = prev_index[k]
        
        lis_path.reverse()
        return lis_length, lis_path

# Example usage
solution = Solution()
length, path = solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(f"Length of LIS: {length}")
print(f"Path of LIS: {path}")

