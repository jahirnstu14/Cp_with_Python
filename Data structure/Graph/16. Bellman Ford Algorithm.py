# Nice explanation : https://takeuforward.org/data-structure/bellman-ford-algorithm-g-41/

# this alogrithm can be used for positive distance or negative distance from node to node. it is done by using dynamic programming procedure. it has high time complexity than dijkstra algorithm. so, it'll be used at the time of negative distance edge present in the graph .

class Solution:
    def bellman_ford(self, V, edges, S):
        # Initialize distance array with a large number
        dist = [1e8] * V
        dist[S] = 0
        
        # Relax all edges V - 1 times
        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != 1e8 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        # Check for negative weight cycles
        for u, v, wt in edges:
            if dist[u] != 1e8 and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist

if __name__ == "__main__":
    V = 6
    edges = [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]
    
    S = 0
    obj = Solution()
    dist = obj.bellman_ford(V, edges, S)
    for d in dist:
        print(d, end=" ")
    print()
