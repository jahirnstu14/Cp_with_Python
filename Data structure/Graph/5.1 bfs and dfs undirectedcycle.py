
# that will be used all places using bfs in undirected graph to find cycle 

# cycle detect using bfs in graph

from typing import List
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i : [] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        queue = deque([(0,-1)])
        
        while queue:
            node, parent = queue.popleft()
            
            if node in visit:
                return False
            visit.add(node)
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                queue.append((neighbor , node ))
        return n==len(visit)
            

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5
    
#     0
#    /|\
#   1-2 3
#   |
#   4
    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
        [1, 2]  # This edge creates a loop
    ]
    print(solution.validTree(n, edges))  # Output should be False
    
    
# graph without loop example
# edges = [
#     [0, 1],
#     [0, 2],
#     [0, 3],
#     [1, 4]
# ]
#  and graph is :
#     0
#    /|\
#   1 2 3
#   |
#   4

# same thing using dfs like above solution for undirected graph

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        # Create an adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Set to track visited nodes
        visit = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visit:
                return False
            
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # Start DFS from node 0, parent of -1
        # Check for cycle and if all nodes are connected
        return dfs(0, -1) and n == len(visit)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
        [1, 2]  # This edge creates a loop
    ]
    print(solution.validTree(n, edges))  # Output should be False


# Another solution difficult to understand 

# Detect a Cycle in an Undirected Graph using BFS and DFS


# nice solution : https://takeuforward.org/data-structure/detect-cycle-in-an-undirected-graph-using-bfs/  
    

# from collections import deque

# class Solution:
#     def detect(self, src, adj, vis):
#         vis[src] = True
#         # Store (source node, parent node)
#         q = deque([(src, -1)])
#         # Traverse until the queue is not empty
#         while q:
#             node, parent = q.popleft()
#             # Go to all adjacent nodes
#             for adjacentNode in adj[node]:
#                 # If the adjacent node is unvisited
#                 if not vis[adjacentNode]:
#                     vis[adjacentNode] = True
#                     q.append((adjacentNode, node))
#                 # If the adjacent node is visited and is not its own parent node
#                 elif parent != adjacentNode:
#                     # Yes, it is a cycle
#                     return True
#         # There's no cycle
#         return False

#     # Function to detect cycle in an undirected graph.
#     def isCycle(self, V, adj):
#         # Initialize them as unvisited
#         vis = [False] * V
#         for i in range(V):
#             if not vis[i]:
#                 if self.detect(i, adj, vis):
#                     return True
#         return False

# if __name__ == "__main__":
#     # V = 4, E = 2
#     adj = [
#         [],       # Vertex 0
#         [2],      # Vertex 1
#         [1, 3],   # Vertex 2
#         [2]       # Vertex 3
#     ]
#     obj = Solution()
#     ans = obj.isCycle(4, adj)
#     if ans:
#         print("1")
#     else:
#         print("0")


# nice solution : https://takeuforward.org/data-structure/detect-cycle-in-an-undirected-graph-using-dfs/
# Detect a Cycle in an Undirected Graph using DFS

# class Solution:
#     def dfs(self, node, parent, vis, adj):
#         vis[node] = True
#         # Visit adjacent nodes
#         for adjacentNode in adj[node]:
#             # Unvisited adjacent node
#             if not vis[adjacentNode]:
#                 if self.dfs(adjacentNode, node, vis, adj):
#                     return True
#             # Visited node but not a parent node
#             elif adjacentNode != parent:
#                 return True
#         return False

#     # Function to detect cycle in an undirected graph.
#     def isCycle(self, V, adj):
#         vis = [False] * V
#         # For graph with connected components
#         for i in range(V):
#             if not vis[i]:
#                 if self.dfs(i, -1, vis, adj):
#                     return True
#         return False

# if __name__ == "__main__":
#     # V = 4, E = 2
#     adj = [
#         [],         # Vertex 0
#         [2],        # Vertex 1
#         [1, 3],     # Vertex 2
#         [2]         # Vertex 3
#     ]
#     obj = Solution()
#     ans = obj.isCycle(4, adj)
#     if ans:
#         print("1")
#     else:
#         print("0")
