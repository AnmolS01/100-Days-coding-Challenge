class Solution:
    def jugglerSequence(self, n):
        # code here
        if n < 1:
            return []
        if n == 1:
            return [1]
        if ( n%2 == 0):
            return [n] + self.jugglerSequence(int(n**0.5))
        else:
            return [n]+self.jugglerSequence(int(n**1.5))
