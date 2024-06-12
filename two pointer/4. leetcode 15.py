# https://leetcode.com/problems/3sum/

# brute force approach

# nums = list((map(int,input().split())))
# n = len(nums)
# nums.sort()
# result_set = set()
# output = []

# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and k != i:
#                 result_set.add((nums[i], nums[j], nums[k]))

# for triplet in result_set:
#     output.append(list(triplet))

# print(output)

# optimize approach using 0(n)
res = []
nums = list((map(int,input().split())))
n = len(nums)
nums.sort()

for i in range(n-2):
    if nums[i]>0:
        break
    if i>0 and nums[i]==nums[i-1]:
        continue
    
    l,r = i+1, n-1
    
    while l<r:
        s = nums[i] + nums[l] + nums[r]
        if s<0:
            l+=1
        elif s>0:
            r-=1
        
        else:
            res.append([nums[i] , nums[l] , nums[r]])
            
            while l<r and nums[l]==nums[l+1]:
                l+=1
            while l<r and nums[r]==nums[r-1]:
                r-=1
            l-=1
            r-=1
print(res)

































