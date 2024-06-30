# All importance backtracking solution : https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

# another solution for leetcode 39  : https://leetcode.com/problems/combination-sum/discuss/1755084/Detailed-Time-and-Space-Complexity-analysisc%2B%2Bjavabacktracking

# For questions like printing combinations or subsequences, the first thing that should strike your mind is recursion. and pick or not pick

from typing import List


class Solution:
    def combinationSum(self, candidates, target):
        def getcomb(nums, i, t, cur, res):
            if t == 0:
                res.append(cur[:])
                return
            if t < 0 or i >= len(nums):
                return
            for k in range(i, len(nums)):
                cur.append(nums[k])
                getcomb(nums, k, t - nums[k], cur, res)
                cur.pop()
        
        cur = []
        res = []
        getcomb(candidates, 0, target, cur, res)
        return res

# Example usage:
sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(candidates, target))      
