def subsetsWithDup(nums):
    res = []  # the final list to store all subsets
    nums.sort()  # sort the array to handle duplicates

    def backtrack(start, aux_arr):
        res.append(aux_arr[:])  # add the current subset to the result
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            aux_arr.append(nums[i])
            backtrack(i + 1, aux_arr)
            aux_arr.pop()  # backtrack

    backtrack(0, [])  # initial call to the backtracking function
    return res  # return the final list of subsets

# Example usage:
nums = [1, 2, 2]
print(subsetsWithDup(nums))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

nums = [0]
print(subsetsWithDup(nums))  # Output: [[], [0]]
