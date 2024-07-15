nums = list(map(int,input().split()))
target = int(input())
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    
    if nums[mid] == target:
        print(mid)
    if nums[left] <= nums[mid]:
        if nums[left]<=target < nums[right]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[left] < target <=nums[right]:
            left = mid + 1
        else:
            right = mid - 1
print(-1)   

# In above problem , first i'll determine the array  is sorted or not. then , search the value between them . 
    