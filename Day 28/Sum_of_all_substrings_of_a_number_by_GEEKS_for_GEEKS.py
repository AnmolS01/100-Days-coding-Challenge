# Problem Statement : Sum of all substrings of a number

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        
        # code here
        n = len(s)
        MOD = 10**9 + 7
        total_sum = 0
        substring_sum = 0

        for i in range(n):
            substring_sum = (substring_sum * 10 + int(s[i]) * (i + 1)) % MOD
            total_sum = (total_sum + substring_sum) % MOD

        return total_sum
