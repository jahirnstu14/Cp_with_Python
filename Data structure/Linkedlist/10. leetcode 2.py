# discuss clearly sotion : https://takeuforward.org/data-structure/add-two-numbers-represented-as-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
                
            
# Helper functions to create linked lists and print them
def create_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Test the solution
if __name__ == "__main__":
    # Example linked lists
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    # Print input linked lists
    print("Input Linked List 1:")
    print_linked_list(l1)
    print("Input Linked List 2:")
    print_linked_list(l2)

    # Add the two numbers
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    # Print result linked list
    print("Result Linked List:")
    print_linked_list(result)
