# Given a string str which may contains lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

# Example 1:

# Input:
# str = "geEksforGEeks"
# Output: 
# "geEksforG"
# Explanation: 
# After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".

# Example 2:

# Input:
# str = "HaPpyNewYear"
# Output: 
# "HaPpyNewYr"
# Explanation: 
# After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".


# -------------------------------------------------------IMPLEMENTATION CODE----------------------------------------------------------

class Solution:
	def removeDuplicates(self,str):
	    unique = set()
        result = ''
        for i in str:
            if i not in unique:
                unique.add(i)
                result += i
        return result
