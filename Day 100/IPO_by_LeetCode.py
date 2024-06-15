# 502. IPO

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = []

        for i in range(n):
            projects.append([capital[i], profits[i]])

        projects.sort()

        # Max-heap to keep track of the highest profit projects that can be started
        max_heap = []

        i = 0
        for j in range(k):
            # Push all projects that can be started with the current capital into the heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            # If no projects can be started, break
            if not max_heap:
                break
            # Pop the project with the highest profit
            w += -heapq.heappop(max_heap)
    
        return w
