
class Solution:
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
    
        for i in range(n):
            if arr[i] <= k:
                current_books += arr[i]
            else:
                current_books = 0
                
            if current_books > max_books:
                max_books = current_books
        return max_books
