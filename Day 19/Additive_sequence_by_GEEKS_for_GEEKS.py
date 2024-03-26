# Problem Statement: Additive sequence 
class Solution:
    def isAdditiveSequence(self, n):
        def isAdditiveHelper(num1, num2, s):
            if not s:
                return 1
            sum_str = str(num1 + num2)
            if s.startswith(sum_str):
                return isAdditiveHelper(num2, int(sum_str), s[len(sum_str):])
            return 0

        length = len(n)
        for i in range(1, length):
            for j in range(i + 1, length):
                num1 = int(n[:i])
                num2 = int(n[i:j])
                if (len(str(num1)) != i or len(str(num2)) != j - i):
                    continue
                if isAdditiveHelper(num1, num2, n[j:]):
                    return 1
                if n[i] == '0':
                    break
        return 0
