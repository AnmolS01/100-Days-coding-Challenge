# Problem Sttatement: Sum of Products

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        
        total_sum = 0
        
        for i in range(32):
            count_set_bits = 0
            
            for num in arr:
                if (num >> i) & 1:
                    count_set_bits += 1
            
            total_sum += count_set_bits * (count_set_bits - 1) // 2 * (1 << i)
            
        return total_sum
