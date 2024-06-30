# solution discussion : https://leetcode.com/problems/reverse-linked-list/discuss/3620367/Best-Method-100-oror-C%2B%2B-oror-JAVA-oror-PYTHON-oror-Beginner-Friendly


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

def reverse_list(head):
    if not head or not head.next :
        return head
    temp = head
    new_node = None
    while temp : 
        after = temp.next
        temp.next = new_node
        new_node = temp
        temp = after
    return new_node

def reverse_list_recursive(head):
    def reverse_list_int(head, new_head):
        if head is None:
            return new_head
        next_node = head.next
        head.next = new_head
        return reverse_list_int(next_node, head)
    return reverse_list_int(head,None)

# Create the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_list(head)

# Iterative solution
iterative_reversed_head = reverse_list(head)
print("Reversed list (Iterative):")
print_list(iterative_reversed_head)

# To test the recursive solution, we need to recreate the list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Recursive solution
recursive_reversed_head = reverse_list_recursive(head)
print("Reversed list (Recursive):")
print_list(recursive_reversed_head)