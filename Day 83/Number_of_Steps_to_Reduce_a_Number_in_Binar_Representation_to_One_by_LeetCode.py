1404. Number of Steps to Reduce a Number in Binary Representation to One

class Solution:
    def numSteps(self, s: str) -> int:
        decimal = int(s,2) # To convert string into decimal value
        count = 0
        while decimal > 1:
            if decimal % 2 == 0:
                count += 1
                decimal //= 2
            else:
                decimal += 1
                count += 1
        return count
