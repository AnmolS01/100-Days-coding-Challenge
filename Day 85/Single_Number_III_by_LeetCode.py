# 260. Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num

        rightmost_set_bit = xor_result & (-xor_result)

        first_unique = 0
        second_unique = 0
        
        for num in nums:
            if num & rightmost_set_bit:
                first_unique ^= num
            else:
                second_unique ^= num
    
        return [first_unique, second_unique]

# ______________________________________________________________________non Bit Manipulation approach________________________________________________________________________

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = b = 0
        for i in range(n):
            if nums[i] in nums[i+1:] or nums[i] in nums[:i]:
                continue
            if a == 0:
                a = nums[i]
            else:
                b = nums[i]
        return [a, b]
        
