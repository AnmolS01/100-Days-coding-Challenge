# Problem Statement : Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxCount = 0
        tempCount = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                tempCount = count
                count -= 1
                maxCount = max(maxCount, tempCount)
                if count < 0:
                    return -1
        # if count !=0:
        #     return -1
        return maxCount
