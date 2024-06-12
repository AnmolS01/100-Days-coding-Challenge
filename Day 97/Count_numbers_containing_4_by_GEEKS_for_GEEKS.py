class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        count = 0
        for i in range (n+1):
            if '4' in str(i):
                count += 1
        return count
