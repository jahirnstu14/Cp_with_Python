#  explain the solution nicely: https://takeuforward.org/data-structure/calculate-the-diameter-of-a-binary-tree/

# problem solved using DFS

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)

        self.diameter = max(self.diameter, lh + rh)

        return 1 + max(lh, rh)

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter = solution.diameterOfBinaryTree(root)

    print(f"The diameter of the binary tree is: {diameter}")
