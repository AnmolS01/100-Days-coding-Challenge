class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(row, col):
            queue = []
            queue.append((row, col))
            while queue:
                row, col = queue.pop(0)
                for i,j in directions:
                    r = row + i
                    c = col + j
                    if (r < rows and
                        c < cols and
                        r >= 0 and
                        c >= 0 and
                        grid[r][c] == '1'):
                        queue.append((r, c))
                        grid[r][c] = '-1'


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid[i][j] = '-1'
                    bfs(i, j)
                    islands += 1

        return islands
