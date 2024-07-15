class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        
        return root

def print_tree(node, level=0, label='.'):
    indent = ' ' * (4 * level)
    print(f"{indent}{label}: {node.val if node else 'None'}")
    if node:
        print_tree(node.left, level + 1, 'L')
        print_tree(node.right, level + 1, 'R')

# Example usage
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

print_tree(tree)

# using iterative process 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if stack[-1].val != inorder[inorder_index]:
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    last = stack.pop()
                    inorder_index += 1
                last.right = node
            stack.append(node)
        
        return root

def print_tree(node, level=0, label='.'):
    indent = ' ' * (4 * level)
    print(f"{indent}{label}: {node.val if node else 'None'}")
    if node:
        print_tree(node.left, level + 1, 'L')
        print_tree(node.right, level + 1, 'R')

# Example usage
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

solution = Solution()
tree = solution.buildTree(preorder, inorder)

print_tree(tree)

