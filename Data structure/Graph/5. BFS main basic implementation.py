from collections import deque

# Number of nodes
n = 5

# Adjacency list representation
adj = [
    [1, 2],    # Neighbors of node 0
    [0, 3, 4], # Neighbors of node 1
    [0, 4],    # Neighbors of node 2
    [1],       # Neighbors of node 3
    [1, 2]     # Neighbors of node 4
]

s = 0
traversal_path = []
q = deque()
d = [0] * n
p = [-1] * n
used = [False] * n

q.append(s)
used[s] =True
d[s] = 0
p[s] = -1
traversal_path.append(0)


while q:
    v = q.popleft()
    
    for u in adj[v]:
        if not used[u]:
            used[u] = True
            q.append(u)
            d[u] = d[v] + 1
            p[u] = v
            traversal_path.append(u)
            
print(f"Distances : {d}")
print(f"parent : {p}")

print("BFS traversal path will be : ")
print(traversal_path)
            
# If we have to restore and display the shortest path from the source to some vertex u , it can be done in the following manner:

def reconstruct_path(s, v, p):
    path = []
    
    while v != -1:
        path.append(v)
        v = p[v]
    path.reverse()
    return path
    
    
print("\nBFS Paths from source vertex", s, ":")
for i in range(n):
    path = reconstruct_path(s, i, p)
    print(f"Path to vertex {i}: {path}")

