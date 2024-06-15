class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
            return 10
        adjacency_list = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8]
        }

        previous_count = [1] * 10 
        current_count = [0] * 10

        for i in range(2, n + 1):
            for digit in range(10):
                current_count[digit] = sum(previous_count[adj] for adj in adjacency_list[digit])
            previous_count = current_count[:]

        return sum(previous_count)

