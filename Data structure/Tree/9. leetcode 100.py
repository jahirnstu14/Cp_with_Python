
# USING BFS 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    queue = deque([(p, q)])
    while queue:
        node1, node2 = queue.popleft()
        if node1 is None and node2 is None:
            continue
        if node1 is None or node2 is None: # if none in [n1,n2] is same thing . ..
            return False
        
        if node1.val != node2.val:
            return False
        
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))
    
    return True
        

# Example usage:
if __name__ == "__main__":
    # Tree 1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    # Tree 2
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    print(isSameTree(tree1, tree2))  # Output should be True

    # Tree 3
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)

    # Tree 4
    tree4 = TreeNode(1)
    tree4.right = TreeNode(2)

    print(isSameTree(tree3, tree4))  # Output should be False


# DFS SOLUTION IS :
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False

# Example usage:
if __name__ == "__main__":
    # Tree 1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    # Tree 2
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    print(isSameTree(tree1, tree2))  # Output should be True

    # Tree 3
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)

    # Tree 4
    tree4 = TreeNode(1)
    tree4.right = TreeNode(2)

    print(isSameTree(tree3, tree4))  # Output should be False


