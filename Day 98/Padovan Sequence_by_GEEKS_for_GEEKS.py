class Solution:
    def padovanSequence(self, n):
        if n == 0 or n == 1 or n == 2:
            return 1
        
        mod = 10**9 + 7
        
        p0, p1, p2 = 1, 1, 1
        for i in range(3, n + 1):
            next_value = (p0 + p1) % mod
            p0, p1, p2 = p1, p2, next_value
        
        return p2



# ________________________________________________________________________This Approach is little inefficient_______________________________________________________________

        # if n == 0 or n == 1 or n == 2:
        #     return 1
        # mod = 10**9 + 7
        # dp = [0]*(n+1)
        # dp[0] = dp[1] = dp[2] = 1
        # for i in range(3,n+1):
        #     dp[i] = (dp[i-2] + dp[i-3]) % mod
        # return dp[n]
