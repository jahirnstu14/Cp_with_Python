class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
        
        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res

# Example usage:
sol = Solution()
candidates = [9, 2, 2, 4, 6, 1, 5]
target = 8
print(sol.combinationSum2(candidates, target))  # Output: [[1, 2, 5], [2, 2, 4], [2, 6]]

candidates = [1, 2, 3, 4, 5]
target = 7
print(sol.combinationSum2(candidates, target))  # Output: [[1, 2, 4], [2, 5], [3, 4]]
