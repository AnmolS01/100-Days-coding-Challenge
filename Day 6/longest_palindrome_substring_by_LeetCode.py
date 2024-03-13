# problem no: 5. Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
  
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        def isPalindrome(st):
            return st==st[::-1]
        longest =""
        for i in range (len(s)):
            for j in range (len(s)-1,i-1,-1):
                if s[i]==s[j]:
                    st = s[i:j+1]
                    result=isPalindrome(st)
                    if result is True and len(st)> len(longest):
                        longest = st
        return longest if longest else ''

      
        # def isPalindrome(st):
        # or    
        # n=len(st)
        # i=0
        # j=n-1
        # while i<j:
        #     if st[i]==st[j]:
        #         i+=1
        #         j-=1
        #     else:
        #         return False
        # return True
