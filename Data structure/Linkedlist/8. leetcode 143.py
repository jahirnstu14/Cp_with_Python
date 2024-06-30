# brute force problem solution : https://leetcode.com/problems/reorder-list/discuss/1640556/C%2B%2B-EASY-TO-SOLVE-oror-Beginner-Friendly-with-detailed-explanation-and-dry-run

# Brute-Force code-:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         # Base case: if the linked list has zero, one, or two elements, just return
#         if not head or not head.next or not head.next.next:
#             return
        
#         # Find the penultimate node, i.e., the second last node of the linked list
#         penultimate = head
#         while penultimate.next.next:
#             penultimate = penultimate.next
        
#         # Link the penultimate with the second element
#         penultimate.next.next = head.next
#         head.next = penultimate.next
        
#         # Again set the penultimate to the last
#         penultimate.next = None
        
#         # Do the above steps recursively
#         self.reorderList(head.next.next)



# Two pointer Approach [Tortoise and Hare method]:-

# for understanding the basic of problem : https://leetcode.com/problems/reorder-list/discuss/801971/Python-O(n)-by-two-pointers-w-Visualization

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Base case: linked list is empty
        if not head:
            return
        
        # Finding the middle with the help of two pointer approach
        tmp, half, prev = head, head, None
        while tmp.next and tmp.next.next:
            tmp = tmp.next.next
            half = half.next
        
        # Adding one bit in case of lists with even length
        if tmp.next:
            half = half.next
        
        # Now reverse the second half
        while half:
            tmp = half.next
            half.next = prev
            prev = half
            half = tmp
        half = prev
        
        # After reversing the second half, let's merge both halves
        while head and half:
            tmp = head.next
            prev = half.next
            head.next = half
            half.next = tmp
            head = tmp
            half = prev
        
        # Base case: closing when we have even length lists
        if head and head.next:
            head.next.next = None

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' -> ' if current.next else '')
        current = current.next
    print()

# Test case
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

solution = Solution()
solution.reorderList(head)

print("Reordered list:")
print_linked_list(head)

# Time Complexity : O(N) [ O(N) to find mid of list, O(N/2) to reverse the 2nd half and in the end O(N) for relinking purpose ]
# Space Complexity : O(1) [intermediate state variables are the only thing that we used]

