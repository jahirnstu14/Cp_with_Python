# nice explanation of using BFS TO FIND MAXIMUM HEIGHT OF A TREE: https://takeuforward.org/data-structure/maximum-depth-of-a-binary-tree/


# the problem is solved by BFS ALOGRITHM 

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        depth = 1
        
        while queue:
            
            for _ in range(len(queue)):
                current = queue.popleft()
                
                if current.left is None and current.right is None:
                    return depth
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            depth += 1
        return depth

# Example usage
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print("Minimum depth of the tree:", solution.minDepth(root))
    
# FOR ABOVE PROBLEM : Complexity:

# Time: In the worst case for a balanced tree, we need to visit all nodes level by level up to the tree height, that excludes the bottom level only. This way we visit N/2 nodes, and thus the time complexity is O(N).
# Space: O(N)


# PROBLEM SOLVED BY dfs 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        # If one of the subtrees is empty, return the depth of the other subtree plus 1
        # If both subtrees are not empty, return the minimum depth of the two subtrees plus 1
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1

# Example usage
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print("Minimum depth of the tree:", solution.minDepth(root))
    
# for depth first search Complexity:

# Time: O(N). Because each node is visited exactly once.
# Space: O(H), where H is the height of the tree, it's the cost for depth of recursion stack memory.