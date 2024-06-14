# 945. Minimum Increment to Make Array Unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort() 
        count = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                difference = nums[i-1] + 1 - nums[i] # '+1' is for increment if duplicates.
                nums[i] += difference
                count += difference
        return count
