class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self, n):
        def decimal_to_binary(decimal_num):
            binary_num = ""
            if decimal_num == 0:
                return "0"
            while decimal_num > 0:
                remainder = decimal_num % 2
                binary_num = str(remainder) + binary_num
                decimal_num //= 2
            return binary_num
        
        binary_num = decimal_to_binary(n)
        stack = []
        for i in range(len(binary_num)):
            if stack:
                stack.append(int(stack[-1]) ^ int(binary_num[i]))
            else:
                stack.append(int(binary_num[i]))
        result = ''.join(map(str, stack))
        
        def binary_to_decimal(result):
            decimal_num = 0
            power = len(result) - 1
            for digit in result:
                decimal_num += int(digit) * (2 ** power)
                power -= 1
            return decimal_num
        
        return binary_to_decimal(result)
