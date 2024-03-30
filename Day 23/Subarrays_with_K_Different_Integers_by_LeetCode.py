# Problem Statement : 992. Subarrays with K Different Integers

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.countOfsubarraysWithKDistinct(nums, k) - self.countOfsubarraysWithKDistinct(nums, k-1)

    def countOfsubarraysWithKDistinct(self, nums, k):
        freq = {}
        n = len(nums)
        start = 0
        end = 0
        count = 0

        while end < n:
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            while len(freq) > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                start += 1  
            count += (end - start) + 1
            end += 1
        return count
