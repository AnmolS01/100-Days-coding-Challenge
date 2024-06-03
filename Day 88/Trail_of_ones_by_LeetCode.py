class Solution:
    def numberOfConsecutiveOnes(self, n):
        MOD = 10**9 + 7
        if n == 2:
            return 1
  
        a = [0] * (n + 1)
        a[1] = 2
        a[2] = 3

        for i in range(3, n + 1):
            a[i] = (a[i-1] + a[i-2]) % MOD
        
        total = pow(2, n, MOD)
        result = (total - a[n] + MOD) % MOD
        
        return result
