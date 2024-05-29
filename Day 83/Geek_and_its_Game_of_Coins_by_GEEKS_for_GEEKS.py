
class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        dp = [False] * (n + 1)
        dp[0] = False
    
        for i in range(1, n + 1):
            if i >= 1 and not dp[i - 1]:
                dp[i] = True

            elif i >= x and not dp[i - x]:
                dp[i] = True

            elif i >= y and not dp[i - y]:
                dp[i] = True

        return 1 if dp[n] else 0



