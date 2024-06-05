class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sumofA = sum(a)
        sumofB = sum(b)
        if sumofA == sumofB:
            return 1
        difference = sumofA - sumofB
        if difference % 2 != 0: 
            return -1
        
        target = difference // 2

        a.sort()
        b.sort()

        i = 0
        j = 0

        while i < n and j < m:
            diff = a[i] - b[j]

            if diff == target:
                return 1
            elif diff < target:
                i += 1
            else:
                j += 1
        return -1
