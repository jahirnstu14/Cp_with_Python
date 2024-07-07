# Great explanation wit solution : https://leetcode.com/problems/number-of-islands/discuss/5043649/FasterLesser2-MethodsDetailed-ApproachBFSDFSPythonJavaC%2B%2B and another solution with explanation : https://leetcode.com/problems/number-of-islands/discuss/429842/JavaScript-DFS-Commented-Thought-Process-Beats-100-Time-and-Space
    
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0  # the counted islands
        # Go through each cell of the 2D array/grid
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    count += 1
                    self.explore(row, col, grid)
        return count

    def explore(self, row: int, col: int, grid: List[List[str]]):
        # Return if out of bounds or current cell is '0'
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == '0':
            return
        
        # Otherwise, explore it!
        # First, set the current spot to '0'
        grid[row][col] = '0'
        
        # Explore all possibilities (right, left, down, up)
        self.explore(row, col + 1, grid)  # right
        self.explore(row, col - 1, grid)  # left
        self.explore(row + 1, col, grid)  # down
        self.explore(row - 1, col, grid)  # up

# Example input
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

solution = Solution()
print(solution.numIslands(grid))  # Output should be 3
