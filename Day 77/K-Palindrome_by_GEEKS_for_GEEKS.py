class Solution:
    def kPalindrome(self, s, n, k):
        def is_k_palindrome(s, n, k):
            dp = [[0] * n for _ in range(n)]

            for length in range(1, n):
                for i in range(n - length):
                    j = i + length
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])


            min_deletions = dp[0][n - 1]
            return min_deletions <= k

        return 1 if is_k_palindrome(s, n, k) else 0
