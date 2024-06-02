# 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        i = 0
        for j in range (n,n//2,-1):
            s[i],s[j] = s[j],s[i]
            i += 1
