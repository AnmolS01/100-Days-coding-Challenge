# Problem Statement : 1544. Make The String Great

class Solution:
    def makeGood(self, s: str) -> str:

        goodString = []

        for char in s:
            if goodString and (ord(goodString[-1]) - ord(char) == 32 or ord(char) - ord(goodString[-1]) == 32):
                goodString.pop()
            else:
                goodString.append(char)

        return ''.join(goodString)
