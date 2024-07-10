def dfs(adj, s, n):
    edge_id = [0] * n
    vis = [0] * n
    path = []

    stack = []
    stack.append(s)
 
    while stack:
        u = stack.pop()
        if vis[u] == 0:
            vis[u] = 1
            path.append(u)
            for v in reversed(adj[u]):  # Reverse to maintain the correct order
                if vis[v] == 0:
                    stack.append(v)
    
    return path

# Example usage:
adj = [ 
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2]
]
s = 0
n = 4
dfs_path = dfs(adj, s, n)
print("DFS Path:", dfs_path)
