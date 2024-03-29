# Problem Statement: 2962. Count Subarrays Where Max Element Appears at Least K Times

# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.
  
# Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

# Example 2:
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.


#________________________________________________________________CODE IS HERE_______________________________________________________________

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        start = 0
        end = 0
        count = 0
        maxFreqCount = 0
        while end < n:
            if nums[end] == max_num :
                maxFreqCount += 1
            while maxFreqCount == k:
                count += (n-end)
                if nums[start] == max_num:
                    maxFreqCount -= 1
                start +=1
            end += 1
        return count
        
