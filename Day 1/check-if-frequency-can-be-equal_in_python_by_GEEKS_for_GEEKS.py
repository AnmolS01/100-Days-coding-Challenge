# problem Statement: check frequency can be equal

class Solution:
    
    def isSame(self, freq, size):
        c = 0
        i = 0
        for i in range(size):
            if freq[i] > 0:
                c = freq[i]
                break
        
        for j in range(i + 1, size):
            if freq[j] > 0 and freq[j] != c:
                return False
        
        return True
    
    def sameFreq(self, s):
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        if self.isSame(freq, 26):
            return True
        
        for i in range(26):
            if freq[i] > 0:
                freq[i] -= 1
                if self.isSame(freq, 26):
                    return True
                freq[i] += 1
        
        return False
