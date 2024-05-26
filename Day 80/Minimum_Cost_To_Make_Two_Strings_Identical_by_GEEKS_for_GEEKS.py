class Solution:
	def findMinCost(self, x, y, costX, costY):
        m = len(x)
        s = len(y)
    
        dp = [[0] * (s + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i * costX
    
    # Initialize the first row
        for j in range(1, s + 1):
            dp[0][j] = j * costY
    
    # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, s + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
    
        return dp[m][s]
