
# Short answer without recusion 

# nums = list(map(int,input().split()))
# subsets = [[]]

# for num in nums:
#     n = len(subsets)
#     for i in range(n):
#         subsets.append(subsets[i] + [num] )
# print(subsets)


# using backtracking method 

def subsets(nums):
    res = []  # the final list, which we will display
    aux_arr = []  # auxiliary list
    i = 0  # starting index

    def recur(nums, i, aux_arr):
        if i == len(nums):
            res.append(aux_arr)
            return
        # take it
        recur(nums, i + 1, aux_arr + [nums[i]])
        # don't take it
        recur(nums, i + 1, aux_arr)

    recur(nums, i, aux_arr)  # passing the global variables declared already
    return res  # return the final 2D list

# Example usage:
nums = list(map(int, input().split()))
print(subsets(nums))
