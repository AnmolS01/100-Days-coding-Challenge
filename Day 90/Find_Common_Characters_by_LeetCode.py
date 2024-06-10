# 1002. Find Common Characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        reference = list(words.pop(0))
        for word in words:
            newWord = list(word)
            result = []
            for char in reference:
                if char in newWord:
                    result.append(char)
                    newWord.remove(char)
            reference = result
        return reference
