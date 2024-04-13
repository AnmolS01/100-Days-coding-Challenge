#problem Statement: Reverse Bit 



class Solution:
    def reversedBits(self, x):
        # code here 
        binary_num = bin(x) [2:]
        rev = binary_num[::-1]
        reversed_binary = rev.ljust(32, '0')
        decimal_number = int(reversed_binary, 2)
        return decimal_number




# Question 
# Given a number x, reverse its binary form and return the answer in decimal.

# Example 1:

# Input:
# x = 1
# Output:
# 2147483648 
# Explanation:
# Binary of 1 in 32 bits representation-
# 00000000000000000000000000000001
# Reversing the binary form we get, 
# 10000000000000000000000000000000,
# whose decimal value is 2147483648.
# Example 2:

# Input:
# x = 5
# Output:
# 2684354560 
# Explanation:
# Binary of 5 in 32 bits representation-
# 00000000000000000000000000000101
# Reversing the binary form we get, 
# 10100000000000000000000000000000,
# whose decimal value is 2684354560.
