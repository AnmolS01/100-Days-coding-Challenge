# Problem Statement : Maximize dot product

class Solution:
    def maxDotProduct(self, n, m, a, b):
        # Initialize the DP table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                dp[i][j] = max(dp[i - 1][j - 1] + a[j - 1] * b[i - 1], dp[i][j - 1])
        
        return dp[m][n]
