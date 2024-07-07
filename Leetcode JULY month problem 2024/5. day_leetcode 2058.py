# easy solution : https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/discuss/1550147/Short-and-Easy-c%2B%2B-Beginner-Friendly.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_critical = last_critical = -1
        min_distance = float('inf')
        prev, curr, next_node = head, head.next, head.next.next
        position = 1
        
        while next_node:
            if (curr.val > prev.val and curr.val > next_node.val) or (curr.val < prev.val and curr.val < next_node.val):
                if first_critical == -1:
                    first_critical = position
                else:
                    min_distance = min(min_distance, position - last_critical)
                
                last_critical = position
                
            prev = curr
            curr = next_node
            next_node = next_node.next
            position += 1
        
        if first_critical == last_critical:
            return [-1, -1]
        
        return [min_distance, last_critical - first_critical]

# Example usage:
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(5)
solution = Solution()
print(solution.nodesBetweenCriticalPoints(head))  # Output should be [2, 3]
