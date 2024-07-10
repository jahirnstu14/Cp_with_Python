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
