class Solution:
    def largestSubsquare(self, n, a):
        #code here
        by_rows = [[0] * n for _ in range(n)]
        by_cols = [[0] * n for _ in range(n)]
        
        for i in range(n):
            row = 0
            for j in range(n):
                if a[i][j] == 'X':
                    row += 1
                else:
                    row = 0
                by_rows[i][j] = row
        
        for i in range(n):
            col = 0
            for j in range(n):
                if a[j][i] == 'X':
                    col += 1
                else:
                    col = 0
                by_cols[j][i] = col
        
        result = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                side = min(by_rows[i][j], by_cols[i][j])
                while side > result:
                    if by_rows[i - side + 1][j] >= side and by_cols[i][j - side + 1] >= side:
                        result = side
                    else:
                        side -= 1
        return result



# Given a square matrix a of size n x n, where each cell can be either 'X' or 'O', you need to find the size of the largest square subgrid that is completely surrounded by 'X'. More formally you need to find the largest square within the grid where all its border cells are 'X'.

# Example 1:

# Input:
# n = 2
# a = [[X,X],
#      [X,X]]
# Output:
# 2
# Explanation:
# The largest square submatrix 
# surrounded by X is the whole 
# input matrix.
# Example 2:

# Input:
# n = 4
# a = [[X,X,X,O],
#      [X,O,X,X],
#      [X,X,X,O],
#      [X,O,X,X]]
# Output:
# 3
# Explanation:
# Here,the input represents following 
# matrix of size 4 x 4
# X X X O
# X O X X
# X X X O
# X O X X
# The square submatrix starting at 
# (0,0) and ending at (2,2) is the 
# largest submatrix surrounded by X.
# Therefore, size of that matrix would be 3.
