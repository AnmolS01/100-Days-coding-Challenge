class Solution:
    def swapNibbles (self, n):
        # code here 
        s = ''
        while n > 0:
            remainder = n % 2
            s = str(remainder) + s
            n = n // 2
        s = s.zfill(8)
    
        swapped = s[4:] + s[:4]
        result = int(swapped, 2)
        
        return result
