class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        start, end = 0, n - 1
        mini = arr[0]

        while start <= end:
            mid = (start + end) // 2
            
            if abs(arr[mid] - k) < abs(mini - k):
                mini = arr[mid]
            elif (abs(arr[mid] - k) == abs(mini - k) and arr[mid] >mini):
                mini = arr[mid]
                
            if arr[mid] < k:
                start = mid + 1
            elif arr[mid] > k:
                end = mid - 1
            else:
                return arr[mid]

        return mini
