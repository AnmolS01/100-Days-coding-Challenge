# Fibonacci series up to Nth term
# You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 109+7.

# Example 1:

# Input:
# n = 5
# Output:
# 0 1 1 2 3 5
# Explanation:
# 0 1 1 2 3 5 is the Fibonacci series up to the 5th term.

class Solution:
    def series(self, n):
        # Code here
        a = 0
        b = 1
        
        modulo = 10**9+7
        
        if n == 0:
            return [a % modulo]
        if n == 1:
            return [a % modulo, b % modulo]

        fibo_series = [a % modulo, b % modulo]
        for i in range(1, n):
            c = (a + b) % modulo
            fibo_series.append(c)
            a = b
            b = c

        return fibo_series
