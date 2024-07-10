
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

    
    