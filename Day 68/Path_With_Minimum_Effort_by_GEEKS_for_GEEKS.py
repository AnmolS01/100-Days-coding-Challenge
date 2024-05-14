from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        # Initialize a 2D array to store the minimum effort to reach each cell
        effort = [[float('inf')] * columns for _ in range(rows)]
    
        # Priority queue to store cells based on their effort
        pq = [(0, 0, 0)]  # (effort, row, column)
    
        # Set effort for top-left cell to 0
        effort[0][0] = 0
    
        while pq:
            cur_effort, row, col = heapq.heappop(pq)
        
            # If current cell is the bottom-right cell, return its effort
            if row == rows - 1 and col == columns - 1:
                return cur_effort
        
            # Explore adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
            
                # Check if the new position is within the grid
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    new_effort = max(cur_effort, abs(heights[row][col] - heights[new_row][new_col]))
                
                    # Update effort if the new path has lower effort
                    if new_effort < effort[new_row][new_col]:
                        effort[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))
   
        return -1
