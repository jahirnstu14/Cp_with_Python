
# main dfs implementation showing graph traversal always will follow this 
def dfs(v):
    visited[v] = True
    dfs_path.append(v)  # Append the vertex itself to dfs_path
    
    for u in adj[v]:
        if not visited[u]:
            dfs(u)

if __name__ == "__main__":  # Corrected condition with double underscores
    n = 5
    visited = [False] * n
    dfs_path = []
    adj = { 
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }

    dfs(0)
    
    print(f"The graph traversal using dfs path is: {dfs_path}")

# to see the exit and entry node of graph :
dfs_timer = 0
def dfs(v):
    global dfs_timer 
    time_in[v] = dfs_timer
    dfs_timer += 1
    color[v] = 1
    
    for u in adj[v]:
        if color[u] == 0:
            dfs(u)
    color[v] = 2
    time_out[v] = dfs_timer
    dfs_timer += 1
    
    # We will color all vertices with the color 0, if we haven't visited them, with the color 1 if we visited them, and with the color 2, if we already exited the vertex.

if __name__ == "__main__":
    n = 5  # Number of vertices
    adj = [
        [1, 2],    # Neighbors of vertex 0
        [0, 3, 4], # Neighbors of vertex 1
        [0, 4],    # Neighbors of vertex 2
        [1],       # Neighbors of vertex 3
        [1, 2]     # Neighbors of vertex 4
    ]
    
    color = [0] * n
    time_in = [0] * n
    time_out = [0] * n 
    
    dfs(0)
    
    print(f"Time in {time_in}")
    print(f"Time out {time_out}")
    