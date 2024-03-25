# Problem Statement: Print N-bit binary numbers having more 1s than 0s on GEEKS FOR GEEKS 

class Solution:
    def NBitBinary(self, n):
        def generate_binary_strings(n):
            res = []
            
            # this will make sure you have generated all the binary number at least equal to 
            # length of n i.e (2**(n+1))
            for i in range(1, 2**(n+1)):
                
                # here bin(i) => this convert the decimal number in to binary. And
                # this => [2:] removes the first two numbers of binary string as it generate
                # binary string like 0b101 for decimal number 5. it remove 0b from 0b101.
                bin_string = bin(i)[2:] 
                if len(bin_string) <= n:
                    
                    # zfill fill that hexadecimal removed value with zero (0) of size of n
                    res.append(bin_string.zfill(n))
            return res

        def find_prefix(bin_list):
            filt_list = []
            for bin_str in bin_list:
                COBZ = 0 #count of one before zero
                COAZ = 0 #count of one after zero
                for digit in bin_str:
                    if digit == '1':
                        if COAZ > COBZ:
                            break
                        COBZ += 1 
                    else:
                        COAZ += 1 
                else:
                    if COBZ >= COAZ:
                        filt_list.append(bin_str)
            return filt_list

        def sort_bin_str(bin_list):
            return sorted(bin_list, reverse=True)

        bin_numb = generate_binary_strings(n)
        filt_numb = find_prefix(bin_numb)
        sorted_numb = sort_bin_str(filt_numb)
        return sorted_numb
