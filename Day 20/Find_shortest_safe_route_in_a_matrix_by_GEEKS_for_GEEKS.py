# problem Statement: Find shortest safe route in a matrix

class Solution:
    def check(self, i, j, mat):
        if i - 1 >= 0 and mat[i - 1][j] == 0:
            return False
        if i + 1 < len(mat) and mat[i + 1][j] == 0:
            return False
        if j - 1 >= 0 and mat[i][j - 1] == 0:
            return False
        if j + 1 < len(mat[0]) and mat[i][j + 1] == 0:
            return False
        return True

    def solve(self, i, j, mat, vis, dp):
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or vis[i][j] == 1 or mat[i][j] == 0:
            return float('inf')

        if dp[i][j] != -1:
            return dp[i][j]

        if not self.check(i, j, mat):
            return float('inf')

        if j == 0:
            return mat[i][0]

        vis[i][j] = 1

        left = self.solve(i, j - 1, mat, vis, dp)
        up = self.solve(i - 1, j, mat, vis, dp)
        down = self.solve(i + 1, j, mat, vis, dp)

        if left != float('inf'):
            left += mat[i][j]
        if up != float('inf'):
            up += mat[i][j]
        if down != float('inf'):
            down += mat[i][j]

        vis[i][j] = 0

        return min(left, min(up, down))

    def findShortestPath(self, mat):
        n = len(mat)
        m = len(mat[0])
        vis = [[0] * m for _ in range(n)]
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        mini = float('inf')
        for i in range(n):
            mini = min(mini, self.solve(i, m - 1, mat, vis, dp))

        if mini == float('inf'):
            return -1
        else:
            return mini
