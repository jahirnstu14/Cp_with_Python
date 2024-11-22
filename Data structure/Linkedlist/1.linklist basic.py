# interviw question about linklist : last e dekbo
#
# 1) Linked List : ***
#
# Generate a linked list from given array ***
# Reverse a linked list ***
# Merge two sorted linked list without using auxiliary space ***
# Detecting a linked list if it is circular in O(n) time. **
# Remove Duplicates from Sorted List ***


# linked for learning linkedlist clearly and it will learn start of linked list learning
# https://leetcode.com/discuss/study-guide/1800120/become-master-in-linked-list


# linklist all basic important problem : https://leetcode.com/discuss/study-guide/2048320/linked-list-all-in-one-must-watch-for-beginners


# head = { "value":11,
#          "next":{
#              "value":23,
#              "next":{
#                  "value":7,
#                  "next":{
#                      "value":4,
#                      "next":None
#                 }
#             }
#         }
     
#  }

#  the most important rule for linkelist that :  if head nirdesh kare new node . then we can write , head = new node and for head->newnode will be head.next = newnode

# print(head["next"]["next"]["value"])

# where linklist squence is : head ->11->23->7->4->none
# first node creation

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
# my_linklist = LinkedList(4)

# print(my_linklist.head.value)
# print(my_linklist.tail.value)
# print(my_linklist.length)


# to append list using linkedlist and then append using append function and print the all items 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next   
    
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
        
# my_linkedlist = Linkedlist(11)
# my_linkedlist.append(13)
# my_linkedlist.append(20)
# my_linkedlist.append(30)
# my_linkedlist.append(50)
# my_linkedlist.printvalue()


# make empty of linked list 
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
        
# my_linkedlist = Linkedlist(11)
# my_linkedlist.append(13)
# my_linkedlist.append(20)
# my_linkedlist.append(30)
# my_linkedlist.append(50)
# my_linkedlist.make_empty()
# my_linkedlist.printvalue()


# pop the element from linkedlist

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
        
        
        
#     def pop(self):
#         if self.length==0:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -=1
#         if self.length ==0:
#             self.head = None
#             self.tail = None
#         return temp    
        
# my_linkedlist = Linkedlist(1)
# my_linkedlist.append(2)
# print(my_linkedlist.pop().value)
# print(my_linkedlist.pop().value)
# print(my_linkedlist.pop())

# prepend or node added in front

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
        
        
        
#     def pop(self):
#         if self.length==0:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -=1
#         if self.length ==0:
#             self.head = None
#             self.tail = None
#         return temp  
#     def prepend(self, value):
#         new_node = Node(value)  
#         if self.length ==0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length +=1
#         return True
            
        
# my_linkedlist = Linkedlist(2)
# my_linkedlist.append(3)
# my_linkedlist.prepend(1)
# my_linkedlist.printvalue()


# first pop from linkedlist

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length +=1
        
        
        
#     def pop(self):
#         if self.length==0:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -=1
#         if self.length ==0:
#             self.head = None
#             self.tail = None
#         return temp  
#     def prepend(self, value):
#         new_node = Node(value)  
#         if self.length ==0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length +=1
#         return True
            
#     def pop_first(self):
#         if self.length ==0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -=1
#         if self.length ==0:
#             self.tail =None
#         return temp.value
        
# my_linkedlist = Linkedlist(2)
# my_linkedlist.append(3)
# my_linkedlist.pop_first()
# my_linkedlist.printvalue()


# to get the specific value according to index:
    
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
        



# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(3).value)


# """
#     EXPECTED OUTPUT:
#     ----------------
#     3

# """

# set_value in specific location or update value same thing 
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
        
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while(temp.next):
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True

#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
        
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    



# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print('LL before set_value():')
# my_linked_list.print_list()

# my_linked_list.set_value(1,4)

# print('\nLL after set_value():')
# my_linked_list.print_list()



# """
#     EXPECTED OUTPUT:
#     ----------------
#     LL before set_value():
#     11
#     3
#     23
#     7

#     LL after set_value():
#     11
#     4
#     23
#     7
# """

# insert value in front , end , middle 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
#         print()  # Add newline for better formatting after printing all values
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
        
#     def pop(self):
#         if self.length == 0:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp  
    
#     def prepend(self, value):
#         new_node = Node(value)  
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
            
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp.value
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length += 1   
#         return True 

# # Testing the linked list operations
# my_linkedlist = Linkedlist(1)
# my_linkedlist.append(3)
# print("Before insert:")
# my_linkedlist.printvalue()

# print("After insert:")
# my_linkedlist.insert(1, 2)
# my_linkedlist.printvalue()


# remove function will be used to remove value in particular index 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
        
#     def printvalue(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value, end=" ")
#             temp = temp.next 
#         print()  # Add newline for better formatting after printing all values
    
#     def make_empty(self):
#         self.head = None
#         self.tail = None
#         self.length = 0  
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
        
#     def pop(self):
#         if self.length == 0:
#             return None
#         pre = self.head
#         temp = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp  
    
#     def prepend(self, value):
#         new_node = Node(value)  
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
            
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp.value
    
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp
    
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
    
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         temp = self.get(index - 1)
#         new_node.next = temp.next
#         temp.next = new_node
#         self.length += 1   
#         return True 

#     def remove(self, index):
#         if index<0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1 :
#             return self.pop()
#         pre = self.get(index - 1)
#         temp = pre.next
#         pre.next = temp.next
#         temp.next  = None
#         self.length -=1
#         return temp
    
            
# my_linkedlist  = Linkedlist(1)
# my_linkedlist.append(2)
# my_linkedlist.append(3)
# my_linkedlist.append(4)
# my_linkedlist.append(5)
# my_linkedlist.printvalue()

# # most important rule : In Python, when a function does not explicitly return a value, it returns None by default. 
    
# my_linkedlist.remove(1)
# my_linkedlist.printvalue()

# reverse function for reversing the order of linkedlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
  
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""