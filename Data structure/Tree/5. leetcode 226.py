# problem solved using bfs 
# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root is None:
#             return None
        
#         queue = deque()
#         queue.append(root)
        
#         while queue:
#             current = queue.popleft()
            
#             current.left, current.right = current.right, current.left
            
#             if current.left: 
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)
#         return root
        
        

# def print_tree(root: TreeNode):
#     if root is None:
#         return
#     print(root.val, end=' ')
#     print_tree(root.left)
#     print_tree(root.right)

# # Example usage
# if __name__ == "__main__":
#     # Creating a simple binary tree
#     root = TreeNode(4)
#     root.left = TreeNode(2)
#     root.right = TreeNode(7)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#     root.right.left = TreeNode(6)
#     root.right.right = TreeNode(9)
#     print("Original tree:")
#     print_tree(root)
#     print("\nInverted tree:")

#     solution = Solution()
#     inverted_root = solution.invertTree(root)
#     print_tree(inverted_root)

# problem solve using DFS 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def print_tree(root: TreeNode):
    if root is None:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

# Example usage
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original tree:")
    print_tree(root)
    print("\nInverted tree:")

    solution = Solution()
    inverted_root = solution.invertTree(root)
    print_tree(inverted_root)


