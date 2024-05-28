# 1208. Get Equal Substrings Within Budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        end = 0
        currentCost = 0
        maxLength = 0

        while end < n:
            currentCost += abs(ord(s[end]) - ord(t[end]))
            while currentCost > maxCost:
                currentCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength
