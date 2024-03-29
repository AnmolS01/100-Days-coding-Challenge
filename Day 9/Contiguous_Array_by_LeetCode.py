# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        map_values = {}
        map_values[0] = -1
        maxlength = 0
        sums = 0

        for i in range(n):
            if nums[i] == 0:
                sums += -1
            else:
                sums += 1
            
            if sums in map_values:
                length = i - map_values[sums]
                maxlength = max(maxlength, length)
            else:
                map_values[sums] = i
        
        return maxlength
