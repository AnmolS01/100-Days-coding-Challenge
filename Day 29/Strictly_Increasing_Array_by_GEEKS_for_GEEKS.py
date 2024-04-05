# Problem Statement: Strictly Increasing Array

class Solution:
    def LIS(self, arr):
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and arr[i] - arr[j] >= i - j:
                    dp[i] = max(dp[i], 1 + dp[j])
        maxi = 0
        for val in dp:
            maxi = max(maxi, val)
        return maxi
    
	def min_operations(self,nums):
		# Code here
		l = self.LIS(nums)
        n = len(nums)
        return n - l
