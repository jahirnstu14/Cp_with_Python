from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head.next
        s = 0
        while ptr2:
            if ptr2.val == 0:
                ptr1 = ptr1.next
                ptr1.val = s
                s = 0
            else:
                s += ptr2.val
            ptr2 = ptr2.next
        ptr1.next = None
        return head.next

# Helper function to create a linked list from a list of values
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

# Example usage
if __name__ == "__main__":
    # Create a linked list from a list of values
    values = [0, 3, 1, 0, 4, 5, 2, 0]
    head = create_linked_list(values)
    
    # Print the original linked list
    print("Original linked list:")
    print_linked_list(head)
    
    # Merge nodes
    solution = Solution()
    merged_head = solution.mergeNodes(head)
    
    # Print the modified linked list
    print("Modified linked list:")
    print_linked_list(merged_head)
