class Solution:
    def minRow(self, n, m, a):
        count = float('inf')
        min_row = -1 
        if not a:
            return 1
        for i in range(n):
            currentCount = 0 
            for j in range(m):
                if a[i][j] == 1:
                    currentCount += 1
            if currentCount < count: 
                count = currentCount
                min_row = i + 1  
        return min_row
