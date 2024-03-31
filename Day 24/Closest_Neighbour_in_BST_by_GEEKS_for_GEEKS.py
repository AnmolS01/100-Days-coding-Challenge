# Given the root of a binary search tree and a number n, find the greatest number in the binary search tree that is less than or equal to n. 
# Example 1 :
# Input : 
#           5
#         /   \
#        2    12
#      /  \  /  \
#     1   3 9   21
#              /  \
#            19    25
# n = 24
# Output : 
# 21
# Explanation : The greatest element in the tree which is less than or equal to 24, is 21. (Searching will be like 5->12->21)


# __________________________________________________________________________________CODE IS HERE________________________________________________________________________________
class Solution:
    def findMaxForN(self, root, n):
        #Print the value of the element if it exists otherwise print -1.
        max_value = -1
        if not root:
            return max_value
        while root:
            if root.key <= n:
                max_value = max (max_value,root.key)
                root = root.right
            else:
                root = root.left
        return max_value
