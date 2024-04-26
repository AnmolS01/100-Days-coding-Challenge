# Problem statement: 1289. Minimum Falling Path Sum II

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        for i in range(1, n):
            for j in range(n):
                min_sum = float('inf')
                for k in range(n):
                    if k != j:
                        min_sum = min(min_sum, grid[i-1][k])
                grid[i][j] += min_sum
    
        return min(grid[-1])
