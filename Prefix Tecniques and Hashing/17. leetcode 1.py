# hashmap problem solving 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)
        
        for i in range(length):
            complementvalue = target - nums[i]
            if complementvalue in hashmap:
                return [hashmap[complementvalue],i]
                
                
            hashmap[nums[i]] = i
        return []
    

if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input().split()))
    target = int(input())
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
