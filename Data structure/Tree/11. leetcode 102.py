# using BFS for tree

from collections import deque

class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        
        q = deque([root])
        
        while q:
            sz = len(q)
            level = []
            
            for _ in range(sz):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(level)
        
        return ans
    


# using dfs 

class Solution:
    def dfs(self, root, ans, d=0):
        if not root:
            return
        if d >= len(ans):
            ans.append([])
        ans[d].append(root.val)
        self.dfs(root.left, ans, d + 1)
        self.dfs(root.right, ans, d + 1)
    
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        self.dfs(root, ans)
        return ans

