# problem Statement: minimum common value from given two list in LeetCode
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        if not nums1 or not nums2:
            return -1

        common = nums1.intersection(nums2)
        if not common:
            return -1
        else:
            return min(common)
