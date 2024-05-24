class Solution:
    def countPartitions(self, n, d, arr):
        mod = 10**9 + 7
        total_sum = sum(arr)
        
        if total_sum < d or (total_sum + d) % 2 != 0:
            return 0
        
        target = (total_sum + d) // 2
        
        dp = [0] * (target + 1)
        dp[0] = 1  # There's one way to make zero sum: choose no elements
        
        for num in arr:
            for t in range(target, num - 1, -1):
                dp[t] = (dp[t] + dp[t - num]) % mod
        
        return dp[target]
