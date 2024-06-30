# discussion and nicely describe : https://leetcode.com/problems/linked-list-cycle/    with time complexity and space complexiy 
# the spacecomplexity is O(N) due to the use of the map to track nodes.
# As the loop iterates through N nodes, the total time complexity is determined by the product of the traversal (O(N)) and the average-case complexity of the hashmap operations (insert and search), resulting in O(N * 2 * log(N)). 

# Brute force solution 

# def find_inklist_loop (head):
#     temp = head
#     node_set = set()
    
#     while temp is not None:
#         if temp in node_set:
#             return True
        
#         node_set.add(temp) 
# #Insert Operation (set.add(item)):
# #Time Complexity: 𝑂(1),O(1) on average, due to the use of a hash table.
        
#         temp = temp.next
#     return False
  
            
# optimal solution for reducing space complexity 

# The previous method uses O(N) additional memory, which can become quite large as the linked list length grows. To enhance efficiency, the Tortoise and Hare Algorithm is introduced as an optimization.


# Node class represents
# a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to detect a loop in a
# linked list using the Tortoise and Hare Algorithm
def detect_cycle(head):
    # Initialize two pointers, slow and fast,
    # to the head of the linked list
    slow = head
    fast = head
    
    while fast.next is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next 
        
        if fast == slow:
            return True
    return False


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_cycle(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    # No need to explicitly free memory
    # in Python; memory management is automatic


