# using DFS PROCEDURE 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not root:
#             return False
#         if self.isSame(root, subRoot):
#             return True
#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#     def isSame(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
#         if not s and not t:
#             return True
#         if not s or not t:
#             return False
#         if s.val != t.val:
#             return False
#         return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)