# Prolem Statement : 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        frequency = {}
        n = len(s)
        for i in range (n):
            if s[i] not in frequency:
                frequency[s[i]] = t[i]
            else:
                if frequency[s[i]] != t[i]:
                     return False
        return (len(set(frequency.values())) == len (frequency))
