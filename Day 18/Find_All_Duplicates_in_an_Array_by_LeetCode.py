# Problem Statement: 442. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice. You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


# __________________________________________________+++++++__________________CODE IS HERE___________________++++++++____________________________________________________
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate_values = []
        for index in range(len(nums)):
            slow = abs(nums[index])
            fast = slow - 1
            if nums[fast] < 0:
                duplicate_values.append(slow)
            else:
                nums[fast] = -nums[fast]
        return duplicate_values

        # this logic takes O(n) space complexity

        # result = []
        # a= set()
        # for val in nums:
        #     if val in a:
        #         result.append(val)
        #     else:
        #         a.add(val)
        # return result
