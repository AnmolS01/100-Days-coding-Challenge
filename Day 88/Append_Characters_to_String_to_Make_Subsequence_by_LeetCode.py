# 2486. Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not s or not t:
            return len(t)
        
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j
