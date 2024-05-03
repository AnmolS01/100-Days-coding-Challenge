# Problem Statement: 2441. Largest Positive Integer That Exists With Its Negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1
        
        while nums:
            positive = max(nums)
            if positive > 0:
                if -positive in nums:
                    return positive
                else:
                    nums.remove(positive)
            else:
                return -1
        return -1
