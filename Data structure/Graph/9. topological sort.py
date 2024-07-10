# this is used for detecting whether a graph has a cycle  . it can be implemented using dfs or bfs . prefer to use bfs because, donot happen stack overflow and dfs is used for short code. and one work must be done before another work. example , for u->v, u work has to be done before v work . it always will be direct acyclic graph . 

# Graph:
# •	5→0
# •	4→0 
# •	5→2
# •	2→3
# . 4->1
# •	3→1
# Topological Sort:
# •	5 4 2 3 1 0
# •	4 5 2 3 1 0

# we'll consider dfs backtracking only 
# jkhon backtracking thekhe ber habe tokhon eta stack a nimbe example : 0->1->3->4
#                                                                             |
#                                                                             5
# in this graph , first go to dfs(0),dfs(1),dfs(3),dfs(4), after calling dfs there has no adjacency node or neigbors to go that's why it'll go back to dfs(3) and put the 4 into stack . afterthat 3 has another unvisited adj 5 , then it'll go to 5 and 5 has no edge for going . for that it'll back in 3, putting 5 into the stack. afterthat , 3 has no unvisited edge so, it go back call to the dfs(1), putting 3 into stack . afterthat ,  similarly , 1 and 0 will be stack. So, the topological order will be : 0 1 3 5 4 

# problem link : https://www.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort

# nice discussion about topological sort : https://takeuforward.org/data-structure/topological-sort-algorithm-dfs-g-21/

# topological sort using dfs 

# from collections import defaultdict, deque

# class Solution:
#     def dfs(self, node, vis, stack, adj):
#         vis[node] = True
#         for it in adj[node]:
#             if not vis[it]:
#                 self.dfs(it, vis, stack, adj)
#         stack.append(node)

#     def topoSort(self, V, adj):
#         vis = [False] * V
#         stack = []
#         for i in range(V):
#             if not vis[i]:
#                 self.dfs(i, vis, stack, adj)
        
#         ans = stack[::-1]  # Reversing the stack to get the topological order
#         return ans

# if __name__ == "__main__":
#     adj = defaultdict(list, {
#         0: [], 
#         1: [], 
#         2: [3], 
#         3: [1], 
#         4: [0, 1], 
#         5: [0, 2]
#     })
#     V = 6
#     obj = Solution()
#     ans = obj.topoSort(V, adj)
    
#     print(" ".join(map(str, ans)))


#  Using BFS(kahn's algorithm ) IMPLEMENT THE TOPOLOGICAL ORDER 

# nice explanaation of below problme : https://takeuforward.org/data-structure/kahns-algorithm-topological-sort-algorithm-bfs-g-22/

# from collections import deque

# class Solution:
#     def topoSort(self, V, adj):
#         indegree = [0] * V
#         outdegree = [0] * V
        
#         for i in range(V):
#             outdegree[i] = len(adj[i])
#             for it in adj[i]:
#                 indegree[it] += 1
#         q = deque()
                
#         for i in range(V):
#             if indegree[i] == 0:
#                 q.append(i)
        
        
#         topological_sort = []
        
#         while q :
#             node = q.popleft()
#             topological_sort.append(node)
            
#             for i in adj[node]:
#                 indegree[i] -= 1
#                 if indegree[i] == 0:
#                     q.append(i)
#         return topological_sort , outdegree
                

# if __name__ == "__main__":
#     adj = [
#         [], 
#         [], 
#         [3], 
#         [1], 
#         [0, 1], 
#         [0, 2]
#     ]

#     V = 6
#     obj = Solution()
#     ans = obj.topoSort(V, adj)
    
#     print(" ".join(map(str, ans)))


# to find the cycle of a graph using topological sort with bfs 

# nice solution to understand : https://takeuforward.org/data-structure/detect-cycle-in-a-directed-graph-using-dfs-g-19/

from collections import deque

class Solution:
    def isCyclic(self, V, adj):
        indegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        cnt = 0
        while q:
            node = q.popleft()
            cnt += 1
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return cnt != V

if __name__ == "__main__":
    adj = [
        [],      # Vertex 0
        [2],     # Vertex 1
        [3],     # Vertex 2
        [4, 5],  # Vertex 3
        [2],     # Vertex 4
        []       # Vertex 5
    ]

    V = 6
    obj = Solution()
    ans = obj.isCyclic(V, adj)
    if ans:
        print("cycle is existed")
    else:
        print("cycle is not found")































































































# if __name__ == "__main__":
#     adj = defaultdict(list)
#     adj[0] = []
#     adj[1] = []
#     adj[2] = [3]
#     adj[3] = [1]
#     adj[4] = [0, 1]
#     adj[5] = [0, 2]
#  and are same thing :
#  adj = [
#         [],      # Vertex 0
#         [],      # Vertex 1
#         [3],     # Vertex 2
#         [1],     # Vertex 3
#         [0, 1],  # Vertex 4
#         [0, 2]   # Vertex 5
#     ]






