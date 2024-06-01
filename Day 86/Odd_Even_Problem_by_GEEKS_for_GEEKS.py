class Solution:
    def oddEven(self, s: str) -> str:
        x = 0
        y = 0
        count = [0] * 27
        
        for char in s:
            count[ord(char) - ord('a') + 1] += 1
        
        for i in range(1, 27):
            if count[i] != 0 and count[i] % 2 == 0 and i % 2 == 0:
                x += 1
            elif count[i] % 2 == 1 and i % 2 == 1:
                y += 1
        
        sum = x + y
        if sum % 2 == 1:
            return "ODD"
        else:
            return "EVEN"
