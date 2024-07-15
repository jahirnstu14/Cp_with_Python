# Using min heap 

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(f"The {k}-th largest element is: {result}")
    
    
# using maxheap in python 

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Convert all nums to negative to use heapq as a max-heap
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(f"The {k}-th largest element is: {result}")

