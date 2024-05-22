class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        def is_feasible(D):
            count = 0
            for i in range(1, len(stations)):
                count += (stations[i] - stations[i - 1]) // D
            return count <= K

        stations.sort()
        low, high = 0, stations[-1] - stations[0]
        while high - low > 1e-6:
            mid = (low + high) / 2
            if is_feasible(mid):
                high = mid
            else:
                low = mid
        return round(high, 2)
