# 3068. Find the Maximum Sum of Node Values

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_sum = 0
        count = 0
        minn = float('inf')

        for num in nums:
            if (num ^ k) > num:
                count += 1
                total_sum += (num ^ k)
            else:
                total_sum += num

            minn = min(minn, abs(num - (num ^ k)))

        if count % 2 == 0:
            return total_sum

        return total_sum - minn


# Doubted Approach:

# pointout the mistake in this code>

# class Solution:
#     def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#         maxi = sum(nums)
#         tempNums = nums[:]
#         for edge in edges:

#             original_val1 = tempNums[edge[0]]
#             original_val2 = tempNums[edge[1]]

#             nums[edge[0]] ^= k
#             nums[edge[1]] ^= k

#             maxi = max(maxi, sum(nums))
            
#             nums[edge[0]] = original_val1
#             nums[edge[1]] = original_val2
            
#         return maxi
