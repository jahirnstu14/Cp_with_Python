from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):
            # Check for out of bounds or water cell
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            # Mark the cell as visited by setting it to 0
            grid[i][j] = 0

            # Explore all 4 directions
            up = dfs(i, j + 1, grid)
            down = dfs(i, j - 1, grid)
            left = dfs(i - 1, j, grid)
            right = dfs(i + 1, j, grid)

            # Return the total area including this cell
            return 1 + up + down + left + right

        max_area = 0
        
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the cell is land (1), perform DFS to find the area
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j, grid), max_area)
                    
        return max_area

# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    ]

    solution = Solution()
    print(solution.maxAreaOfIsland(grid))  # Output: 6
