409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:

        n = len(s)
        char_counts = {}

        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1 

        result = 0
        take_central_char = False

        for count in char_counts.values():
            if count % 2 == 0:
                result += count
            else:
                result += count - 1 
                take_central_char = True 

        if take_central_char:
            result += 1 

        return result
