# 1608. Special Array With X Elements Greater Than or Equal X

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        nums.sort()
        n = len(nums)
        
        start, end = 0, n
        
        while start <= end:
            mid = (start + end) // 2
            count = sum(1 for num in nums if num >= mid) #mid gives value not index
            
            if count == mid:
                return mid
            elif count > mid:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
