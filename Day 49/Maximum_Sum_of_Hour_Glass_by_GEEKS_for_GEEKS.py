class Solution:
    def findMaxSum(self,n,m,mat):
        max_sum = float('-inf')
        for i in range(n - 2):
            for j in range(m - 2):
                hourglass_sum = (
                    mat[i][j] + mat[i][j + 1] + mat[i][j + 2] +
                    mat[i + 1][j + 1] +
                    mat[i + 2][j] + mat[i + 2][j + 1] + mat[i + 2][j + 2]
                )
                max_sum = max(max_sum, hourglass_sum)
        if max_sum == float('-inf'):
            return -1
        else:
            return max_sum
