
# Summary
# collections.deque: Most efficient and recommended for general use.
# queue.Queue: Suitable for multi-threaded applications.
# List: Simple but less efficient for large queues due to O(n) complexity for dequeue operation.

# basic without linkedlist

# In Python, a queue is a data structure that follows the First In First Out (FIFO) principle, where the first element added to the queue will be the first one to be removed. There are several ways to implement a queue in Python:

# 1. Using collections.deque
# The collections.deque class from the collections module is an excellent choice for implementing a queue because it provides efficient appending and popping from both ends.

# Advantages:

# Fast appending and popping from both ends (O(1) time complexity for append and pop operations).
# python
# Copy code
# from collections import deque

# # Initialize a deque
# queue = deque()

# # Add elements to the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)

# # Remove elements from the queue
# first = queue.popleft()  # Removes and returns the leftmost item (1)
# second = queue.popleft()  # Removes and returns the leftmost item (2)

# # Check if the queue is empty
# is_empty = len(queue) == 0
# 2. Using queue.Queue
# The queue.Queue class from the queue module is another way to implement a queue. It is especially useful in multithreaded programs where you need a thread-safe queue.

# Advantages:

# Thread-safe operations, making it suitable for multi-threading.
# python
# Copy code
# import queue

# # Initialize a queue
# q = queue.Queue()

# # Add elements to the queue
# q.put(1)
# q.put(2)
# q.put(3)

# # Remove elements from the queue
# first = q.get()  # Removes and returns the first item (1)
# second = q.get()  # Removes and returns the first item (2)

# # Check if the queue is empty
# is_empty = q.empty()
# 3. Using a List
# A list can be used to implement a queue by using append to add elements to the end of the list and pop(0) to remove elements from the front.

# Advantages:

# Simple and straightforward implementation.
# Disadvantages:

# Removing elements from the front of the list (pop(0)) has O(n) time complexity, which is less efficient for large queues.
# python
# Copy code
# # Initialize a list as a queue
# queue = []

# # Add elements to the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)

# # Remove elements from the queue
# first = queue.pop(0)  # Removes and returns the first item (1)
# second = queue.pop(0)  # Removes and returns the first item (2)

# # Check if the queue is empty
# is_empty = len(queue) == 0
# Summary
# For most purposes, collections.deque is recommended for implementing a queue in Python due to its simplicity and efficiency. The queue.Queue class is suitable for multi-threaded applications, while using a list is generally not recommended for queue operations due to its inefficiency with large data sets.


# queue implementation using linkedlist 
# the constructor for queues 

# class Node :
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.first = new_node
#         self.length = 1
#     def print_Value(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next
            
# my_queue = Queue(4)
# my_queue.print_Value()

# For enqueue method 

# class Node :
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1
#     def print_Value(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next
    
#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
            
# my_queue = Queue(4)
# my_queue.print_Value()
# print("after enqueue method : ")
# my_queue.enqueue(6)
# my_queue.enqueue(7)
# my_queue.print_Value()

# deque method 
# class Node :
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1
#     def print_Value(self):
#         temp = self.first
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next
    
#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
        
#     def dequeue(self):
#         if self.length == 0 :
#             return None
#         temp = self.first
        
#         if self.length == 1:
#             self.first = None
#             self.last = None
#         else:
#             self.first = self.first.next
#             temp.next = None
#         self.length -=1
#         return temp
            
# my_queue = Queue(4)
# print("\n after enqueue method : ")
# my_queue.enqueue(6)
# my_queue.enqueue(7)
# my_queue.print_Value()

# print( " \n after implementing dequeue method : ")
# my_queue.dequeue()
# my_queue.print_Value()

