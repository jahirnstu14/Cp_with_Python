# stack constructor to make the first node :
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value) 
#         self.top = new_node
#         height = 1
    
#     def print_value(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value, end = " " )
#             temp = temp.next

# myfirst_stack = Stack(4)
# myfirst_stack.print_value()

# push method for stacks

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value) 
#         self.top = new_node
#         self.height = 1
    
#     def print_value(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value, end = " " )
#             temp = temp.next
#     def push_method(self, value):
#         new_node = Node(value)
        
#         if self.height == 0 :
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1

# myfirst_stack = Stack(4)
# myfirst_stack.push_method(1)
# myfirst_stack.print_value()


# use pop method to delete the node from the last 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self, value):
        new_node = Node(value) 
        self.top = new_node
        self.height = 1
    
    def print_value(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end = " " )
            temp = temp.next
    def push_method(self, value):
        new_node = Node(value)
        
        if self.height == 0 :
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop_method(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp

myfirst_stack = Stack(4)
myfirst_stack.push_method(3)
myfirst_stack.push_method(2)
myfirst_stack.print_value()
print(f"after the calling pop functionwe can write : ");
myfirst_stack.pop_method()
myfirst_stack.print_value()











