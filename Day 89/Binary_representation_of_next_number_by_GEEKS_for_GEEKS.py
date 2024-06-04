class Solution:
    def binaryNextNumber(self, s):
        first_one_index = s.find('1')
        if first_one_index == -1:
            return '1'

        s = s[first_one_index:]
        s = list(s)
    
        carry = 1
        for i in range(len(s) - 1, -1, -1):
            if carry == 0:
                break
            if s[i] == '1':
                s[i] = '0'
            else:
                s[i] = '1'
                carry = 0
    
        if carry == 1:
            s.insert(0, '1')
    
        return ''.join(s)
