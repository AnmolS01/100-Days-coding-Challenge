# Problem Statement : 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)

        if ch not in word:
            return word

        result = ''
        c = 0
        for i in range(n):
            if word[i] == ch:
                break
            c += 1
        for j in range(c, -1, -1):
            result += word[j]

        result += word[c+1:]
        return result
