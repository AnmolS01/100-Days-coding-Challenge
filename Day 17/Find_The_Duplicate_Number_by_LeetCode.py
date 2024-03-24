# Problem Statement: 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

# _________________________________________________CODE WITH TIME SPACE COMPLEXITY O(1)____________________________________________________

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]  # point out first index
        fast = nums[nums[0]]  # point out the index represented
                              # by the value of element at slow-th index

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Reset one of the pointers to the beginning
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # At this point, both pointers meet at the start of the cycle
        return slow


#________________________________________________CODE NOT WITH SPACE COMPLEXITY O(1)____________________________________________________

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_elements = set()
        for val in nums:
            if val in unique_elements:
                return val
            else:
                unique_elements.add(val)
