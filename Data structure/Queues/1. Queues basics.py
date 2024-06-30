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
class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    def print_Value(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
    def dequeue(self):
        if self.length == 0 :
            return None
        temp = self.first
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp
            
my_queue = Queue(4)
print("\n after enqueue method : ")
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.print_Value()

print( " \n after implementing dequeue method : ")
my_queue.dequeue()
my_queue.print_Value()