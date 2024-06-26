class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        dp = [float('inf')] * (w + 1)
    
        dp[0] = 0
    
        for i in range(1, n + 1):
            if cost[i - 1] != -1:
                for j in range(i, w + 1):
                    if dp[j - i] != float('inf'):
                        dp[j] = min(dp[j], dp[j - i] + cost[i - 1])

        return dp[w] if dp[w] != float('inf') else -1
