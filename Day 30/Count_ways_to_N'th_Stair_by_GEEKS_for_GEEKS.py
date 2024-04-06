# Problem Statement: Count ways to N'th Stair
# There are n stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
# Count the number of ways, the person can reach the top (order does not matter).

# Example 1:

# Input:
# n = 4
# Output: 
# 3
# Explanation: 
# You can reach 4th stair in 3 ways.
# 3 possible ways are:
# 1, 1, 1, 1
# 1, 1, 2
# 2, 2
# Here, note that {1, 1, 2}, {1, 2, 1} and {2, 1, 1} are considered same as their order does not matter. 

# __________________________________________________________________________________CODE IS HERE_____________________________________________________________________________________

class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):

        mod = 1000000007
        # code here
        return 1+n//2
