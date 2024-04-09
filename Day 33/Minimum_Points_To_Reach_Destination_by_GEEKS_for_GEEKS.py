class Solution:
	def minPoints(self, m, n, points):
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = max(1, 1 - points[m-1][n-1])

        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - points[i][n-1])
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - points[m-1][j])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                minPoints = min(dp[i+1][j], dp[i][j+1]) - points[i][j]
                dp[i][j] = max(1, minPoints)

        return dp[0][0]


# Initialize a 2D array to store the minimum points required (dp):

# We initialize a 2D array dp with dimensions m rows and n columns to store the minimum points required to reach the destination cell from each cell of the grid.
# dp[i][j] will represent the minimum points required to reach the destination cell from cell (i, j).
# Start from the destination cell (dp[m-1][n-1]):

# We start from the destination cell (m-1, n-1) and calculate the minimum points required to reach the destination from this cell.
# At the destination cell, we need at least 1 point to ensure that we have positive points throughout the path. So, we initialize dp[m-1][n-1] as max(1, 1 - points[m-1][n-1]).
# Calculate minimum points required from bottom-right to top-left:

# We iterate through the cells from bottom to top and from right to left of the grid.
# At each cell (i, j), we calculate the minimum points required to reach the destination cell while ensuring that we have enough points to move to the next cell.
# Let's break down the calculation of dp[i][j]:

# dp[i][j] can be calculated based on the points needed at the next cells (i+1, j) and (i, j+1).
# We calculate minPoints as min(dp[i+1][j], dp[i][j+1]) - points[i][j].
# minPoints represents the minimum points needed to reach the destination cell after moving from cell (i, j).
# However, if minPoints becomes <= 0, it implies that we don't have enough points to proceed to the next cell while maintaining positive points. So, we update minPoints to ensure we have at least 1 point left.
# Finally, we set dp[i][j] as max(1, minPoints).
# Return the minimum initial points required (dp[0][0]):

# Once we have calculated the minimum points required to reach the destination cell from the source cell (0, 0), we return dp[0][0], which represents the minimum initial points needed at the starting cell.
# Let's illustrate this approach with an example:

# Example:
# Consider the grid:

# points = [[-2,-3, 3],
#           [-5,-10,1],
#           [10,30,-5]]
# Initialize dp array:
# dp = [[0, 0, 0],
#       [0, 0, 0],
#       [0, 0, 0]]

# Start from the destination cell:

# dp[2][2] = max(1, 1 - points[2][2]) = max(1, 1 - (-5)) = max(1, 6) = 6
# Calculate minimum points required from bottom-right to top-left:

# Calculate dp[2][1] and dp[1][2] based on dp[2][2].

# Then, calculate dp[1][1] based on dp[2][1] and dp[1][2].

# Finally, calculate dp[0][0] based on dp[1][0] and dp[0][1].

# Return the minimum initial points required:
# Return dp[0][0] = dp[0][0] = 7
