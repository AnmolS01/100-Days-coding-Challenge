131. Palindrome Partitioning

class Solution:
    def __init__(self):
        self.result = []

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.backtrack(s, 0, [])
        return self.result

    def backtrack(self, s, start, path):
        if start == len(s):
            self.result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                path.append(s[start:end+1])
                self.backtrack(s, end + 1, path)
                path.pop()

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
