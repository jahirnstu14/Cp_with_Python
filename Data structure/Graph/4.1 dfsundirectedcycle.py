# nice solution : https://takeuforward.org/data-structure/detect-cycle-in-an-undirected-graph-using-dfs/
# Detect a Cycle in an Undirected Graph using DFS

class Solution:
    def dfs(self, node, parent, vis, adj):
        vis[node] = True
        # Visit adjacent nodes
        for adjacentNode in adj[node]:
            # Unvisited adjacent node
            if not vis[adjacentNode]:
                if self.dfs(adjacentNode, node, vis, adj):
                    return True
            # Visited node but not a parent node
            elif adjacentNode != parent:
                return True
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        vis = [False] * V
        # For graph with connected components
        for i in range(V):
            if not vis[i]:
                if self.dfs(i, -1, vis, adj):
                    return True
        return False

if __name__ == "__main__":
    # V = 4, E = 2
    adj = [
        [],         # Vertex 0
        [2],        # Vertex 1
        [1, 3],     # Vertex 2
        [2]         # Vertex 3
    ]
    obj = Solution()
    ans = obj.isCycle(4, adj)
    if ans:
        print("1")
    else:
        print("0")
