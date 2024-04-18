class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        
        def dfs(row, column):

            # check if it not out of matrix and matrix is not 0
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == 0:
                return 1

            # check if visited
            if grid[row][column] == -1:
                return 0

            # mark the value negative to identify it is visited
            grid[row][column] = -1

            perimeter = dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1)

            return perimeter

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)
