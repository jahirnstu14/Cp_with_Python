# Using dictionary 

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        ret = []
        for i in nums2:
            if i in dict1 and dict1[i] > 0:
                ret.append(i)
                dict1[i] -= 1
        return ret
    
# Time Complexity: 𝑂(𝑛+𝑚),O(n+m), where 𝑛 ,n is the length of nums1 and 𝑚,m is the length of nums2.
# Space Complexity: 𝑂(𝑛),where n ,  is the length of nums1.

# Example usage:
solution = Solution()
nums1 = [4, 9, 5, 9]
nums2 = [9, 4, 9, 8, 4]
result = solution.intersect(nums1, nums2)
print(result)  # Output: [4, 9, 9]



# same solution using counter or hashmap function 
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
    
# counter function example :
# # Example list
# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# # Create a Counter object
# count = Counter(nums)
# # Print the Counter object
# print(count)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})
# # Accessing counts
# print(count[2])  # Output: 2
# print(count[5])  # Output: 0 (5 is not in the list)

# Example usage:
solution = Solution()
nums1 = [4, 9, 5, 9]
nums2 = [9, 4, 9, 8, 4]
result = solution.intersect(nums1, nums2)
print(result)  # Output: [4, 9, 9]