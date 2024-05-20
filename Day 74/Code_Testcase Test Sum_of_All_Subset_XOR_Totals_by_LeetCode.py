# 1863. Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(nums, index, xor):
            if index == len(nums):
                return xor
            pick = helper(nums,index+1, nums[index]^xor)
            noPick = helper(nums,index+1, xor)
            
            return pick+noPick
        return helper(nums,0,0)
