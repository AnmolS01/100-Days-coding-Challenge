# Problem Statement: 2997. Minimum Number of Operations to Make Array XOR Equal to K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        init_Xor = 0
        for i in range (n):
            init_Xor ^= nums[i]
        if init_Xor == k:
            return 0
        else:
            while (k > 0 or init_Xor > 0):
                if k % 2 != init_Xor % 2:
                    count += 1
                k = k//2
                init_Xor = init_Xor//2
            return count
