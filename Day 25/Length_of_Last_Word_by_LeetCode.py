# Problem Statement : 58. Length of last word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
  
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

#_________________________________________________________________________________CODE IS HERE__________________________________________________________________________________________

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len (s) - 1
        count = 0
        while n:
            if s[n] == ' ':
                n -= 1
            else:
                break
        for i in range (n,-1,-1):
            if s[i] != ' ':
                count +=1
            else:
                break
        return count
