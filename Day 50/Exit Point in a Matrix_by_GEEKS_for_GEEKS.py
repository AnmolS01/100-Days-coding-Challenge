# Exit Point in a Matrix

class Solution:
	def FindExitPoint(self, n, m, matrix):
        n = len(matrix)
        m = len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i, j, direction = 0, 0, 0
        while True:
            if i < 0 or i >= n or j < 0 or j >= m:
                break
            if matrix[i][j] == 0:
                i += directions[direction][0]
                j += directions[direction][1]
            else:
                direction = (direction + 1) % 4
                matrix[i][j] = 0
        return [i - directions[direction][0], j - directions[direction][1]]
