# problem link : https://neetcode.io/problems/count-connected-components

# for Directed and Undirected graph main code will be same . only change will be taking input for directed graph : like :
#  adj_list = {i: [] for i in range(n)}
#         for edge in edges:
#             u, v = edge
#             adj_list[u].append(v)

# using bfs to count the number of discrete graph in a one big graph
from collections import deque
from typing import List
class Solution:
    def bfs(self, node: int, adj_list: dict, visited: List[bool]) -> None:
        queue = deque([node])
        visited[node] = True

        while queue:
            current = queue.popleft()
            for neighbor in adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)   #here will be changes for directed graph 
            adj_list[v].append(u)

        # Initialize visited list
        visited = [False] * n
        count = 0

        # Traverse all nodes
        for i in range(n):
            if not visited[i]:
                self.bfs(i, adj_list, visited)
                count += 1

        return count

# Example usage
solution = Solution()
n = 5
edges = [
    [0, 1],
    [1, 2],
    [3, 4]
]

print(solution.countComponents(n, edges))  # Output: 2


# same problem solve in same way using dfs by implementing recursive function 

from typing import List

class Solution:
    def dfs(self, node: int, adj_list: dict, visited: List[bool]) -> None:
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Initialize visited list
        visited = [False] * n
        count = 0

        # Traverse all nodes
        for i in range(n):
            if not visited[i]:
                self.dfs(i, adj_list, visited)
                count += 1

        return count

# Example usage
solution = Solution()
n = 6
edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [3, 4],
    [4, 5],
    [5, 3]
]

print(solution.countComponents(n, edges))  # Output: 2



# same problem solve in same way using dfs by implementing stack 

from typing import List

class Solution:
    def dfs(self, node: int, adj_list: dict, visited: List[bool]) -> None:
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for neighbor in adj_list[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Initialize visited list
        visited = [False] * n
        count = 0

        # Traverse all nodes
        for i in range(n):
            if not visited[i]:
                self.dfs(i, adj_list, visited)
                count += 1

        return count

# Example usage
solution = Solution()
n = 6
edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [3, 4],
    [4, 5],
    [5, 3]
]

print(solution.countComponents(n, edges))  # Output: 2


        
        