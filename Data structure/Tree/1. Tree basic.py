# interview preparation : last a dekbo
# 2) Binary Tree : ***
#
# Reverse a binary tree ***
# Calculate the height/depth of a binary tree ***
# Calculate the diameter of a binary tree **
# Post Traverse a Binary Tree. ***
# Pre Order traversal Binary Tree ***
# Inorder Traversal of a Binary Tree ***
#
# 3) Binary Search Tree : ***
#
# Insert new element in a BST ***
# Delete Item from BST ***
# Min Heap / Priority Queue ***
# Max Heap ***













# binary search tree is best for lookup(),remove() with complexity 0(log(n))whereas for linklist or list is will be o(n) and for insertion any value binary search tree taking time complexity 0(log n ) whereas linklist or list takes 0(1). here, linkedlist is best for inserion

# to learn the tree basic nice blog with problem : https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/

# create root node for tree

# class Node : 
#     def __init__(self, value):
#         self.value = value
#         self.left  = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
        
        
# my_tree = BinarySearchTree()
# print(my_tree.root)

# insert node in the tree and most important 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left  = None
#         self.right = None
        
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         new_node = Node(value)
        
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
        
#         while True:
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right


# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# """
#     THE LINES ABOVE CREATE THIS TREE:
#                  2
#                 / \
#                1   3
# """
# print(f"root : {my_tree.root.value}")
# print(f"root->left : {my_tree.root.left.value}")
# print(f"root->right : {my_tree.root.right.value}")

# check a value is contain in tree or not 

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
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.contains(27))
print(my_tree.contains(17))

"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""