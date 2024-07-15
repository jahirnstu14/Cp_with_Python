
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
   
    # YOU CAN ALSO WRITE BFS WITH A QUEUE INSTEAD OF LIST
    # (TECHNICALLY THIS IS A BETTER SOLUTION)
    #
    # def BFS(self):
    #     current_node = self.root
    #     queue = Queue()
    #     results = []
    #     queue.put(current_node)

    #     while not queue.empty():
    #         current_node = queue.get()
    #         results.append(current_node.value)
    #         if current_node.left is not None:
    #             queue.put(current_node.left)
    #         if current_node.right is not None:
    #             queue.put(current_node.right)
    #     return results
                
    
    def BFS(self):
        current_node = self.root
        queue = deque()
        result = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.popleft()
            result.append(current_node.value)
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result
            


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """





                



 