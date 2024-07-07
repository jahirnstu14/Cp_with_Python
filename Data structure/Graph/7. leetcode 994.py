from collections import deque

class Solution:
    def orangesRotting(self, grid):
        # figure out the grid size
        n = len(grid)
        m = len(grid[0])
        
        # store {{row, column}, time}
        q = deque()
        vis = [[0] * m for _ in range(n)]
        cntFresh = 0
        
        for i in range(n):
            for j in range(m):
                # if cell contains rotten orange
                if grid[i][j] == 2:
                    q.append(((i, j), 0))
                    # mark as visited (rotten) in visited array
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0
                # count fresh oranges
                if grid[i][j] == 1:
                    cntFresh += 1
        
        tm = 0
        # delta row and delta column
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        cnt = 0
        
        # bfs traversal (until the queue becomes empty)
        while q:
            r, c = q[0][0]
            t = q[0][1]
            tm = max(tm, t)
            q.popleft()
            # exactly 4 neighbours 
            for i in range(4):
                # neighbouring row and column
                nrow = r + drow[i]
                ncol = c + dcol[i]
                # check for valid cell and 
                # then for unvisited fresh orange
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    # push in queue with timer increased
                    q.append(((nrow, ncol), t + 1))
                    # mark as rotten
                    vis[nrow][ncol] = 2
                    cnt += 1
        
        # if all oranges are not rotten
        if cnt != cntFresh:
            return -1
        
        return tm

# Example usage:
grid = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
obj = Solution()
ans = obj.orangesRotting(grid)
print(ans)
