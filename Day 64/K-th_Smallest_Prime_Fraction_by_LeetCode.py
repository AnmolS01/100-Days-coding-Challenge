# Problem Statement : 786. K-th Smallest Prime Fraction

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        if k == 1:
            return (arr[0], arr[-1])
        if n == 2:
            return arr

        result = []
        for i in range(n):
            for j in range(i+1, n):
                result.append((arr[i] / arr[j], arr[i], arr[j]))
        m = len(result)
        result.sort()
        
        for i in range(m):
            if k == 1:
                return [result[i][1], result[i][2]] 
            k -= 1
