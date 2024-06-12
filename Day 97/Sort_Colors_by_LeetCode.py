# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            keyValue = nums[i] # to store the value as we required in future.
            j = i - 1
            while j >= 0 and keyValue < nums[j]:
                nums[j+1] = nums[j] # putting value of Jth position to j+1th position
                j -= 1 # to check if, is there any other value greater than keyValue.
            nums[j+1] = keyValue # placing key value at its position
