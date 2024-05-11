# Problem Statement : 857. Minimum Cost to Hire K Workers

class Worker:
    def __init__(self, quality, wage):
        self.quality = quality
        self.wage = wage

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = []
        for i in range(n):
            workers.append(Worker(quality[i], wage[i]))
        
        workers.sort(key=lambda x: x.wage / x.quality)
        
        min_cost = float('inf')
        quality_sum = 0
        
        import heapq
        
        heap = []
        
        for worker in workers:
            quality_sum += worker.quality
            heapq.heappush(heap, -worker.quality)
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            if len(heap) == k:
                min_cost = min(min_cost, quality_sum * (worker.wage / worker.quality))
        
        return min_cost
