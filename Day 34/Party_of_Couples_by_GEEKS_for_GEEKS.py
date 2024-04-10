class Solution:
    def findSingle(self, n, arr):
        single_person = 0
        for num in arr:
            single_person ^= num
        return single_person
