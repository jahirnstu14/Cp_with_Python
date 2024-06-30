# problem discussion and how to solve  with logic : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/3417980/Without-min-comparison-or-Detailed-explanation 

nums = list(map(int,input().split()))
left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2
    
    if nums[mid] > nums[right]:
        left = mid + 1
    else :
        # condition : nums[mid] <= nums[right]
        right = mid  # because, if codition has with equal to sign with greater than or less than then , right or left equal to only mid otherwise , it'll be mid-1 or mid + 1. and if left = right becasue , of dividing using 2 , one time left and right will be same and the loop will continue for infinite time . that's why left < right is preferable .
print(nums[left])