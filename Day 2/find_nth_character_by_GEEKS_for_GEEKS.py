# problem statement: find nth character 
class Solution:
    def nthCharacter(self, s, r, n):
        if r==0:
            return s[n]
        c=self.nthCharacter(s, r-1, n//2)
        if n%2==1:
            if c=='0':
                return '1'
            return '0'
        else:
            if c=='0':
                return '0'
            return '1'

# another easy approach but the time complexity is not suitable. just for idea.
# def nthCharacter(self, s, r, n):
#         while r:
#             new_s = ''
#             for i in s:
#                 if i == '0':
#                     new_s += '01'
#                 elif i == '1':
#                     new_s += '10'
#                 elif i>n:
#                     break
#             r -= 1
#             s = new_s
#         return new_s[n]
