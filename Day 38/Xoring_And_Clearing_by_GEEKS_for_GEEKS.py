# Problem Statement: Xoring and Clearing

# You are given an array arr[] of size n. You need to do the following:
# You need to calculate the bitwise XOR of each element in the array with its corresponding index (indices start from 0).
# After step1, print the array.
# Now, set all the elements of arr[] to zero.
# Now, print arr[].

# Example 1:

# Input:
# n = 10
# arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Output:
# 1 3 1 7 1 3 1 15 1 3
# 0 0 0 0 0 0 0 0 0 0

# Explanation:
# First we take xor of every element with
# their indices, like (1xor0), (2xor1), (3xor2), (4xor3) and so on.
# Now print the resultant array
# Now set all the elements of array to zero
# Now print the resultant array

# _____________________________________________________________________________________________CODE IS HERE_________________________________________________________________________________________

class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        return
    
    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range (n):
            arr[i] = 0
            print(arr[i], end=' ')
        print()

    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range (n):
            arr[i] = arr[i] ^ i
            print(arr[i], end= ' ')
        print()
