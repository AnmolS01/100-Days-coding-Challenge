class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp = n
        sums = 0
        while n:
            remainder = n % 10
            sums += remainder**3
            n //= 10
            
        if temp == sums:
            return 'true'
        else:
            return 'false'
