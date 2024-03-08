# problem statement: count element with maximum frequency
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = len(nums)
        f1 = []
        f2 = []
        c = 0
        freq= {}
        
        for i in range(n):
            freq[nums[i]] = freq_map.get(nums[i], 0) + 1
            c = max(c, freq[nums[i]])
        
        for i in range(n):
            if freq_map[nums[i]] == max_freq:
                f1.append(nums[i])
        
        if max_freq > 1:
            return len(f1)
        else:
            return n
