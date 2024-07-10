from typing import List
from collections import deque

# it is same like find cycle in a directed graph using bfs with topological sort 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list and initialize the indegree array
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build the graph and the indegree array
        for dest, src in prerequisites:
            adjList[src].append(dest)
            indegree[dest] += 1

        # Initialize the queue with nodes that have no incoming edges
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # Process the nodes
        cnt = 0
        while q:
            node = q.popleft()
            cnt += 1
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If we were able to process all the nodes, return True
        return cnt == numCourses



# nice solution : https://takeuforward.org/data-structure/detect-cycle-in-a-directed-graph-using-dfs-g-19/
# cycle detection for directed acyclic graph using dfs

class Solution:
    def dfsCheck(self, node, adj, vis, pathVis):
        vis[node] = True
        pathVis[node] = True

        # Traverse for adjacent nodes
        for it in adj[node]:
            # When the node is not visited
            if not vis[it]:
                if self.dfsCheck(it, adj, vis, pathVis):
                    return True
            # If the node has been previously visited
            # but it has to be visited on the same path
            elif pathVis[it]:
                return True

        pathVis[node] = False
        return False

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis = [False] * V
        pathVis = [False] * V

        for i in range(V):
            if not vis[i]:
                if self.dfsCheck(i, adj, vis, pathVis):
                    return True
        return False


if __name__ == "__main__":
    adj = [
        [],         # Vertex 0
        [2],        # Vertex 1
        [3],        # Vertex 2
        [4, 7],     # Vertex 3
        [5],        # Vertex 4
        [6],        # Vertex 5
        [],         # Vertex 6
        [5],        # Vertex 7
        [9],        # Vertex 8
        [10],       # Vertex 9
        [8]         # Vertex 10
    ]

    V = 11
    obj = Solution()
    ans = obj.isCyclic(V, adj)

    if ans:
        print("True")
    else:
        print("False")
