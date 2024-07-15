import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Example usage
if __name__ == "__main__":
    # Initialize the KthLargest class with k = 3 and a list of numbers
    kth_largest = KthLargest(3, [4, 5, 8, 2])

    # Add new numbers and get the k-th largest element after each addition
    print(kth_largest.add(3))  # Output: 4
    print(kth_largest.add(5))  # Output: 5
    print(kth_largest.add(10)) # Output: 5
    print(kth_largest.add(9))  # Output: 8
    print(kth_largest.add(4))  # Output: 8
