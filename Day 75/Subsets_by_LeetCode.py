# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(index, current):
            if index == len(nums):
                result.append(current[:]) #add whole set into result
                return
            # Include the current element
            current.append(nums[index])
            helper(index + 1, current)
            # not include the current element
            current.pop()
            helper(index + 1, current)
        
        helper(0, [])
        return result
