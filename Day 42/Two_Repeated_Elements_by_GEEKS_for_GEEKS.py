class Solution:
    
    # Function to find two repeated elements.
    def twoRepeated(self, arr, n):
        repeated = []
        for val in range(n + 2):
            if arr[abs(arr[val])] > 0:
                #setting repeated value to negative. so that it will not print repeated value
                # more than one time if it appears again.
                arr[abs(arr[val])] = -arr[abs(arr[val])] 
            else:
                repeated.append(abs(arr[val]))
        return repeated
