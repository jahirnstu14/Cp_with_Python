
# without using dummy variable and place in 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # if list1 happens to be None
        # we will simply return list2.
        if list1 is None:
            return list2
        # # if list2 happens to be None
        # # we will simply return list1.
        if list2 is None:
            return list1
        
        
        if list1.val <= list2.val:
            ptr = list1
            list1 = list1.next
        else:
            ptr = list2
            list2 = list2.next
        
        current = ptr 
        
        # # till one of the lists doesn't reach None
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
                
        
        # # adding remaining elements of bigger list
        if not list1:
            current.next = list2
        else:
            current.next = list1
        return ptr

def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# convert to list to linkedlist 

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value) #this line 
        current = current.next #and this line  , this two line are most important for creating list 
    return head

# Create two linked lists
list1 = create_linked_list([1, 3, 5,7])
list2 = create_linked_list([2, 4, 6])

# Merge the two linked lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged linked list
print("Merged Linked List:")
print_list(merged_list)


# using recursion method and use only fuction : 

# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

#         if l1 is None:
#             return l2

#         if l2 is None:
#             return l1

#         if l1.val <= l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         # we call recursively the whole l1 list and l2.next
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2 

# Using dummy variable :

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = node = ListNode()

#         while list1 and list2:
#             if list1.val < list2.val: 
#                 node.next = list1
#                 list1 = list1.next
#             else:
#                 node.next = list2
#                 list2 = list2.next
#             node = node.next

#         node.next = list1 or list2

#         return dummy.next

