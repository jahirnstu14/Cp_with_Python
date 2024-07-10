# Nicely describe or explanation Dijkstra algorithm : https://takeuforward.org/data-structure/dijkstras-algorithm-using-priority-queue-g-32/

# find shortest path from source to all other node using dijsktra algorithm using priority queue

import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        # Priority queue for storing nodes as (dist, node)
        pq = []
        
        # Initializing distTo list with a large number to indicate unvisited nodes
        distTo = [float('inf')] * V
        
        # Source initialized with dist=0
        distTo[S] = 0
        heapq.heappush(pq, (0, S))
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            # Check all adjacent nodes of the popped element
            for it in adj[node]:
                v = it[0]
                w = it[1]
                if dis + w < distTo[v]:
                    distTo[v] = dis + w
                    heapq.heappush(pq, (dis + w, v))
        
        # Return the list containing shortest distances from source to all nodes
        return distTo

if __name__ == "__main__":
    # Driver code
    # dynamic input or user defined input 
    
    # V = int(input("Enter number of vertices: "))
    # E = int(input("Enter number of edges: "))
    # S = int(input("Enter the source vertex: "))
    
    # adj = {}
    
    # print("Enter edges in the format 'u v w' (u to v with weight w):")
    # for _ in range(E):
    #     u, v, w = map(int, input().split())
    #     if u not in adj:
    #         adj[u] = []
    #     adj[u].append([v, w])
        
    # default taking input    using dictionary : 
    # adj = {
    #     0: [[1, 1], [2, 6]],
    #     1: [[2, 3], [0, 1]],
    #     2: [[1, 3], [0, 6]]
    # }
    # same input taking like above
    
    V, E, S = 3, 3, 2
    adj = [[] for _ in range(V)]
    edges = []
    
    v1, v2 = [1, 1], [2, 6]
    v3, v4 = [2, 3], [0, 1]
    v5, v6 = [1, 3], [0, 6]
    
    adj[0].append(v1)
    adj[0].append(v2)
    adj[1].append(v3)
    adj[1].append(v4)
    adj[2].append(v5)
    adj[2].append(v6)
    
    obj = Solution()
    res = obj.dijkstra(V, adj, S)
    
    print(" ".join(map(str, res)))


# dijkstra algorithm using set 
# nice explanation : https://takeuforward.org/data-structure/dijkstras-algorithm-using-set-g-33/

class Solution:
    def dijkstra(self, V, adj, S):
        # Create a set for storing the nodes as a pair (dist, node)
        # where dist is the distance from source to the node.
        st = set()
        
        # Initialising dist list with a large number to
        # indicate the nodes are unvisited initially.
        # This list contains distance from source to the nodes.
        dist = [float('inf')] * V
        
        # Source initialised with dist=0
        dist[S] = 0
        st.add((0, S))
        
        # Now, erase the minimum distance node first from the set
        # and traverse for all its adjacent nodes.
        while st:
            # Get the node with the smallest distance
            dis, node = min(st)
            st.remove((dis, node))
            
            # Check for all adjacent nodes of the erased
            # element whether the previous dist is larger than current or not.
            for it in adj[node]:
                adjNode, edgW = it[0], it[1]
                
                if dis + edgW < dist[adjNode]:
                    # Erase if it was visited previously at a greater cost.
                    if dist[adjNode] != float('inf'):
                        st.discard((dist[adjNode], adjNode))
                        
                    # If current distance is smaller,
                    # push it into the set
                    dist[adjNode] = dis + edgW
                    st.add((dist[adjNode], adjNode))
        
        # Return the list containing shortest distances
        # from source to all the nodes.
        return dist

# Driver code.
if __name__ == "__main__":
    V = 3
    S = 2
    adj = [[] for _ in range(V)]
    adj[0].append([1, 1])
    adj[0].append([2, 6])
    adj[1].append([2, 3])
    adj[1].append([0, 1])
    adj[2].append([1, 3])
    adj[2].append([0, 6])

    obj = Solution()
    res = obj.dijkstra(V, adj, S)

    for i in range(V):
        print(res[i], end=" ")
    print()


# print the shortest path using dijsktra algorithm 
# nice solution : https://takeuforward.org/data-structure/g-35-print-shortest-path-dijkstras-algorithm/

import heapq

class Solution:
    def shortestPath(self, n, m, edges):
        # Create an adjacency list of pairs of the form node1 -> {node2, edge weight}
        adj = [[] for _ in range(n + 1)]
        for it in edges:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))
        
        # Create a priority queue for storing the nodes along with distances 
        # in the form of a pair (dist, node).
        pq = []
        
        # Create a dist array for storing the updated distances and a parent array
        # for storing the nodes from where the current nodes represented by indices of
        # the parent array came from.
        dist = [float('inf')] * (n + 1)
        parent = list(range(n + 1))
        
        dist[1] = 0

        # Push the source node to the queue.
        heapq.heappush(pq, (0, 1))
        
        while pq:
            # Topmost element of the priority queue is with minimum distance value.
            dis, node = heapq.heappop(pq)
            
            # Iterate through the adjacent nodes of the current popped node.
            for adjNode, edW in adj[node]:
                # Check if the previously stored distance value is 
                # greater than the current computed value or not, 
                # if yes then update the distance value.
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))

                    # Update the parent of the adjNode to the recent 
                    # node where it came from.
                    parent[adjNode] = node
        
        # If distance to a node could not be found, return an array containing -1.
        if dist[n] == float('inf'):
            return [-1]
        
        # Store the final path in the `path` array.
        path = []
        node = n
        
        # Iterate backwards from destination to source through the parent array.
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        
        # Since the path stored is in a reverse order, we reverse the array
        # to get the final answer and then return the array.
        path.reverse()
        return path

# Driver Code
if __name__ == "__main__":
    V = 5
    E = 6
    edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    obj = Solution()
    path = obj.shortestPath(V, E, edges)

    for i in range(len(path)):
        print(path[i], end=" ")
    print()
