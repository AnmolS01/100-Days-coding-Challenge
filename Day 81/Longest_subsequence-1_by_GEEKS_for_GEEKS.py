class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
        dp = [0] * n
        ans = 0
        for i in range(n - 1, -1, -1):
            maxi = 0
            for j in range(i + 1, n):
                if abs(a[i] - a[j]) == 1:
                    maxi = max(maxi, dp[j])
            dp[i] = 1 + maxi
            ans = max(ans, dp[i])
        return ans
