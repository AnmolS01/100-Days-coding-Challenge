# problem Statement: Optimal Strategy For A Game

class Solution:
    def optimalStrategyOfGame(self, n, arr):
        def help(i, j, arr, dp):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            sum1, sum2 = arr[i], arr[j]
            sum1 += min(help(i + 2, j, arr, dp), help(i + 1, j - 1, arr, dp))
            sum2 += min(help(i + 1, j - 1, arr, dp), help(i, j - 2, arr, dp))
            dp[i][j] = max(sum1, sum2)
            return dp[i][j]

        def maximumAmount(n, arr):
            dp = [[-1] * n for _ in range(n)]
            return help(0, n - 1, arr, dp)

        return maximumAmount(n, arr)








# If i exceeds j, it means the indices have crossed each other, indicating that there are no elements left to pick. In this case, the function returns 0, as there are no points to gain.
      
# if dp[i][j] != -1:: This checks if the value for the current indices i and j has already been computed and stored in the memoization table. If it has, 
# it returns the value stored in dp[i][j] without recalculating.
      
# sum1, sum2 = arr[i], arr[j]: This initializes sum1 and sum2 with the values at indices i and j respectively. 
# These variables will store the total points for each player after they pick an element.

# sum1 += min(help(i + 2, j, arr, dp), help(i + 1, j - 1, arr, dp)): This line calculates the total points sum1 for the first player if they pick the element at index i.
# It adds the value at index i to the minimum of the points the second player can get if the first player picks the next element (at index i+1) or if the first player
# picks the element after the next (at index i+2) while the second player picks the next one or the one before the last one respectively.

# sum2 += min(help(i + 1, j - 1, arr, dp), help(i, j - 2, arr, dp)): Similarly, this line calculates the total points sum2 for the first player if they pick the element at index j.
# It adds the value at index j to the minimum of the points the second player can get if the first player picks the next element (at index i+1) or if the first player picks the
# element before the next (at index j-1) while the second player picks the next one or the one before the last one respectively.

# dp[i][j] = max(sum1, sum2): This stores the maximum points the first player can get by picking either the element at index i or the one at index j.
# It updates the memoization table with this value for future reference.

# Finally, the function returns dp[0][n-1], which represents the maximum points the first player can get by using the maximumAmount function.

# The maximumAmount function initializes the memoization table dp and calls the help function to compute the maximum points for the first player.
