# 974. Subarray Sums Divisible by K

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix += num
            mod = prefix % k
            
            if mod in prefix_count:
                count += prefix_count[mod]
                prefix_count[mod] += 1
            else:
                prefix_count[mod] = 1

        return count
