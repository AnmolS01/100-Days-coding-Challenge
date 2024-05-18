class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        # Check if the array is empty
        if not arr:
            return -1
        arr.sort()
        
        left = 0
        right = 1
        

        while right < n:
            
            if abs(arr[left] - arr[right]) == x:
                return 1
            
            elif abs(arr[left] - arr[right]) < x:
                right += 1
            
            else:
                left += 1
                
                if left == right:
                    right += 1
        return -1
